
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bolsa_horas(models.Model):
    """
    Define una escuela
    """

    _name = 'fichaje.bolsa_horas'
    _description = 'fichaje.bolsa_horas'
    # _rec_name = 'code'


    code = fields.Char(required = True, string='Código empleado', store=True)
    horas = fields.Integer(string='Horas de libre disposición')


     # Un empleado tiene una bolsa de horas y una bolsa de horas pertenece a un solo empleado
     # empleado [1] : bolsa_horas [1]
     # esto se simula con:
     
     # empleado [1] : bolsa_horas [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    empleado_name = fields.Char(related = 'empleado_id.name')



     # empleado [N] : bolsa_horas [1]
    
    el_empleado_ids = fields.One2many('fichaje.empleado','la_bolsa_id')

    _sql_constraints = [
        ('code_uniq_bolsa_horas', 'unique(code)', 'El código debe ser único'),
    ]


    @api.onchange('empleado_id')
    def _onchange_empleado_id(self):
        if self.empleado_id:
            empleados = self.env['fichaje.empleado'].search([('code', '=', self.empleado_id.code)])
            self.code = empleados.code
