# -*- coding: utf-8 -*-
from odoo import models,Command

class EvInvoice(models.Model):
    _inherit = "ev.purchase"

    def action_purchase(self):
        print("=========")
        print(self.name)
        ev_invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'invoice_line_ids': [Command.create({
                'name': self.company_name_id.name,
                'price_unit': self.subtotal
            })

            ]
        })
        return super().action_purchase()