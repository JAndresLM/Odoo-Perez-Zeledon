# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class Cosechas(models.Model):
    _name = 'aso.cosechas'
    name = fields.Char(string="Descripción", required=True)
    active = fields.Boolean(string="Activa", default=True)
    acta= fields.Char(string="Acta Junta Directiva")
    fecha = fields.Date(string="Fecha", default=fields.Datetime.now)