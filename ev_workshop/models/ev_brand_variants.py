# -*- coding: utf-8 -*-
from odoo import fields,models,api,exceptions

class EvBrandVariants(models.Model):
    _name = "ev.brand.variants"
    _description = "This is EV Brand Variant Model"
    _order = "vehicle_type"

    # Fields
    vehicle_type = fields.Selection(
            string="Vehicle Type",
            selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
        )
    price = fields.Float(string="Price of Model")
    color = fields.Selection(
        string="Color",
        selection=[('black','Black'),('white','White'),('silver','Silver')]
    )
    # Relational Fields
    brand_variant_id = fields.Many2one('ev.brands',string="Brand")
    
    # @api.model
    # def create(self,vals):
    #     res = self.env['ev.brands'].browse(vals['brand_variant_id'])
    #     print("===========")
    #     print(res.name)
    #     print(vals['color'])
    #     print(vals['vehicle_type'])
    #     if vals['color'] in vals['vehicle_type']:
    #         raise exceptions.ValidationError("hhhhhh")


    #     return super().create(vals)
        


        
