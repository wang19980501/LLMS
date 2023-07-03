import openai
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# 读取data文件夹中的PDF文件

folder_path = "./data"
pdf_list = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith(".pdf"):
        pdf = open(file=file_path, mode="rb")
        pdf_list.append(pdf)

# 从 PDF 中提取文本
text = ""
for file in pdf_list:
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()

# 将文本分成块
text_splitter = CharacterTextSplitter(
    separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
)
chunks = text_splitter.split_text(text)

# 创建嵌入向量
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(chunks, embeddings)

# 用户输入问题
user_input = st.text_input("请问您对 PDF 文件有什么疑问？", placeholder="回车键提交 ...")


def gen_prompt(docs, query) -> str:
    return f"""To answer the question please only use the Context, nothing else. Do not make up answer, simply say 'I don't know' if you are not sure.
Question: {query}
Context: {[doc.page_content for doc in docs]}
Answer:
"""


def prompt(query):
    docs = docsearch.similarity_search(query, k=4)
    prompt = gen_prompt(docs, query)
    return prompt


if user_input:
    st.markdown("----")
    res_box = st.empty()
    report = []
    content = prompt(user_input)
    content = f"已知信息：{content}，我提问的是estun机器人相关的知识,根据已知信息回答下列问题：{user_input},并用中文回答"
    print(content)

    # 使用 ChatGPT 进行对话
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You're an assistant."},
            {"role": "user", "content": f"{content}"},
        ],
        stream=True,
        temperature=0,
    )

    for line in completion:
        if "content" in line["choices"][0]["delta"]:
            report.append(line["choices"][0]["delta"]["content"])
        result = "".join(report).strip()
        res_box.markdown(f"{result}")

    st.markdown("----")
