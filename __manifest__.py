# -*- coding: utf-8 -*-
{
    'name': "Fichajes",

    'summary': """
        Este módulo trata de controlar los fichajes de entrada y salida en la empresa,
        así como el incremento y disfrute de las horas de libre disposición""",

    'description': """
        Listado de los últimos fichajes realizados en la empresa
    """,


    'author': "Isabel Marti Romeu",
    'website': "http://www.isamarrom.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
