"""Gera os SVGs do perfil em assets/: o header (linha do tempo), o terminal e os cards de projeto, claro e escuro.

Para rodar: python3 scripts/perfil.py
O workflow .github/workflows/perfil.yml roda o script quando ele muda e gera a cobrinha todo dia.

Os SVGs têm 1200 de largura, mas o README do perfil mostra uns 840 px (cerca de 70%). Por isso nenhum texto
fica abaixo de 15–16 no desenho: na tela, isso dá uns 11 px.
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
    "light": dict(win="#ffffff", bar="#f6f8fa", card="#f6f8fa", hdr="#f6f8fa", border="#d0d7de", faint="#d8dee4",
                  fg="#1f2328", muted="#59636e", blue="#0969da", faint_blue="#80b7f0", purple="#8250df",
                  green="#1a7f37", orange="#bc4c00", teal="#1b7c83", lav="#5a5fc8", terra="#b4542f", pill_fg="#ffffff"),
    "dark": dict(win="#161b22", bar="#1c2128", card="#0d1117", hdr="#161b22", border="#30363d", faint="#21262d",
                 fg="#e6edf3", muted="#9198a1", blue="#58a6ff", faint_blue="#1f6feb", purple="#bc8cff",
                 green="#3fb950", orange="#ffa657", teal="#39c5cf", lav="#b1b9f9", terra="#d77757", pill_fg="#161b22"),
}

# ---------------------------------------------------------------- SVG

SANS = '-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace'
CSS = f"""
.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}.b{{font-weight:700}}
@keyframes in{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
@keyframes draw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@keyframes pop{{0%{{opacity:0;transform:scale(.55)}}70%{{opacity:1;transform:scale(1.06)}}100%{{opacity:1;transform:scale(1)}}}}
@keyframes listras{{from{{transform:translateX(0)}}to{{transform:translateX(-28px)}}}}
.f{{animation:in .45s ease-out both}}
.u{{animation:up .6s ease-out both}}
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


def svg(W, H, alt, corpo, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(alt)}">\n'
            f'<title>{escape(alt)}</title>\n<style>{CSS}</style>\n<defs>{defs}</defs>\n{corpo}\n</svg>\n')


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


# ---------------------------------------------------------------- header: linha do tempo

