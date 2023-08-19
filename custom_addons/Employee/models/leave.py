from odoo import api, models, fields

class leave(models.Model):
    _name = 'employee.leave'
    _description = 'Employee Leave'

    leave_id = fields.Integer(string='Employee Leave')
    emp_id = fields.Integer(string='Employee ID')
    Date = fields.Date(string='Leave Date')
    reason = fields.Text(string='Leave Reason')
