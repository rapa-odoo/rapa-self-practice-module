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
    
    workshop_ids = fields.One2many('ev.workshop','available_mechanic')
    task_ids = fields.One2many('ev.workshop','task_id')
    task_counts = fields.Integer(compute="_compute_task")

    def _compute_task(self):
        for record in self:
            record.task_counts = len(record.workshop_ids)

    def project_redirect(self):
        # breakpoint()

        for record in self:
            
            res=  {
                'name': ("Projects"),
                'type': 'ir.actions.act_window',
                'res_model': 'project.project',
                # 'res_id': 
                'view_mode': 'kanban',
                
                
            }
            return res
    