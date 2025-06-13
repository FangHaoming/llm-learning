from src.llm.ali_llm import llm
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate


# 第一个链：生成产品描述
product_template = """你是一个产品描述专家。根据以下产品名称，创建一个吸引人的产品描述。

产品名称: {product_name}

产品描述:"""

product_prompt = PromptTemplate(
    input_variables=["product_name"],
    template=product_template
)

product_chain = LLMChain(
    llm=llm,
    prompt=product_prompt,
    output_key="product_description"
)

# 第二个链：生成营销标语
slogan_template = """你是一个营销专家。根据以下产品描述，创建一个简短有力的营销标语。

产品描述: {product_description}

营销标语:"""

slogan_prompt = PromptTemplate(
    input_variables=["product_description"],
    template=slogan_template
)

slogan_chain = LLMChain(
    llm=llm,
    prompt=slogan_prompt,
    output_key="marketing_slogan"
)

# 第三个链：生成社交媒体帖子
social_template = """你是一个社交媒体专家。根据以下产品描述和营销标语，创建一个吸引人的社交媒体帖子。

产品描述: {product_description}
营销标语: {marketing_slogan}

社交媒体帖子:"""

social_prompt = PromptTemplate(
    input_variables=["product_description", "marketing_slogan"],
    template=social_template
)

social_chain = LLMChain(
    llm=llm,
    prompt=social_prompt,
    output_key="social_media_post"
)

# 组合所有链
full_chain = SequentialChain(
    chains=[product_chain, slogan_chain, social_chain],
    input_variables=["product_name"],
    output_variables=["product_description", "marketing_slogan", "social_media_post"],
    verbose=True
)

# 运行链式调用
result = full_chain({"product_name": "MacBook Air M4"})
print("\n产品描述:")
print(result["product_description"])
print("\n营销标语:")
print(result["marketing_slogan"])
print("\n社交媒体帖子:")
print(result["social_media_post"])
