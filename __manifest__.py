# -*- coding: utf-8 -*-
{
    'name': "State Selection Colors",
    'author': 'Rising Systems',
    'summary': 'This module add more colors when using the widget state_selection',
    'description': """
Adding more colors to state_selection widget on odoo
====================================================
Default odoo state_selection widget is giving 3 colors when used on state field:
    - Gray >> when state value is 'normal'
    - Green >> when state value is 'done'
    - Red >> when state value is 'blocked'
    .. image:: /state_selection_colors/static/description/before.png
    
With this module we can add more colrs:
    - Gray >> when state value is 'normal'
    - Green >> when state value is 'done'
    - Red >> when state value is 'blocked'
    - Yellow >> when state value is 'status_yellow'
    - Blue >> when state value is 'status_blue'

Just add the desired color to your state field like:
      state = fields.Selection([('blocked', 'Red'),('status_yellow', 'Yello'),
      ('done', 'Green'),
      ('status_blue', 'Blue'),
      ('normal', 'Gray')], default='normal', tracking=True)
And in the xml use the widget = 'state_selection' on the state field
now the state field will be shown like this
    .. image:: /state_selection_colors/static/description/after.png

            """,
    'website': 'http://www.rising-systems.de/',
    'version': '15.0.0.1',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'project'],
    'assets': {
        'web.assets_backend': [
            'state_selection_colors/static/src/scss/views.scss',
            'state_selection_colors/static/src/js/state.js'
        ]
    },
    'price': 4.99,
    'price': 'EUR',

}
