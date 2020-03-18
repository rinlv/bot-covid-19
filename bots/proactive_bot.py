# Copyright (c) Microsoft Corporation.  All rights reserved.
# Licensed under the MIT License.
from typing import Dict

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount, ConversationReference, Activity

from bots.data import *
from bots.constants import *


class ProactiveBot(ActivityHandler):
    def __init__(self, conversation_references: Dict[str, ConversationReference]):
        self.conversation_references = conversation_references

    async def on_conversation_update_activity(self, turn_context: TurnContext):
        self._add_conversation_reference(turn_context.activity)
        return await super().on_conversation_update_activity(turn_context)

    async def on_message_activity(self, context: TurnContext):
        self._add_conversation_reference(context.activity)
        text = context.activity.text
        message = text.lower().strip()
        if 'SARS-CoV-2'.lower() in message:
            message = ''.join(message.split(' ')[1:])

        if (message == COMMAND_WORLD):
            text = world()
        elif (message == COMMAND_NEWS):
            text = news()
        elif (message == COMMAND_COUNTRY):
            text = list_country()
        else:
            text = country(message)
        return await context.send_activity(text)

    def _add_conversation_reference(self, activity: Activity):
        """
        This populates the shared Dictionary that holds conversation references. In this sample,
        this dictionary is used to send a message to members when /api/notify is hit.
        :param activity:
        :return:
        """
        conversation_reference = TurnContext.get_conversation_reference(activity)
        self.conversation_references[conversation_reference.user.id] = conversation_reference
