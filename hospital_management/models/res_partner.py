# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import config


class ResPartner(models.Model):
    _inherit = "res.partner"

    localization = fields.Char(string='Geolocation')
    localization_two = fields.Char(string='Geolocation Two')

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        print('======self=======',self)
        print('======name=======',name)
        domain = domain or []
        print('======domain=======',domain)
        res = self._search(domain, limit=limit, order=order)
        print('======res=======',res)
        return res