from odoo import api, fields, models


class customers(models.Model):
    _name = 'nt.customer'
    _description = 'user details'
    _rec_name = 'fname'

    customer_id = fields.Integer(string='Customer ID')
    user_id = fields.Many2one('nt.user', string='User')
    fname = fields.Char(string='First Name')
    lname = fields.Char(string='Last Name')
    address = fields.Char(string='Address')
    phone_no = fields.Integer(string='Phone No')
