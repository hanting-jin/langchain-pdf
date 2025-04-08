from functools import partial
from .chatopenai import build_llm

llm_map = {
    "gpt-4": partial(build_llm, model="gpt-4"),
    "gpt-3.5-turbo": partial(build_llm, model="gpt-3.5-turbo"),
}