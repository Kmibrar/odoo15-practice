from odoo import api, fields, models


class inheritsale(models.Model):
    _inherit = 'sale.order'
    _description = 'extend sale'


    customer_city = fields.Char(string='customer_city')
