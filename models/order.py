# -*- coding: utf-8 -*-
from odoo import fields, models


class Order(models.Model):
    _inherit = ['stock.picking']

    loc_id = fields.Many2one('stock.location', string="From")
    des_id = fields.Many2one('stock.location', string="To")



