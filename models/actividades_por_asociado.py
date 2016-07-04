# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

class Actividades_por_Asociado(models.Model):
	_name = 'aso.actividades_por_asociado'
	#name = fields.Char(string="Nombre")
	asociado_id=fields.Many2one('res.partner', string="Asociado",ondelete='cascade', domain=[('asociado', '=', True)])
	actividad=fields.Many2one('aso.actividades', string="Actividad",ondelete='set null', required=True)
	area=fields.Float(string='Area')
	tenencia=fields.Selection([
        ('p', "Propio"),
        ('a', "Alquilado"),
        ('o', "Otro"),
    ])
	ubicacion=fields.Char(string='Ubicación')