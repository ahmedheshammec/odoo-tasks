# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderAutomation(http.Controller):
#     @http.route('/purchase_order_automation/purchase_order_automation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_automation/purchase_order_automation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_automation.listing', {
#             'root': '/purchase_order_automation/purchase_order_automation',
#             'objects': http.request.env['purchase_order_automation.purchase_order_automation'].search([]),
#         })

#     @http.route('/purchase_order_automation/purchase_order_automation/objects/<model("purchase_order_automation.purchase_order_automation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_automation.object', {
#             'object': obj
#         })
