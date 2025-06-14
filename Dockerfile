# 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖（根据项目需求调整）
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 Poetry
RUN pip install poetry

# 配置 Poetry（禁用虚拟环境，直接安装到系统）
RUN poetry config virtualenvs.create false

# 复制依赖文件
COPY . .

# 安装生产依赖
RUN poetry install --no-root
