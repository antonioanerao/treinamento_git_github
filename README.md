# Treinamento Git e GitHUB

API simples usando `FastAPI` para demonstrar alguns comandos Git

## Como instalar

Primeiramente, configurar o ambiente com `uv`

```bash
uv sync
```

Depois, inicializar o ambiente

```bash
source .venv/bin/activate
```

Se estiver no Windows

```bash
source .venv/Scripts/activate
```

Para iniciar a API

```bash
uv run python -m uvicorn src.app:app
```
