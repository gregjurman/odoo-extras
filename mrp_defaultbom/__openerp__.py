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


{
    'name': 'Default BOM for Products',
    'version': '0.1',
    'category': 'Manufacturing',
    'description': """
Automatically create a blank BoM for new Products.
=============================================================

Creates a BOM for a product when the product is first created
to quickly get them running in MRP. Useful when purchasing is
done in a seperate system and/or deployment is being staged.

HINT: Use Set Defaults in developer mode to set default routing and
other settings to carry over to newly generated BoMs.

""",
    'author': 'Greg Jurman',
    'website': 'https://github.com/gregjurman/',
    'depends': ['product', 'mrp'],
    'data': [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
