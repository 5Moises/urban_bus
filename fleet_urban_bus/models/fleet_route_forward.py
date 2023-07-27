from odoo import _, api, fields, models, tools

class fleet_route_forward(models.Model):
    _name = 'fleet.route.forward'
    _description = 'Salidas'

    lon = fields.Float(string="Longitud")
    lat = fields.Float(string="Latitud")
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehiculo',
        )