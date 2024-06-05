from odoo import models,fields,api,_
from odoo.tools import format_date, formatLang, frozendict, date_utils


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="hospital management system"


    name = fields.Char(string="Name", store=True, translate=True)    
    resultshow = fields.Char(string="result", compute="_compute_result", store=True)
    total_mark = fields.Integer(string="total mark", default=100)
    obtain_mark = fields.Integer(string="obtain mark", default=50)
    file = fields.Binary('File', attachment=True)
    file_name = fields.Char('File Name')
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one('res.partner',string="customer")

    # api.depends('name')
    def _compute_result(self):
        for rec in self:
            # rec.obtain_mark = rec.total_mark/2 
            print('======rec=======',rec)

    @api.onchange('file_name')
    def _onchange_filename(self):
        print('=====self.env.lang======',self.env.lang)
        print('=====self.env.lang======',self.env.user)
        print('=====self.user.company_id======',self.env.user.company_id)
        print('======is_superuser=====',self.env.is_superuser())
        print('======is_admin=====',self.env.is_admin())
        print('=======self.origin=======',self._origin.id)
        print('=======filename========',type(self.file_name))
        print('=======file========',type(self.file))        
        print('=======is_system========',self.env.is_system())
        print('=====self.env.companies=========',self.env.companies)        
        print('=====cr_execute======',self._cr.execute('SELECT * FROM hospital_patient'))
        # print('=====self.env.cr=========',self.env.cr.execute(""))        

