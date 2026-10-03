<div align="center">

# Cesar Schutz
### Designing systems that remain understandable as they grow

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1100&center=true&vCenter=true&width=800&lines=Client+%E2%86%92+Gateway+%E2%86%92+Services+%E2%86%92+Events+%E2%86%92+Data;Domain+%E2%86%92+Boundaries+%E2%86%92+Contracts+%E2%86%92+Observability;Architecture+%E2%86%92+Code+%E2%86%92+Feedback+%E2%86%92+Evolution" />

</div>

```mermaid
flowchart LR
    UI[Client] --> GW[Gateway]
    GW --> S1[Service A]
    GW --> S2[Service B]
    S1 --> BUS((Events))
    S2 --> BUS
    BUS --> DB[(Data)]
    S1 -. traces .-> OBS[Observability]
    S2 -. traces .-> OBS
```

## Current landscape

| Layer | Technologies / interests |
|---|---|
| Domain | DDD, modularity, boundaries |
| Integration | APIs, events, messaging |
| Runtime | Java, Spring, containers |
| Platform | Cloud, Kubernetes, observability |
| Intelligence | Agents, MCP, ADK, LLM workflows |

## Selected experiments

`swagger-agent` · `swagger-agent-adk` · `first-mcp-weather` · `google-adk-cards` · `claude-code-kit`


---

### Recursos invisíveis deste modelo

- Typing SVG usado como “fluxo arquitetural animado”
- Mermaid renderizado pelo GitHub para arquitetura
- Na versão final eu faria um SVG próprio com pulsos percorrendo conexões
- Pode incluir animação CSS dentro do SVG, sem JavaScript no README

> Protótipo visual. Na versão final, posso substituir serviços externos por SVGs próprios e Actions no seu repositório.
