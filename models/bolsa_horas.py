
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bolsa_horas(models.Model):
    """
    Define una escuela
    """

    _name = 'fichaje.bolsa_horas'
    _description = 'fichaje.bolsa_horas'


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

    user_id = fields.Char(related = 'empleado_id.user_id')

    horas = fields.Integer(string='Horas de libre disposición')


    _sql_constraints = [
        ('empleado_id_uniq_bolsa_horas', 'unique(empleado_id)', 'El empñeado debe ser único'),
        ('code_uniq_bolsa_horas', 'unique(code)', 'El empñeado debe ser único'),
    ]


    @api.onchange('empleado_id')
    def _onchange_empleado_id(self):
        if self.empleado_id:
            empleados = self.env['fichaje.empleado'].search([('name', '=', self.empleado_id.name)])
            self.user_id = empleados.user_id

    def imprimir_informe(self):
	     return self.env.ref('mantenprev.bolsa_horas_pdf_report').report_action(self)