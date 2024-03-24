# -*- coding: utf-8 -*-

# Empleado
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import re 
import datetime

class Empleado(models.Model):
     """
     Define un empleado
     """  

     _name = 'fichajes.empleado'
     _description = 'Empleado'
     _rec_name = 'code'
     _order = 'name'

     code = fields.Char(string='Código', required = True)
     name = fields.Char(string = 'Nombre', required = True)

     dni = fields.Char(string = 'DNI', size = 9)

     fechanacimiento = fields.Date(string = 'Fecha nacimiento', required = True)
     direccion = fields.Char(string = 'Direccion')
     movil = fields.Char(string = 'Movil', size = 9)
     fechacomienzoempresa =  fields.Date(string = 'Fecha comienzo en empresa')

     #Parte de la relación con PETICIONHORAS
     #peticionhoras [N] : [1]empleado 
     peticionhoras_ids = fields.One2many('fichajes.peticionhoras','empleado_id')

     #Parte de la relación con FICHAJES
     # empleado [N] : [1]fichajes
     #estamos en la parte de la N

     fichajes_id = fields.Many2one('fichajes.fichaje')  

     #La clave principal en fichajes es code
     fichajes_fecha = fields.Char(related = 'fichajes_id.code')


     #Parte de la relación con BOLSAHORAS

     # empleado [1] : [1] bolsahoras. 
     # Simulamos: bolsahoras [N] : [1] empleado  Y empleado [N] : [1] bolsahoras

     #programando la parte de la N
     #bolsahoras [N] : [1] empleado

     bolsahoras_id = fields.Many2one('fichajes.bolsahoras')
     bolsahoras_codigo = fields.Char(related = 'bolsahoras_id.code')

     #programando la parte de la 1 empleado [N] : [1] bolsahoras
     bolsahorasUno_ids = fields.One2many('fichajes.bolsahoras','empleUno_ids')

     #Conexión con BOLSAHORAS



     # Actúan sobre un singleton
     _sql_constraints = [
          ('nom_uniq', 'unique(name)', 'El NOMBRE debe ser único'),
          ('dni_uniq', 'unique(dni)', 'El DNI debe ser único'),
          ('movil_uniq', 'unique(movil)', 'El MOVIL debe ser único'),
     ]