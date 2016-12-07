#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from etc import config

ATM_LEVEL = 'logging.%s' % config.ATM_LOG_LEVEL

logger = logging.getLogger('[ATM]')
logger.setLevel(logging.INFO)

amt_log = logging.FileHandler(config.ATM_LOG_PATH)
amt_log.setLevel(ATM_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

amt_log.setFormatter(formatter)

logger.addHandler(amt_log)


def debug_log(message):
    logger.debug('[DEBUG] - ' + message)


def info_log(message):
    logger.info('[INFO] - ' + message)


def warn_log(message):
    logger.warn('[WARN] - ' + message)

warn_log("test")
