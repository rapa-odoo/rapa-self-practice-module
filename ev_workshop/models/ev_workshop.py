# -*- coding: utf-8 -*-
from odoo import fields,models,api

class EvWorkshop(models.Model):
    _name = "ev.workshop"
    _description = "This is EV Workshop Model"
    # Fields
    name = fields.Char(string="Name",required=True)
    year_purchased = fields.Char(string="Year Purchased",default= lambda self : fields.datetime.now().year)
    description = fields.Text(string="Description")
    maintenance_stage = fields.Selection(
        string="Maintenance Stage",
        selection=[
            ('new','New'),('req_recieved','Request Recieved'),('req_accepted','Request Accepted'),('in_prog','In Progress'),('done','Done')
        ],
        default='new',
    )
    brand = fields.Many2one('ev.brands',string="Model Brand")
    vehicle_type = fields.Selection(
        string="Vehicle Type",
        selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
    )
    address = fields.Text(string="Address")
    city = fields.Char(string="City")
    need_mechanic = fields.Boolean(string="Need a Mechanic")
    available_mechanic = fields.Many2one('ev.mechanic',compute="_compute_mechanics",readonly=False)

    
