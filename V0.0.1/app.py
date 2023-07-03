from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.docstore.document import Document
import os


def main():
    load_dotenv()

    # 打开两个 PDF 文件
    pdf1 = open(file="./data/robot1.pdf", mode="rb")  # 以二进制方式打开
    pdf2 = open(file="./data/robot2.pdf", mode="rb")  # 以二进制方式打开
    pdf_list = [pdf1, pdf2]

    text = ""
    for file in pdf_list:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    # 将文本分割成块
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)

    # 创建语义向量嵌入
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # 用户输入问题
    user_question = st.text_input("请问您对 PDF 文件有什么疑问？")
    if user_question:
        # 在知识库中搜索与问题相关的文档
        docs = knowledge_base.similarity_search(user_question)

        # 加载用于问答的预训练模型
        llm = OpenAI(
            model_name="gpt-3.5-turbo-16k",
        )

        # 使用预训练模型生成答案
        st.write(
            llm(f"已知信息：{docs}，我提问的是 estun 机器人相关的知识，根据已知信息回答下列问题：{user_question}，并用中文回答")
        )


if __name__ == "__main__":
    main()
