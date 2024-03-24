# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Peticionhoras(models.Model):
     """
     Define una petición de horas
     """

     _name = 'fichajes.peticionhoras'
     _description = 'Petición de horas'
  
     fechadisfrute = fields.Date(string='Fecha disfrute', required = True)
     horacomienzo = fields.Datetime(string='Hora comienzo', required = True)
     numerohoras = fields.Integer(string='Número de horas', required = True)
          
     estado= fields.Selection([('PEN','Pendiente'),('APR','Aprobada'),('RECH','Rechazada'),
                              ('DISF','Disfrutada'), ('POST','Pospuesta')]) 

     # peticionhoras [N] : [1]empleado 
     #estamos en la parte de la N

     empleado_id = fields.Many2one('fichajes.empleado')    
     empleado_name = fields.Char(related = 'fichajes.nombre')

     _sql_constraints = [
          ('cod_uniq_peticion', 'unique(code)', 'El código debe ser único'),
     ]
