import random
from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import build_retriever
from app.chat.memories.sql_memory import build_memory
from app.chat.llms.chatopenai import build_llm
from app.chat.chains.retrieval import StreamingConversationRetrievalChain
from app.web.api import get_conversation_components, set_conversation_components
from app.chat.vector_stores.__init__ import retriever_map
from app.chat.llms.__init__ import llm_map
from app.chat.memories.__init__ import memory_map
from app.chat.score import random_component_by_score

def select_component(
    component_type, 
    component_map,
    chat_args: ChatArgs,
):
    components = get_conversation_components(chat_args.conversation_id)
    pervious_component = components[component_type]
    if pervious_component:
        builder = component_map(pervious_component)
        return pervious_component, builder(chat_args)
    else:
        random_name = random_component_by_score(component_type, component_map,)
        builder = component_map[random_name]
        return random_name, builder(chat_args)


def build_chat(chat_args: ChatArgs):
    retriever_name, retriever = select_component("retriever", retriever_map, chat_args)
    llm_name, llm = select_component("llm", llm_map, chat_args)
    memory_name, memory = select_component("memory", memory_map, chat_args)

    set_conversation_components(
        chat_args.conversation_id,
        retriever=retriever_name,
        llm=llm_name,
        memory=memory_name,
    )

    condense_question_llm = ChatOpenAI(streaming=False)

    
    return StreamingConversationRetrievalChain.from_llm(
            llm=llm,
            condense_question_llm=condense_question_llm,
            retriever=retriever,
            memory=memory,
        )
    
