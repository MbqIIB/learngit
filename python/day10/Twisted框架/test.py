#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

from source import event_drive


class MyHandler(event_drive.BaseHandler):

    def execute(self):
        print('event-drive execute MyHandler')


event_drive.event_list.append(MyHandler)
event_drive.run()