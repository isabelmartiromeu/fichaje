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
     #_rec_name = 'code'


     code = fields.Char(string='Código', required = True)
     name = fields.Char(string = 'Nombre', required = True)
     _order = 'name'
     
     dni = fields.Char(string = 'DNI', size = 9, required = True)

     fecha_nacimiento = fields.Date(string = 'Fecha nacimiento', required = True)
     direccion = fields.Char(string = 'Direccion')
     movil = fields.Char(string = 'Movil', size = 9, required = True)
     fecha_comienzo_empresa =  fields.Date(string = 'Fecha comienzo en empresa')


     # Parte de la relación con FICHAJES
     # Un empleado puede realizar muchos fichajes, pero un fichaje pertenece a un solo empleado.
     # empleado [1] : registro_fichaje [N]

     fichaje_ids = fields.One2many('fichaje.registro_fichaje','empleado_id')

     # Parte de la relación con Petición de horas
     # Un empleado puede realizar muchas peticiones de horas de libre disposición,
     # pero una petición de hora de libre disposición pertenece a un solo empleado.
     # empleado [1] : peticion_horas [N]
     
     peticion_hora_ids = fields.One2many('fichaje.peticion_horas','empleado_id')

     # Un empleado tiene una bolsa de horas y una bolsa de horas pertenece a un solo empleado
     # empleado [1] : bolsa_horas [1]
     # esto se simula con:
     # empleado [1] : bolsa_horas [N]
     bolsa_hora_ids = fields.One2many('fichaje.bolsa_horas','empleado_id')

     # empleado [N] : bolsa_horas [1]
     la_bolsa_id = fields.Many2one('fichaje.bolsa_horas')
     la_bolsa_name = fields.Char(related = 'la_bolsa_id.code') 



     # Actúan sobre un singleton
     _sql_constraints = [
          ('code_uniq_empleado', 'unique(code)', 'El CÓDIGO debe ser único'),
          ('nom_uniq_empleado', 'unique(name)', 'El NOMBRE debe ser único'),
          ('dni_uniq_empleado', 'unique(dni)', 'El DNI debe ser único'),
          ('movil_uniq_empleado', 'unique(movil)', 'El MOVIL debe ser único'),
     ]