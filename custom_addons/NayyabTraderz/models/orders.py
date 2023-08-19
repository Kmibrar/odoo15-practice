from odoo import api, fields, models


class orders(models.Model):
    _name = 'nt.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'user details'


    # name =fields.One2many(comodel_name="nt.product", inverse_name='product_id')
    partner_id = fields.Many2one('nt.customer', string='Partner ID')
    order_date = fields.Date(string='Order Date')

    order_id = fields.One2many(comodel_name="nt.product", inverse_name='product_id')
