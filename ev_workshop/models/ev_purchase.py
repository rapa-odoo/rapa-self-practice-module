# -*- coding: utf-8 -*-
from odoo import fields,models,api

class EvPurchase(models.Model):
    _name = "ev.purchase"
    _description = "This is EV Purchase Model"
    # Fields
    name = fields.Char(string="Customer Name")
    vehicle_type = fields.Selection(
        string="Vehicle Type",
        selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
    )
    color = fields.Selection(
        string="Color",
        selection = [('black','Black'),('white','White'),('grey','Grey'),('silver','Silver')]
    )
    contact = fields.Char(string="Contact No.")
    address = fields.Text(string="Address")
    subtotal = fields.Float(string="Subtotal", readonly=True)
    price = fields.Float(string="Price of Model", readonly=True, compute="_compute_price",store=True)
    seller_id = fields.Many2one('res.users',string="Seller",default= lambda self: self.env.user)
    # Relational Fields
    company_name_id = fields.Many2one('ev.brands',string="Company Name")
    purchase_ids = fields.One2many('ev.brand.variants','purchase_id')

    @api.depends("purchase_ids","company_name_id")
    def _compute_price(self):
        for record in self:
            if record.company_name_id==record.purchase_ids.brand_variant_id :
                record.price = record.purchase_ids.price
            