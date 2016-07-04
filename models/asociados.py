# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    asociado = fields.Boolean("Asociado", default=False)
    actividades_ids= fields.One2many('aso.actividades_por_asociado','asociado_id','Actividades del Asociado')
    cedula = fields.Char(string="Cédula")