"""Gera os SVGs do perfil em assets/: o terminal (claro e escuro) e os cards de projeto.

Para rodar: python3 scripts/perfil.py
O workflow .github/workflows/perfil.yml roda o script quando ele muda e gera a cobrinha todo dia.
"""
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- conteúdo

SOBRE = ("Sou arquiteto de software e soluções. Programo em Java desde 2011 e estou na plataforma de cartões desde "
         "2019, onde fui dev sênior, líder técnico e, desde 2021, arquiteto. Desde 2025 também cuido da arquitetura "
         "do programa de fidelidade.",
         "Trabalho perto do time: estou nas dailys, desenho a solução junto com os devs e continuo discutindo "
         "código, porque é ali que a decisão de arquitetura se prova.")

PERTO = ["participo das dailys",
         "desenho técnico junto com os devs",
         "apoio à sustentação quando o problema aparece em produção",
         "atualização de versões: Java, Spring Boot e dependências",
         "discussão de código e revisão de design"]
DESENHO = ["decisões técnicas tomadas com o time, com alternativas e consequências claras",
           "modelo C4 no Structurizr e fluxos em PlantUML e Mermaid",
           "padrões que o time reaproveita, como Transactional Outbox, Job Pattern, idempotência e eventos com SNS/SQS"]

FORMACAO = [  # período, título, detalhe, tipo (andamento | cert | None)
    ("2025 – 2026", "MBA em Arquitetura de Software", "Full Cycle  ·  em andamento", "andamento"),
    ("2025 – 2026", "MBA em Engenharia de Software com IA", "Full Cycle  ·  em andamento", "andamento"),
    ("2021 – 2022", "Pós-graduação em Engenharia de Software", "Unisinos", None),
    ("2018", "Agile Scrum Foundation", "certificação · EXIN", "cert"),
    ("2013 – 2019", "Tecnólogo em Análise e Desenvolvimento de Sistemas", "Senac RS", None),
    ("2009 – 2011", "Técnico em Informática", "Universitário Escola Técnica", None),
]

PROJETOS = [  # repositório, descrição, linguagem, status
    ("claude-code-kit", "Marketplace de plugins para o Claude Code: mods, skills, agentes, hooks e temas.", "TypeScript", "ativo"),
    ("CSRFinance", "Sistema financeiro para gerenciar as contas pessoais.", "TypeScript", "ativo"),
    ("blog", "O código do blog.cesarschutz.com.br, feito em Astro.", "Astro", "publicando"),
    ("blog-exemplos", "O código que acompanha os artigos do blog: Java, Spring e Terraform.", "Java", "ativo"),
    ("BrainAPI", "Transforma specs OpenAPI em endpoints usáveis em linguagem natural, via MCP.", "Java", "experimento"),
    ("langchain", "Estudos de LangChain: chains com LCEL, agentes com tools, memória e RAG com banco vetorial.", "Python", "estudo"),
    ("google-adk-cards", "Agentes sobre uma API de cartões, com o Google ADK em Java.", "Java", "experimento"),
    ("knowledge-base", "Minha base de conhecimento técnico.", "TypeScript", "em pausa"),
]
COR_LINGUAGEM = {"TypeScript": "#3178c6", "Java": "#b07219", "Python": "#3572A5", "Astro": "#ff5a03"}
COR_STATUS = {"ativo": "green", "publicando": "green", "experimento": "blue", "estudo": "purple", "em pausa": "muted"}

TEMAS = {
    "light": dict(win="#ffffff", bar="#f6f8fa", card="#f6f8fa", border="#d0d7de", faint="#d8dee4", fg="#1f2328",
                  muted="#59636e", blue="#0969da", purple="#8250df", green="#1a7f37", orange="#bc4c00",
                  teal="#1b7c83", lav="#5a5fc8", terra="#b4542f", pill_fg="#ffffff"),
    "dark": dict(win="#161b22", bar="#1c2128", card="#0d1117", border="#30363d", faint="#21262d", fg="#e6edf3",
                 muted="#9198a1", blue="#58a6ff", purple="#bc8cff", green="#3fb950", orange="#ffa657",
                 teal="#39c5cf", lav="#b1b9f9", terra="#d77757", pill_fg="#161b22"),
}

# ---------------------------------------------------------------- SVG

