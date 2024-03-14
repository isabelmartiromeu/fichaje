---
layout: default
---
# - Modulo Fichaje -
## Descripción corta. 
Este módulo se utilizará para controlar el fichaje de los trabajadores de la empresa y tener en cuenta las horas trabajadas al día para generar horas de libre disposición. Controlando además las incidencias que se puedan generar.

## Descripción detallada de todas las funcionalidades a cubrir.
A través de este módulo se pretende llevar un control del registro de fichajes de las entradas y salidas de los trabajadores a la empresa cada día, para ello se deberá tener en cuenta los siguientes requisitos:
Cuando el trabajador entra con su usuario a la aplicación Odoo, se realiza de forma automática el fichaje de entrada. Además, se muestra un mensaje en el que se muestra la información sobre el fichaje: día y hora de entrada. La pantalla por defecto que se carga en pantalla es la de los fichajes.
En la opción de menú de fichajes que se muestra por defecto, se puede visualizar los últimos 5 fichajes. Además, dispone de un botón que permite registrar el fichaje de salida.
En caso de que caiga el sistema o se reinicie el ordenador por un corte eléctrico, al volver a registrarse el usuario en el sistema, no se fichará la entrada, ya que no ha habido fichaje de salida.
En caso de que un trabajador fiche la salida y vuelva a entrar en otro momento del mismo día, se volverá a realizar un fichaje de entrada, generando un nuevo fichaje en el mismo día.
El trabajador no debe fichar cuando vaya a comer, ya que está estipulado un tiempo de una hora y media al día para esto.
Cuando el trabajador ficha la salida, se realiza un cálculo de las horas que el trabajador ha estado en su puesto de trabajo. Si se realiza más de un fichaje al día, se suman el tiempo al fichaje anterior.
El fichaje diario quedará como el tiempo entre el fichaje de la entrada y la salida, restando una hora y media de la comida.
En caso de que el tiempo de permanencia en su puesto de trabajo supere los 60 minutos y múltiplos de este, se incrementarán las horas de libre disposición del trabajador.
Como el trabajador puede solicitar el disfrute de las horas de libre disposición en un día concreto, cuando se realiza el fichaje de salida y se calcula el tiempo de permanencia en su puesto de trabajo, se tendrá en cuenta las horas de libre disposición solicitadas y disfrutadas, para que no se genere ninguna incidencia.
En caso de que el fichaje atestigüe que el trabajador ha permanecido menos de 8 horas de trabajo en su puesto de trabajo, se generará un registro de incidencia, en la tabla que solo podrá ser consultada por el departamento de recursos humanos. Además, se mandará un email a la persona encargada de supervisar este tipo de incidencias.
El trabajador podrá acceder a ver un resumen de los últimos cinco fichajes que ha realizado (de los últimos cinco días laborales). En caso de detectar alguna anomalía, podrá acceder a la opción de menú de "Incidencias" y generar una petición de revisión, para que el error sea subsanado o incluso podrá adjuntar un justificante de la falta de asistencia. Así mismo podrá eliminar una incidencia creada por él anteriormente.
El trabajador podrá acceder a la consulta de la bolsa de horas de libre disposición acumuladas, donde podrá ver las horas de libre disposición que le quedan por disfrutar.
Existe también una opción de menú de petición de las horas de libre disposición: el trabajador pedirá las horas por unidades separadas, con lo que, si quiere disfrutar de dos horas seguidas, deberá realizar dos peticiones sobre el mismo día. Las peticiones tendrán los siguientes estados: pendiente, aprobada, rechazada, disfrutada, pospuesta.  Al solicitar la petición, estará en el estado "pendiente".
El trabajador podrá cambiar el estado de las peticiones solamente para posponerlas. En este caso, al día siguiente la petición será eliminada.
Una vez pasado el día de disfrute de las horas de libre disposición, serán eliminadas las horas de la bolsa de horas de libre disposición.
El trabajador podrá acceder a la opción de menú "Informes", donde podrá realizar dos tipos de consultas:
  - Relacionadas con las horas de libre disposición:
  - Sobre los días en los que se han acumulado horas de libre disposición.
  - Sobre los días que se han disfrutado horas de libre disposición
  - Incidencias generadas y resolución.
- Relacionadas con los fichajes:
  - Últimos fichajes realizados: últimos 10 días, 15 días, 20 días, 25 días o 30 días.
  - Incidencias generadas y resolución.
