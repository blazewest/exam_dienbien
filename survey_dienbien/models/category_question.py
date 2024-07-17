from odoo import api, fields, models, tools, _


class CategoryQuestion(models.Model):
    _name = 'category.question'


    name = fields.Char('Tên nhóm', required=True)
    code = fields.Char('Mã nhóm', required=True)