SANS = '-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace'
CSS = f"""
.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}.b{{font-weight:700}}
@keyframes in{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
@keyframes draw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@keyframes pop{{0%{{opacity:0;transform:scale(.55)}}70%{{opacity:1;transform:scale(1.06)}}100%{{opacity:1;transform:scale(1)}}}}
@keyframes listras{{from{{transform:translateX(0)}}to{{transform:translateX(-28px)}}}}
.f{{animation:in .45s ease-out both}}
.blink{{animation:blink 1.05s steps(1) infinite}}
.pulse{{animation:pulse 2.4s ease-in-out infinite}}
.draw{{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1s ease-out both}}
.pop{{transform-box:fill-box;transform-origin:center;animation:pop .5s cubic-bezier(.2,.7,.3,1) both}}
.listras{{animation:listras 1.2s linear infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.draw{{stroke-dashoffset:0}}}}
"""


def d(t):
    return f'style="animation-delay:{t:.2f}s"'


def mono(s, x, y, size, fill, extra="", cls="mono"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" class="{cls}" {extra} '
            f'textLength="{len(s) * size * 0.6:.1f}" lengthAdjust="spacing" xml:space="preserve">{escape(s)}</text>')


def text(s, x, y, size, fill, cls="sans", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" class="{cls}" {extra}>{escape(s)}</text>'


def cx_mono(s, cx, y, size, fill, cls="mono"):
    return mono(s, cx - len(s) * size * 0.6 / 2, y, size, fill, cls=cls)


class Digitador:
    """Texto monoespaçado revelado caractere a caractere por um clipPath (SMIL)."""

    def __init__(self):
        self.defs, self.n = [], 0

    def __call__(self, s, x, y, size, fill, begin, cps=22):
        self.n += 1
        cid, cw, n = f"dig{self.n}", size * 0.6, len(s)
        larguras = ";".join(f"{i * cw + (2 if i else 0):.1f}" for i in range(n + 1))
        tempos = ";".join(f"{i / n:.4f}" for i in range(n + 1))
        self.defs.append(f'<clipPath id="{cid}"><rect x="{x - 1}" y="{y - size}" height="{size * 1.5:.1f}" width="0">'
                         f'<animate attributeName="width" values="{larguras}" keyTimes="{tempos}" calcMode="discrete" '
                         f'begin="{begin:.2f}s" dur="{n / cps:.2f}s" fill="freeze"/></rect></clipPath>')
        return mono(s, x, y, size, fill).replace("<text ", f'<text clip-path="url(#{cid})" ', 1), begin + n / cps


def terminal(p):
    W, X, S = 1200, 52, 17
    cw = S * 0.6
    dig = Digitador()
    b, defs = [], []
    y, relogio = 100, 0.3
    largura = W - 2 * X

    def comando(cmd, t0):
        b.append(f'<g class="f" {d(t0)}>' + mono("❯", X, y, S, p["terra"], cls="mono b")
                 + mono("~", X + 2 * cw, y, S, p["lav"], cls="mono b") + "</g>")
        txt, fim = dig(cmd, X + 4 * cw, y, S, p["fg"], t0 + 0.15)
        b.append(txt)
        return fim

    def secao(titulo, t0, cor):
        x2 = X + 34 + len(titulo) * 9.2 + 16
        b.append(f'<g class="f" {d(t0)}><path d="M{X} {y}h24" stroke="{p[cor]}" stroke-width="2"/>'
                 + mono(titulo.upper(), X + 34, y + 4.5, 12, p[cor], 'letter-spacing="2"', "mono b")
                 + f'<path d="M{x2:.0f} {y}H{W - X}" stroke="{p["border"]}"/></g>')

    # sobre
    fim = comando("cat sobre.md", relogio)
    y += 40
    secao("sobre", fim + 0.1, "lav")
    y += 34
    k = 0
    for par in SOBRE:
        for linha in textwrap.wrap(par, 112):
            b.append(f'<g class="f" {d(fim + 0.25 + k * 0.08)}>' + text(linha, X, y, 18, p["fg"]) + "</g>")
            y, k = y + 29, k + 1
        y += 12
    relogio = fim + 0.4 + k * 0.08
    y += 18

    # como eu trabalho
    fim = comando("cat como-eu-trabalho.md", relogio)
    y += 40
    secao("como eu trabalho", fim + 0.1, "terra")
    y += 26
    gap = 24
    colw = (largura - gap) / 2
    blocos = []
    for tit, cor, itens in (("perto do time", "lav", PERTO), ("decisões e desenho", "orange", DESENHO)):
        blocos.append((tit, cor, [textwrap.wrap(it, 52) for it in itens]))
    h = max(64 + sum(len(l) * 24 + 12 for l in ls) + 6 for _, _, ls in blocos)
    for ci, (tit, cor, linhas) in enumerate(blocos):
        cx, t0 = X + ci * (colw + gap), fim + 0.2 + ci * 0.15
        b.append(f'<rect x="{cx:.1f}" y="{y}" width="{colw:.1f}" height="{h}" rx="12" fill="{p["card"]}" stroke="{p["border"]}" class="f" {d(t0)}/>')
        b.append(f'<rect x="{cx:.1f}" y="{y}" width="4" height="{h}" rx="2" fill="{p[cor]}" class="f" {d(t0)}/>')
        b.append(f'<g class="f" {d(t0)}>' + text(tit, cx + 24, y + 38, 19, p[cor], "sans b") + "</g>")
        yy = y + 72
        for i, partes in enumerate(linhas):
            ti = t0 + 0.25 + i * 0.12
            b.append(f'<circle cx="{cx + 30:.1f}" cy="{yy - 5}" r="4" fill="{p[cor]}" class="pop" {d(ti)}/>')
            for j, linha in enumerate(partes):
                b.append(f'<g class="f" {d(ti)}>' + text(linha, cx + 46, yy + j * 24, 16, p["fg"]) + "</g>")
            yy += len(partes) * 24 + 12
    relogio = fim + 0.6 + max(len(PERTO), len(DESENHO)) * 0.12
    y += h + 44

    # stack (em construção)
    fim = comando("ls stack/", relogio)
    y += 40
    secao("stack", fim + 0.1, "teal")
    y += 24
    t0 = fim + 0.2
    b.append(f'<rect x="{X}" y="{y}" width="{largura}" height="128" rx="12" fill="none" stroke="{p["border"]}" stroke-width="1.5" stroke-dasharray="6 6" class="f" {d(t0)}/>')
    b.append(f'<g class="f" {d(t0)}>' + text("em construção", X + 32, y + 50, 22, p["fg"], "sans b")
             + mono("a lista de ferramentas está sendo revisada e volta em breve, em ícones por área", X + 32, y + 80, 14, p["muted"]) + "</g>")
    bx, bw, by = X + 32, largura - 64, y + 98
    defs.append(f'<clipPath id="barra"><rect x="{bx}" y="{by}" width="{bw * 0.62:.0f}" height="10" rx="5"/></clipPath>')
    b.append(f'<g class="f" {d(t0 + 0.2)}><rect x="{bx}" y="{by}" width="{bw}" height="10" rx="5" fill="{p["faint"]}"/>'
             '<g clip-path="url(#barra)"><g class="listras">'
             + "".join(f'<path d="M{bx + i * 14} {by + 10}l10 -10h7l-10 10z" fill="{p["teal"]}" opacity=".85"/>'
                       for i in range(-2, int(bw * 0.62 / 14) + 3)) + "</g></g></g>")
    relogio = t0 + 0.8
    y += 128 + 44

    # formação
    fim = comando("cat formacao.md", relogio)
    y += 40
    secao("formação", fim + 0.1, "purple")
    y += 40
    lx, rh = X + 150, 64
    b.append(f'<path d="M{lx} {y - 8}V{y + (len(FORMACAO) - 1) * rh + 8}" stroke="{p["border"]}" stroke-width="2" '
             f'pathLength="1" class="draw" style="animation-delay:{fim + 0.2:.2f}s"/>')
    for i, (per, titulo, detalhe, tipo) in enumerate(FORMACAO):
        yy, ti = y + i * rh, fim + 0.3 + i * 0.12
        b.append(f'<g class="f" {d(ti)}>' + mono(per, X, yy + 5, 14, p["muted"]) + "</g>")
        if tipo == "cert":
            b.append(f'<rect x="{lx - 7}" y="{yy - 7}" width="14" height="14" fill="{p["green"]}" stroke="{p["win"]}" '
                     f'stroke-width="2" transform="rotate(45 {lx} {yy})" class="f" {d(ti)}/>')
        else:
            cor = p["teal"] if tipo == "andamento" else p["purple"]
            b.append(f'<circle cx="{lx}" cy="{yy}" r="7" fill="{p["win"]}" stroke="{cor}" stroke-width="3" class="pop" {d(ti)}/>')
        b.append(f'<g class="f" {d(ti)}>' + text(titulo, lx + 24, yy + 6, 18, p["fg"], "sans b")
                 + text(detalhe, lx + 24, yy + 30, 15, p["muted"]) + "</g>")
    relogio = fim + 0.5 + len(FORMACAO) * 0.12
    y += (len(FORMACAO) - 1) * rh + 76

    b.append(f'<g class="f" {d(relogio)}>' + mono("❯", X, y, S, p["terra"], cls="mono b") + mono("~", X + 2 * cw, y, S, p["lav"], cls="mono b") + "</g>")
    b.append(f'<g class="f" {d(relogio)}><rect x="{X + 4 * cw}" y="{y - S + 3}" width="{cw}" height="{S + 3}" fill="{p["lav"]}" class="blink"/></g>')
    H = int(y + 32 + 44)

    moldura = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{p["win"]}" stroke="{p["border"]}"/>',
               f'<path d="M1 45V15a14 14 0 0 1 14 -14H{W - 15}a14 14 0 0 1 14 14V45Z" fill="{p["bar"]}"/>',
               f'<path d="M1 45H{W - 1}" stroke="{p["border"]}"/>']
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        moldura.append(f'<circle cx="{30 + i * 22}" cy="23" r="6.5" fill="{c}"/>')
    moldura.append(cx_mono("cesar@arquitetura: ~", W / 2, 28, 13, p["muted"]))
    sy = H - 44
    moldura += [f'<path d="M1 {sy}H{W - 1}V{H - 15}a14 14 0 0 1 -14 14H15a14 14 0 0 1 -14 -14Z" fill="{p["bar"]}"/>',
                f'<path d="M1 {sy}H{W - 1}" stroke="{p["border"]}"/>']
    pill = " cesarschutz "
    moldura.append(f'<rect x="20" y="{sy + 10}" width="{len(pill) * 8.4:.0f}" height="24" rx="12" fill="{p["lav"]}"/>')
    moldura.append(mono(pill, 20, sy + 27, 14, p["pill_fg"], cls="mono b"))
    moldura.append(mono("arquiteto de software e soluções  ·  java · spring · aws  ·  claude code", 20 + len(pill) * 8.4 + 16, sy + 27, 14, p["muted"]))
    moldura.append(f'<circle cx="{W - 96}" cy="{sy + 22}" r="5" fill="{p["green"]}" class="pulse"/>')
    moldura.append(mono("online", W - 84, sy + 27, 14, p["muted"]))

    alt = ("Terminal do perfil. Sobre: " + " ".join(SOBRE) + " Como eu trabalho, perto do time: " + "; ".join(PERTO)
           + ". Decisões e desenho: " + "; ".join(DESENHO) + ". Stack: em construção. Formação: "
           + "; ".join(f"{t}, {dd}, {pp}" for pp, t, dd, _ in FORMACAO) + ".")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(alt)}">\n'
            f'<title>{escape(alt)}</title>\n<style>{CSS}</style>\n<defs>{"".join(dig.defs + defs)}</defs>\n'
            + "\n".join(moldura + b) + "\n</svg>\n")


