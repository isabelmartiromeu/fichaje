
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bolsa_horas(models.Model):
    """
    Define una escuela
    """

    _name = 'fichaje.bolsa_horas'
    _description = 'fichaje.bolsa_horas'
    _rec_name = 'code'


    code = fields.Char(required = True, string='Código empleado')
    name = fields.Integer(string='Horas de libre disposición')

    #Parte de la relación con EMPLEADO
    # empleado [1] : [1] bolsahoras. 
    # Simulamos: bolsahoras [N] : [1] empleado  Y empleado [N] : [1] bolsahoras

    #programando la parte de la N
    #bolsahoras [N] : [1] empleado

    #empleado_id = fields.Many2one('fichaje.empleado')
    #empleado_name = fields.Char(related = 'empleado_id.name')

    #programando la parte de la 1 empleado [N] : [1] bolsahoras
    #empleUno_ids = fields.One2many('fichaje.empleado','bolsahoras_id')

    
    _sql_constraints = [
        ('code_uniq_bolsa_horas', 'unique(code)', 'El código debe ser único'),
    ]