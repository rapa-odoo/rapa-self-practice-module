# -*- coding: utf-8 -*-
{
    'name':"EV Workshop",
    'version': "1.0",
    'category': 'Category',
    'summary': "Module which helps to Purchase an EV as well as maintain it",
    'description': "EV Workshop Module",
    'author': "Raj Patani",
    # 'installable': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ev_workshop_views.xml',
        'views/ev_purchase_view.xml',
        'views/ev_brands_view.xml',
        'views/ev_brand_variants.xml',
        'views/ev_mechanic_view.xml',
        'views/ev_workshop_menus.xml',
    ],
    'sequence': -100,
    'application': True,
    'license': "LGPL-3"
}