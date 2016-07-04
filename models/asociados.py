from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    asociado = fields.Boolean("Asociado", default=False)