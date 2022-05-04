# -*- coding: utf-8 -*-
from odoo import api, fields, models


# class Task(models.Model):
#     _inherit='project.task'
#
#     kanban_state = fields.Selection([
#         ('normal', 'In Progress'),
#         ('done', 'Ready'),
#         ('bad', 'Bad'),
#         ('good', 'Good'),
#         ('blocked', 'Blocked')], string='Status',
#         copy=False, default='normal', required=True)
