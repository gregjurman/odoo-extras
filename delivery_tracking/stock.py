# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields
from openerp.tools.translate import _

class stock_transfer_details(models.TransientModel):
    _inherit = 'stock.transfer_details'

    carrier_tracking_ref = fields.Char("Carrier Tracking Ref", copy=False)
    carrier_tracking_req = fields.Boolean("Carrier Tracking Required")

    def default_get(self, cr, uid, ids, context=None):
        if context is None: context = {}
        res = super(stock_transfer_details, self).default_get(cr,uid,ids,context=context)
        picking_ids = context.get('active_ids', [])
        active_model = context.get('active_model')

        if not picking_ids or len(picking_ids) != 1:
            return res
        assert active_model in ('stock.picking'), 'Bad context propagetion'
        picking_id, = picking_ids
        picking = self.pool.get('stock.picking').browse(cr,uid,picking_id, context=context)
        is_trk_req = picking.carrier_id.is_trackable
        res.update(carrier_tracking_req=is_trk_req)

        return res

    def do_detailed_transfer(self, cr, uid, ids, context=None):
        if context is None: context = {}
        res = self.browse(cr, uid, ids, context=context)
        s = super(stock_transfer_details, self).do_detailed_transfer(cr,uid,ids, context=context)
        if not s:
            return False
        picking_ids = context.get('active_ids', [])
        active_model = context.get('active_model')

        if not picking_ids or len(picking_ids) != 1:
            return res
        assert active_model in ('stock.picking'), 'Bad context propagetion'
        picking_id, = picking_ids
        picking = self.pool.get('stock.picking').browse(cr, uid, picking_id, context=context)
	carrier_tracking_ref = res.carrier_tracking_ref
        picking.write({"carrier_tracking_ref": carrier_tracking_ref})

	return True


