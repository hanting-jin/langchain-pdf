from blinker import base
from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory

from app.web.api import (
  get_messages_by_conversation_id,
  add_message_to_conversation
)

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)
      

    def add_message(self, message):
       return add_message_to_conversation(
        conversation_id=self.conversation_id,
        role=message.role,
        content=message.content
       )

    def clear(self):
        pass

def build_memory(chat_args):
    message_history = SqlMessageHistory(conversation_id=chat_args.conversation_id)
    return ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True
    )