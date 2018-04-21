# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields, api


class ir_actions_report(models.Model):
    _inherit = 'ir.actions.report.xml'

    template_id = fields.Many2one("ir.attachment", "Template *.odt")
    output_file = fields.Selection(
        (("pdf", "pdf"),
         ("ods", "ods"),
         ("doc", "doc"),
         ("docx", "docx")), string="Format Output File.", help='Format Output File. (Format Default *.odt Output File)', 
    )

    @api.onchange('report_name')
    def onchange_report_name(self):
        if self.report_name:
            self.report_rml = "/report/download_document/" + self.report_name
