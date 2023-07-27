from odoo import _, api, fields, models, tools

class fleet_timetable(models.Model):
    _name = 'fleet.timetable'
    _description = 'Horarios'

  

    stop_id = fields.Many2one(
        'fleet.stops',
        string='Bus',
    )
    routenumber_id = fields.Many2one(
        'fleet.vehicle',
        string='Bus',
    )
    arrivaltime = fields.Char(string="Hora")
    destinationstopname = fields.Selection([('ida', 'Ida'),('salida', 'Salida'),('i/s', 'I/S')])
    