# Recursos: o que havia nos 10 modelos e onde foi parar

Levantamento feito nas 10 branches `modelo-01` a `modelo-10` (README + SVGs de cada uma) e nos
rascunhos `modelos/*.md` que ficavam na `main`. Recursos repetidos entre modelos aparecem uma vez só,
com todos os modelos onde apareciam.

Legenda das capas: **C1** = [01 · Rastro](./capas/01-rastro/) · **C2** = [02 · Caderno](./capas/02-caderno/) · **C3** = [03 · Terminal](./capas/03-terminal/) ·
**C4** = [04 · Trajetória](./capas/04-trajetoria/) · **C5** = [05 · Painel](./capas/05-painel/) · **C6** = [06 · Neofetch](./capas/06-neofetch/)

As seções 1 a 3 descrevem a primeira leva (C1–C3). A seção 4 mostra onde cada recurso entrou na segunda
leva (C4–C6), que fala da minha trajetória em vez do blog.

## Resumo

| | Quantidade |
|---|---|
| Recursos distintos nos modelos antigos | 41 |
| Usados em pelo menos uma capa | 29 |
| Não usados | 12 |
| Recursos novos (não existiam em nenhum modelo) | 12 |

## 1. Recursos usados

### Banner e animações em SVG

| # | Recurso | Aparecia em | Usado em | Onde, exatamente |
|---|---|---|---|---|
| 1 | Banner SVG autoral dentro do repositório | 01 a 10 | C1 · C2 · C3 | A capa no topo de cada README (`capas/*/assets/capa-*.svg`). |
| 2 | Banner diferente no modo claro e no escuro (`<picture>` + `prefers-color-scheme`) | 09 | C1 · C2 · C3 | Todas as capas têm `capa-light.svg` e `capa-dark.svg`. |
| 3 | Pulso de opacidade (ponto "respirando") | 01, 09 | C1 · C2 · C3 | C1: ponto verde do `200 OK`. C2: ponto de "agentes e Claude Code" na ficha. C3: `online` na barra de status. |
| 4 | Cursor piscando | 02 | C2 · C3 | C2: caret depois de "agentes e Claude Code". C3: cursor em bloco no último prompt. |
| 5 | Elemento percorrendo um caminho (`animateMotion`) | 03, 10 | C1 (adaptado) | Linha vertical que varre o trace de ponta a ponta, em loop, como o cursor de tempo do Jaeger. |
| 6 | Traço que se desenha sozinho (`stroke-dasharray`/`stroke-dashoffset`) | 06, 08 | C2 | Sublinhado azul de caneta embaixo do nome e os ✓ da ficha se desenhando um a um. |
| 7 | Fundo quadriculado (`<pattern>`) | 01, 03 | C1 | Grade de fundo da capa inteira. |
| 8 | Janela de terminal com os botões do macOS | 02 | C3 | A capa inteira é a janela, com barra de título `cesar@arquitetura: ~/perfil`. |
| 9 | Folha pautada com margem vermelha | 04 | C2 | A capa inteira é a folha, com furos de fichário e margem. |

### Serviços externos (imagens geradas por URL)

| # | Recurso | Aparecia em | Usado em | Onde, exatamente |
|---|---|---|---|---|
| 10 | `readme-typing-svg` (texto digitando) | 02, 05, 10 | C3 | Logo abaixo da capa, com cor própria para cada tema (lilás no escuro, índigo no claro). |
| 11 | `skillicons.dev` (ícones da stack) | 01, 02, 03, 05, 06, 08, 09 | C1 | Seção **Stack**, com `theme=light`/`theme=dark` trocando pelo `<picture>`. |
| 12 | `github-readme-stats`: card de estatísticas | 02, 04, 06, 08, 09 | C1 | Seção **Telemetria**, sem o rank (`hide_rank`), em pt-BR, com tema claro/escuro. |
| 13 | `github-readme-stats`: linguagens mais usadas | 02, 08, rascunho 06 | C1 | Seção **Telemetria**, ao lado do card de estatísticas. |
| 14 | `github-readme-streak-stats` (sequência de contribuições) | 06 | C3 | Seção **`$ git log --graph`**, em pt-BR, com as cores da capa em cada tema. Troquei o endereço antigo do Heroku pelo atual (`streak-stats.demolab.com`). |
| 15 | Badges `shields.io` | 01 | C2 · C3 | C2: badges de blog, RSS e idioma abaixo da capa. C3: badges dinâmicos (versão do `csr-cockpit` e tamanho do catálogo, lidos do JSON do claude-code-kit), RSS e dev-note na tabela **`$ status`**. |

