# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _
import pdb

class product_template(osv.osv):
    _inherit = "product.template"

    def create(self, cr, uid, vals, context=None):
        product_template_id = super(product_template, self).create(cr, uid, vals, context=context)
        mrp_bom = self.pool.get("mrp.bom")
#        pdb.set_trace()
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
