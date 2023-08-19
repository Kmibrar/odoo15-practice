from odoo import api, fields, models
class products(models.Model):
    _name = 'nt.product'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'user details'
    _rec_name = 'product_id'

    product_id = fields.Many2one(comodel_name='nt.order')
    product_id2 = fields.Many2one(comodel_name='nt.order.items')
    name = fields.Char(string='Name', tracking=True)
    description = fields.Text(string='Description')
    list_price = fields.Char(string= 'List Price')
    qty_available = fields.Integer(string='Quantity Available')
    create_date = fields.Date(string='Create Date')


class extendsale(models.Model):
    _inherit = 'sale.order'
    _description = 'extend sale'

    customer_city = fields.Char(string='customer_city')