## Mapa del módulo
Las diferentes opciones de menú que se pueden encontrar en el módulo de fichajes, son las siguientes:
![](mapa_modulo_fichajes.png)
## Dependencias con otros módulos
El módulo de fichajes tiene relación con los módulos:
- Empleados
## Wireframes de las páginas a mostrar. 
Existe un menú que permite acceder a las diferentes acciones que se pueden realizar en el módulo. La vista que se muestra por defecto es la siguiente.
Listado de fichajes de un empleado:
![](boceto_listado_fichajes.png)


## Control de accesos. 
### Departamentos
Departamentos existentes en la empresa:
- Producción
- Mantenimiento preventivo
- Mantenimiento correctivo
- Comercial
- Contabilidad
- Recursos Humanos

Cada departamento tiene un responsable.

### Grupos

Habrá un grupo por departamento; otro para todos los responsables de cualquier departamento; un grupo por responsables de cada departamento.

### Permisos

Módulo de fichaje:

|Funcionalidad|Departamento|Tipo de permiso|
| :-: | :-: | :-: |
|Fichaje de entrada|Todos|Insertar|
|Fichaje de salida|Todos|Insertar|
|Consultar horas libres|Todos|Consultar|
|Solicitar horas libres|Todos|Insertar|
|Crear incidencia fichaje|Todos|Insertar, Consultar, Imprimir|
|Crear incidencia horas libres|Todos|Insertar, Consultar, Imprimir|
|Autorizar horas libres|Recursos humanos|Editar|
|Consultar incidencias horas|Recursos humanos|Editar, Borrar, Consultar, Imprimir|
|Consultar incidencias fichajes|Recursos humanos|Editar, Borrar, Consultar, Imprimir|

## Diagramas de flujo funcionales de las diferentes partes del módulo. 

### Opción del menú del listado de fichajes

Al entrar en la aplicación se verá si ya se ha realizado un fichaje ese mismo día, en caso de que no sea así, se registrará la entrada al trabajo. En caso de que ya se haya fichado ese mismo día, se verá si hay un fichaje de salida, en caso de que sí que haya, significa que el sistema ha caído y se están reiniciando los ordenadores, en caso de que haya un fichaje de salida, se vuelve a fichar la entrada y queda a la espera del fichaje de salida.

Al acceder al menú de fichajes, aparece un resumen de los últimos 5 fichajes realizados. Tendremos la oportunidad de fichar la salida.

Es posible que se haya fichado más de una vez la entrada y salida a la empresa, por lo que se tendrán que sumar las horas para tener el cómputo de la jornada laboral diaria. Del mismo modo, es posible que se haya disfrutado del permiso por hora de libre disposición, con lo que también se sumarán al cómputo de horas y así saber si se han cubierto de forma correcta el resto de horas.

![](diagr_flujo_fichaje.png)

### Opción del menú de petición de horas de libre disposición

Al entrar aparecerá el listado de las horas de libre disposición solicitadas y no disfrutadas.

Se podrá editar la petición no disfrutada, modificarla e incluso cancelarla.


![](diagr_flujo_horas_disposicion.png)

### Opción del menú de Incidencias

Al entrar en esta opción del menú se mostrarán las incidencias relacionadas con algún fichaje o con alguna solicitud del disfrute de las horas de libre disposición.

Las incidencias pueden haber sido creadas por el trabajador o por el departamento de recursos humanos.

El trabajador podrá adjuntar un documento que justifique cualquier incidencia y eliminar una incidencia creada anteriormente por él.

![](diagr_flujo_incidencias.png)

### Opción del menú de Informes

En esta opción del menú de informes se podrá elegir si se quieren obtener informes relacionados con las horas de libre disposición o relacionados con los fichajes.

Sobre las horas de libre disposición, se podrá elegir obtener un informe sobre las horas acumuladas por días; los días en los que se ha disfrutado de las horas de libre disposición o sobre incidencias relacionadas con las horas de libre disposición. Además, se podrá imprimir el informe.

Sobre los fichajes, se podrá elegir obtener un informe los últimos fiches o sobre incidencias relacionadas con los fichajes. Además, se podrá imprimir cualquier informe.

![](diagr_flujo_informes.png)

## Esquema relacional de las nuevas tablas en la base de datos 

La tabla *empleado* será una herencia de la tabla que ya existe en Odoo.

![](e-r_modulo_fichaje.png)

## Plantillas de comunicación

La aplicación notificará a través de correos electrónicos internos a los departamentos implicados, siguiendo la siguiente plantilla:

- Departamento origen
- Departamento destino
- Persona a la que se dirige
- Asunto
- Descripción de la comunicación
- Tarea a realizar por el departamento destino 
- Persona que debe realizar la tarea
- Espera de una respuesta (si /no)
- Confirmación de lectura (si / no)

## Referencias

- WireFramePro

https://wireframepro.mockflow.com/
