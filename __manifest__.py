# -*- coding: utf-8 -*-

{
    'name': 'HR Report',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'HR',
    'depends': [
        'hr',
        "resource",
        "hr_attendance",
        "hr_attendance",
        "vit_overtime",
    ],
    'data': [
        "views/menu.xml",
        "wizard/hr_overtime_report.xml",

        "report/hr_overtime_report.xml",
        "report/report_overtime_temp.xml",
    ],
    'qweb': [
        # 'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    "installable": True,
	"auto_instal": False,
	"application": False,
}
