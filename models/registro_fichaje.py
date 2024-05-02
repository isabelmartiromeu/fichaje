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

    # code = fields.Char(string='Código', required = True)
    fecha = fields.Date(string='Fecha', required = True,default=date.today(),readonly=True) #Debe tener la fecha de cuando se entra
    hora_entrada = fields.Char(string="Hora de entrada",readonly=True, required = True, default=lambda self:fields.Datetime.now().strftime('%H:%M:%S')) #Debe tener la hora de cuando se entra 

    hora_salida = fields.Char(string='Hora de salida') #No se debe poder rellenar
    
     # Parte de la relación con FICHAJES
     # Un empleado puede realizar muchos fichajes, pero un fichaje pertenece a un solo empleado.
     # empleado [1] : registro_fichaje [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    name = fields.Char(related = 'empleado_id.name')
    

    _sql_constraints = [
        ('fecha_hora_entrada_uniq_fichaje', 'unique(fecha,hora_entrada)', 'La fecha y hora de entrada deben ser únicos'),
        ('code_uniq_fichaje', 'unique(code)', 'El código debe ser único'),
    ]



    @api.model
    def create(self, vals):
        if 'hora_entrada' not in vals:
            vals['hora_entrada'] = fields.Datetime.now().strftime('%H:%M:%S')
        return super(registro_fichaje, self).create(vals)
    

    # @api.onchange('hora_salida')
    # def _onchange_hora_salida(self):
    #     if self.hora_entrada and self.hora_salida:
    #         hora_entrada = datetime.strptime(self.hora_entrada, '%H:%M:%S')
    #         hora_salida = datetime.strptime(self.hora_salida, '%H:%M:%S')
    #         horas_trabajadas = hora_salida - hora_entrada - timedelta(hours=1)  # Restar una hora
    #         if horas_trabajadas.total_seconds() / 3600 > 8:
    #             # Incrementar el campo 'name' del modelo 'bolsa_horas', que guarda el número de horas
    #             # de libre disposición
    #             bolsa_horas = self.env['fichaje.bolsa_horas'].search([('empleado_id', '=', self.empleado_id.id)])
    #             # Redondea hacia abajo el número de más trabajadas.
    #             bolsa_horas.name +=  math.floor(horas_trabajadas) - 8

    def crea_fichaje_salida(self):
        self.hora_salida = fields.Datetime.now().strftime('%H:%M:%S')