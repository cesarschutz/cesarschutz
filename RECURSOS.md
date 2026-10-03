# Notas sobre recursos dinâmicos

## Troca de painel claro/escuro

O GitHub suporta `<picture>` no Markdown. Exemplo:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img src="./assets/banner-dark.svg">
</picture>
```

O navegador escolhe o asset conforme o tema do visitante.

## Troca real por horário do dia

Isso não é feito diretamente pelo README. Existem duas abordagens:

1. Um serviço externo retorna uma imagem diferente conforme horário/localização.
2. Um GitHub Action roda em horários definidos e regenera/substitui o asset que o README referencia.

Para um perfil profissional, eu prefiro **tema claro/escuro automático** ou um SVG autoral que tenha aparência diferente em dark/light. Trocar por relógio é interessante, mas adiciona manutenção.

## Animações

O GitHub bloqueia JavaScript. Portanto animações devem vir de:
- SVG animado;
- GIF/WebP;
- serviços que retornam SVG;
- arquivos gerados por Actions.

A versão final pode ter SVGs próprios em `assets/`, evitando depender de serviços externos.
