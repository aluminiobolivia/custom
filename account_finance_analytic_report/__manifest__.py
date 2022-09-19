# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Financial Reports Filter by Analytic Accounts',
    'version': '1.0',
    'price': 65.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'category': 'Accounting',
    'summary': 'This module allow user to filter financial report by anlytic accounts.',
    'description': """
Tags:

Financial report with analytic
Profit and loss with analytic
analytic report
analytic account report
analytic account on accounting reports
analytic account in general ledger
analytic account in account balance
analytic account in trial balance
analytic account selection in wizard
wizard analytic account
report anlaytic account
filter by analytic account
filter by analytic
report by analytic
accounting reports by analytic
ledger by analytic
P&L by analytic

            """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'depends': ['account'],
    'data': [
            'wizard/account_financial_report_view.xml',
            'views/report_financial.xml',
             ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
