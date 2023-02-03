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
            ('ahmedabad','Ahmedabad'),('delhi','Delhi'),('mumbai','Mumbai'),('bangalore','Bangalore')
        ]
    )
    description = fields.Text(string="Description")
    
    workshop_ids = fields.One2many('ev.workshop','mechanic_id')

    
