# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AccountReportFinance(models.TransientModel):
    _inherit = "accounting.report"

    analytic_account_ids = fields.Many2many(
        'account.analytic.account',
        string='Analytic Accounts'
    )

    @api.multi
    def check_report(self):
        res = super(AccountReportFinance, self).check_report()
        if self.analytic_account_ids:
            res['data']['form'].update({'analytic_account_ids': self.analytic_account_ids.ids})
        return res

#vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