def cabecalho(p):
    W, H = 1200, 614
    b = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{p["hdr"]}" stroke="{p["border"]}"/>']
    b.append(f'<g class="f" {d(0.1)}>' + mono("ARQUITETO DE SOFTWARE E SOLUÇÕES", 64, 80, 17, p["blue"], 'letter-spacing="3"', "mono b") + "</g>")
    b.append(text("Cesar Schutz", 62, 150, 66, p["fg"], "sans b u", d(0.25)))
    b.append(text("Programo em Java desde 2011. Na plataforma de cartões desde 2019:", 64, 198, 23, p["muted"], "sans u", d(0.45)))
    b.append(text("dev sênior, líder técnico e, desde 2021, arquiteto perto do time.", 64, 230, 23, p["muted"], "sans u", d(0.55)))
    for i, (num, linhas) in enumerate([("2011", ["Java desde", "o estágio"]), ("2021", ["arquiteto de", "software e", "soluções"])]):
        x, t0 = 880 + i * 160, 0.7 + i * 0.15
        g = [f'<path d="M{x - 22} 58V196" stroke="{p["border"]}"/>' if i else "", text(num, x, 116, 42, p["fg"], "sans b")]
        g += [mono(l, x, 146 + k * 21, 16, p["muted"]) for k, l in enumerate(linhas)]
        b.append(f'<g class="u" {d(t0)}>' + "".join(g) + "</g>")

    x0, x1, ly = 70, 1100, 406
    yx = lambda yr: x0 + (yr - 2011) * (x1 - x0) / 15
    T0, TD = 0.9, 2.6
    t_of = lambda yr: T0 + (yx(yr) - x0) / (x1 - x0) * TD
    def centro(cx, s, size):  # mantém o rótulo dentro do card
        meia = len(s) * size * 0.6 / 2
        return min(max(cx, 24 + meia), W - 24 - meia)

    b.append(f'<path d="M{x0} {ly}H{x1}" stroke="{p["faint"]}" stroke-width="5" stroke-linecap="round"/>')
    for yr in range(2011, 2027):
        x = yx(yr)
        if yr in (2011, 2014, 2017, 2020, 2023, 2026):
            b.append(f'<g class="f" {d(t_of(yr))}>' + cx_mono(str(yr), x, ly + 32, 15, p["muted"]) + "</g>")
        else:
            b.append(f'<circle cx="{x:.1f}" cy="{ly}" r="2.5" fill="{p["muted"]}" opacity=".5"/>')

    for ya, yb, cor, nome in ((2011.92, 2013.92, "faint_blue", "estágio"), (2013.92, 2019.9, "blue", "desenvolvedor Java"),
                              (2019.92, 2020.5, "green", None), (2020.5, 2021.92, "purple", "líder técnico"),
                              (2021.92, 2026, "orange", "arquiteto de software e soluções")):
        xa, xb = yx(ya), yx(yb)
        b.append(f'<rect x="{xa:.1f}" y="{ly - 5}" width="0" height="10" rx="5" fill="{p[cor]}">'
                 f'<animate attributeName="width" from="0" to="{xb - xa:.1f}" begin="{t_of(ya):.2f}s" '
                 f'dur="{t_of(yb) - t_of(ya):.2f}s" fill="freeze"/></rect>')
        if nome:
            cx = W if yb == 2026 else (xa + xb) / 2  # a última fase fica alinhada à direita
            b.append(f'<g class="f" {d(t_of((ya + yb) / 2))}>' + cx_mono(nome, centro(cx, nome, 17), ly + 62, 17, p[cor], "mono b") + "</g>")

    for yr, tier, l1, l2, cor in ((2011.92, 1, "estágio em Java", "imagens médicas", "faint_blue"),
                                  (2013.92, 2, "desenvolvedor Java", "Java SE", "blue"),
                                  (2015.37, 1, "Java EE e JSF", "sistemas web", "blue"),
                                  (2017.7, 2, "microsserviços", "Spring Cloud e Angular", "blue"),
                                  (2019.92, 1, "plataforma de cartões", "dev Java sênior", "green"),
                                  (2021.92, 2, "arquiteto de software", "e soluções, perto do time", "orange"),
                                  (2025.85, 1, "programa de fidelidade", "motor de pontos", "orange")):
        x, t0 = yx(yr), t_of(yr)
        top = ly - (46 if tier == 1 else 106)
        lx = centro(x, max(l1, l2, key=len), 17)
        b.append(f'<path d="M{x:.1f} {ly - 11}V{top + 8}" stroke="{p[cor]}" stroke-dasharray="{"0" if tier == 1 else "2 3"}" class="f" {d(t0)}/>')
        b.append(f'<circle cx="{x:.1f}" cy="{ly}" r="9" fill="{p["hdr"]}" stroke="{p[cor]}" stroke-width="3.5" class="pop" {d(t0)}/>')
        b.append(f'<g class="f" {d(t0 + 0.1)}>' + cx_mono(l1, lx, top - 22, 17, p["fg"], "mono b") + cx_mono(l2, lx, top, 17, p["muted"]) + "</g>")

    # formação
    ly2 = ly + 112
    b.append(f'<g class="f" {d(T0)}>' + mono("FORMAÇÃO", x0 - 2, ly2 - 20, 14, p["muted"], 'letter-spacing="2"', "mono b") + "</g>")
    b.append(f'<path d="M{x0} {ly2}H{x1}" stroke="{p["faint"]}" stroke-width="2" stroke-dasharray="2 5"/>')
    for ya, yb, dy in ((2013.0, 2019.5, 0), (2021.0, 2022.9, 0), (2025.42, 2026.96, -6), (2025.5, 2026.5, 6)):
        xa, xb = yx(ya), min(yx(yb), x1 + 30)
        b.append(f'<rect x="{xa:.1f}" y="{ly2 - 4 + dy}" width="0" height="8" rx="4" fill="{p["teal"]}">'
                 f'<animate attributeName="width" from="0" to="{xb - xa:.1f}" begin="{t_of(ya):.2f}s" '
                 f'dur="{max(t_of(min(yb, 2026)) - t_of(ya), .3):.2f}s" fill="freeze"/></rect>')
    fs = 16
    for cx, dy, s, tt in ((yx(2016.25), 34, "tecnólogo em ADS · Senac RS", 2016), (yx(2021.95), 34, "pós em eng. de software · Unisinos", 2022),
                          (None, 58, "MBA arquitetura de software", 2025.9), (None, 82, "MBA eng. de software com IA", 2025.9)):
        cx = cx if cx is not None else W - 24 - len(s) * fs * 0.6 / 2
        b.append(f'<g class="f" {d(t_of(tt) + 0.2)}>' + cx_mono(s, centro(cx, s, fs), ly2 + dy, fs, p["fg"]) + "</g>")
    xc = yx(2018.7)
    b.append(f'<rect x="{xc - 7:.1f}" y="{ly2 - 7}" width="14" height="14" fill="{p["green"]}" stroke="{p["hdr"]}" stroke-width="2" '
             f'transform="rotate(45 {xc:.1f} {ly2})" class="f" {d(t_of(2018.7))}/>')
    xl = 300
    b.append(f'<g class="f" {d(t_of(2018.7) + 0.2)}>'
             f'<rect x="{xl}" y="{ly2 + 47}" width="10" height="10" fill="{p["green"]}" transform="rotate(45 {xl + 5} {ly2 + 52})"/>'
             + mono("certificação: Agile Scrum Foundation · EXIN (2018)", xl + 20, ly2 + 58, fs, p["muted"]) + "</g>")

    xe, t0 = yx(2026), t_of(2026)
    b.append(f'<circle cx="{xe:.1f}" cy="{ly}" r="18" fill="{p["orange"]}" opacity=".18" class="pulse" style="animation-delay:{t0:.2f}s"/>')
    b.append(f'<circle cx="{xe:.1f}" cy="{ly}" r="8" fill="{p["orange"]}" class="pop" {d(t0)}/>')
    b.append(f'<g class="f" {d(t0 + 0.1)}>' + mono("hoje", xe + 24, ly + 6, 17, p["orange"], cls="mono b") + "</g>")

    alt = ("Cesar Schutz, arquiteto de software e soluções. Linha do tempo de 2011 até hoje: estágio em Java de 2011 a 2013, "
           "desenvolvedor Java SE em 2013, Java EE e JSF em 2015, microsserviços em 2017, plataforma de cartões como dev sênior "
           "em 2019, líder técnico em 2020, arquiteto de software e soluções desde 2021 e programa de fidelidade desde 2025. "
           "Formação: tecnólogo em ADS, pós em engenharia de software, MBAs em arquitetura de software e em engenharia de "
           "software com IA; certificação Agile Scrum Foundation (2018).")
    return svg(W, H, alt, "\n".join(b))


