# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Wizard(models.TransientModel):
    _name = 'blog.wizard'

    def _default_readlist(self):
        return self.env['blog.readlist'].browse(self._context.get('active_id'))

    readlist_id = fields.Many2one(
        'blog.readlist',
        string='Readlist',
        required=True,
        default=_default_readlist
    )

    article_ids = fields.Many2many(
        'blog.article',
        string="Articles"
    )

    @api.multi
    def add(self):
        self.readlist_id.article_ids |= self.article_ids
        return {}
