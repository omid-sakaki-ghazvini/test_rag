from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = "LANGCHAIN_API_KEY"
os.environ['OPENAI_API_KEY'] = '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'
