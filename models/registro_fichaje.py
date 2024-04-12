# -*- coding: utf-8 -*-
from odoo import models, fields, api

class registro_fichaje(models.Model):
    """
    Define un fichaje
    """
    
    _name = 'fichaje.registro_fichaje'
    _description = 'fichaje.registro_fichaje'
    _rec_name = 'code'

    code = fields.Char(string='Código', required = True)
    fecha = fields.Date(string='Fecha', required = True) #Debe tener la fecha de cuando se entra
    hora_entrada = fields.Datetime(string='Hora de entrada', required = True) #Debe tener la hora de cuando se entra 
    hora_salida = fields.Datetime(string='Hora de salida') #No se debe poder rellenar
    
     # empleado [N] : [1]fichajes 
    #empleado_ids = fields.One2many('fichaje.empleado','fichajes_id')
    

    # _sql_constraints = [
    #     ('fecha_hora_entrada_uniq', 'unique(fecha,hora_entrada)', 'La fecha y hora de entrada deben ser únicos'),
    #     ('code_uniq_fichaje', 'unique(code)', 'El código debe ser único'),
    # ]