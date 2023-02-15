# -*- coding: utf-8 -*-
from odoo import models,fields

class InheritedProjectTasks(models.Model):
    _inherit = "project.task"

    accept_req = fields.Boolean(string="Accept Request")
    workshop = fields.Many2one('ev.workshop',ondelete = 'cascade')