def card(p, nome, desc, lang, st):
    W, H = 600, 180
    cor = p[COR_STATUS[st]]
    g = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{p["bar"]}" stroke="{p["border"]}" stroke-width="1.5"/>',
         f'<g transform="translate(28 30)" fill="none" stroke="{p["muted"]}" stroke-width="1.8" stroke-linejoin="round">'
         '<path d="M3 2h13v16H5.5A2.5 2.5 0 0 1 3 15.5z"/><path d="M3 15.5A2.5 2.5 0 0 1 5.5 13H16"/></g>',
         text(nome, 60, 47, 22, p["fg"], "sans b")]
    for j, linha in enumerate(textwrap.wrap(desc, 62)[:2]):
        g.append(text(linha, 28, 86 + j * 23, 16, p["muted"]))
    g.append(f'<circle cx="35" cy="{H - 30}" r="6" fill="{COR_LINGUAGEM[lang]}"/>')
    g.append(text(lang, 50, H - 25, 14, p["fg"]))
    sw = len(st) * 8.4 + 40
    sx = W - 24 - sw
    g.append(f'<rect x="{sx:.1f}" y="{H - 44}" width="{sw:.1f}" height="28" rx="14" fill="none" stroke="{p["border"]}"/>')
    g.append(f'<circle cx="{sx + 16:.1f}" cy="{H - 30}" r="4.5" fill="{cor}"' + (' class="pulse"' if st in ("ativo", "publicando") else "") + "/>")
    g.append(mono(st, sx + 28, H - 25.5, 14, p["fg"]))
    alt = f"{nome}: {desc} Linguagem: {lang}. Status: {st}."
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(alt)}">'
            f'<title>{escape(alt)}</title><style>{CSS}</style><g class="f">{"".join(g)}</g></svg>\n')


def main():
    for tema, p in TEMAS.items():
        destino = RAIZ / "assets" / f"terminal-{tema}.svg"
        destino.write_text(terminal(p), encoding="utf-8")
        print(destino.relative_to(RAIZ), f"{destino.stat().st_size // 1024} KB")
        for nome, desc, lang, st in PROJETOS:
            (RAIZ / "assets" / f"projeto-{nome.lower()}-{tema}.svg").write_text(card(p, nome, desc, lang, st), encoding="utf-8")


if __name__ == "__main__":
    main()
