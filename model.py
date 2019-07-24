from odoo import models, fields, api



class test(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'


    test = fields.Char('more info')  # type: Char
    size = fields.Selection([('m', 'medium'), ('l', 'large'), ('s', 'small')], string='size')





