<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/capa-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/capa-light.svg">
  <img src="./assets/capa-light.svg" width="100%" alt="Página de caderno com o nome Cesar Schutz e a frase: o que eu estudo virando artigo. Ao lado, uma ficha com os temas já estudados e o que está em andamento.">
</picture>

<br>

[![blog](https://img.shields.io/badge/blog-blog.cesarschutz.com.br-0b5cad?style=flat-square&labelColor=3a3a3a)](https://blog.cesarschutz.com.br)
[![rss](https://img.shields.io/badge/rss-assinar-c2410c?style=flat-square&logo=rss&logoColor=white&labelColor=3a3a3a)](https://blog.cesarschutz.com.br/rss.xml)
[![idioma](https://img.shields.io/badge/escrito%20em-pt--BR-1a7f37?style=flat-square&labelColor=3a3a3a)](https://blog.cesarschutz.com.br)

</div>

## Sobre este caderno

Sou o Cesar, arquiteto de soluções. Este perfil funciona como o meu caderno: o que eu estudo vira
repositório, o repositório vira teste e o teste vira artigo. Escrevo sobre arquitetura, Java,
pagamentos, AWS, Kubernetes e IA aplicada, sempre com código que roda e SQL testado.

## Últimas páginas

<!-- BLOG-POST-LIST:START -->
- `03/10/2026` · [Parquet e snapshots — o arquivo não garante a fotografia](https://blog.cesarschutz.com.br/posts/parquet-snapshot-banco-de-dados/)
- `02/10/2026` · [Um mod do Claude Code na prática — instalação, testes e limites &lpar;parte 2 de 2&rpar;](https://blog.cesarschutz.com.br/posts/claude-code-csr-cockpit/)
- `02/10/2026` · [Mods do Claude Code — o que são e as peças que vieram antes &lpar;parte 1 de 2&rpar;](https://blog.cesarschutz.com.br/posts/claude-code-do-claude-md-ao-mod/)
- `29/09/2026` · [Criptografia em repouso e em trânsito — o que é e como ativar no Postgres e no MongoDB](https://blog.cesarschutz.com.br/posts/criptografia-em-repouso-e-em-transito/)
- `25/09/2026` · [Filtros de serialização no Jackson — mascarando número de cartão nos logs](https://blog.cesarschutz.com.br/posts/jackson-filtros-mascarando-cartao/)
- `23/09/2026` · [CronJob ou endpoint + fila — onde rodar o batch de uma API Spring Boot no Kubernetes](https://blog.cesarschutz.com.br/posts/cronjob-vs-endpoint-sqs/)

<!-- BLOG-POST-LIST:END -->

<sub>Esta lista se atualiza sozinha todo dia, a partir do RSS do blog.</sub>

## Decisões que eu repito

No caderno, toda decisão ganha número. Estas aparecem em quase todo projeto:

<details>
<summary><b>D01 · Grave a intenção antes de causar o efeito</b></summary>
<br>

**Contexto:** a cobrança passou no adquirente e o banco não gravou.<br>
**Decisão:** transação local com outbox; o efeito externo sai depois, pelo relay.<br>
**Consequência:** consistência eventual explícita e conciliação como entregável.<br>
→ [Efeito externo sem registro local](https://blog.cesarschutz.com.br/posts/efeito-externo-sem-registro-local/)

</details>

<details>
<summary><b>D02 · Retry sem chave de idempotência é cobrança em dobro</b></summary>
<br>

**Contexto:** consultar antes de gravar não segura dois retries concorrentes.<br>
**Decisão:** chave de idempotência, restrição única no banco e resposta guardada.<br>
**Consequência:** o retry passa a ser seguro, e não só provável de dar certo.<br>
→ [Chave de idempotência](https://blog.cesarschutz.com.br/posts/cobranca-duplicada-no-retry/)

</details>

<details>
<summary><b>D03 · Se não tem traceparent, não aconteceu</b></summary>
<br>

**Contexto:** um erro atravessa cinco serviços e cada log conta só um pedaço.<br>
**Decisão:** W3C Trace Context em toda chamada, inclusive passando pela outbox.<br>
**Consequência:** uma busca pelo trace-id conta a história inteira.<br>
→ [W3C Trace Context](https://blog.cesarschutz.com.br/posts/w3c-trace-context/)

</details>

<details>
<summary><b>D04 · Toda escolha tem overhead; o problema é o overkill</b></summary>
<br>

**Contexto:** padrão bom aplicado no lugar errado vira custo sem retorno.<br>
**Decisão:** escrever o custo de cada escolha antes de adotá-la.<br>
**Consequência:** menos arquitetura de vitrine, mais arquitetura que se paga.<br>
→ [Overhead vs overkill](https://blog.cesarschutz.com.br/posts/overhead-vs-overkill/)

</details>

<details>
<summary><b>D05 · IA é mais um componente: tem contrato, custo e telemetria</b></summary>
<br>

**Contexto:** agentes rodando sem ninguém saber quanto custaram nem o que fizeram.<br>
**Decisão:** tratar o agente como qualquer dependência: medir, limitar e registrar.<br>
**Consequência:** foi daí que nasceu o painel de custo por agente do claude-code-kit.<br>
→ [Do CLAUDE.md ao mod no Claude Code](https://blog.cesarschutz.com.br/posts/claude-code-do-claude-md-ao-mod/)

</details>

## Índice do caderno

| Capítulo | Páginas |
|---|---|
| Pagamentos e consistência | [ledger](https://blog.cesarschutz.com.br/posts/arquitetura-de-ledger/) · [idempotência](https://blog.cesarschutz.com.br/posts/cobranca-duplicada-no-retry/) · [outbox](https://blog.cesarschutz.com.br/posts/efeito-externo-sem-registro-local/) · [bloqueio otimista e pessimista](https://blog.cesarschutz.com.br/posts/bloqueio-otimista-e-pessimista/) |
| Java e Spring | [Java 21](https://blog.cesarschutz.com.br/posts/java-21/) · [Java 25](https://blog.cesarschutz.com.br/posts/java-25/) · [virtual threads](https://blog.cesarschutz.com.br/posts/virtual-threads-pinning-close-wait/) · [AOP](https://blog.cesarschutz.com.br/posts/aop-jdk-proxy-cglib/) · [Jackson](https://blog.cesarschutz.com.br/posts/jackson-filtros-mascarando-cartao/) |
| Nuvem e runtime | [SNS e SQS](https://blog.cesarschutz.com.br/posts/sns-filter-policy/) · [CronJob](https://blog.cesarschutz.com.br/posts/kubernetes-cronjob-concorrencia/) · [SIGTERM e SIGKILL](https://blog.cesarschutz.com.br/posts/sigterm-sigkill-kubernetes/) · [criptografia](https://blog.cesarschutz.com.br/posts/criptografia-em-repouso-e-em-transito/) |
| Observabilidade | [traceparent](https://blog.cesarschutz.com.br/posts/w3c-trace-context/) · [logging estruturado](https://blog.cesarschutz.com.br/posts/logging-estruturado-spring-boot/) · [wide events](https://blog.cesarschutz.com.br/posts/wide-events-canonical-log-lines/) |
| IA aplicada | [claude-code-kit](https://github.com/cesarschutz/claude-code-kit) · [swagger-agent-adk](https://github.com/cesarschutz/swagger-agent-adk) · [BrainAPI](https://github.com/cesarschutz/BrainAPI) · [first-mcp-weather](https://github.com/cesarschutz/first-mcp-weather) |

## Os rascunhos

- [**blog**](https://github.com/cesarschutz/blog): o código do blog, em Astro.
- [**blog-exemplos**](https://github.com/cesarschutz/blog-exemplos): o código que acompanha os artigos.
- [**knowledge-base**](https://github.com/cesarschutz/knowledge-base): minha base de conhecimento.
- [**dev-note**](https://github.com/cesarschutz/dev-note): notícias técnicas que viram aprendizado.

<p align="center"><sub>Papel de dia, grafite à noite: este perfil acompanha o tema do seu GitHub.</sub></p>
