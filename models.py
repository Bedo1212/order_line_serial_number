from openerp import models, fields, api


class sale_order_line_number(models.Model):
    _inherit = 'sale.order.line'

    def _get_line_numbers(self):

        line_num = 1
        #order = self[1].order_id.browse(self)
        first_line_rec = self[0]

        for line_rec in first_line_rec.order_id.order_line:
                line_rec.line_no = line_num
                line_num += 1

    line_no = fields.Integer(compute='_get_line_numbers', string='Serial Number', readonly=False, default=False)


class purchase_order_line_number(models.Model):
    _inherit = 'purchase.order.line'

    def _get_line_numbers(self):

        line_num = 1
        first_line_rec = self[0]


        for line_rec in first_line_rec.order_id.order_line:
                line_rec.line_no = line_num
                line_num += 1

    line_no = fields.Integer(compute='_get_line_numbers', string='Serial Number', readonly=False, default=False)
