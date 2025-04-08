from langchain.chains import ConversationRetrievalChain
from app.chat.chains.streamable import Streamable

class StreamingConversationRetrievalChain(Streamable, ConversationRetrievalChain):
    def stream(self, input):
        return super().stream(input)