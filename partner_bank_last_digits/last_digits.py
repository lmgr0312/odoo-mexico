# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: Luis Torres (luis@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from osv import fields, osv
from tools.translate import _

class res_partner_bank(osv.osv):
    _inherit = 'res.partner.bank'
    
    def _get_take_digits(self, cr, uid, ids, field, args, context=None):
        result = {}
        res=''
        n=-1
        for last in self.browse(cr, uid, ids, context=context):
            for digit in last.acc_number[::-1]:
                if(digit.isdigit()==True) and len(res)<4:
                    res = digit+res
            result[last.id]=res
        return result
    
    _columns = {
        'last_acc_number': fields.function(_get_take_digits,method=True, type='char', string="Ultimos 4 digitos"),
    }
res_partner_bank()