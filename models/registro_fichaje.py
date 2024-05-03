# -*- coding: utf-8 -*-
from datetime import date, timedelta
from odoo import models, fields, api
from datetime import datetime, timedelta
import math

class registro_fichaje(models.Model):
    """
    Define un fichaje
    """
    
    _name = 'fichaje.registro_fichaje'
    _description = 'fichaje.registro_fichaje'


    fecha = fields.Date(string='Fecha', required = True,default=date.today(),readonly=True) #Debe tener la fecha de cuando se entra
    _order = 'fecha'

    hora_entrada = fields.Char(string="Hora de entrada",readonly=True, required = True, default=lambda self:fields.Datetime.now().strftime('%H:%M:%S')) #Debe tener la hora de cuando se entra 
    #hora_entrada = fields.Char(string="Hora de entrada",required = True) #Debe tener la hora de cuando se entra 


    hora_salida = fields.Char(string='Hora de salida') #No se debe poder rellenar
    
     # Parte de la relación con FICHAJES
     # Un empleado puede realizar muchos fichajes, pero un fichaje pertenece a un solo empleado.
     # empleado [1] : registro_fichaje [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    name = fields.Char(related = 'empleado_id.name')
    

    _sql_constraints = [
        ('fecha_hora_entrada_uniq_fichaje', 'unique(fecha,hora_entrada)', 'La fecha y hora de entrada deben ser únicos'),
    ]


    def crea_fichaje_salida(self):
        self.hora_salida = fields.Datetime.now().strftime('%H:%M:%S')
        # if self.hora_entrada and self.hora_salida:
        #     h_entrada = datetime.strptime(self.hora_entrada, '%H:%M:%S')
        #     h_salida = datetime.strptime(self.hora_salida, '%H:%M:%S')
        #     # Calculamos la diferencia de tiempo
        #     diferencia = h_salida - h_entrada

        #     # Obtenemos la diferencia en horas enteras
        #     horas_enteras =  math.floor(diferencia.total_seconds() // 3600)
        #     if horas_enteras > 0:
        #         bolsa_horas = self.env['fichaje.bolsa_horas'].search([('empleado_id', '=', self.empleado_id.name)])
        #         bolsa_horas.horas += horas_enteras

