# -*- coding: utf-8 -*-
from openerp import http


class Blog(http.Controller):

    @http.route('/blog/articles', auth='public')
    def index(self, **kw):
        Articles = http.request.env['blog.article']
        return http.request.render('blog.article_index', {
            'articles': Articles.search([('state', '=', 'done')])
        })

    @http.route('/blog/articles/<model("blog.article"):article>/', auth='public')
    def object(self, article, **kw):
        return http.request.render('blog.article_show', {
            'article': article
        })

#     @http.route('/blog/blog/objects/<model("blog.blog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blog.object', {
#             'object': obj
#         })
