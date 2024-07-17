# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import collections
import contextlib
import itertools
import json
import operator
from textwrap import shorten

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    question_and_page_ids = fields.Many2many('survey.question', string='Sections and Questions', copy=True)

class SurveyQuestionAnswer(models.Model):
    _inherit = 'survey.question.answer'



