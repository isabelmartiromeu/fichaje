# # -*- coding: utf-8 -*-

#from datetime import timedelta
#from datetime import datetime
#import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import date_utils

class peticion_horas(models.Model):
    """
    Define una petición de horas
    """

    _name = 'fichaje.peticion_horas'
    _description = 'Petición de horas'

    fecha_disfrute = fields.Date(string='Fecha disfrute', required = True)
    hora_disfrute = fields.Selection([
        ('8', '8:00'),
        ('9', '9:00'),
        ('10', '10:00'),
        ('11', '11:00'),
        ('12', '12:00'),
        ('13', '13:00'),
        ('15', '15:00'),
        ('16', '16:00'),
        ('17', '17:00')
    ], required=True, default='8')

    numero_horas = fields.Integer(string='Número de horas', required = True)
    
            
    estado= fields.Selection([('pendiente','Pendiente'),('aprobada','Aprobada'),('rechazada','Rechazada'),
                            ('disfrutada','Disfrutada'), ('pospuesta','Pospuesta')]) 

     # Parte de la relación con Petición de horas
     # Un empleado puede realizar muchas peticiones de horas de libre disposición,
     # pero una petición de hora de libre disposición pertenece a un solo empleado.
     # empleado [1] : peticion_horas [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    empleado_name = fields.Char(related = 'empleado_id.name')

    # _sql_constraints = [
    #     ('fecha_empleado_disfrute_uniq_peticion_horas', 'unique(fecha_disfrute,empleado_id)', 'No se puede elegir el mismo día de disfrute'),
    # ]

    @api.onchange('fecha_disfrute')
    def _onchange_fecha_disfrute(self):
        for record in self:
            if record.fecha_disfrute:
                if record.fecha_disfrute.weekday() >= 5:  # sábado (5) o domingo (6)
                    record.fecha_disfrute = False
                    return {
                        'warning': {
                            'title': "Advertencia",
                            'message': "La fecha debe ser de un día laborable",
                            'type': 'notification'  # Cambia el tipo a 'notification' si quieres que sea permanente
                        }
                    }

    ###### GITHUB

    # @api.model
    # def _get_next_working_day(self, date):
    #     # Realizará la modificación en la bolsa el día siguiente laborable de la fecha de disfrute
    #     # Retorna el siguiente día laborable a partir de la fecha dada
    #     next_day = date + timedelta(days=1)
    #     while next_day.weekday() in [5, 6]:  # 5 y 6 corresponden al sábado y domingo
    #         next_day += timedelta(days=1)
    #     return next_day

    # @api.model
    # def _get_bolsa_horas(self):
    #     # Retorna el registro de bolsa_horas asociado al empleado
    #     bolsa_horas = self.env['fichaje.bolsa_horas'].search([('empleado_id', '=', self.empleado_id.id)])
    #     return bolsa_horas

    # def _subtract_hours_from_bolsa_horas(self, hours_to_subtract):
    #     # Resta horas del campo name de bolsa_horas
    #     bolsa_horas = self._get_bolsa_horas()
    #     bolsa_horas.name -= hours_to_subtract

    # @api.model
    # def _auto_subtract_hours(self):
    #     # Método que se ejecuta automáticamente al día siguiente laborable de la fecha de disfrute
    #     for peticion in self.search([('fecha_disfrute', '=', self._get_next_working_day(datetime.now().date()))]):
    #         peticion._subtract_hours_from_bolsa_horas(peticion.numero_horas)