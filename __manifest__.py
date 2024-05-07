# -*- coding: utf-8 -*-
{
    'name': "Fichaje",

    'summary': """
        Este módulo trata de controlar los fichajes de entrada y salida en la empresa,
        así como el incremento y disfrute de las horas de libre disposición""",

    'description': """
        Listado de los últimos fichajes realizados en la empresa
    """,


    'author': "Isabel Marti Romeu",
    'website': "https://isabelmartiromeu.github.io/fichaje",

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
        'security/groups.xml',
        'security/access.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/registro_fichaje_report.xml',
        'reports/peticion_horas_report.xml',
        'reports/bolsa_horas_report.xml',
        'data/demo/empleado.xml',
        'data/demo/registro_fichaje.xml',
        'data/demo/bolsa_horas.xml',
        #'data/demo/peticion_horas.xml',
        'data/demo/incidencia.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
