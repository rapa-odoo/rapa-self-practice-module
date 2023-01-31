# -*- coding: utf-8 -*-
from odoo import fields,models

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
    # purchase_id = fields.Many2one('ev.purchase',string="Purchase")
    # purchase_ids = fields.One2many('ev.purchase','p_id')
    # brand_type_id = fields.Many2one(related="brand_variant_id.brand_type_id")
