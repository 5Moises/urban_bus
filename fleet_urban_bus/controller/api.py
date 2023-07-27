# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import json
import pytz
import logging
from datetime import date, datetime, timedelta
from psycopg2 import IntegrityError
from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, Warning, UserError
from odoo.addons.base.models.ir_qweb_fields import nl2br

_logger = logging.getLogger(__name__)

class ApiWebService(http.Controller):

	@http.route('/api/webservice/en_bus_lines/', type='http', auth="public", methods=['GET'],csrf=False)
	def api_licitacionadvancelineareport_post(self, *args, **kw):
		try:
			user = kw['UserName']
			password = kw['Password']
			data = []
			if user == 'API_bus_urban_User' and password == 'Api$pass&256Gt4tHE63':            
				sql = """SELECT color as "Color", 
								id as "Id", 
								longname as "LongName", 
								routenumber as "RouteNumber", 
								stopa as "StopA", 
								stopb as "StopB",
								type as "Type" 
						 FROM fleet_vehicle""" 
				request.env.cr.execute(sql)
				data = request.env.cr.dictfetchall()

				# Construir el resultado final
				result = {
					"Bus": data
				}

				return request.make_response(json.dumps(result), [('Content-Type', 'application/json')])

			else:
				rpta = {
					'status':'Error Data',
					'log':'Datos de Conexion erroneos',
				}
				return request.make_response(json.dumps(rpta), [('Content-Type', 'application/json')])

		except Exception as err:
			rpta = {
				'status':'Error Process',
				'log':'Datos de Conexion erroneos',
				'detail': str(err),
			}
			return request.make_response(json.dumps(rpta), [('Content-Type', 'application/json')])
