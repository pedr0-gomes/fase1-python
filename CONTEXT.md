# CONTEXT.md — fase1

Mapa do projeto: contexto, stack, progressão e método.
As leis (como o assistente trabalha aqui) vivem no `CLAUDE.md`.

---

## Próximo passo

Introduzir `pytest` na Camada 3 — maior gap da camada (nada foi testado de
forma automatizada ainda). Alvo: o capstone `03_estrutura/01_nomes_em_lote/`.
Testar `entrada.normalizar`/`validar` (funções puras) e `ibge.consulta` (com a
rede mockada, pra não bater na API real). Pré-requisito: criar o `.venv`
(ainda não existe — tudo rodou com o `python3` do sistema) e instalar `pytest`.

---

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

---

## Três camadas de aprendizado (progressão)

Os exercícios sobem por camadas. Pedro só avança quando dominar a anterior.

1. **Dados** — tipos, `list`/`dict`/`set`/`tuple`, comprehensions, leitura/escrita de arquivos
   (txt, csv, json), manipulação com stdlib.
2. **APIs** — `requests`, parsing de JSON, tratamento de erros HTTP, integração com serviços externos.
3. **Estrutura** — módulos, pacotes, classes, separação de responsabilidades, testes com `pytest`.

A camada atual fica registrada no `README.md` do projeto à medida que avança.

---

## Blocos do método neste projeto

O fase1 roda pelo método de blocos componíveis do sistema global — mapa em
`/home/pedro/.claude/CONTEXT.md` (fonte do método; **não** re-explicar os blocos aqui).
Nem todo bloco serve a um projeto de aprendizado. Os que se aplicam, e como rodam aqui:

- **Aprender** — embutido (aprende-fazendo). Dúvida just-in-time durante o exercício; o
  assistente explica o mecanismo inline. Sem desvio formal, salvo conceito grande travando antes.
- **Construir** — esteira colapsada em `Implementation (mão de Pedro) + QA (rodar no terminal)`.
  Sem PRD/Kanban/Prototype/`tdd` — pesados demais para exercício onde Pedro escreve cada linha.
  Design, quando preciso, fica em palavras no chat — daqui pra frente sem `design.md`
  (os `design.md` em `01_dados/05_loteria/` e `01_dados/06_arquivos/` são legado de antes desta regra).
- **Destilar** — fecha cada exercício: commit + atualizar `README.md` + memória.

**Não se aplica:** **Investigar** — sem pesquisa externa (aprender APIs/`requests` é
curiosidade-pra-fazer: vai pro **Aprender**, não pro Investigar).

**Não ativado por ora:** **Expor** — não por incompatibilidade. A jornada de aprender Python
construindo, exercício a exercício, é candidata legítima a post; só não foi ativado ainda.
Quando ativar: o raciocínio expositivo (dossiê/arco/draft) mora no Notion, não no repo —
só o post final e o código vão a público.

---

## Estrutura do projeto (a crescer)

```
fase1/
├── .venv/              # Ambiente virtual (ignorado)
├── .gitignore
├── CLAUDE.md           # Leis do projeto
├── CONTEXT.md          # Este arquivo — mapa do projeto
├── README.md           # Diário do progresso (camada atual, exercícios feitos)
└── <pasta por camada>/ # Ex: 01_dados/, 02_apis/, 03_estrutura/
```

A estrutura por pastas só nasce quando o primeiro exercício de cada camada chegar — não criar antes.

---

## Comandos básicos

- Ativar venv: `source .venv/bin/activate`
- Rodar script: `python caminho/do/script.py`
- Rodar testes: `pytest` (após instalar `pytest` no venv)
- Instalar pacote: `pip install <pacote>` (só com aprovação de Pedro)
