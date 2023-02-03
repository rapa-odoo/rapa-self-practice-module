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
    available_mechanic = fields.Many2one('ev.mechanic',domain="[('location','=',city)]",store=True,readonly=False)
    assigned_mechanic = fields.Char(string="Assigned Mechanic",readonly=True,store=True)
    mechanic_id = fields.Many2one('ev.workshop')
   
    def action_request(self):
        for record in self:
            print(record.city)
            if record.maintenance_stage == 'new' and record.need_mechanic== True:
                record.maintenance_stage = 'req_recieved'
                record.assigned_mechanic = record.available_mechanic.name
            elif record.maintenance_stage == 'new' and record.need_mechanic == False:
                record.maintenance_stage = 'in_prog'
    
    
            
                    
