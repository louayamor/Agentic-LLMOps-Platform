from pathlib import Path

PROJECT_NAME = "agentic-llmops"

DIRS = [
    "agents",
    "graphs",
    "chains",
    "models",
    "pipelines",
    "vectorstore",
    "data/raw",
    "data/processed",
    "experiments",
    "configs",
    "docker",
    "scripts",
    "tests",
    "logs"
]

FILES = {
    "agents/__init__.py": "",
    "agents/crew.py": "# CrewAI agent definitions\n",

    "graphs/__init__.py": "",
    "graphs/workflow.py": "# LangGraph workflow definitions\n",

    "chains/__init__.py": "",
    "chains/rag_chain.py": "# LangChain RAG logic\n",

    "models/__init__.py": "",
    "models/ollama.py": "# Ollama LLM configuration\n",

    "pipelines/__init__.py": "",
    "pipelines/ingestion.py": "# Data ingestion pipeline\n",
    "pipelines/inference.py": "# Inference pipeline\n",

    "configs/settings.py": "# Global configuration settings\n",

    "scripts/run_pipeline.py": "# Entry point to run pipelines\n",

    "tests/__init__.py": "",
    "tests/test_smoke.py": "# Basic smoke tests\n",

    "docker/Dockerfile": "# Dockerfile\n",
    "docker/docker-compose.yml": "# Docker Compose configuration\n",

    ".env.example": "# Environment variables\n",
    ".gitignore": "__pycache__/\n.env\nlogs/\nvectorstore/\n",
    "README.md": "# Agentic LLMOps Platform\n"
}

def create_project_structure(base_path: Path):
    for dir_path in DIRS:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)

    for file_path, content in FILES.items():
        path = base_path / file_path
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

if __name__ == "__main__":
    root = Path(PROJECT_NAME)
    root.mkdir(exist_ok=True)
    create_project_structure(root)
