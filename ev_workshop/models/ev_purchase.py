# -*- coding: utf-8 -*-
from odoo import fields,models,api,exceptions
import re

class EvPurchase(models.Model):
    _name = "ev.purchase"
    _description = "This is EV Purchase Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # Fields
    name = fields.Char(string="Customer Name",required=True)
    vehicle_type = fields.Selection(
        string="Vehicle Type",
        selection=[('moped','Moped'),('bike','Bike'),('car','Car')]
    )
    color = fields.Selection(
        string="Color",
        selection = [('black','Black'),('white','White'),('silver','Silver')]
    )
    stage = fields.Selection(
        selection = [('new','New'),('purchase','Purchased'),('cancel','Cancel')],
        default = 'new',
        tracking=True,


    )
    contact = fields.Char(string="Contact No.",compute="_compute_contact",store=True,readonly=False)
    address = fields.Text(string="Address")
    subtotal = fields.Float(string="Subtotal (including GST i.e-5%)", readonly=True,compute="_compute_subtotal",store=True)
    price = fields.Float(string="Price of Model", readonly=True, compute="_compute_price",store=True)
    seller_id = fields.Many2one('res.users',string="Seller",default= lambda self: self.env.user)
    # Relational Fields
    company_name_id = fields.Many2one('ev.brands',string="Company Name")
    # purchase_ids = fields.One2many('ev.brand.variants','purchase_id')
    variant_ids = fields.One2many(related="company_name_id.variant_ids")
    # brand_variant_id = fields.Many2one(related='company_name_id.brand_variant_id')
   
    

    @api.depends("variant_ids")
    def _compute_price(self):
        for record in self:
            for variant in record.variant_ids:
                
                if variant.vehicle_type==record.vehicle_type and variant.color==record.color:
                    print("================")
                    # print(variant.vehicle_type)
                    print(variant.price)
                    record.price = variant.price
               

    @api.depends("price")
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.price * 1.05

    @api.depends("contact")
    def _compute_contact(self):
        for record in self:
            print("============")
            print(record.contact)
            if record.contact:
                match = re.match('^[0-9]\d{10}$',record.contact)
            if not match:
                raise exceptions.ValidationError("Invalid Contact Number")

    def action_purchase(self):
        for record in self:
            if  record.stage == 'new':
                record.stage = 'purchase'

    def action_cancel_btn(self):
        for record in self:
            if record.stage == 'new':
                record.stage = 'cancel'