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
    monto = fields.Float(string="Monto", compute='_get_monto_plazo')
    plazo = fields.Integer(string="Plazo (meses)", compute='_get_monto_plazo')
    pagare_vigente= fields.Boolean(string="Pagaré Vigente", compute='_esta_vigente')
    fecha_aprobacion = fields.Date(string="Fecha de Aprobación")
    fecha_vencimiento = fields.Date(string="Fecha de Vencimiento", compute='_get_monto_plazo')
    observaciones = fields.Text(string="Observaciones")
    formalizaciones_ids = fields.One2many('aso.formalizaciones','credito_id','Formalizaciones')
    pagos_ids = fields.One2many('aso.pagos','credito_id','Pagos Realizados')
    state=fields.Selection([
        ('r', "Rechazado"),
        ('ti', "Trámite Inicial"),
        ('a', "Aprobado"),
        ('eu', "Enviado"),
        ('du', "Desembolsado"),
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

    @api.depends('asociado_id')
    def _esta_vigente(self):
    	for r in self:
			if r.asociado_id:
				if r.asociado_id.vence_pagare:
					inicio = fields.Datetime.from_string(r.fecha_solicitud)
					fin = fields.Datetime.from_string(r.asociado_id.vence_pagare)
					r.pagare_vigente = ((fin-inicio).days>0)
    
    @api.onchange('asociado_id')
    def _get_actividades(self):
		self.actividad = self.env['aso.actividades_por_asociado']
		vals = {}
		if self.asociado_id:
			vals['domain'] = {'actividad':[('asociado_id','=',self.asociado_id.id)]}
		return vals

    @api.onchange('actividad')
    def _get_monto_plazo(self):
        self.monto = self.actividad.name.credito_fide * self.actividad.area
        self.plazo = self.actividad.name.plazo
        self.fecha_vencimiento = self.fecha_solicitud
		