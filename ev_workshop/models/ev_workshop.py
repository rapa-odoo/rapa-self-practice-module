# -*- coding: utf-8 -*-
from odoo import fields,models

class EvWorkshop(models.Model):
    _name = "ev.workshop"
    _description = "This is EV Workshop Model"
    # Fields
    name = fields.Char(string="Name",required=True)