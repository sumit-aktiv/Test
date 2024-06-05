# -*- coding: utf-8 -*-

{
    "name": "Hospital Management",
    "summary": """
        Hospital Management system
    """,
    "description": """
        Hospital Management system
    """,
    "author": "MMY Auto",
    "website": "http://www.mmyauto.com",
    "category": "Hidden",
    "version": "17.0.1.1.7",
    "license": "LGPL-3",
    "depends": ["base",'mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/hospital_patient.xml'
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
