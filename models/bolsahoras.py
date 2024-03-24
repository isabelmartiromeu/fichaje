
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Bolsahoras(models.Model):
    """
    Define una escuela
    """
    
    _name = 'fichajes.bolsahoras'
    _description = 'Bolsa de horas'
    _rec_name = 'code'


    code = fields.Char(string='Código')
    numerohoras = fields.Integer(string='Número de horas')

    #Parte de la relación con EMPLEADO
    # empleado [1] : [1] bolsahoras. 
    # Simulamos: bolsahoras [N] : [1] empleado  Y empleado [N] : [1] bolsahoras

    #programando la parte de la N
    #bolsahoras [N] : [1] empleado

    empleado_id = fields.Many2one('fichajes.empleado')
    empleado_name = fields.Char(related = 'empleado_id.name')

    #programando la parte de la 1 empleado [N] : [1] bolsahoras
    empleUno_ids = fields.One2many('fichajes.empleado','bolsahoras_id')

    
    _sql_constraints = [
        ('code_uniq_bolsa', 'unique(code)', 'El código debe ser único'),
    ]