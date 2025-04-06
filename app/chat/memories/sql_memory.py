from typing import List
from pydantic import BaseModel, Field
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str
    messages: List = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        # 防止 pydantic 限制赋值
        object.__setattr__(self, 'messages', get_messages_by_conversation_id(self.conversation_id))

    def add_message(self, message):
        add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )
        self.messages.append(message)

    def clear(self):
        self.messages = []

def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )