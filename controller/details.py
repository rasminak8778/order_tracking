from odoo import http
from odoo.http import request


class Details(http.Controller):
    @http.route(['/details/<int:web_id>/'], type='http',
                auth="public", website=True)
    def order(self, web_id):
        """function for retrieving the delivery order object with id and show
        the details in webpage"""
        data = request.env['stock.picking'].sudo().browse(web_id)
        values = {
            'data': data
        }
        print('new value',values)
        return request.render("order_tracking.online_details_form",
                              values)