### Markdown e HTML que o GitHub renderiza

| # | Recurso | Aparecia em | Usado em | Onde, exatamente |
|---|---|---|---|---|
| 16 | Diagrama Mermaid | 03, 05, 10 (e rascunhos 03, 10) | C1 | Seção **O caminho de uma requisição**, como `sequenceDiagram` (os modelos usavam `flowchart`). O GitHub já adapta o Mermaid ao tema. |
| 17 | Bloco de código como terminal (`console`) | 02 | C3 | Seções **`~/sobre`** e o `exit` no final. |
| 18 | Árvore de diretórios em texto | 02 | C3 | Seção **`~/projetos`**. |
| 19 | Tabela Markdown | 01, 03, 05, 06, 08, 10 | C1 · C2 · C3 | C1: passos → artigos e projetos. C2: **Índice do caderno**. C3: **`$ status`**. |
| 20 | Grade em colunas com `<table>` HTML | 03, 08, 09 | C1 | Seção **Onde eu passo o tempo** (Arquitetura · Runtime · IA aplicada). |
| 21 | Citação como lema (`>`) | 01, 03, 04, 05, 06, 10 | C1 | Fecho: "Se não tem `traceparent`, não aconteceu." |
| 22 | Status com emoji (🟢) | 06 | C3 | Tabela **`$ status`**, com legenda 🟢 🔵 ⚪. |
| 23 | Tags em `inline code` | rascunhos 07, 09, 10 | C3 | Seção **`$ stack`**. |
| 24 | Chamada para o blog | 01, 04, 07 | C1 · C2 · C3 | C1: texto do **Sobre** e as leituras. C2: badges + a capa inteira. C3: barra de status da capa e badge de RSS. |
| 25 | Cards externos claro/escuro com `<picture>` | 09 | C1 · C3 | C1: stats, linguagens e skill icons. C3: texto digitando, streak e snake. |
| 26 | Lista de projetos com descrição | 01, 04, 07 | C1 · C2 | C1: tabela **Projetos**. C2: **Os rascunhos**. |

### GitHub Actions (nos modelos eram só ideia; aqui estão implementadas)

| # | Recurso | Aparecia em | Usado em | Onde, exatamente |
|---|---|---|---|---|
| 27 | Últimos artigos do blog via RSS | rascunhos 04, 08 | C2 | Seção **Últimas páginas**. Workflow `.github/workflows/capa-02-artigos.yml`, todo dia às 06:17 (Brasília). |
| 28 | Snake comendo o gráfico de contribuições | rascunho 08 | C3 | Fim da seção **`$ git log --graph`**. Workflow `.github/workflows/capa-03-snake.yml` gera as versões clara e escura todo dia. |
| 29 | Conteúdo que fica atualizado sem edição manual | 08 | C1 · C2 · C3 | C1: stats e linguagens. C2: artigos via RSS. C3: streak, snake e badges dinâmicos. |

## 2. Recursos não usados

