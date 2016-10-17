# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api

class Formalizaciones(models.Model):
    _name = 'aso.formalizaciones'
    name = fields.Char(string="N° de Formalización", required=True)
    credito_id=fields.Many2one('aso.creditos', string="Crédito",ondelete='cascade')