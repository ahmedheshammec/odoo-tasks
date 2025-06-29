# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Automation",
    'author': "CapStone Solutions",
    'website': "http://www.capstonesolutions.com/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_workflow.xml',
        'views/purchase_order.xml',
    ],
}
