# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api

class Pagos(models.Model):
    _name = 'aso.pagos'
    name = fields.Char(string="N° de Pago", required=True)
    credito_id=fields.Many2one('aso.creditos', string="Crédito",ondelete='cascade')
    fecha_pago = fields.Date(string="Fecha de pago", default=fields.Datetime.now)
    fecha_efectiva = fields.Date(string="Fecha Efectiva")
    dias_cobrados = fields.Integer(string='Días cobrados')
    monto_pagar = fields.Float(string='Monto a pagar')
    forma_pago = fields.Selection([
        ('ef', "Efectivo"),
        ('ch', "Cheque"),],string="Forma de Pago")
    cheque = fields.Char(string='N° de Cheque')