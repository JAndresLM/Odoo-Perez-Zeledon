# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Pesos(models.Model):
	_name = 'aso.pesos'
	name = fields.Char("Hoja N°", required=True)
	hoja_productor = fields.Char("Hoja de facturación del productor")
	hoja_socio = fields.Char("Hoja de facturación del socio")
	responsable = fields.Many2one('res.users', string="Responsable",default=lambda self: self.env.user, required=True)
	productor = fields.Many2one('res.partner', string="Productor", required=True)
	prod_sociedad = fields.Boolean("¿Producto en Sociedad?")
	socio = fields.Many2one('res.partner', string="Nombre del Socio")
	fecha = fields.Datetime(string="Fecha y Hora", default=fields.Datetime.now)
	producto = fields.Many2one('product.template', string="Producto")
	pesos_lines_ids = fields.One2many('aso.pesos_lines','name','Líneas de peso')
	total_final_kg = fields.Float(string='Total Kg', readonly=True, compute='_calcular_total_final_kg')
	total_final_qq = fields.Float(string='Total QQ', readonly=True, compute='_calcular_total_final_qq')
	parte = fields.Integer(string="Parte (División)", default=1)
	saldo_productor = fields.Float(string="Saldo Productor QQ", readonly=True, compute='_calcular_saldo_productor')
	saldo_socio = fields.Float(string="Saldo Socio QQ", readonly=True, compute='_calcular_saldo_socio')
	observaciones = fields.Text(string="Observaciones")

	@api.depends('pesos_lines_ids')
	def _calcular_total_final_kg(self):
		for r in self:
			total = 0
			for p in r.pesos_lines_ids:
				total = total + p.total_kg
			r.total_final_kg = total

	@api.depends('total_final_kg')
	def _calcular_total_final_qq(self):
		for r in self:
			r.total_final_qq = r.total_final_kg/46

	@api.depends('total_final_qq','parte','prod_sociedad')
	def _calcular_saldo_productor(self):
		for r in self:
			if r.parte>1 and r.prod_sociedad:
				r.saldo_productor = r.total_final_qq - (r.total_final_qq / r.parte)
			else:
				r.saldo_productor = r.total_final_qq
				r.parte = 1
				r.socio = ''
				r.hoja_socio = ''

	@api.depends('total_final_qq','parte','prod_sociedad')
	def _calcular_saldo_socio(self):
		for r in self:
			if r.parte>1 and r.prod_sociedad:
				r.saldo_socio = r.total_final_qq / r.parte
			else:
				r.saldo_socio = 0
				r.parte = 1
				r.socio = ''
				r.hoja_socio = ''