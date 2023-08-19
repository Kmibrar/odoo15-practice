from odoo import api, fields, models


class OrdersItems(models.Model):
    _name = 'nt.order.items'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'order items details'
    _rec_name = 'order_no'

    order_no =fields.Integer(string='order no')
    customer_name = fields.Many2one('nt.customer',string='customer name')

    my_order_id =fields.One2many('nt.product',inverse_name='product_id2',string='MyOrder')

    price_unit = fields.Float(string='Price')
    qty = fields.Integer(string='Quantity')






