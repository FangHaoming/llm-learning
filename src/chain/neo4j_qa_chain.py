from langchain_neo4j import Neo4jGraph
from langchain_neo4j import GraphCypherQAChain
from dotenv import load_dotenv
from src.llm.ali_llm import llm
import os
load_dotenv()

def neo4j_qa_chain():
    """使用GraphCypherQAChain的简单问答示例"""
    # 初始化图数据库连接
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        enhanced_schema=True
    )
    
    # 初始化问答链
    chain = GraphCypherQAChain.from_llm(
        graph=graph, 
        llm=llm, 
        verbose=True, 
        allow_dangerous_requests=True,
        return_intermediate_steps=True
    )
    return chain

def invoke_neo4j_qa_chain():
    chain = neo4j_qa_chain()

    result = chain.invoke({"query": "目前，中国哪些省市的哪些部门发布了关于航空货运发展的政策"})


    print(f"Response content: {result}")