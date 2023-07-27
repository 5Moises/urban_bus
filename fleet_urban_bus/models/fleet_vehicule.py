from odoo import _, api, fields, models, tools

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    color = fields.Char(string="Color",default="11518A")
    longname = fields.Char(string="Nombre")
    routenumber = fields.Char(string="Ruta")
    stopa = fields.Char(string="Paradero Inicial")
    stopb = fields.Char(string="Paradero Final")
    type = fields.Char(default="Bus", string="Bus")


    backward_ids = fields.One2many('fleet.route.backward', 'vehicle_id', string="Regresos")
    forward_ids = fields.One2many('fleet.route.forward', 'vehicle_id', string="Salidas")