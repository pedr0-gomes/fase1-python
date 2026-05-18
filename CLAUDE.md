# CLAUDE.md — fase1

## Contexto

Primeira fase de uma trajetória de aprendizado de Python planejada em múltiplas fases (`fase1`, `fase2`, ...).
Cada fase vive em seu próprio repositório.

**Objetivo da fase1**: construir base sólida de Python — sintaxe, estruturas de dados, consumo
de APIs e organização de código — exercício a exercício, com Pedro escrevendo cada linha.

**Repositório**: https://github.com/pedr0-gomes/fase1-python

---

## Stack

- **Linguagem**: Python 3.12+ (instalado: 3.14.3)
- **Isolamento**: `venv` em `.venv/` (ignorado pelo Git)
- **Bibliotecas previstas**:
  - `stdlib` — base de tudo (json, csv, pathlib, urllib, datetime)
  - `requests` — quando entrar na camada de APIs
  - `pytest` — testes automatizados desde os primeiros exercícios não-triviais

Novas dependências entram no projeto **só quando Pedro entender o porquê** e instalar manualmente.
Sem `requirements.txt` automático; sem `pip install` por iniciativa do assistente.

---

## Três camadas de aprendizado (progressão)

Os exercícios sobem por camadas. Pedro só avança quando dominar a anterior.

1. **Dados** — tipos, `list`/`dict`/`set`/`tuple`, comprehensions, leitura/escrita de arquivos
   (txt, csv, json), manipulação com stdlib.
2. **APIs** — `requests`, parsing de JSON, tratamento de erros HTTP, integração com serviços externos.
3. **Estrutura** — módulos, pacotes, classes, separação de responsabilidades, testes com `pytest`.

A camada atual fica registrada no `README.md` do projeto à medida que avança.

---

## Dinâmica de trabalho

**Pedro escreve. O assistente explica.**

- Pedro digita cada linha de código de exercício. O assistente **nunca** escreve a lógica central
  no lugar dele — pode escrever boilerplate trivial (imports, scaffolding) só quando explicitamente pedido.
- Antes de qualquer ação (criar arquivo, rodar comando, editar), o assistente **explica o que vai
  fazer e por quê, e espera aprovação**.
- Quando Pedro erra: aponte o erro, espere ele tentar corrigir. Intervenha só se travar.
- Explicações priorizam **mecanismo** (por que funciona) antes de **resultado** (o que faz).

---

## Regras do projeto

1. **Todo script vai para o repositório.** Mesmo exercícios pequenos e descartáveis. Histórico é
   parte do aprendizado.
2. **Commit após cada exercício** com mensagem descritiva (`exercise: descrição curta` ou
   `learn: tópico estudado`).
3. **Nunca gere código que Pedro não consegue explicar.** Se uma sugestão usa conceito que ele
   ainda não viu, explique o conceito primeiro e espere ele dizer que entendeu antes de aplicar.
4. **Sem abstrações precoces.** Solução simples e direta primeiro; refatorar só quando houver
   motivo real e Pedro pedir.

---

## Estrutura do projeto (a crescer)

```
fase1/
├── .venv/              # Ambiente virtual (ignorado)
├── .gitignore
├── CLAUDE.md           # Este arquivo
├── README.md           # Diário do progresso (camada atual, exercícios feitos)
└── <pasta por camada>/ # Ex: 01_dados/, 02_apis/, 03_estrutura/
```

A estrutura por pastas só nasce quando o primeiro exercício de cada camada chegar — não criar antes.

---

## Comandos básicos

- Ativar venv: `.venv\Scripts\Activate.ps1` (PowerShell)
- Rodar script: `python caminho/do/script.py`
- Rodar testes: `pytest` (após instalar `pytest` no venv)
- Instalar pacote: `pip install <pacote>` (só com aprovação de Pedro)
