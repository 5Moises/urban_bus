from odoo import _, api, fields, models, tools

class fleet_route_backward(models.Model):
    _name = 'fleet.route.backward'
    _description = 'Regreso'

    
    lon = fields.Float(string="Longitud", digits=(64,12))
    lat = fields.Float(string="Latitud", digits=(64,12))
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehiculo',
        )