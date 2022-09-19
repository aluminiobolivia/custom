# -*- coding: utf-8 -*-

import time
from odoo import api, models

class ReportFinancial(models.AbstractModel):
    _inherit = 'report.account.report_financial'

    @api.model
    def render_html(self, docids, data=None):
        data['form']['analytic_codes'] = []
        if data['form'].get('analytic_account_ids'):
            analytic = self.env['account.analytic.account'].browse(data['form']['analytic_account_ids'] )
            data['form']['used_context'].update({'analytic_account_ids': analytic})
            
            if data['form'].get('analytic_account_ids', False):
                analytic_codes = [str(analytic.code) for analytic in self.env['account.analytic.account'].search([('id', 'in', data['form']['analytic_account_ids'])])]
            data['form']['analytic_codes'] = analytic_codes

        return super(ReportFinancial, self).render_html(docids, data)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: