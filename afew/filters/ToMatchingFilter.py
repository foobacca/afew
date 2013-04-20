# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from ..Filter import register_filter
from .HeaderMatchingFilter import HeaderMatchingFilter


@register_filter
class ToMatchingFilter(HeaderMatchingFilter):
    message = 'Tagging based on To/Cc/Bcc header values matching a given RE'

    def handle_message(self, message):
        if self.pattern is not None:
            if not self._tag_blacklist.intersection(message.get_tags()):
                for header in ['To', 'Cc', 'Bcc']:
                    self.tag_if_header_matches(message, header)
