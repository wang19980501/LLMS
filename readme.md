# 人工智能项目

## 版本更新

### 软件版本 V0.0.2 更新信息

#### 主要变更

##### 新增功能

```
pdf 读取指定文件夹
结果以流的方式显示
```

##### 其他变更

##### 已知问题

### 软件版本 V0.0.1 更新信息

#### 主要变更

##### 新增功能

```
实现了从 PDF 文件中提取文本的功能。
实现了将文本分割成块的功能，以便进行后续的语义处理。
实现了使用 OpenAIEmbeddings 创建语义向量嵌入的功能。
实现了使用 FAISS 搜索与用户问题相关的文档的功能。
实现了使用 openai 的 GPT-3.5-turbo-16k 模型 进行问答的功能。
```

##### 其他变更

##### 已知问题

```
pdf 读取没有写成读取指定文件夹
结果是一次性返回，等待时间较长
```
