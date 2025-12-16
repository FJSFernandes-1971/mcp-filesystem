from mcp.server.fastmcp import FastMCP
from pathlib import Path

BASE_DIR = Path.home() / "Documentos" / "MCP_SANDBOX"

mcp = FastMCP("filesystem-mcp")

# Pasta permitida (segurança)
BASE_DIR = Path.home() / "Documentos"


def _resolve_safe(rel_path: str) -> Path:
    """
    Resolve um caminho relativo dentro da BASE_DIR, impedindo "escapar" (.., caminhos absolutos).
    """
    p = (BASE_DIR / rel_path).resolve()

    base = BASE_DIR.resolve()
    # Garante que p está dentro de base
    if base not in p.parents and p != base:
        raise ValueError("Caminho fora da pasta permitida (Documentos).")

    return p


@mcp.tool()
def listar_itens(rel_path: str = ""):
    """
    Lista arquivos e pastas dentro de Documentos (ou de uma subpasta).
    rel_path: caminho relativo dentro de Documentos (ex: 'projetos-python')
    """
    pasta = _resolve_safe(rel_path)

    if not pasta.exists():
        return [f"ERRO: caminho não existe: {rel_path}"]
    if not pasta.is_dir():
        return [f"ERRO: não é pasta: {rel_path}"]

    itens = []
    for p in pasta.iterdir():
        if p.is_dir():
            itens.append(f"PASTA: {p.name}")
        elif p.is_file():
            itens.append(f"ARQUIVO: {p.name}")
    return itens



@mcp.tool()

def ler_texto(rel_path: str, max_chars: int = 6000):
    """
    Lê um arquivo de texto dentro da pasta Documentos.
    Tenta UTF-8 primeiro, depois CP1252 (Windows).
    """
    arquivo = BASE_DIR / rel_path

    if not arquivo.exists():
        return f"ERRO: arquivo não existe: {rel_path}"

    try:
        try:
            conteudo = arquivo.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            conteudo = arquivo.read_text(encoding="cp1252")

        if len(conteudo) > max_chars:
            return conteudo[:max_chars] + "\n\n[...cortado por limite de segurança...]"

        return conteudo

    except Exception as e:
        return f"ERRO ao ler arquivo: {e}"




    except Exception as e:
        return f"ERRO ao ler arquivo: {e}"

from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Nome do MCP
mcp = FastMCP("filesystem-mcp")

# Pasta segura (sandbox)
BASE_DIR = Path.home() / "Documentos" / "MCP_SANDBOX"


@mcp.tool()
def listar():
    """Lista arquivos e pastas da sandbox."""
    return [p.name for p in BASE_DIR.iterdir()]


@mcp.tool()
def ler(nome: str):
    """Lê um arquivo de texto da sandbox."""
    arquivo = BASE_DIR / nome
    if not arquivo.exists():
        return "Arquivo não existe"
    return arquivo.read_text(encoding="utf-8", errors="replace")



