# -*- coding: utf-8 -*-
from odoo import models,fields
from dateutil.relativedelta import relativedelta

class EvMechanic(models.Model):
    _inherit = "ev.workshop"

    def action_request(self):
        print("##########")

        if self.need_mechanic:
            if not self.env['project.project'].search([('name','=',self.available_mechanic.name)]):
                self.env['project.project'].create({
                'name': self.available_mechanic.name
                })
            project = self.env['project.project'].search([('name','=',self.available_mechanic.name)])
            ev_task = self.env['project.task'].create({
                'name': "Customer Name: "+ self.name,
                'project_id': project.id,
                'description': "Brand Name: "+self.brand.name+ ", Problem: "+self.description,
                'date_deadline': fields.datetime.now() + relativedelta(days=1)
            })

        return super().action_request()

