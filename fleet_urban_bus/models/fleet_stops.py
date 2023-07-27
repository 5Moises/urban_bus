from odoo import _, api, fields, models, tools

class FleetStops(models.Model):
    _name = 'fleet.stops'
    _description = 'Paraderos'

    name = fields.Char(string="Nombre")
    direccion = fields.Char(string="Direccion")
    forward = fields.Boolean(default=True)
    lon = fields.Float(string="Longitud")
    lat = fields.Float(string="Latitud")
    type = fields.Char(default="Bus")
    has_board = fields.Boolean(default=True)
    virtual = fields.Boolean(default=True)
    timetable_ids = fields.One2many('fleet.timetable', 'stop_id', string="Horario")
    