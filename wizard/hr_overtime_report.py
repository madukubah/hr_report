# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
from calendar import monthrange
import logging
_logger = logging.getLogger(__name__)

class HROvertimeReport(models.TransientModel):
    _name = 'hr.overtime.report'

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date(string="End Date", required=True)
    type = fields.Selection([
        ( "per_department" , 'Per Department'),
        ( "per_employee" , 'Per Employee'),
        ], default="per_department", string='Type', index=True, required=True )
    
    @api.multi
    def action_print(self):        
        final_dict = {}
        if self.type == 'per_department' :
            hr_overtime_employees = self.env['hr.overtime.employee'].search([ ( 'overtime_id.date', '>=', self.start_date ), ( 'overtime_id.date', '<=', self.end_date ), ( 'overtime_id.state', '=', "validate" ) ])
            department_employee_dict = {}
            for hr_overtime_employee in hr_overtime_employees:
                department_name = hr_overtime_employee.overtime_id.department_id.name
                temp = {}
                temp['date'] = hr_overtime_employee.overtime_id.date
                temp['department_name'] = department_name
                temp['employee_name'] = hr_overtime_employee.employee_id.name
                temp['ovt_hour'] = hr_overtime_employee.ovt_hour
                if department_employee_dict.get( department_name , False):
                    department_employee_dict[ department_name ] += [ temp ]
                else :
                    department_employee_dict[ department_name ] = [ temp ]
                    
            final_dict = department_employee_dict
        elif self.type == 'per_employee' :
            hr_overtime_employees = self.env['hr.overtime.employee'].search([ ( 'overtime_id.date', '>=', self.start_date ), ( 'overtime_id.date', '<=', self.end_date ), ( 'overtime_id.state', '=', "validate" ) ])
            employee_overtime_dict = {}
            for hr_overtime_employee in hr_overtime_employees:
                department_name = hr_overtime_employee.overtime_id.department_id.name
                temp = {}
                temp['date'] = hr_overtime_employee.overtime_id.date
                temp['department_name'] = department_name
                temp['employee_name'] = hr_overtime_employee.employee_id.name
                temp['ovt_hour'] = hr_overtime_employee.ovt_hour
                if employee_overtime_dict.get( temp['employee_name'] , False):
                    employee_overtime_dict[ temp['employee_name'] ] += [ temp ]
                else :
                    employee_overtime_dict[ temp['employee_name'] ] = [ temp ]
                    
            final_dict = employee_overtime_dict
        datas = {
            'ids': self.ids,
            'model': 'hr.overtime.report',
            'form': final_dict,
            'type': self.type,
            'start_date': self.start_date,
            'end_date': self.end_date,

        }
        # _logger.warning( department_employee_dict )
        return self.env['report'].get_action(self,'hr_report.report_overtime_temp', data=datas)
