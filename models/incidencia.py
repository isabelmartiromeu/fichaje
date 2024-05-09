# # -*- coding: utf-8 -*-

# # incidencia
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import re 
import datetime

class incidencia(models.Model):
     """
     Define una incidencia
     """  

     _name = 'fichaje.incidencia'
     _description = 'incidencia'


     asunto = fields.Selection([
        ('fichaje', 'Fichaje'),
        ('bolsa', 'Bolsa horas'),
        ('peticion', 'Petición horas'),
        ('incidencias', 'Incidencias')
    ], required=True, default='fichaje')

     fecha_incidencia = fields.Date(string = 'Fecha incidencia', required = True)

     estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('revisada', 'Revisada'),
        ('postpuesta', 'Postpuesta')
    ], required=True, default='pendiente')

     observaciones = fields.Text(string="Observaciones")

     # Un empleado puede tener muchas incidencias, pero una incidencia solo corresponde a un empleado
     # empleado [1] - incidencia [N]
     empleado_id = fields.Many2one('fichaje.empleado')
     #empleado_name = fields.Char(related = 'empleado_id.name') 
     user_id = fields.Char(related = 'empleado_id.user_id')
