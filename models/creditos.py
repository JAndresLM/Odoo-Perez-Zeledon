# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api

class Creditos(models.Model):
    _name = 'aso.creditos'
    name = fields.Char(string="N° de Crédito", required=True)
    asociado_id = fields.Many2one('res.partner', string="Asociado", required=True, domain=[('asociado', '=', True)])
    fuente_id = fields.Many2one('aso.fuentes', string="Fuente")
    fecha = fields.Datetime(string="Fecha de solicitud", default=fields.Datetime.now)
    actividad= fields.Many2one('aso.actividades_por_asociado',string="Actividad", domain=[('asociado_id', '=', 0)])

    @api.onchange('asociado_id')
    def _get_actividades(self):
        self.actividad = self.env['aso.actividades_por_asociado']
        vals = {}
        if self.asociado_id:
            vals['domain'] = {
                'actividad': [('asociado_id', '=', self.asociado_id.id)]
            }
        return vals