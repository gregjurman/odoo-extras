# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  Greg Jurman  (http://github.com/gregjurman)
#    All Rights Reserved.
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
from openerp.tools.translate import _


class product_template(osv.osv):
    _inherit = "product.template"

    def create(self, cr, uid, vals, context=None):
        product_template_id = super(product_template, self).create(cr, uid, vals, context=context)
        mrp_bom = self.pool.get("mrp.bom")

        data = {
            'name': "%s - Default BoM" % vals['name'],
            'product_tmpl_id': product_template_id,
            'active': True,
            'type': 'normal',
            'product_qty': 1,
            'product_uom': vals['uom_id'],
            'product_efficiency': 1,
            'company_id': vals['company_id']
        }

        mrp_bom.create(cr, uid, data, context=context)
        
        return product_template_id
