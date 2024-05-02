# # -*- coding: utf-8 -*-

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