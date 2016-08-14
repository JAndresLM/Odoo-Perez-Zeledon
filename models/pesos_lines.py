# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class Pesos_lines(models.Model):
	_name = 'aso.pesos_lines'
	name = fields.Many2one('aso.pesos', string="Hoja de pesos", ondelete='cascade', required=True)
	humedad = fields.Float(string="Humedad (Kg)")
	subtotal=fields.Float(string='Subtotal (Kg)')
	por_dano = fields.Float(string='Daño (%)')
	merma_dano = fields.Float(string='Merma (Kg)', readonly=True, compute='_calcular_merma_dano')
	por_humedad = fields.Float(string='Humedad (%)', readonly=True, compute='_calcular_por_humedad')
	merma_humedad = fields.Float(string='Merma (Kg)', readonly=True, compute='_calcular_merma_humedad')
	total_kg = fields.Float(string='Total (Kg)', readonly=True, compute='_calcular_total_line')

	@api.depends('subtotal','por_dano')
	def _calcular_merma_dano(self):
		for r in self:
			r.merma_dano = r.subtotal * (r.por_dano/100)

	@api.depends('subtotal','humedad')
	def _calcular_por_humedad(self):
		for r in self:
			r.por_humedad = 0.0
			if r.humedad > 16:
				r.por_humedad = r.humedad - 16

	@api.depends('subtotal','por_humedad')
	def _calcular_merma_humedad(self):
		for r in self:
			r.merma_humedad = r.subtotal * (r.por_humedad/100)

	@api.depends('subtotal','merma_humedad','merma_dano')
	def _calcular_total_line(self):
		for r in self:
			r.total_kg = r.subtotal - r.merma_humedad - r.merma_dano
