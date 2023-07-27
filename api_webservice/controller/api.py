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
	

	@http.route('/api/webservice/licitacionadvancelineareport/', type='http', auth="public", methods=['POST'],csrf=False)
	def api_licitacionadvancelineareport_post(self, *args, **kw):
		try:
			user = kw['UserName']
			password = kw['Password']
			data = []
			if user == 'APIJoyaUser' and password == 'Api$pass&256Gt4tHE63':
				sql_id = ""
				if kw['ID'] != '':
					sql_id = "AND ID = %s"%(kw['ID'])
				sql_padre = ""
				if kw['Padre'] != '':
					sql_padre = "AND padre = %s"%(kw['Padre'])
				sql_product_id = ""
				if kw['ProductID'] != '':
					sql_product_id = "AND product_id = %s"%(kw['ProductID'])
				sql_descripcion = ""
				if kw['Descripcion'] != '':
					sql_descripcion = "AND descripcion LIKE '%{descripcion}%'".format(descripcion = kw['Descripcion'])
				sql = """SELECT * FROM licitacion_advance_linea WHERE ID IS NOT NULL %s %s %s %s"""%(sql_id,sql_padre,sql_product_id,sql_descripcion)
				request.env.cr.execute(sql)
				data = request.env.cr.dictfetchall()
				return str(data)
			else:
				rpta = {
					'status':'Error Data',
					'log':'Datos de Conexion erroneos',
				}
				return str(rpta)
		except Exception as err:
			rpta = {
				'status':'Error Process',
				'log':'Datos de Conexion erroneos',
				'detail': str(err),
			}
			return str(rpta)
