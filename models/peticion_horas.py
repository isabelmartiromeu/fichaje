# # -*- coding: utf-8 -*-

from datetime import timedelta
import datetime
from odoo import models, fields, api

class peticion_horas(models.Model):
    """
    Define una petición de horas
    """

    _name = 'fichaje.peticion_horas'
    _description = 'Petición de horas'
    _rec_name = 'code'

    code = fields.Char(string='Código', required = True)
    fecha_disfrute = fields.Date(string='Fecha disfrute', required = True)
    hora_comienzo = fields.Datetime(string='Hora comienzo', required = True)
    numero_horas = fields.Integer(string='Número de horas', required = True)
            
    estado= fields.Selection([('PEN','Pendiente'),('APR','Aprobada'),('RECH','Rechazada'),
                            ('DISF','Disfrutada'), ('POST','Pospuesta')]) 

     # Parte de la relación con Petición de horas
     # Un empleado puede realizar muchas peticiones de horas de libre disposición,
     # pero una petición de hora de libre disposición pertenece a un solo empleado.
     # empleado [1] : peticion_horas [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    empleado_name = fields.Char(related = 'empleado_id.name')


    _sql_constraints = [
        ('cod_uniq_peticion_horas', 'unique(code)', 'El código debe ser único'),
    ]



    @api.model
    def _get_next_working_day(self, date):
        # Realizará la modificación en la bolsa el día siguiente laborable de la fecha de disfrute
        # Retorna el siguiente día laborable a partir de la fecha dada
        next_day = date + timedelta(days=1)
        while next_day.weekday() in [5, 6]:  # 5 y 6 corresponden al sábado y domingo
            next_day += timedelta(days=1)
        return next_day

    @api.model
    def _get_bolsa_horas(self):
        # Retorna el registro de bolsa_horas asociado al empleado
        bolsa_horas = self.env['fichaje.bolsa_horas'].search([('empleado_id', '=', self.empleado_id.id)])
        return bolsa_horas

    def _subtract_hours_from_bolsa_horas(self, hours_to_subtract):
        # Resta horas del campo name de bolsa_horas
        bolsa_horas = self._get_bolsa_horas()
        bolsa_horas.name -= hours_to_subtract

    @api.model
    def _auto_subtract_hours(self):
        # Método que se ejecuta automáticamente al día siguiente laborable de la fecha de disfrute
        for peticion in self.search([('fecha_disfrute', '=', self._get_next_working_day(datetime.now().date()))]):
            peticion._subtract_hours_from_bolsa_horas(peticion.numero_horas)
