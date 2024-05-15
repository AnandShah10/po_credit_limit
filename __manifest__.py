# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'po_credit_limit',
    'version': '1.0',
    'summary': "PO Credit Limit module",
    'sequence': 11,
    'author': "anand",
    'description': """
Add PO limit in settings for purchase""",
    'category': 'Custom/Purchase',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail', 'purchase', 'base'],
    'data': [
        'views/po_settings.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
