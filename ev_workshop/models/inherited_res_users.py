# -*- coding: utf-8 -*-

from odoo import fields,models

class InheritedResUsers(models.Model):
    _inherit = 'res.users'

    purchase_ids = fields.One2many('ev.purchase','seller_id',string="Purchase Orders")