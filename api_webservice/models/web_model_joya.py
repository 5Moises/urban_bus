# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning, UserError


class WebModelJoya(models.TransientModel):
	_name = 'web.model.joya'

	def make_liquidation(self,values):
		liq_obj = self.env['purchase.liquidation.it']

		liq_search = liq_obj.sudo().search([
			('lote','=',values.get('lote')),
			('company_id','=',int(values.get("company_id")))
		], limit=1)

		zone_id = self.find_zone(values.get("zona"),values.get("company_id"))
		collector_id = self.find_collector(values.get("collector"),values.get("company_id"))
		product_id = self.find_product(values.get("material"))
		grupo_id = self.find_grupo(values.get("grupo"),values.get("company_id"))

		if liq_search:
			self.make_liquidation_line(values,liq_search)
			liq_search.write({'date_reception' : values.get('date_reception')})
			liq_search.write({'zone_id' : zone_id})
			liq_search.write({'collector_id' : collector_id})
			liq_search.write({'doc_partner' : values.get('doc_partner')})
			liq_search.write({'name_partner' : values.get('name_partner')})
			liq_search.write({'weight_tmh' : values.get('weight_tmh')})
			liq_search.write({'h2o' : values.get('h2o')})
			liq_search.write({'weight_tm' : values.get('weight_tm')})
			liq_search.write({'ley_au' : values.get('ley_au')})
			liq_search.write({'ley_ag' : values.get('ley_ag')})
			liq_search.write({'material' : product_id})
			liq_search.write({'group_analitic_id' : grupo_id})
			return True
		else:
			
			liq_id = liq_obj.sudo().create({
				'lote': values.get('lote'),
				'date_reception': values.get('date_reception'),
				'zone_id': zone_id,
				'collector_id': collector_id,
				'doc_partner': values.get('doc_partner'),
				'name_partner': values.get('name_partner'),
				'weight_tmh': values.get('weight_tmh'),
				'h2o': values.get('h2o'),
				'weight_tm': values.get('weight_tm'),
				'ley_au': values.get('ley_au'),
				'ley_ag': values.get('ley_ag'),
				'material': product_id,
				'group_analitic_id': grupo_id,
				'company_id': values.get('company_id'),
			})
			self.make_liquidation_line(values,liq_id)
			return True

	def make_liquidation_line(self,values,liq_id):
		liq_line_obj = self.env['purchase.liquidation.it.line']

		liq_line_search = liq_line_obj.sudo().search([
			('main_id','=',liq_id.id),
			('status_liquidation','=',str(values.get('status_liquidation')))
		], limit=1)
		
		if liq_line_search:
			liq_line_search.write({
			'type_liquidation': str(values.get('type_liquidation')),
			'ley_au_liq': values.get('ley_au_liq'),
			'ley_ag_liq': values.get('ley_ag_liq'),
			'h2o_liq': values.get('h2o_liq'),
			'pseco_liq': values.get('pseco_liq'),
			'rec_au': str(values.get('rec_au')),
			'price_au': str(values.get('price_au')),
			'margen_pi': str(values.get('margen_pi')),
			'maquila': str(values.get('maquila')),
			'consumo_q': str(values.get('consumo_q')),
			'gast_adm': str(values.get('gast_adm')),
			'sobre_costo': str(values.get('sobre_costo')),
			'rec_ag': str(values.get('rec_ag')),
			'price_ag': str(values.get('price_ag')),
			'margen_ag': str(values.get('margen_ag')),
			'calc_esp': values.get('calc_esp'),
			'cost_total': values.get('cost_total'),
			'cost_analysis': values.get('cost_analysis'),
			'discount': values.get('discount'),
			'nbase_au': values.get('nbase_au'),
			'nbase_ag': values.get('nbase_ag'),
			'person_prop': str(values.get('person_prop')),
			'date_prop': values.get('date_prop'),
			'lot_vol': values.get('lot_vol'),
			})
		else:
			vals = {
				'status_liquidation': str(values.get('status_liquidation')),
				'type_liquidation': str(values.get('type_liquidation')),
				'ley_au_liq': values.get('ley_au_liq'),
				'ley_ag_liq': values.get('ley_ag_liq'),
				'h2o_liq': values.get('h2o_liq'),
				'pseco_liq': values.get('pseco_liq'),
				'rec_au': str(values.get('rec_au')),
				'price_au': str(values.get('price_au')),
				'margen_pi': str(values.get('margen_pi')),
				'maquila': str(values.get('maquila')),
				'consumo_q': str(values.get('consumo_q')),
				'gast_adm': str(values.get('gast_adm')),
				'sobre_costo': str(values.get('sobre_costo')),
				'rec_ag': str(values.get('rec_ag')),
				'price_ag': str(values.get('price_ag')),
				'margen_ag': str(values.get('margen_ag')),
				'calc_esp': values.get('calc_esp'),
				'cost_total': values.get('cost_total'),
				'cost_analysis': values.get('cost_analysis'),
				'discount': values.get('discount'),
				'nbase_au': values.get('nbase_au'),
				'nbase_ag': values.get('nbase_ag'),
				'person_prop': str(values.get('person_prop')),
				'date_prop': values.get('date_prop'),
				'lot_vol': values.get('lot_vol'),
			}
			liq_id.write({'line_ids' :([(0,0,vals)]) })
		return True

	def make_zone(self,values):
		zone_obj = self.env['model.zone.it']

		zone_search = zone_obj.sudo().search([
			('code','=',values.get('code')),
			('company_id','=',int(values.get("company_id")))
		], limit=1)

		account_analytic_id = self.find_account_analytic(values.get("cta_analitica"),values.get("company_id"))

		if zone_search:
			zone_search.write({'name' : values.get('name')})
			zone_search.write({'account_analytic_id' : account_analytic_id})
			return True
		else:
			
			zone_search = zone_obj.sudo().create({
				'code': values.get('code'),
				'name': values.get('name'),
				'account_analytic_id': account_analytic_id,
				'company_id': values.get('company_id'),
			})
			return True
	
	def make_collector(self,values):
		collector_obj = self.env['model.collector.it']

		collector_search = collector_obj.sudo().search([
			('code','=',values.get('code')),
			('company_id','=',int(values.get("company_id")))
		], limit=1)

		if collector_search:
			collector_search.write({'name' : values.get('name')})
			return True
		else:
			
			collector_search = collector_obj.sudo().create({
				'code': values.get('code'),
				'name': values.get('name'),
				'company_id': values.get('company_id'),
			})
			return True
	
	def make_groups(self,values):
		group_obj = self.env['purchase.liquidation.group']

		group_search = group_obj.sudo().search([
			('item','=',values.get('item')),
			('company_id','=',int(values.get("company_id")))
		], limit=1)

		account_analytic_id = self.find_account_analytic(values.get("cta_analitica"),values.get("company_id"))

		if group_search:
			group_search.write({'name' : values.get('name')})
			group_search.write({'analytic_id' : account_analytic_id})
			return True
		else:
			group_search = group_obj.sudo().create({
				'item': values.get('item'),
				'name': values.get('name'),
				'analytic_id': account_analytic_id,
				'company_id': values.get('company_id'),
			})
			return True

	def find_account_analytic(self,code,company):
		if not code:
			return None
		analytic_obj = self.env['account.analytic.account']
		analytic_search = analytic_obj.sudo().search([('code', '=', str(code)),('company_id','=',int(company))],limit=1)
		if analytic_search:
			return analytic_search.id
		else:
			raise Warning(_('No existe una Cuenta Analitica con el Codigo "%s" en esta Compañia') % code)


	def find_zone(self,code,company):
		if not code:
			return None
		zone_obj = self.env['model.zone.it']
		zone_search = zone_obj.sudo().search([('code', '=', str(code)),('company_id','=',int(company))],limit=1)
		if zone_search:
			return zone_search.id
		else:
			raise Warning(_('No existe una Zona con el Codigo "%s" en esta Compañia') % code)
	
	def find_grupo(self,code,company):
		if not code:
			return None
		group_obj = self.env['purchase.liquidation.group']
		group_search = group_obj.sudo().search([('item', '=', int(code)),('company_id','=',int(company))],limit=1)
		if group_search:
			return group_search.id
		else:
			raise Warning(_('No existe un Grupo con el Item "%s" en esta Compañia') % code)

	def find_collector(self,code,company):
		if not code:
			return None
		collector_obj = self.env['model.collector.it']
		collector_search = collector_obj.sudo().search([('code', '=', str(code)),('company_id','=',int(company))],limit=1)
		if collector_search:
			return collector_search.id
		else:
			raise Warning(_('No existe un Acopiador con el Codigo "%s" en esta Compañia') % code)

	def find_product(self,code):
		if not code:
			return None
		product_obj = self.env['product.product']
		product_search = product_obj.sudo().search([('default_code', '=', str(code))],limit=1)
		if product_search:
			return product_search.id
		else:
			raise Warning(_('No existe un Producto con el Codigo "%s"') % code)