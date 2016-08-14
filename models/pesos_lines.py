# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Pesos_lines(models.Model):
	_name = 'aso.pesos_lines'
	name = fields.Many2one('aso.pesos', string="Hoja de pesos", ondelete='cascade', required=True)
	humedad = fields.Float(string="Humedad (Kg)")
	subtotal=fields.Float(string='Subtotal (Kg)')
	por_dano = fields.Float(string='Daño (%)')
	merma_dano = fields.Float(string='Merma (Kg)')
	por_humedad = fields.Float(string='Humedad (%)')
	merma_humedad = fields.Float(string='Merma (Kg)')
	total_kg = fields.Float(string='Total Kg')
	total_qq = fields.Float(string='Total QQ')
