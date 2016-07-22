# -*- coding: utf-8 -*-

from openerp import models, fields


class article(models.Model):
    _name = 'blog.article'

    title = fields.Char(string="Title", required=True)
    content = fields.Text(string="Content")
