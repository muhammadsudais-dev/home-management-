# -*- coding: utf-8 -*-
# from odoo import http


# class HomeManagement(http.Controller):
#     @http.route('/home_management/home_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/home_management/home_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('home_management.listing', {
#             'root': '/home_management/home_management',
#             'objects': http.request.env['home_management.home_management'].search([]),
#         })

#     @http.route('/home_management/home_management/objects/<model("home_management.home_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('home_management.object', {
#             'object': obj
#         })

