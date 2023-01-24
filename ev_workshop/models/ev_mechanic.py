# -*- coding: utf-8 -*-
from odoo import fields,models

class EvMechanic(models.Model):
    _name = "ev.mechanic"
    _description = "This is EV Mechanic Model"

    name = fields.Char(string="Name")
    experience = fields.Float(string="Years of Experience")
    location= fields.Selection(
        string="Location",
        selection=[
            ('ahmedabad','Ahmedabad'),('delhi','Delhi'),('mumbai','Mumbai'),('banagalore','Bangalore')
        ]
    )
    description = fields.Text(string="Description")
