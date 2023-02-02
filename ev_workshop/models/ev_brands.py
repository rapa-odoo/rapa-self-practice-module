# -*- coding: utf-8 -*-
from odoo import fields,models

class EvBrands(models.Model):
    _name = "ev.brands"
    _description = "This is EV Brands Model"
    # Fields
    name = fields.Char(string="Brand")
    description = fields.Text(string="Description about Brand") 
    image = fields.Binary(string="Brand Logo")
    # Relational Fields
    variant_ids = fields.One2many('ev.brand.variants','brand_variant_id')
    
    # order_count = fields.Integer(compute="_compute_order_count",string="Orders")
    _sql_constraints = [
        ('unique_name','unique(name)','There happens to be an existing brand name, Give a unique name!')
        ]

    # def _compute_order_count(self):
    #     for record in self:
    #         record.order_count = len(record.order_ids)
    