# ---------------------------------------------------------------- terminal

def terminal(p):
    W, X, S = 1200, 52, 22
    cw = S * 0.6
    dig = Digitador()
    b, defs = [], []
    y, relogio = 112, 0.3
    largura = W - 2 * X

    def comando(cmd, t0):
        b.append(f'<g class="f" {d(t0)}>' + mono("❯", X, y, S, p["terra"], cls="mono b")
                 + mono("~", X + 2 * cw, y, S, p["lav"], cls="mono b") + "</g>")
        txt, fim = dig(cmd, X + 4 * cw, y, S, p["fg"], t0 + 0.15)
        b.append(txt)
        return fim

    def secao(titulo, t0, cor):
        x2 = X + 40 + len(titulo) * (16 * 0.6 + 2) + 16
        b.append(f'<g class="f" {d(t0)}><path d="M{X} {y}h28" stroke="{p[cor]}" stroke-width="2.5"/>'
                 + mono(titulo.upper(), X + 40, y + 5.5, 16, p[cor], 'letter-spacing="2"', "mono b")
                 + f'<path d="M{x2:.0f} {y}H{W - X}" stroke="{p["border"]}"/></g>')

    # sobre
    fim = comando("cat sobre.md", relogio)
    y += 48
    secao("sobre", fim + 0.1, "lav")
    y += 44
    k = 0
    for par in SOBRE:
        for linha in textwrap.wrap(par, 93):
            b.append(f'<g class="f" {d(fim + 0.25 + k * 0.08)}>' + text(linha, X, y, 24, p["fg"]) + "</g>")
            y, k = y + 37, k + 1
        y += 14
    relogio = fim + 0.4 + k * 0.08
    y += 22

    # como eu trabalho
    fim = comando("cat como-eu-trabalho.md", relogio)
    y += 48
    secao("como eu trabalho", fim + 0.1, "terra")
    y += 30
    gap = 24
    colw = (largura - gap) / 2
    blocos = [(tit, cor, [textwrap.wrap(it, 42) for it in itens])
              for tit, cor, itens in (("perto do time", "lav", PERTO), ("decisões e desenho", "orange", DESENHO))]
    lh = 30
    h = max(84 + sum(len(l) * lh + 14 for l in ls) + 8 for _, _, ls in blocos)
    for ci, (tit, cor, linhas) in enumerate(blocos):
        cx, t0 = X + ci * (colw + gap), fim + 0.2 + ci * 0.15
        b.append(f'<rect x="{cx:.1f}" y="{y}" width="{colw:.1f}" height="{h}" rx="14" fill="{p["card"]}" stroke="{p["border"]}" class="f" {d(t0)}/>')
        b.append(f'<rect x="{cx:.1f}" y="{y}" width="5" height="{h}" rx="2.5" fill="{p[cor]}" class="f" {d(t0)}/>')
        b.append(f'<g class="f" {d(t0)}>' + text(tit, cx + 28, y + 46, 25, p[cor], "sans b") + "</g>")
        yy = y + 90
        for i, partes in enumerate(linhas):
            ti = t0 + 0.25 + i * 0.12
            b.append(f'<circle cx="{cx + 34:.1f}" cy="{yy - 7}" r="5" fill="{p[cor]}" class="pop" {d(ti)}/>')
            for j, linha in enumerate(partes):
                b.append(f'<g class="f" {d(ti)}>' + text(linha, cx + 54, yy + j * lh, 21, p["fg"]) + "</g>")
            yy += len(partes) * lh + 14
    relogio = fim + 0.6 + max(len(PERTO), len(DESENHO)) * 0.12
    y += h + 52

    # stack (em construção)
    fim = comando("ls stack/", relogio)
    y += 48
    secao("stack", fim + 0.1, "teal")
    y += 28
    t0, bh = fim + 0.2, 156
    b.append(f'<rect x="{X}" y="{y}" width="{largura}" height="{bh}" rx="14" fill="none" stroke="{p["border"]}" stroke-width="1.5" stroke-dasharray="7 7" class="f" {d(t0)}/>')
    b.append(f'<g class="f" {d(t0)}>' + text("em construção", X + 34, y + 58, 28, p["fg"], "sans b")
             + mono("a lista de ferramentas está sendo revisada e volta em breve, em ícones por área", X + 34, y + 94, 17, p["muted"]) + "</g>")
    bx, bw, by = X + 34, largura - 68, y + 118
    defs.append(f'<clipPath id="barra"><rect x="{bx}" y="{by}" width="{bw * 0.62:.0f}" height="12" rx="6"/></clipPath>')
    b.append(f'<g class="f" {d(t0 + 0.2)}><rect x="{bx}" y="{by}" width="{bw}" height="12" rx="6" fill="{p["faint"]}"/>'
             '<g clip-path="url(#barra)"><g class="listras">'
             + "".join(f'<path d="M{bx + i * 14} {by + 12}l12 -12h7l-12 12z" fill="{p["teal"]}" opacity=".85"/>'
                       for i in range(-2, int(bw * 0.62 / 14) + 3)) + "</g></g></g>")
    relogio = t0 + 0.8
    y += bh + 52

    # formação
    fim = comando("cat formacao.md", relogio)
    y += 48
    secao("formação", fim + 0.1, "purple")
    y += 48
    lx, rh = X + 166, 78
    b.append(f'<path d="M{lx} {y - 10}V{y + (len(FORMACAO) - 1) * rh + 10}" stroke="{p["border"]}" stroke-width="2.5" '
             f'pathLength="1" class="draw" style="animation-delay:{fim + 0.2:.2f}s"/>')
    for i, (per, titulo, detalhe, tipo) in enumerate(FORMACAO):
        yy, ti = y + i * rh, fim + 0.3 + i * 0.12
        b.append(f'<g class="f" {d(ti)}>' + mono(per, X, yy + 6, 18, p["muted"]) + "</g>")
        if tipo == "cert":
            b.append(f'<rect x="{lx - 9}" y="{yy - 9}" width="18" height="18" fill="{p["green"]}" stroke="{p["win"]}" '
                     f'stroke-width="2.5" transform="rotate(45 {lx} {yy})" class="f" {d(ti)}/>')
        else:
            cor = p["teal"] if tipo == "andamento" else p["purple"]
            b.append(f'<circle cx="{lx}" cy="{yy}" r="9" fill="{p["win"]}" stroke="{cor}" stroke-width="3.5" class="pop" {d(ti)}/>')
        b.append(f'<g class="f" {d(ti)}>' + text(titulo, lx + 30, yy + 8, 23, p["fg"], "sans b")
                 + text(detalhe, lx + 30, yy + 37, 19, p["muted"]) + "</g>")
    relogio = fim + 0.5 + len(FORMACAO) * 0.12
    y += (len(FORMACAO) - 1) * rh + 92

    b.append(f'<g class="f" {d(relogio)}>' + mono("❯", X, y, S, p["terra"], cls="mono b") + mono("~", X + 2 * cw, y, S, p["lav"], cls="mono b") + "</g>")
    b.append(f'<g class="f" {d(relogio)}><rect x="{X + 4 * cw}" y="{y - S + 4}" width="{cw}" height="{S + 4}" fill="{p["lav"]}" class="blink"/></g>')
    BB = 54  # altura das barras de título e de status
    H = int(y + 40 + BB)

    moldura = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["win"]}" stroke="{p["border"]}"/>',
               f'<path d="M1 {BB}V17a16 16 0 0 1 16 -16H{W - 17}a16 16 0 0 1 16 16V{BB}Z" fill="{p["bar"]}"/>',
               f'<path d="M1 {BB}H{W - 1}" stroke="{p["border"]}"/>']
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        moldura.append(f'<circle cx="{34 + i * 26}" cy="{BB / 2}" r="8" fill="{c}"/>')
    moldura.append(cx_mono("cesar@arquitetura: ~", W / 2, BB / 2 + 6, 17, p["muted"]))
    sy = H - BB
    moldura += [f'<path d="M1 {sy}H{W - 1}V{H - 17}a16 16 0 0 1 -16 16H17a16 16 0 0 1 -16 -16Z" fill="{p["bar"]}"/>',
                f'<path d="M1 {sy}H{W - 1}" stroke="{p["border"]}"/>']
    pill, fs = " cesarschutz ", 17
    pw = len(pill) * fs * 0.6
    moldura.append(f'<rect x="20" y="{sy + 12}" width="{pw:.0f}" height="30" rx="15" fill="{p["lav"]}"/>')
    moldura.append(mono(pill, 20, sy + 33, fs, p["pill_fg"], cls="mono b"))
    moldura.append(mono("arquiteto de software e soluções  ·  java · spring · aws", 20 + pw + 18, sy + 33, fs, p["muted"]))
    moldura.append(f'<circle cx="{W - 110}" cy="{sy + 27}" r="6" fill="{p["green"]}" class="pulse"/>')
    moldura.append(mono("online", W - 96, sy + 33, fs, p["muted"]))

    alt = ("Terminal do perfil. Sobre: " + " ".join(SOBRE) + " Como eu trabalho, perto do time: " + "; ".join(PERTO)
           + ". Decisões e desenho: " + "; ".join(DESENHO) + ". Stack: em construção. Formação: "
           + "; ".join(f"{t}, {dd}, {pp}" for pp, t, dd, _ in FORMACAO) + ".")
    return svg(W, H, alt, "\n".join(moldura + b), "".join(dig.defs + defs))


