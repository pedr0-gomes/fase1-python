# CLAUDE.md — fase1

Leis do projeto. Mapa (contexto, stack, camadas, método, estrutura, comandos): ver `CONTEXT.md`.

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
5. **Sem dependências por iniciativa do assistente.** Novas bibliotecas entram só quando Pedro
   entender o porquê e instalar manualmente. Sem `requirements.txt` automático; sem `pip install`
   pelo assistente.
