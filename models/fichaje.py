# -*- coding: utf-8 -*-

from odoo import models, fields, api


from odoo import models, fields, api

class Fichaje(models.Model):
    """
    Define un fichaje
    """
    
    _name = 'fichajes.fichaje'
    _description = 'Fichaje'
    _rec_name = 'code'

    code = fields.Char(string='Código', required = True)
    fecha = fields.Date(string='Fecha', required = True) #Debe tener la fecha de cuando se entra
    horaentrada = fields.Datetime(string='Hora de entrada', required = True) #Debe tener la hora de cuando se entra 
    horasalida = fields.Datetime(string='Hora de salida') #No se debe poder rellenar
    
     # empleado [N] : [1]fichajes 
    empleado_ids = fields.One2many('fichajes.empleado','fichajes_id')
    

    _sql_constraints = [
        ('fechahoraentrada_uniq', 'unique(fecha,horaentrada)', 'La fecha y hora de entrada deben ser únicos'),
        ('code_uniq_fichaje', 'unique(code)', 'El código debe ser único'),
    ]