| # | Recurso | Aparecia em | Por que ficou de fora |
|---|---|---|---|
| 30 | `github-readme-activity-graph` | 01, 06, 08, 10 | **Está fora do ar.** A instância pública responde `402 Payment required / DEPLOYMENT_DISABLED` (testado em 03/10/2026), ou seja, esses quatro modelos já mostravam imagem quebrada. A snake da C3 ocupa o lugar de "gráfico de atividade". |
| 31 | `capsule-render` (banner ondulado com fade-in) | rascunhos 05, 09 | Os banners autorais fazem o mesmo papel com mais personalidade e sem depender de serviço externo. |
| 32 | Nó que pulsa mudando de tamanho (`animate r`) | 05 | Fazia sentido no grafo de agentes do modelo 05, que também não entrou (#35). O pulso de opacidade (#3) cobre o efeito de "vivo". |
| 33 | Tracejado andando sem parar ("formigas marchando") | 04 | Movimento infinito numa linha decorativa distrai. Usei a mesma técnica para desenhar o traço uma vez só (#6). |
| 34 | Gradiente linear/radial no fundo | 01, 05 | Fundos chapados conversam melhor com o visual do próprio GitHub e são mais fáceis de manter iguais nos dois temas. |
| 35 | Grafo de nós (agentes ligados) | 05 | A parte de IA aparece de forma mais concreta: o comando do claude-code-kit na C3 e a ficha da C2. |
| 36 | Gráfico de linha que se desenha (sparkline) | 06, 08 | Era um gráfico decorativo, sem dado real. O trace da C1 cumpre o papel de "painel" com conteúdo que significa algo. |
| 37 | Barras de progresso em texto (`[████░░] 80%`) | 06 | Porcentagem de habilidade é um número inventado; fica pouco sério para um arquiteto. |
| 38 | Caixas de arquitetura desenhadas no SVG | 03, 10 | Substituídas pelo trace (C1), que mostra a arquitetura em funcionamento, e pelo Mermaid, que adapta ao tema sozinho. |
| 39 | Diagrama ASCII de caixas | rascunhos 03, 05 | O Mermaid faz o mesmo, fica legível no celular e muda de cor com o tema. |
| 40 | Atividade recente automática (commits/PRs via Action) | rascunho 08 | O próprio GitHub já mostra isso logo abaixo do README do perfil. |
| 41 | Troca de banner por horário (dia/noite via Action) | rascunho 09, `RECURSOS.md` antigo | A Action só sabe o horário do servidor, não o do visitante, e precisaria rodar várias vezes ao dia. A troca pelo tema (#2) é instantânea e não tem manutenção. |

## 3. Recursos novos (não existiam em nenhum modelo)

| Recurso | Onde |
|---|---|
| Texto digitado caractere a caractere **dentro do próprio SVG**, sem serviço externo (`clipPath` + `animate` discreto) | C1: o `traceparent`. C3: `whoami`, `cat foco.txt` e `claude plugin install …`. |
| Nome "escrito à caneta" (revelado da esquerda para a direita) | C2 |
| Waterfall de trace com spans crescendo em sequência | C1 |
| Marca-texto que passa por trás da frase | C2 |
| Ficha de estudo inclinada, com sombra, e checks que se desenham | C2 |
| Saídas de comando aparecendo em sequência, como num terminal de verdade | C3 |
| Barra de status no estilo do Claude Code | C3 |
| Monograma "CS" em blocos | C3 |
| `prefers-reduced-motion`: quem pede menos movimento no sistema vê a capa parada | todos os SVGs |
| Mermaid `sequenceDiagram` com `alt`/`else` | C1 |
| Seções recolhíveis com `<details>`, no formato de decisão (contexto · decisão · consequência) | C2: **Decisões que eu repito** |
| Cores próprias por tema também nos serviços externos (skillicons, typing, stats, streak) | C1 · C3 |

## 4. Segunda leva (C4–C6)

### Recursos dos modelos antigos reaproveitados

| # | Recurso | C4 · Trajetória | C5 · Painel | C6 · Neofetch |
|---|---|---|---|---|
| 1, 2 | Banner SVG autoral claro/escuro | capa | capa | capa e faixas de stack |
| 3 | Pulso de opacidade | ponto "hoje" na linha do tempo | — | `online` na barra de status |
| 4 | Cursor piscando | — | — | último prompt |
| 5 | Elemento percorrendo um caminho | — | evento indo de API até worker no mini C4 | — |
| 6 | Traço que se desenha | linha do tempo de 2011 a 2026 | linha do tempo da identidade | — |
| 8 | Janela de terminal | — | — | capa inteira |
| 10 | `readme-typing-svg` | — | — | abaixo da capa |
| 11 | Ícones da stack (skillicons) | painel **Stack** por área | bloco **Stack do dia a dia** | `ls ~/stack` na capa e tabela **`~/stack`** |
| 12, 13 | `github-readme-stats` (stats e linguagens) | — | seção **GitHub** | — |
| 14 | Streak de contribuições | — | — | **`$ git log --graph`** |
| 15 | Badges `shields.io` | LinkedIn, blog, claude-code-kit | LinkedIn, blog | LinkedIn, blog, claude-code-kit |
| 19 | Tabela Markdown | **Formação** e **Projetos pessoais** | **Stack completa** | **`~/stack`** e **`~/projetos`** |
| 20 | Grade com `<table>` HTML | **O que eu faço** | — | — |
| 17 | Bloco `console` | — | — | **`~/sobre`** |
| 28 | Snake | — | — | fim da página (workflow `capas-snake.yml`) |

Não entraram na segunda leva: Mermaid (#16), artigos via RSS (#27) e o traço de trace da C1, porque
eram conteúdo do blog e não sobre mim.

### Recursos novos da segunda leva

| Recurso | Onde |
|---|---|
| Linha do tempo animada com a trajetória real (estágio em 2011, dev Java, dev sênior em 2019, líder técnico em 2020, arquiteto de soluções em 2021) e uma faixa de formação (tecnólogo, pós, MBAs e certificação Scrum) | C4 (capa) · C5 (identidade) |
| Números do trabalho: 1.200+ commits (sem merges) em 36 serviços | C4 · C5 · C6 |
| Ícones da stack **dentro** do SVG, com animação de entrada um a um | C4 · C5 · C6 |
| Ícones que o skillicons não tem (Quarkus, Dynatrace, Jaeger, Cucumber, JUnit, Claude, MCP, LangChain, Mermaid, Excalidraw, Serverless, Keycloak) desenhados no mesmo molde, a partir do Simple Icons | C4 · C5 · C6 |
| Ícones de texto para o que não tem logo (ADR, C4/Structurizr, PlantUML, SNS/SQS, Google ADK) | C4 · C6 |
| Painel em blocos (bento) | C5 |
| `neofetch` como cartão de visita | C6 |
| Mini diagrama C4 animado | C5 |
| Cards de repositório (`github-readme-stats` pin) com tema claro/escuro | C5 · **Projetos** |
| Gráfico 3D de contribuições (`github-profile-3d-contrib`) | C4 · **Contribuições** (workflow `capa-04-3d.yml`) |
| Stack completa recolhível com `<details>` | C5 |

### De onde veio o conteúdo

- **Trajetória, formação e certificação:** LinkedIn (cargos, cursos e datas).
- **Números:** commits sem merge nos repositórios de serviço (fora repositórios de documentação). Commits
  de documentação não entraram: na wiki cada salvamento vira um commit, então o número não mede trabalho.
- **Stack:** arquivos de build dos serviços (`build.gradle`, `package.json`, Terraform, Serverless/SAM).
- **O que eu faço:** as ADRs e a forma como elas são escritas (ADR curta, C4 no Structurizr, padrões).
- Nada interno aparece nas capas: nenhum nome de ADR, sistema, parceiro ou endereço da empresa.

## 5. Modo claro e escuro: dá?

**Dá, e as três capas já fazem isso.** Existem dois jeitos:

1. **`<picture>` com `prefers-color-scheme`** (o que eu usei). O README aponta para dois arquivos, e o
   GitHub mostra um ou outro conforme o tema do visitante. É o jeito documentado pelo GitHub desde 2022
   e funciona em todos os navegadores:

   ```html
   <picture>
     <source media="(prefers-color-scheme: dark)" srcset="./assets/capa-dark.svg">
     <source media="(prefers-color-scheme: light)" srcset="./assets/capa-light.svg">
     <img src="./assets/capa-light.svg" alt="…">
   </picture>
   ```

2. **Um SVG só, com `@media (prefers-color-scheme: dark)` no `<style>` interno.** O navegador passa o
   `color-scheme` da página para a imagem, então também acompanha o tema do GitHub. Funciona no Chrome e
   no Firefox, mas o Safari nem sempre atualiza a imagem quando o tema muda. Por isso fiquei com o
   `<picture>`.

O tema segue a configuração de aparência do GitHub de quem visita (ou a do sistema, se a pessoa
deixou em "sync with system"). Não dá para trocar pelo horário do dia direto no README, porque o GitHub
não executa JavaScript (ver #41).

Fontes: [GitHub Changelog: tema em imagens no Markdown (GA)](https://github.blog/changelog/2022-08-15-specify-theme-context-for-images-in-markdown-ga) ·
[GitHub Blog: imagens que se ajustam ao modo claro e escuro](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/) ·
[MDN: `prefers-color-scheme` em SVG embutido](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
