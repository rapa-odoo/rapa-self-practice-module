# -*- coding: utf-8 -*-
from odoo import fields,models,api,exceptions
import re

class EvPurchase(models.Model):
    _name = "ev.purchase"
    _description = "This is EV Purchase Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _inherits = {'ev.brands':'total_id'}
    # Fields
    name = fields.Char(string="Customer Name")
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
    contact = fields.Char(string="Contact No.")
    address = fields.Text(string="Address")
    subtotal = fields.Float(string="Subtotal (including GST i.e-5%)", readonly=True,compute="_compute_subtotal",store=True)
    price = fields.Float(string="Price of Model", readonly=True, compute="_compute_price",store=True)
    seller_id = fields.Many2one('res.users',string="Seller",default= lambda self: self.env.user)
    # Relational Fields
    company_name_id = fields.Many2one('ev.brands',string="Company Name",domain="[('id','=',active_id)]")
    variant_ids = fields.One2many(related="company_name_id.variant_ids")
   
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

    @api.constrains("contact")
    def _check_contact(self):
        for record in self:
            if record.contact and len(record.contact) != 10:
                raise exceptions.ValidationError("Invalid Contact")

    def action_purchase(self):
        for record in self:
            if  record.stage == 'cancel':
                raise exceptions.UserError("Cancelled Orders can't be reverted back to Purchase Orders!")
            record.stage = 'purchase'

    def action_cancel_btn(self):
        for record in self:
            if record.stage == 'purchase':
                raise exceptions.UserError("Purchase Orders can't be Cancelled!")
            record.stage = 'cancel'

    # @api.model
    # def create(self,vals):
    #     res = self.env['ev.brands'].browse(vals['company_name_id'])
    #     print("------------")
    #     print(res.order_ids)

    # @api.depends("price")
    # def compute_total(self):
    #     for record in self:
    #         record.total= sum(record.variant_ids.mapped('price'))
                