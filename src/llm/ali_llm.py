from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# 初始化语言模型
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
)