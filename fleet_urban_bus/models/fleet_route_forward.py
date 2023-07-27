from odoo import _, api, fields, models, tools

class fleet_route_forward(models.Model):
    _name = 'fleet.route.forward'
    _description = 'Salidas'

    lon = fields.Char(string="Longitud")
    lat = fields.Char(string="Latitud")
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehiculo',
        )