# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Asociación de Productores Concepción",
    'summary': """ Modificaciones adaptadas para la asociación de productores Concepción""",
    'author': "Andrés López Molina",
    'website': "josandlopmol@hotmail.com",
    'category': 'Agronomía',
    'version': '8.0.1',
    'depends': ['base','sale'],
    'data': [
        'views/menu.xml',
        'views/asociados.xml',
        'views/actividades.xml',
        'views/fiadores.xml',
        'views/cosechas.xml',
        'views/estados.xml',
        'views/fuentes.xml',
        'views/creditos.xml',
        'views/pesos.xml',
        'reports/report_lista_de_asociados.xml'
    ],
    'demo': [
    ],
}
