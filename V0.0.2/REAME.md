# PDF 文件处理和 OpenAI 文本生成

这个项目用于处理 PDF 文件并使用 OpenAI 的语言模型进行文本生成。

[参考项目](https://github.com/DanteNoguez/StreamlitGPT)

# 使用方法

准备 PDF 文件，将其放置在项目`data`目录下。

## 运行应用：

```
cp .env.example .env
```

将 OpenAI 的 key 写在.env 中

```
pip install -r requirements.txt
streamlit run app.py
```

在浏览器中打开应用，并向输入框中提问与 PDF 文件相关的问题。

应用会从 PDF 文件中提取文本，并使用 OpenAI 的 ChatGPT 模型生成答案。

答案将显示在应用界面上。

## 注意事项

请确保已经安装了所需的依赖项，并且正确配置了 OpenAI 的认证密钥。
如果需要修改或扩展功能，可以编辑 `app.py` 文件。
在运行应用之前，确保已经准备好要处理的 PDF 文件，并按照指定的命名方式进行命名。
PDF 文件内容质量越高，回答越准确
