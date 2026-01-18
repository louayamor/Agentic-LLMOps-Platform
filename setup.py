import setuptools

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Agentic-LLMOps-Platform"
AUTHOR_USER_NAME = "louayamor"
PACKAGE_NAME = "agentic_llmops"
AUTHOR_EMAIL = "amor.louay20@gmail.com"

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Agentic LLMOps platform for reasoning, orchestration, and vector-based retrieval",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.12,<3.13",
    install_requires=[
        "langchain",
        "ollama",
        "crewai",
        "langgraph",
        "pandas",
        "numpy",
        "faiss-cpu",
        "sentence-transformers",
        "requests",
        "aiohttp",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
