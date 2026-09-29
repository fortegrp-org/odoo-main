# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
import logging
import json

import requests
import werkzeug.urls

from ast import literal_eval

from odoo import api, release, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.models import AbstractModel
from odoo.tools.translate import _
from odoo.tools import config, misc

_logger = logging.getLogger(__name__)


class PublisherWarrantyContract(AbstractModel):
    _name = "publisher_warranty.contract"
    _description = 'Publisher Warranty Contract'

    @api.model
    def _get_message(self):
        return True

    @api.model
    def _get_sys_logs(self):
        return True

    def update_notification(self, cron_mode=True):
        return True
