# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Actividades(models.Model):
	_name = 'aso.actividades'
	name = fields.Char(string="Nombre", required=True)
	credito_fide=fields.Float(string='Crédito Fideicomiso [x Ha]')
	credito_abar=fields.Float(string='Crédito Abarrotes [x Ha]')
	credito_insu=fields.Float(string='Crédito Insumos [x Ha]')
	plazo=fields.Float(string='Plazo [Meses]')
	tasa_anual=fields.Float(string='Tasa Anual [%]')
	precio=fields.Float(string='Precio [x QQ]')