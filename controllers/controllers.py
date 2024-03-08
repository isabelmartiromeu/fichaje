# -*- coding: utf-8 -*-
# from odoo import http


# class Fichajes(http.Controller):
#     @http.route('/fichajes/fichajes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fichajes/fichajes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fichajes.listing', {
#             'root': '/fichajes/fichajes',
#             'objects': http.request.env['fichajes.fichajes'].search([]),
#         })

#     @http.route('/fichajes/fichajes/objects/<model("fichajes.fichajes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fichajes.object', {
#             'object': obj
#         })
