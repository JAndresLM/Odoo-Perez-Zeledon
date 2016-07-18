# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Pesos(models.Model):
	_name = 'aso.pesos'
	name = fields.Char("Hoja de facturación del productor", required=True)
	hoja_socio = fields.Char("Hoja de facturación del socio")
	responsable = fields.Many2one('res.users', string="Responsable",default=lambda self: self.env.user, required=True)
	productor = fields.Many2one('res.partner', string="Productor", required=True)
	prod_propio = fields.Boolean("Producto Propio")
	prod_sociedad = fields.Boolean("Producto en Sociedad")
	socio = fields.Many2one('res.partner', string="Nombre del Socio", required=True)
	fecha = fields.Datetime(string="Fecha", default=fields.Datetime.now)
	producto = fields.Char("Producto")
	pesos_lines_ids = fields.One2many('aso.pesos_lines','name','Líneas de peso')
	observaciones = fields.Text(string="Observaciones") 