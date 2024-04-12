# # -*- coding: utf-8 -*-

# # Empleado
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import re 
import datetime

class empleado(models.Model):
     """
     Define un empleado
     """  

     _name = 'fichaje.empleado'
     _description = 'Empleado'
     _rec_name = 'code'
     _order = 'name'

     code = fields.Char(string='Código', required = True)
     name = fields.Char(string = 'Nombre', required = True)

     dni = fields.Char(string = 'DNI', size = 9)

     fecha_nacimiento = fields.Date(string = 'Fecha nacimiento', required = True)
     direccion = fields.Char(string = 'Direccion')
     movil = fields.Char(string = 'Movil', size = 9)
     fecha_comienzo_empresa =  fields.Date(string = 'Fecha comienzo en empresa')


     #Parte de la relación con FICHAJES
     # empleado [N] : [1]fichajes
     #estamos en la parte de la N

     #fichajes_id = fields.Many2one('fichaje.registro_fichaje')  

     #La clave principal en fichajes es code
     #fichajes_fecha = fields.Char(related = 'fichajes_id.code')


     # Actúan sobre un singleton
     _sql_constraints = [
          ('nom_uniq', 'unique(name)', 'El NOMBRE debe ser único'),
          ('dni_uniq', 'unique(dni)', 'El DNI debe ser único'),
          ('movil_uniq', 'unique(movil)', 'El MOVIL debe ser único'),
     ]