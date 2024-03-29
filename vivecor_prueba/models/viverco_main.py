from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError, Warning, UserError


class viverco_main(models.Model):

	_name = 'viverco.main'
	_description = 'Viverco SAC'


	name = fields.Char(string = "Nombre", traking=1)
	state = fields.Selection([  ('draft', 'Borrador'),
								('aproved', 'Aprobado'),
								('cancel', 'Cancelado')], string="Estado", traking=1)
	descrip = fields.Text(string=u"Descripción",traking=1)
	date_create = fields.Datetime(string = "Fecha de Registro", traking=1)
	date_update = fields.Datetime(string="Fecha de Actualización",traking=1)

	#@api.model
	#def create(self, values):        
	#	result = super().create(values)
	#	self.asig_date()
	#	return result
	

   
	
	def unlink(self):
		res = super().unlink()
		
		return res

	#def asig_date(self):
	#	for i in self:
	#		if not i.date_create:
	#			
	#		if  fields.Date.today() !=  i.date_update:
	#			i.date_update =  fields.Date.today()


	def get_aproved():
		for i in self:
			i.state = "aproved"

	def get_cancel():
		for i in self:
			i.state = "cancel"     
			