# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

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
	total_final_kg = fields.Float(string='Total Kg', readonly=True)
	total_final_qq = fields.Float(string='Total QQ', readonly=True)
	parte = fields.Integer(string="Parte (División)", default=1)
	saldo_productor = fields.Float(string="Saldo Productor QQ", readonly=True)
	saldo_socio = fields.Float(string="Saldo Socio QQ", readonly=True)
	observaciones = fields.Text(string="Observaciones") 