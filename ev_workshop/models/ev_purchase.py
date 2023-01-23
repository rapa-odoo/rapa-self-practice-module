# -*- coding: utf-8 -*-
from odoo import fields,models

class EvPurchase(models.Model):
    _name = "ev.purchase"
    _description = "This is EV Purchase Model"
    # Fields
    name = fields.Char(string="Customer Name")
    vehicle_type = fields.Selection(
        string="Vehicle Type",
        selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
    )
    # Relational Fields
    company_name_id = fields.Many2one('ev.brands',string="Company Name")