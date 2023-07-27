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
	def get_en_bus_lines(self, *args, **kw):
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

			
	@http.route('/api/webservice/paraderos/', type='http', auth="public", methods=['GET'],csrf=False)
	def getparaderos(self, *args, **kw):
		try:
			user = kw['UserName']
			password = kw['Password']
			data = []
			if user == 'API_bus_urban_User' and password == 'Api$pass&256Gt4tHE63':            
				sql = """SELECT  
								id as "StopId", 
								name as "Name", 
								direccion as "Direccion", 
								forward as "Forward", 
								lon as "Lon",
								lat as "Lat",
								type as "Type",
								has_board as "HasBoard",
								virtual as "Virtual"
						 FROM fleet_stops""" 
				request.env.cr.execute(sql)
				data = request.env.cr.dictfetchall()

				# Construir el resultado final
				result = {
					"Stops": data
				}

				return request.make_response(json.dumps(data), [('Content-Type', 'application/json')])

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

	@http.route('/api/webservice/rutas/', type='http', auth="public", methods=['GET'],csrf=False)	
	def getrutas(self, *args, **kw):
		try:
			user = kw['UserName']
			password = kw['Password']
			codigo_ruta = kw['code_ruta']
			id_o_vuelta = kw['type_ruta']
			data = []
			if user == 'API_bus_urban_User' and password == 'Api$pass&256Gt4tHE63':            
				sql = ""
				if id_o_vuelta == "forward":
					sql = """SELECT  								
								frf.lon as "longitude",
								frf.lat as "latitude"							
						 FROM fleet_route_forward frf
						 LEFT JOIN fleet_vehicle fv ON fv.id = frf.vehicle_id
						 where fv.routenumber = %s"""%(str("'"+str(codigo_ruta)+"'"))
				if id_o_vuelta == "backward":
					sql = """SELECT  
								frb.lon as "longitude",
								frb.lat as "latitude"	
						 FROM fleet_route_backward frb
						 LEFT JOIN fleet_vehicle fv ON fv.id = frb.vehicle_id
						 where fv.routenumber = %s"""%(str("'"+str(codigo_ruta)+"'"))

				 
				request.env.cr.execute(sql)
				data = request.env.cr.dictfetchall()				
				return request.make_response(json.dumps(data), [('Content-Type', 'application/json')])

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



	@http.route('/api/webservice/horario/', type='http', auth="public", methods=['GET'],csrf=False)	
	def gethorario(self, *args, **kw):
		try:
			user = kw['UserName']
			password = kw['Password']
			codigo_paradero = kw['id_paradero']			
			data = []
			if user == 'API_bus_urban_User' and password == 'Api$pass&256Gt4tHE63':            
				
				sql = """SELECT
						fv.routenumber as "RouteNumber",								
						ft.destinationstopname as "DestinationStopName",
						ft.arrivaltime as "ArrivalTime"							
						FROM fleet_timetable ft
						LEFT JOIN fleet_vehicle fv ON fv.id = ft.routenumber_id
						where ft.stop_id = %d"""% (int(codigo_paradero))


				 
				request.env.cr.execute(sql)
				data = request.env.cr.dictfetchall()
				result = {
					"stationId": str(codigo_paradero),
    				"stationName": "Estación A",
					"ArrivalTime": data
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



