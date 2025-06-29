# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # def get_workflow(self):
    #     workflow = self.env['purchase.workflow'].search([('is_default', '=', True)])
    #     return workflow

    purchase_workflow_id = fields.Many2one(comodel_name="purchase.workflow", string="Workflow", )

    def create_invoice(self):
        if self.purchase_workflow_id.is_create_invoice:
            journal = self.env['account.journal'].search([('type', '=', 'purchase')], limit=1)

            # Prepare the values for the bill (account.move)
            bill_vals = {
                'date': fields.Date.today(),
                'partner_id': self.partner_id.id,
                'ref': self.partner_ref,
                'company_id': self.env.company.id,
                'invoice_payment_term_id': self.payment_term_id.id,
                'currency_id': self.currency_id.id,
                'fiscal_position_id': self.fiscal_position_id.id,
                'journal_id': journal.id,
                'move_type': 'in_invoice',
                'purchase_id': self.id,
            }

            # Create the invoice/bill (this saves it to the database)
            bill = self.env['account.move'].create(bill_vals)

            # Call the auto-complete method after creation (if needed)
            bill._onchange_purchase_auto_complete()

            # Add the created bill to the purchase order's invoice_ids field
            self.invoice_ids = [(4, bill.id)]

    # def create_invoice(self):
    #     """ This Method from addon wedo_auto_invoice
    #         https://apps.odoo.com/apps/modules/13.0/wedo_auto_invoice/
    #     """
    #     if self.purchase_workflow_id.is_create_invoice:
    #         bill = self.env['account.move'].browse()
    #         journal = self.env['account.journal'].search([('move_type', '=', 'purchase')], limit=1)
    #         bill = bill.new({
    #             'date': fields.date.today(),
    #             'partner_id': self.partner_id.id,
    #             'ref': self.partner_ref,
    #             'company_id': self.env.company.id,
    #             'invoice_payment_term_id': self.payment_term_id.id,
    #             'currency_id': self.currency_id.id,
    #             'fiscal_position_id': self.fiscal_position_id,
    #             'journal_id': journal.id,
    #             'move_type': 'in_invoice',
    #             'purchase_id': self.id,
    #         })
    #         bill._onchange_purchase_auto_complete()
    #         self.invoice_ids += bill

    def _get_invoiced(self):
        """
            This Method from addon wedo_auto_invoice
            https://apps.odoo.com/apps/modules/13.0/wedo_auto_invoice/
        """
        if self.purchase_workflow_id.is_create_invoice:
            super(PurchaseOrder, self)._get_invoiced()
            if self.invoice_status == 'to invoice':
                self.create_invoice()
                if self.purchase_workflow_id.is_post_invoice:
                    for invoice in self.invoice_ids:
                        invoice.action_post()
                super(PurchaseOrder, self)._get_invoiced()

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        if self.picking_ids and self.purchase_workflow_id.is_validate_stock:
            for picking in self.picking_ids:
                picking.action_assign()
                picking.action_confirm()
                for mv in picking.move_ids_without_package:
                    mv.quantity_done = mv.product_uom_qty
                picking.button_validate()
        return res
