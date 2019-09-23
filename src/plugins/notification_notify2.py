# -*- coding: utf-8 -*-
"""
src/plugins/notification_notify2.py
===================================
"""

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init('pybitmessage')


def connect_plugin(title, subtitle, category, label, icon):
    """Plugin for notify2"""
    if not icon:
        icon = 'mail-message-new' if category == 2 else 'pybitmessage'
    connect_plugin.notification.update(title, subtitle, icon)
    connect_plugin.notification.show()


connect_plugin.notification = Notify.Notification.new("Init", "Init")
