# -*- coding; utf-8 -*-
from odoo import http
from odoo.http import request


class OrderTracking(http.Controller):
    @http.route(['/order'], type='http', auth='user', website='True')
    def create_order(self, **post):
        """function for creating delivery transfer based on condition"""
        tracking_number = post.get('tracking_number')
        if tracking_number:
            website_request = request.env['stock.picking'].sudo().search(
                [('website_id', '!=', False), ('name', 'ilike',
                                               tracking_number), ('partner_id',
                                                                 '=', request.env.user.partner_id.id)])
            values = {
                'website_request': website_request,
            }
            return request.render("order_tracking.online_order_list", values)
        else:
            website_request = (request.env['stock.picking'].sudo().
                               search([('website_id', '!=', False),
                                       ]))
            values = {
                'website_request': website_request,
            }
            return request.render("order_tracking.online_order_list", values)
