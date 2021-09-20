# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class QuantPackage(models.Model):
    _inherit = "stock.quant.package"

    location_name = fields.Many2one('stock.location', 'Location', related="location_id.name")
