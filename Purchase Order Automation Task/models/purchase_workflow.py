# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseWorkflow(models.Model):
    _name = 'purchase.workflow'
    _rec_name = 'name'
    _description = 'Purchase Workflow'

    name = fields.Char()
    is_default = fields.Boolean()
    is_create_invoice = fields.Boolean()
    is_post_invoice = fields.Boolean()
    is_validate_stock = fields.Boolean()
