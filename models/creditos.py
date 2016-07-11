# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api

class Creditos(models.Model):
    _name = 'aso.creditos'
    name = fields.Char(string="N° de Crédito", required=True)
    asociado_id = fields.Many2one('res.partner', string="Asociado", required=True, domain=[('asociado', '=', True)])
    fuente_id = fields.Many2one('aso.fuentes', string="Fuente")
    fecha_solicitud = fields.Date(string="Fecha de solicitud", default=fields.Datetime.now)
    actividad= fields.Many2one('aso.actividades_por_asociado',string="Actividad", domain=[('asociado_id', '=', 0)])
    solicitud_c1= fields.Char(string="N° Solicitud C1")
    cosecha = fields.Many2one('aso.cosechas',string="Cosecha")
    monto = fields.Float(string="Monto")
    plazo = fields.Integer(string="Plazo (meses)")
    pagare_vigente= fields.Boolean(string="Pagaré Vigente")
    fecha_aprobacion = fields.Date(string="Fecha de Aprobación")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento")
    observaciones = fields.Text(string="Observaciones")
    state=fields.Selection([
        ('r', "Rechazado"),
        ('ti', "Trámite Inicial"),
        ('a', "Aprobado"),
        ('eu', "Enviado a UPIAV"),
        ('du', "Desembolsado por UPIAV"),
        ('f', "Formalizado"),
        ('pp', "Pago Parcial"),
        ('c', "Cancelado"),],default='ti',string="Estado")

    @api.multi
    def action_tramite_inicial(self):
    	self.state='ti'
    
    @api.multi
    def action_aprobado(self):
    	self.state='a'
    
    @api.multi
    def action_enviado(self):
    	self.state='eu'
    
    @api.multi
    def action_desembolsado(self):
    	self.state='du'
    
    @api.multi
    def action_formalizado(self):
    	self.state='f'
    
    @api.multi
    def action_pago_parcial(self):
    	self.state='pp'
    
    @api.multi
    def action_cancelado(self):
    	self.state='c'
    
    @api.multi
    def action_rechazado(self):
    	self.state='r'
    
    @api.onchange('asociado_id')
    def _get_actividades(self):
		self.actividad = self.env['aso.actividades_por_asociado']
		vals = {}
		if self.asociado_id:
			vals['domain'] = {'actividad':[('asociado_id','=',self.asociado_id.id)]}
		return vals