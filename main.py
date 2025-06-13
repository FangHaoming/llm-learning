from src.chain.neo4j_qa_chain import neo4j_qa_chain

chain = neo4j_qa_chain()

result = chain.invoke({"query": "目前，中国哪些省市的哪些部门发布了关于航空货运发展的政策"})


print(f"Response content: {result}")