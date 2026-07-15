"""
Script para renomear os arquivos de exercícios, adicionando zero à esquerda
nos números (ex: exercicio36.py -> exercicio036.py).

Isso resolve o problema do GitHub ordenar os arquivos como TEXTO
(1, 10, 100, 101... 2, 20...) em vez de ordenar como NÚMERO (1, 2, 3...36...105).

Como usar:
1. Coloque este arquivo (renomear_exercicios.py) na MESMA pasta dos seus exercícios
   (dentro de MUNDO2-EXERCÍCIOS)
2. Rode primeiro em modo TESTE (sem alterar nada de verdade):
       python renomear_exercicios.py
3. Se a prévia estiver certa, rode em modo APLICAR:
       python renomear_exercicios.py --aplicar
"""

import re
import subprocess
import sys
from pathlib import Path

# Quantidade de dígitos que os números vão ter depois de renomeado.
# 3 dígitos cobre até 999 exercícios (ex: 036, 105, 999) - dá margem de sobra.
QTD_DIGITOS = 3

# Padrão que reconhece nomes tipo:
#   exercício36.py
#   exercício46- For.py
#   exercício96-Def.py
# Captura 3 partes: o prefixo (exercício/exercicio), o número, e o que sobrar antes do .py
PADRAO = re.compile(r'^(?P<prefixo>[Ee]xerc[ií]cio)(?P<numero>\d+)(?P<sufixo>.*)\.py$')


def montar_novo_nome(nome_arquivo: str) -> str | None:
    """Recebe o nome atual do arquivo e devolve o novo nome (com zero-padding).
    Devolve None se o nome não seguir o padrão esperado."""
    match = PADRAO.match(nome_arquivo)
    if not match:
        return None

    prefixo = match.group("prefixo")
    numero = int(match.group("numero"))
    sufixo = match.group("sufixo")  # ex: "- For", "-While", "" (vazio na maioria)

    numero_formatado = str(numero).zfill(QTD_DIGITOS)  # 36 -> "036"
    return f"{prefixo}{numero_formatado}{sufixo}.py"


def usa_git(pasta: Path) -> bool:
    """Verifica se a pasta está dentro de um repositório Git."""
    return (pasta / ".git").exists()


def renomear_arquivo(caminho_antigo: Path, novo_nome: str, aplicar: bool, com_git: bool):
    caminho_novo = caminho_antigo.parent / novo_nome

    if not aplicar:
        print(f"[PRÉVIA] {caminho_antigo.name}  ->  {novo_nome}")
        return

    if com_git:
        # git mv preserva o histórico do arquivo (aparece como "renomeado" no commit,
        # e não como "arquivo deletado + arquivo novo")
        resultado = subprocess.run(
            ["git", "mv", str(caminho_antigo.name), novo_nome],
            cwd=caminho_antigo.parent,
            capture_output=True,
            text=True,
        )
        if resultado.returncode != 0:
            print(f"[ERRO] Falha ao renomear {caminho_antigo.name}: {resultado.stderr.strip()}")
        else:
            print(f"[OK] {caminho_antigo.name}  ->  {novo_nome}")
    else:
        caminho_antigo.rename(caminho_novo)
        print(f"[OK] {caminho_antigo.name}  ->  {novo_nome}")


def main():
    aplicar = "--aplicar" in sys.argv
    pasta_atual = Path.cwd()
    com_git = usa_git(pasta_atual)

    arquivos_py = sorted(pasta_atual.glob("*.py"))

    if not arquivos_py:
        print("Nenhum arquivo .py encontrado nesta pasta.")
        return

    total_renomeados = 0
    total_ignorados = 0

    for arquivo in arquivos_py:
        # Não tenta renomear o próprio script
        if arquivo.name == Path(__file__).name:
            continue

        novo_nome = montar_novo_nome(arquivo.name)

        if novo_nome is None:
            print(f"[IGNORADO] {arquivo.name} (não segue o padrão 'exercicioNN.py')")
            total_ignorados += 1
            continue

        if novo_nome == arquivo.name:
            # já está no formato certo, não precisa fazer nada
            continue

        renomear_arquivo(arquivo, novo_nome, aplicar, com_git)
        total_renomeados += 1

    print("\n----------------------------------------")
    if aplicar:
        print(f"Renomeação concluída: {total_renomeados} arquivo(s) renomeado(s).")
    else:
        print(f"Modo PRÉVIA: {total_renomeados} arquivo(s) seriam renomeados.")
        print("Se a lista acima estiver certa, rode novamente com:  python renomear_exercicios.py --aplicar")
    if total_ignorados:
        print(f"{total_ignorados} arquivo(s) ignorado(s) (fora do padrão esperado).")


if __name__ == "__main__":
    main()