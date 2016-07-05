# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    asociado = fields.Boolean("Asociado", default=False)
    actividades_ids= fields.One2many('aso.actividades_por_asociado','asociado_id','Actividades del Asociado')
    cedula = fields.Char(string="Cédula")
    cred_abarrotes=fields.Boolean("Crédito Abarrotes", default=False)
    lim_cred_abarrotes=fields.Float("Limite Crédito Abarrotes")
    cred_insumos=fields.Boolean("Crédito Insumos", default=False)
    lim_cred_insumos=fields.Float("Limite Crédito Insumos")
    proveedor_granos=fields.Boolean("Proveedor Granos", default=False)
    fiadores_ids=fields.Many2many('aso.fiadores',string='Fiadores')
    vence_pagare=fields.Date("Vencimiento Pagaré")