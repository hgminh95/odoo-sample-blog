# -*- coding: utf-8 -*-
{
    'name': "blog",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "hgminh95",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/article_views.xml',
        'views/article_templates.xml',

        'views/readlist_views.xml',

        'views/wizard.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
