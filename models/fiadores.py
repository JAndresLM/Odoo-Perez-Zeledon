# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class Fiadores(models.Model):
    _name = 'aso.fiadores'
    name = fields.Char(string="Nombre", required=True)
    cedula = fields.Char(string="Cédula")
    telefono= fields.Char(string="Telefono")
    correo = fields.Char(string="Correo")