# ---------------------------------------------------------------- cards de projeto

def card(p, nome, desc, lang, st):
    W, H = 600, 214
    cor = p[COR_STATUS[st]]
    g = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="{p["bar"]}" stroke="{p["border"]}" stroke-width="1.5"/>',
         f'<g transform="translate(26 26) scale(1.3)" fill="none" stroke="{p["muted"]}" stroke-width="1.8" stroke-linejoin="round">'
         '<path d="M3 2h13v16H5.5A2.5 2.5 0 0 1 3 15.5z"/><path d="M3 15.5A2.5 2.5 0 0 1 5.5 13H16"/></g>',
         text(nome, 66, 52, 29, p["fg"], "sans b")]
    for j, linha in enumerate(textwrap.wrap(desc, 50)[:2]):
        g.append(text(linha, 28, 98 + j * 29, 21, p["muted"]))
    g.append(f'<circle cx="36" cy="{H - 36}" r="8" fill="{COR_LINGUAGEM[lang]}"/>')
    g.append(text(lang, 54, H - 29, 19, p["fg"]))
    fs = 18
    sw = len(st) * fs * 0.6 + 48
    sx = W - 24 - sw
    g.append(f'<rect x="{sx:.1f}" y="{H - 54}" width="{sw:.1f}" height="36" rx="18" fill="none" stroke="{p["border"]}" stroke-width="1.5"/>')
    g.append(f'<circle cx="{sx + 19:.1f}" cy="{H - 36}" r="6" fill="{cor}"' + (' class="pulse"' if st in ("ativo", "publicando") else "") + "/>")
    g.append(mono(st, sx + 33, H - 30, fs, p["fg"]))
    return svg(W, H, f"{nome}: {desc} Linguagem: {lang}. Status: {st}.", f'<g class="f">{"".join(g)}</g>')


def main():
    destino = RAIZ / "assets"
    for tema, p in TEMAS.items():
        (destino / f"capa-{tema}.svg").write_text(cabecalho(p), encoding="utf-8")
        (destino / f"terminal-{tema}.svg").write_text(terminal(p), encoding="utf-8")
        for nome, desc, lang, st in PROJETOS:
            (destino / f"projeto-{nome.lower()}-{tema}.svg").write_text(card(p, nome, desc, lang, st), encoding="utf-8")
    print("ok:", ", ".join(sorted(f.name for f in destino.glob("*-dark.svg"))))


if __name__ == "__main__":
    main()
