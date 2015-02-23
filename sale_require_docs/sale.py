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

from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = "sale.order"

    def action_button_confirm(self, cr, uid, ids, context=None):
        sale_order_attachment_obj = self.pool.get('ir.attachment')
        a_ids = sale_order_attachment_obj.search(cr, uid,[('res_model','=','sale.order'),('res_id','=',ids[0])])
        if not a_ids:
            raise osv.except_osv(
                _('Cannot confirm this sales order!'),
                _('Please attach supporting documentation.'))

        return super(sale_order, self).action_button_confirm(cr, uid, ids, context)
