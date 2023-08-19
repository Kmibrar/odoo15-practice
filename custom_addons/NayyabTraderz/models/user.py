from odoo import api, fields, models
class user(models.Model):
    _name = 'nt.user'
    _description = 'user details'

    name = fields.Char(string= 'Full Name')
    login = fields.Char(string='User Name')
    email = fields.Char(string='Email')
    password = fields.Char(string= 'Password')
    create_date = fields.Date(string='Date')



