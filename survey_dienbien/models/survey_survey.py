
from odoo import api, fields, models, tools, _

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    # question_and_page_ids = fields.Many2many('survey.question', string='Sections and Questions', copy=True)

class SurveyQuestionAnswer(models.Model):
    _inherit = 'survey.question.answer'



