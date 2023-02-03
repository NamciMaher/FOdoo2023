# -*- coding: utf-8 -*-
{
    'name': 'Lifetime Product',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Choose a product from a list of all products',
    'description': '''
        This module allows you to choose a product from a list of all products in the database and displays it in a view called "lifetime".
    ''',
    'author': 'OpenAI',
    'website': 'https://www.openai.com',
    'depends': ['product'],
    'data': [
        'views/lifetime_product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
