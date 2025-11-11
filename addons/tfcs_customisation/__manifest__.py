# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TFCS Customisation',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Custom SQL View',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_sql_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 