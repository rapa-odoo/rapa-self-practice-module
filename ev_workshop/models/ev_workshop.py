# -*- coding: utf-8 -*-
from odoo import fields,models,api

class EvWorkshop(models.Model):
    _name = "ev.workshop"
    _description = "This is EV Workshop Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
        tracking=True,
    )
    brand = fields.Many2one('ev.brands',string="Model Brand")
    vehicle_type = fields.Selection(
        string="Vehicle Type",
        selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
    )
    address = fields.Text(string="Address")
    city = fields.Selection(
        string="Location",
        selection=[
            ('ahmedabad','Ahmedabad'),('delhi','Delhi'),('mumbai','Mumbai'),('bangalore','Bangalore')
        ]
    )
    need_mechanic = fields.Boolean(string="Need a Mechanic")
    available_mechanic = fields.Many2one('ev.mechanic',domain="[('location','=','ahmedabad')]")
    
    # print("===============")
    # print(mechanic_ids.name)
    def action_request(self):
        for record in self:
            if record.maintenance_stage == 'new':
                record.maintenance_stage = 'req_recieved'
    # compute="_compute_mechanic"
    # domain="[('location','=',workshop_ids.city)]"

    @api.depends("mechanic_ids","city")
    def _compute_mechanic(self):
        for record in self:
            for mechanic in record.mechanic_ids:
                if mechanic.location == mechanic.workshop_ids.city:
                    print("============")
                    print(mechanic.workshop_ids.city)
                
                    
