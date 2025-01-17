import streamlit as st

st.set_page_config(page_title="KnowledgeGPT", page_icon="📖", layout="wide")
st.header("📖KnowledgeGPT")

import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
import os

from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader


openapi_key=os.getenv('open_key')




def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text


pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

text=get_pdf_text(pdf_docs)



template="""You are an assistant for question-ansering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer,just say that you don't know.
Use ten sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

prompt=ChatPromptTemplate.from_template(template)




with st.form(key="qa_form"):
    query = st.text_area("Ask a question about the document")
    submit = st.form_submit_button("Submit")


if submit:

     with st.spinner("Processing..."):
        text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
        text_chunks=text_splitter.split_text(text)

        embeddings=OpenAIEmbeddings(openai_api_key=openapi_key)

        vectorstore=FAISS.from_texts(text_chunks,embeddings)

        retriver=vectorstore.as_retriever()
        llm_model=ChatOpenAI(openai_api_key=openapi_key,model="gpt-3.5-turbo")
        output_parser=StrOutputParser()
        rag_chain=({
        "context":retriver, "question": RunnablePassthrough()}
        | prompt
        | llm_model
        | output_parser)
        st.write(rag_chain.invoke(query))
