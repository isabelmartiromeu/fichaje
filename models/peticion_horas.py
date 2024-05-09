# # -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

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
    
            
    estado= fields.Selection([('pendiente','Pendiente'),
        ('aprobada','Aprobada'),
        ('rechazada','Rechazada'),
        ('disfrutada','Disfrutada'), 
        ('pospuesta','Pospuesta')
        ],default='pendiente') 

     # Parte de la relación con Petición de horas
     # Un empleado puede realizar muchas peticiones de horas de libre disposición,
     # pero una petición de hora de libre disposición pertenece a un solo empleado.
     # empleado [1] : peticion_horas [N]

    empleado_id = fields.Many2one('fichaje.empleado')
    #empleado_name = fields.Char(related = 'empleado_id.name')
    user_id = fields.Char(related = 'empleado_id.user_id')

    email_responsable = fields.Char(string="Email responsable",default="isamarrom@alu.edu.gva.es",readonly=True)
    pendiente_notificar = fields.Boolean(string="Pendiente de notificar", default=True, readonly=True)

    @api.onchange('fecha_disfrute')
    def _onchange_fecha_disfrute(self):
    # Cuando se elija un día, se comprobará si es un día festivo o si es un día anterior al actual
        for record in self:
            if record.fecha_disfrute:
                # Verifica si la fecha es un sábado (5) o domingo (6)
                if record.fecha_disfrute.weekday() >= 5:
                    record.fecha_disfrute = False
                    return {
                        'warning': {
                            'title': "Advertencia",
                            'message': "La fecha debe ser de un día laborable",
                            'type': 'notification' 
                        }
                    }
                print("Fecha de disfrute: " + record.fecha_disfrute.strftime('%Y-%m-%d'))
                
                # Verifica si la fecha es anterior a la fecha actual
                if record.fecha_disfrute < fields.Datetime.now().date():
                    record.fecha_disfrute = False
                    return {
                        'warning': {
                            'title': "Advertencia",
                            'message': "La fecha no puede ser anterior a la actual",
                            'type': 'notification'  
                        }
                    }



def actualizar_registros(self):
    peticiones = self.env['fichaje.peticion_horas'].search([('pendiente_notificar', '=', True)])
    for peticion in peticiones:
        email_to = peticion.email_responsable
        numero_horas = peticion.numero_horas
        
        if numero_horas > 0:
            if email_to:
                try:
                    mail = self.env['mail.mail'].create({
                        'email_from': 'isamarrom@alu.edu.gva.es',
                        'email_to': email_to,
                        'subject': 'Revisión de petición de horas de libre disposición',
                        'body_html': '<p>Se ha creado o modificado una petición de horas de libre disposición del empleado: %s</p>, se espera aprobación' % peticion.empleado_id,
                    })
                    mail.send()
                except MailDeliveryException as e:
                    raise UserError("Error al enviar el correo electrónico: %s" % str(e))
                except Exception as e:
                    raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))
        else:
            if email_to:
                try:
                    mail = self.env['mail.mail'].create({
                        'email_from': 'isamarrom@alu.edu.gva.es',
                        'email_to': email_to,
                        'subject': 'Eliminación de petición de horas de libre disposición',
                        'body_html': '<p>Se ha eliminado una petición de horas de libre disposición del empleado: %s</p>, se espera aprobación' % peticion.empleado_id,
                    })
                    mail.send()
                except MailDeliveryException as e:
                    raise UserError("Error al enviar el correo electrónico: %s" % str(e))
                except Exception as e:
                    raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))

        # Actualizar el campo pendiente_notificar a False
        peticion.write({'pendiente_notificar': False, 'actualizar_registros': False})

    return False



    @api.model
    def create(self, vals):
    # Se crea un registro 
        record = super(peticion_horas, self).create(vals)
        # Comprueba que se pida alguna hora de disfrute
        for registro in record:
            if registro.numero_horas == 0:
                raise ValidationError("Debes pedir alguna hora de disfrute. No puede tener valor cero")
            else:
                self.actualizar_registros()
                # registro.pendiente_notificar=True

        return record

    def write(self, vals):
    # Se modifica un registro
        res = super(peticion_horas, self).write(vals)
        if self.numero_horas == 0:
             raise ValidationError("Debes pedir alguna hora de disfrute. No puede tener valor cero")
        else:
             self.actualizar_registros()
            #  self.pendiente_notificar=True


        # for record in res:
        #     mi_numero_horas = record.numero_horas
        #     if mi_numero_horas == 0:
        #         raise ValidationError("Debes pedir alguna hora de disfrute. No puede tener valor cero")
        #     else:
        #         self.actualizar_registros()
        #         record.pendiente_notificar=True
        return res

    
    def unlink(self):
        records_with_emails = self.filtered(lambda r: r.email_responsable)
        
        for record in records_with_emails:
            record.numero_horas = 0 #Con esto diferenciamos los registros que piden ser eliminados
            record.pendiente_notificar=True

    
        # Llamamos a super().unlink() fuera del bucle for para que no se quede en un bucle infinito
        return super().unlink()

    def imprimir_informe(self):
	     return self.env.ref('mantenprev.peticion_horas_pdf_report').report_action(self)