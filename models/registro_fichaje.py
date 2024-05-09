# -*- coding: utf-8 -*-
from datetime import date, timedelta
from odoo import models, fields, api
from datetime import datetime, timedelta
import math

import pytz

class registro_fichaje(models.Model):
    """
    Define un fichaje
    """
    
    _name = 'fichaje.registro_fichaje'
    _description = 'fichaje.registro_fichaje'


    fecha = fields.Date(string='Fecha', required = True,default=date.today(),readonly=True) #Debe tener la fecha de cuando se entra
    _order = 'fecha'

    hora_entrada = fields.Char(string="Hora de entrada",readonly=True, required = True, default=lambda self:fields.Datetime.now().strftime('%H:%M:%S')) #Debe tener la hora de cuando se entra 

    hora_salida = fields.Char(string='Hora de salida',readonly=True) #No se debe poder rellenar
    
     # Parte de la relación con FICHAJES
     # Un empleado puede realizar muchos fichajes, pero un fichaje pertenece a un solo empleado.
     # empleado [1] : registro_fichaje [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    name = fields.Char(related = 'empleado_id.name')
    user_id = fields.Char(related = 'empleado_id.user_id')

    _sql_constraints = [
        ('fecha_hora_empleado_uniq_fichaje', 'unique(fecha,hora_entrada,empleado_id)', 'La fecha y hora de entrada deben ser únicos para cada empleado'),
    ]

    def crea_fichaje_salida(self):
    # Va a contralar si se han realizado horas de más para aumentar las horas
    # de libre disposición en bolsa_horas.
        if not self.hora_salida: #Si ya hay algo no se ejecuta el código
            timezone_es = pytz.timezone('Europe/Madrid')
            hora_actual = fields.Datetime.now(timezone_es)
            # En formato string:
            hora_salida_dt = hora_actual.strftime('%H:%M:%S')

            #En formato hora:
            hora_salida_dt = datetime.strptime(hora_salida_dt, "%H:%M:%S")

            hora_entrada_dt = datetime.strptime(self.hora_entrada, "%H:%M:%S")

            # Restamos la hora de salida menos la hora de entrada
            diferencia_horas = hora_salida_dt - hora_entrada_dt

            diferencia_horas = (diferencia_horas.total_seconds() / 3600)  # Convertir a horas
            #  Restamos una hora para comer, redondeando hacia abajo
            diferencia_horas = math.floor(diferencia_horas) - 1


            # Solo suma la diferencia de horas a la bolsa de horas si es mayor que 8
            if diferencia_horas > 8:
                if self.empleado_id:
                    bolsa_horas_obj = self.env['fichaje.bolsa_horas']
                    bolsa_horas = bolsa_horas_obj.search([('empleado_id', '=', self.empleado_id.id)], limit=1)
                    if bolsa_horas:
                        bolsa_horas.horas += diferencia_horas - 8
                    else:
                        bolsa_horas_obj.create({
                            'empleado_id': self.empleado_id.id,
                            'horas': diferencia_horas,
                        })
            else:
                # Si no llega a las 8 horas trabajadas, crea un nuevo registro en el modelo incidencia
                if self.empleado_id:
                    incidencia_obj = self.env['fichaje.incidencia']
                    incidencia_obj.create({
                        'asunto': 'fichaje',  # Puedes cambiar esto según necesites
                        'fecha_incidencia': fields.Date.today(),  # O usa la fecha que necesites
                        'estado': 'pendiente',  # O usa el estado que necesites
                        'observaciones': 'Horas insuficientes',  # O agrega observaciones según necesites
                        'empleado_id': self.empleado_id.id,
                    })

            # Actualizar la hora de salida en el registro de fichaje
            self.hora_salida = fields.Datetime.now().strftime('%H:%M')
        
    def imprimir_informe(self):
	     return self.env.ref('mantenprev.registro_fichaje_pdf_report').report_action(self)

