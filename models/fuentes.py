# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class Fuentes(models.Model):
    _name = 'aso.fuentes'
    name = fields.Char(string="Descripción", required=True)