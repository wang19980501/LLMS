# Langchain Ask PDF (Tutorial)

[原创 github 地址](https://github.com/alejandro-ao/langchain-ask-pdf)

> You may find the step-by-step video tutorial to build this application [on Youtube](https://youtu.be/wUAUdEw5oxM).

This is a Python application that allows you to load a PDF and ask questions about it using natural language. The application uses a LLM to generate a response about your PDF. The LLM will not answer questions unrelated to the document.

## How it works

The application reads the PDF and splits the text into smaller chunks that can be then fed into a LLM. It uses OpenAI embeddings to create vector representations of the chunks. The application then finds the chunks that are semantically similar to the question that the user asked and feeds those chunks to the LLM to generate a response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.

## Installation

To install the repository, please clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to add your OpenAI API key to the `.env` file.

## Usage

To use the application, run the `main.py` file with the streamlit CLI (after having installed streamlit):

```
streamlit run app.py
```

## Contributing

This repository is for educational purposes only and is not intended to receive further contributions. It is supposed to be used as support material for the YouTube tutorial that shows how to build the project.

# Langchain Ask PDF (Tutorial)

这是一个 Python 应用程序，允许您加载 PDF 并使用自然语言提问相关内容。该应用程序使用 LLM 生成有关您的 PDF 的回答。LLM 不会回答与文档无关的问题。

## 工作原理

应用程序读取 PDF 并将其文本分割成较小的块，然后将这些块输入到 LLM 中。它使用 OpenAI 嵌入来创建块的向量表示。然后，应用程序找到与用户提出的问题在语义上相似的块，并将这些块输入 LLM 以生成回答。

应用程序使用 Streamlit 创建 GUI 界面，并使用 Langchain 处理 LLM。

## 安装

要安装该代码库，请克隆此存储库并安装所需的依赖项：

```shell
pip install -r requirements.txt
```

您还需要将您的 OpenAI API 密钥添加到.env 文件中。

## 使用方法

要使用该应用程序，请使用 streamlit CLI 运行 main.py 文件（在安装了 streamlit 之后）：

```shell
streamlit run app.py
```

贡献
此代码库仅供教育目的，不接受进一步的贡献。它被用作支持材料，配合展示如何构建该项目的 YouTube 教程。
