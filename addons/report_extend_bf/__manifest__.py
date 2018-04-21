# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Template Report',
    'description': 'Is Easy an elegant and scalable solution to design reports using LibreOffice or OpenOffice.',
    'summary': 'Export data all objects odoo to OpenOffice, LibreOffice output files odt, pdf, doc, docx, ods',
    'category': 'All',
    'version': '1.0',
    'website': 'http://www.buildfish.com/',
    "license": "AGPL-3",
    'author': 'BuildFish',
    'depends': [
        'base', 'report',
    ],
    "external_dependencies": {
        "python": ["py3o.template", "genshi"],
        "bin": ["unoconv"],
    },
    'data': [
        'views/report_view.xml',
    ],
    'price': 109.00,
    'currency': 'EUR',
    'images': ['images/main_screenshot.png'],
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
