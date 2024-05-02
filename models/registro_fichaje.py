# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
import time

class registro_fichaje(models.Model):
    """
    Define un fichaje
    """
    
    _name = 'fichaje.registro_fichaje'
    _description = 'fichaje.registro_fichaje'


    code = fields.Char(string='Código', required = True)
    fecha = fields.Date(string='Fecha', required = True,default=date.today(),readonly=True) #Debe tener la fecha de cuando se entra
    hora_entrada = fields.Char(string="Hora de entrada", required = True) #Debe tener la hora de cuando se entra 

    hora_salida = fields.Char(string='Hora de salida') #No se debe poder rellenar
    
     # Parte de la relación con FICHAJES
     # Un empleado puede realizar muchos fichajes, pero un fichaje pertenece a un solo empleado.
     # empleado [1] : registro_fichaje [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    empleado_name = fields.Char(related = 'empleado_id.name')
    

    _sql_constraints = [
        ('fecha_hora_entrada_uniq_fichaje', 'unique(fecha,hora_entrada)', 'La fecha y hora de entrada deben ser únicos'),
        ('code_uniq_fichaje', 'unique(code)', 'El código debe ser único'),
    ]


    @api.model
    def create(self, vals):
        if 'hora_entrada' not in vals:
            vals['hora_entrada'] = fields.Datetime.now().strftime('%H:%M:%S')
        return super(registro_fichaje, self).create(vals)