# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import url_for, redirect, abort
from jinja2.exceptions import TemplateNotFound

from udata import theme
from udata.models import Reuse, Organization, Dataset
from udata.i18n import I18nBlueprint
from udata.sitemap import sitemap

blueprint = I18nBlueprint('components-guidelines', __name__,
                          template_folder='templates',
                          static_folder='static',
                          static_url_path='/static/gouvfr')


@blueprint.route('/carousel')
def carousel():
    theme.render('carousel.html')
