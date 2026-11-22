"""Build the static, multi-language Mr. Picked site from copy.json."""
import json, re, sys, os, math
from html import escape as _e

_here = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_here, 'copy.json')
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(_here, '..', 'site')
D = json.load(open(SRC, encoding='utf-8'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import GEN, IND, ROI, IND_PATH, META_MAIN, META_IND, IND_ORDER
from privacy import PRIV, PRIV_PATH

CMP = {
 'EN': dict(cmpK="Compare", cmpH="Compare packages", g0="In every package", g1="Added in Recommended", g2="Added in Concierge", setupRow="One-time setup"),
 'SL': dict(cmpK="Primerjava", cmpH="Primerjava paketov", g0="V vseh paketih", g1="Dodatno v Recommended", g2="Dodatno v Concierge", setupRow="Enkratna namestitev"),
 'HR': dict(cmpK="Usporedba", cmpH="Usporedba paketa", g0="U svim paketima", g1="Dodatno u Recommended", g2="Dodatno u Concierge", setupRow="Jednokratno postavljanje"),
 'IT': dict(cmpK="Confronto", cmpH="Confronta i pacchetti", g0="In tutti i pacchetti", g1="In più con Recommended", g2="In più con Concierge", setupRow="Attivazione una tantum"),
 'DE': dict(cmpK="Vergleich", cmpH="Pakete vergleichen", g0="In jedem Paket", g1="Zusätzlich in Recommended", g2="Zusätzlich in Concierge", setupRow="Einmalige Einrichtung"),
 'HU': dict(cmpK="Összehasonlítás", cmpH="Csomagok összehasonlítása", g0="Minden csomagban", g1="A Recommended csomagban pluszban", g2="A Concierge csomagban pluszban", setupRow="Egyszeri beállítás"),
}

def rel(from_path, to_path):
    """Relative link from one page directory to another (paths like '' or 'sl/avtovleka/')."""
    up = '../' * from_path.count('/')
    return (up + to_path) or './'

def main_path(L): return '' if L == 'EN' else L.lower() + '/'

def page_path(L, variant): return main_path(L) if variant == 'main' else IND_PATH[variant][L]

def group(variant): return LANGS if variant == 'main' else ['EN', 'SL']
LANGS = ['EN', 'SL', 'HR', 'IT', 'DE', 'HU']
SITE = 'https://mrpicked.eu/'
CAL = 'https://calendly.com/drolcluka77/30min'
NAMES, PRICES, ADDONS = D['NAMES'], D['PRICES'], D['ADDONS']
SETUPS = [0, 0, 490]  # one-time setup per package
ACC = '#B8F36E'
BRAND_RE = re.compile(r'(?<!Mr\. )\bPicked')

def brand(v):
    if isinstance(v, str): return BRAND_RE.sub('Mr. Picked', v)
    if isinstance(v, list): return [brand(x) for x in v]
    if isinstance(v, dict): return {k: brand(x) for k, x in v.items()}
    return v

def e(s): return _e(str(s), quote=True)

META = {
 'EN': dict(html='en', hl='en', og='en_GB', path='', title='Mr. Picked — Get recommended by AI | AI + Google visibility for restaurants & hotels',
            desc='When guests ask ChatGPT, Gemini or Perplexity where to eat or stay, AI names three places. Mr. Picked makes sure yours is one of them — in 6 languages. Free AI check.'),
 'SL': dict(html='sl', hl='sl', og='sl_SI', path='sl/', title='Mr. Picked — Naj vas priporoči AI | AI + Google vidnost za restavracije in hotele',
            desc='Ko gostje vprašajo ChatGPT, Gemini ali Perplexity, kje jesti ali spati, AI imenuje tri lokale. Mr. Picked poskrbi, da je vaš med njimi — v 6 jezikih. Brezplačen AI pregled.'),
 'HR': dict(html='hr', hl='hr', og='hr_HR', path='hr/', title='Mr. Picked — Neka vas AI preporuči | AI + Google vidljivost za restorane i hotele',
            desc='Kad gosti pitaju ChatGPT, Gemini ili Perplexity gdje jesti ili spavati, AI navede tri mjesta. Mr. Picked se brine da je vaše među njima — na 6 jezika. Besplatna AI provjera.'),
 'IT': dict(html='it', hl='it', og='it_IT', path='it/', title='Mr. Picked — Fatti consigliare dall’AI | Visibilità su AI e Google per ristoranti e hotel',
            desc='Quando gli ospiti chiedono a ChatGPT, Gemini o Perplexity dove mangiare o dormire, l’AI nomina tre posti. Mr. Picked fa in modo che il tuo sia tra questi — in 6 lingue. Analisi AI gratuita.'),
 'DE': dict(html='de-AT', hl='de', og='de_AT', path='de/', title='Mr. Picked — Von der KI empfohlen werden | KI- und Google-Sichtbarkeit für Restaurants & Hotels',
            desc='Wenn Gäste ChatGPT, Gemini oder Perplexity fragen, wo sie essen oder übernachten sollen, nennt die KI drei Orte. Mr. Picked sorgt dafür, dass Ihrer dabei ist — in 6 Sprachen. Gratis KI-Check.'),
 'HU': dict(html='hu', hl='hu', og='hu_HU', path='hu/', title='Mr. Picked — Ajánljon az AI | AI- és Google-láthatóság éttermeknek és szállodáknak',
            desc='Amikor a vendégek megkérdezik a ChatGPT-t, a Geminit vagy a Perplexityt, hol egyenek vagy szálljanak meg, az AI három helyet nevez meg. A Mr. Picked gondoskodik róla, hogy az Öné köztük legyen — 6 nyelven. Ingyenes AI-ellenőrzés.'),
}

SEP = {'EN': ',', 'SL': '.', 'HR': '.', 'IT': '.', 'DE': '.', 'HU': ' '}
def fmt(n, L):
    s = f'{int(round(abs(n))):,}'.replace(',', SEP[L])
    return '€' + s if L == 'EN' else s + ' €'

CK = lambda stroke, w=16, sw=3, cls='': (f'<svg class="check {cls}" width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" '
                                        f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"></path></svg>')

MR_SVG = f'''<svg width="220" height="240" viewBox="0 0 200 220" role="img" aria-label="Mr. Picked">
<path d="M30 220 Q36 158 100 150 Q164 158 170 220 Z" fill="#26364D"/><path d="M84 150 L116 150 L100 196 Z" fill="#FFFFFF"/>
<path d="M44 220 Q50 168 86 156 L100 196 L114 156 Q150 168 156 220 Z" fill="#172539"/>
<path d="M82 150 L100 160 L82 170 Z" fill="{ACC}"/><path d="M118 150 L100 160 L118 170 Z" fill="{ACC}"/><circle cx="100" cy="160" r="5" fill="{ACC}"/>
<circle cx="132" cy="186" r="8" fill="{ACC}"/><path d="M128 186 l3 3 l5 -6" fill="none" stroke="#0E1A2B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="100" cy="88" r="54" fill="#F2C9A8"/>
<circle cx="48" cy="84" r="13" fill="#FFFFFF"/><circle cx="44" cy="98" r="11" fill="#FFFFFF"/><circle cx="152" cy="84" r="13" fill="#FFFFFF"/><circle cx="156" cy="98" r="11" fill="#FFFFFF"/>
<ellipse cx="72" cy="104" rx="9" ry="6" fill="#F0A98F"/><ellipse cx="128" cy="104" rx="9" ry="6" fill="#F0A98F"/>
<path d="M66 70 Q78 62 90 70" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M110 66 Q122 56 134 66" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path id="mp-brow" d="M110 62 Q122 50 134 62" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0"/>
<circle cx="80" cy="86" r="13" fill="rgba(255,255,255,0.25)" stroke="#C9A227" stroke-width="3"/><circle cx="120" cy="86" r="13" fill="rgba(255,255,255,0.25)" stroke="#C9A227" stroke-width="3"/>
<path d="M93 86 L107 86" stroke="#C9A227" stroke-width="3"/>
<circle cx="80" cy="87" r="3.5" fill="#0E1A2B"/><circle id="mp-open" cx="120" cy="87" r="3.5" fill="#0E1A2B"/>
<path id="mp-wink" d="M115 88 Q120 84 125 88" fill="none" stroke="#0E1A2B" stroke-width="3" stroke-linecap="round" opacity="0"/>
<circle cx="100" cy="100" r="7" fill="#E8B08F"/>
<path d="M100 108 Q86 102 70 110 Q56 118 46 106 Q50 124 72 122 Q88 120 100 114 Q112 120 128 122 Q150 124 154 106 Q144 118 130 110 Q114 102 100 108 Z" fill="#FFFFFF"/>
<path d="M90 126 Q100 132 110 126" fill="none" stroke="#B5654A" stroke-width="3" stroke-linecap="round"/>
</svg>'''

SPARK = f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"></path></svg>'
PLAY = '<span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="#0E1A2B" aria-hidden="true"><path d="M8 5v14l11-7z"></path></svg></span>'

WORK = [
 ('Aqua Veritas', 'AV', 'aquaveritas.eu', 'https://aquaveritas.eu', '#E3F2F7', '#0F6E8C', '#FFFFFF', '#0B4A5E'),
 ('EURO TRADE', 'ET', 'euro-mach.com', 'https://euro-mach.com', '#EEF0F3', '#1F2A37', '#F5B83D', '#1F2A37'),
 ('Unbusyness', 'U', 'unbusyness.com', 'https://unbusyness.com', '#0E1A2B', ACC, '#0E1A2B', '#F3F5F9'),
]

def ld_json(L, t, path, title, desc):
    m = dict(META[L], path=path, title=title, desc=desc)
    org = {"@type": "Organization", "@id": SITE + "#org", "name": "Mr. Picked", "alternateName": "Picked",
           "legalName": "Cyberfinance, računalniško programiranje d.o.o.", "url": SITE, "logo": SITE + "icon-512.png",
           "image": SITE + "og-image.png", "email": "info@mrpicked.eu", "telephone": "+386 40 290 963", "taxID": "83314512",
           "address": {"@type": "PostalAddress", "streetAddress": "Celovška cesta 136", "postalCode": "1000", "addressLocality": "Ljubljana", "addressCountry": "SI"},
           "founder": {"@type": "Person", "name": "Luka Drolc"}, "areaServed": ["SI", "HR", "IT", "AT", "HU"],
           "knowsLanguage": ["en", "sl", "hr", "it", "de", "hu"]}
    site = {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Mr. Picked", "publisher": {"@id": SITE + "#org"},
            "inLanguage": ["en", "sl", "hr", "it", "de", "hu"]}
    page = {"@type": "WebPage", "@id": SITE + m['path'] + "#page", "url": SITE + m['path'], "name": m['title'], "description": m['desc'],
            "inLanguage": m['hl'], "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#service"}}
    offers = []
    for i, nm in enumerate(NAMES):
        setup_txt = f' + {SETUPS[i]} EUR {t["setup"]} ({t["once"]})' if SETUPS[i] else ''
        offers.append({"@type": "Offer", "name": nm, "price": str(PRICES[i]), "priceCurrency": "EUR",
                       "description": t['tags'][i] + ' — ' + '; '.join(t['lists'][i]) + ' (' + t['perMonth'] + setup_txt + ')'})
    service = {"@type": "Service", "@id": SITE + "#service", "name": t['eyebrow'], "serviceType": "Generative engine optimization (GEO) and local SEO",
               "provider": {"@id": SITE + "#org"}, "areaServed": ["SI", "HR", "IT", "AT", "HU"], "description": t['sub'], "offers": offers}
    faq = {"@type": "FAQPage", "@id": SITE + m['path'] + "#faq", "inLanguage": m['hl'],
           "mainEntity": [{"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in t['faqs']]}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site, page, service, faq]}, ensure_ascii=False, indent=1).replace('</', '<\\/')

# Mr. Picked explainer video (served by the API server from object storage)
VIDEO = {
    'EN': ("See how Mr. Picked works.", "A 30-second introduction to how Mr. Picked helps your business get discovered and recommended by AI.", "Open video"),
    'SL': ("Poglejte, kako deluje Mr. Picked.", "V 30 sekundah spoznajte, kako Mr. Picked pomaga vašemu podjetju, da ga umetna inteligenca odkrije in priporoči.", "Odpri video"),
    'HR': ("Pogledajte kako Mr. Picked funkcionira.", "U 30 sekundi saznajte kako Mr. Picked pomaže vašoj tvrtki da je umjetna inteligencija pronađe i preporuči.", "Otvori video"),
    'IT': ("Scopri come funziona Mr. Picked.", "In 30 secondi, scopri come Mr. Picked aiuta la tua azienda a essere trovata e consigliata dall’intelligenza artificiale.", "Apri il video"),
    'DE': ("So funktioniert Mr. Picked.", "Erfahren Sie in 30 Sekunden, wie Mr. Picked Ihrem Unternehmen hilft, von KI gefunden und empfohlen zu werden.", "Video öffnen"),
    'HU': ("Nézze meg, hogyan működik a Mr. Picked.", "Ismerje meg 30 másodperc alatt, hogyan segít a Mr. Picked abban, hogy a mesterséges intelligencia megtalálja és ajánlja vállalkozását.", "Videó megnyitása"),
}
VIDEO_SRC, VIDEO_POSTER = '/api/media/picked-explainer.mp4', '/api/media/picked-explainer.jpg'

# Form status messages: sending, invalid input, failed, rate limited, confirmation email failed
MAIL_TEXT = {
    'EN': ['Sending…', 'Enter a valid email and your business name.', 'Sending failed. Please try again or email info@mrpicked.eu.', 'Too many requests. Please try again in 15 minutes.', 'We received your request, but could not send the confirmation email. No need to resubmit.'],
    'SL': ['Pošiljanje…', 'Vnesite veljaven e-poštni naslov in ime podjetja.', 'Pošiljanje ni uspelo. Poskusite znova ali pišite na info@mrpicked.eu.', 'Preveč zahtev. Poskusite znova čez 15 minut.', 'Povpraševanje smo prejeli, potrditvenega e-sporočila pa ni bilo mogoče poslati. Ponovna oddaja ni potrebna.'],
    'HR': ['Slanje…', 'Unesite valjanu e-adresu i naziv tvrtke.', 'Slanje nije uspjelo. Pokušajte ponovno ili pišite na info@mrpicked.eu.', 'Previše zahtjeva. Pokušajte za 15 minuta.', 'Primili smo upit, ali potvrda nije poslana. Ne trebate ponovno slati upit.'],
    'IT': ['Invio…', 'Inserisci un indirizzo email valido e il nome della tua attività.', 'Invio non riuscito. Riprova o scrivi a info@mrpicked.eu.', 'Troppe richieste. Riprova tra 15 minuti.', 'Richiesta ricevuta, ma email di conferma non inviata. Non inviare di nuovo.'],
    'DE': ['Wird gesendet…', 'Geben Sie eine gültige E-Mail-Adresse und Ihren Firmennamen ein.', 'Senden fehlgeschlagen. Erneut versuchen oder info@mrpicked.eu kontaktieren.', 'Zu viele Anfragen. In 15 Minuten erneut versuchen.', 'Anfrage erhalten, Bestätigung konnte nicht gesendet werden. Bitte nicht erneut absenden.'],
    'HU': ['Küldés…', 'Adjon meg érvényes e-mail-címet és cégnevet.', 'Sikertelen küldés. Próbálja újra, vagy írjon: info@mrpicked.eu.', 'Túl sok kérés. Próbálja újra 15 perc múlva.', 'Kérését megkaptuk, de a visszaigazolást nem sikerült elküldeni. Nem kell újra beküldenie.'],
}

def page(L, variant):
    base = {**D['T'][L], **D['T2'][L], 'mailPh': 'you@restaurant.si'}
    base.update(GEN[L] if variant == 'main' else IND[variant][L])
    base['faqs'] = [D['T'][L]['faqs'][f] if isinstance(f, int) else f for f in base['faqs']]
    t = brand({**base, **CMP[L]})
    path = page_path(L, variant)
    title, desc = META_MAIN[L] if variant == 'main' else META_IND[variant][L]
    m = dict(META[L], path=path, title=title, desc=desc)
    A = '../' * path.count('/')  # relative prefix to site root
    url = SITE + path
    grp = group(variant)
    alt = '\n'.join(f'<link rel="alternate" hreflang="{META[x]["hl"]}" href="{SITE + page_path(x, variant)}">' for x in grp)
    alt += f'\n<link rel="alternate" hreflang="x-default" href="{SITE + page_path("EN", variant)}">'
    langs = ''.join(f'<a href="{rel(path, page_path(x, variant))}" hreflang="{META[x]["hl"]}" lang="{META[x]["hl"]}" data-lang="{x.lower()}"'
                    + (' aria-current="page"' if x == L else '') + f'>{x}</a>' for x in grp)
    redirect = '' if (L != 'EN' or variant != 'main') else (
        "<script>try{if(!localStorage.getItem('mp-lang')){var l=(navigator.language||'').slice(0,2).toLowerCase();"
        "if({sl:1,hr:1,it:1,de:1,hu:1}[l]){location.replace(l+'/');}}}catch(e){}</script>\n")
    words = ''.join(f'<span class="word" style="--d:{1.45 + i*0.07:.2f}s">{e(w)}</span>' for i, w in enumerate(t['h1'].split(' ')))

    # How it works
    tabs, panels = '', ''
    for i, st in enumerate(t['steps']):
        sel = i == 0
        ti = '' if sel else ' tabindex="-1"'
        tabs += (f'<button type="button" role="tab" id="how-t-{i}" aria-controls="how-p-{i}" aria-selected="{str(sel).lower()}"'
                 f'{ti}>0{i+1} · {e(st["tab"])}</button>')
        items = ''.join(f'<li><span class="dot-ok">{CK(ACC, 12, 4)}</span>{e(x)}</li>' for x in st['items'])
        panels += (f'<div class="how-panel" role="tabpanel" id="how-p-{i}" aria-labelledby="how-t-{i}"{"" if sel else " hidden"}>'
                   f'<div class="card-w"><h3>{e(st["h"])}</h3><p class="lead" style="color:var(--ink2)">{e(st["p"])}</p><ul class="checklist">{items}</ul></div>'
                   f'<div class="how-num" aria-hidden="true"><div class="big">0{i+1}</div><div class="stack" style="gap:8px"><div class="tab-name">{e(st["tab"])}</div>'
                   f'<div class="bar"><span style="width:{round((i+1)/3*100)}%"></span></div></div></div></div>')

    vids = ''.join(f'<div class="feat"><span class="feat-ic">{SPARK}</span><div><b>{e(v["h"])}</b><span>{e(v["p"])}</span></div></div>' for v in t['vids'])

    # Pricing
    tiers = ''
    for i, nm in enumerate(NAMES):
        hi = ''.join(f'<span>{CK("currentColor", 16, 3, "ck")}{e(x)}</span>' for x in t['hi'][i])
        badge = f'<span class="badge">{e(t["popular"])}</span>' if i == 1 else ''
        tiers += (f'<button type="button" class="tier" data-tier="{i}" aria-pressed="{str(i == 1).lower()}">'
                  f'<span class="tier-head"><span><span class="tier-name">{nm}</span><span class="tier-tag">{e(t["tags"][i])}</span></span>{badge}</span>'
                  f'<span class="price"><b>{fmt(PRICES[i], L)}</b> <span class="per">{e(t["perMonth"])}</span>'
                  + (f'<span class="tier-setup">+ {fmt(SETUPS[i], L)} {e(t["setup"])} ({e(t["once"])})</span>' if SETUPS[i] else '')
                  + '</span>'
                  f'<span class="tier-hi">{hi}</span></button>')
    incl = ''.join(f'<ul class="incl" data-incl="{i}"{"" if i == 1 else " hidden"}>'
                   + ''.join(f'<li>{CK(ACC)}{e(x)}</li>' for x in lst) + '</ul>' for i, lst in enumerate(t['lists']))
    def plabel(a):
        parts = []
        if a['mo']: parts.append(fmt(a['mo'], L) + ' ' + t['perMonth'])
        if a['once']: parts.append(fmt(a['once'], L) + ' ' + (t['setup'] if a['mo'] else t['once']))
        return ' + '.join(parts)
    addons = ''
    for i, a in enumerate(ADDONS):
        inc = a['inc'] is not None and 1 >= a['inc']
        addons += (f'<button type="button" class="addon" data-addon="{a["id"]}" aria-pressed="false"{" disabled" if inc else ""}>'
                   f'<span class="cb">{CK("#0E1A2B", 12, 4)}</span><span class="a-txt"><span class="a-nm">{e(t["addons"][i]["name"])}</span>'
                   f'<span class="a-ds">{e(t["addons"][i]["desc"])}</span><span class="a-pr">{e(t["included"] if inc else plabel(a))}</span></span></button>')

    # Comparison table: grouped by the package that adds each item
    def cell(on): return f'<td>{CK("#0E1A2B", 12, 4, "cmp-ck") if on else ""}<span class="sr">{"✓" if on else "—"}</span>{"" if on else "<span class=cmp-no aria-hidden=true>—</span>"}</td>'
    cmp_rows = ''
    chev = '<svg class="cmp-chev" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
    def grp_head(g, label, pk, n):
        return (f'<tr class="cmp-g"><th scope="rowgroup" colspan="4"><button type="button" class="cmp-tg" aria-expanded="true" aria-controls="cmp-g{g}">'
                f'<span class="cmp-gl">{e(label)}<span class="cmp-pk">{e(pk)}</span></span><span class="cmp-cnt">{n}</span>{chev}</button></th></tr>')
    for g, lst in enumerate(t['lists']):
        items = lst if g == 0 else lst[1:]
        cmp_rows += f'<tbody class="cmp-grp" id="cmp-g{g}">' + grp_head(g, t['g' + str(g)], ' · '.join(NAMES[g:]), len(items))
        for it in items:
            cmp_rows += f'<tr><th scope="row"><span class="cmp-mk" aria-hidden="true">{CK("#0E1A2B", 10, 4)}</span>{e(it)}</th>' + ''.join(cell(k >= g) for k in range(3)) + '</tr>'
        cmp_rows += '</tbody>'
    cmp_rows += (f'<tbody class="cmp-grp" id="cmp-g3">' + grp_head(3, t['setupRow'], '', 1) + f'<tr class="cmp-setup"><th scope="row">{e(t["setupRow"])}</th>'
                 + ''.join(f'<td class="cmp-v" data-label="{nm}">{fmt(s, L) if s else "—"}</td>' for nm, s in zip(NAMES, SETUPS)) + '</tr></tbody>')
    cmp_head = ''.join(f'<th scope="col"{" class=cmp-hi" if i == 1 else ""}><span class="cmp-n">{nm}</span><span class="cmp-p">{fmt(PRICES[i], L)} <small>{e(t["perMonth"])}</small></span></th>'
                       for i, nm in enumerate(NAMES))

    # Industries (main pages only)
    inds_html = ''
    if variant == 'main':
        keys = IND_ORDER
        for i, ind in enumerate(t['inds']):
            if i < len(keys):
                target = IND_PATH[keys[i]].get(L) or IND_PATH[keys[i]]['EN']
                more = t['indMore'] + ('' if L in ('EN', 'SL') else ' (EN)')
                link = f'<a class="ind-more" href="{rel(path, target)}">{e(more)} →</a>'
            else:
                link = ''
            inds_html += f'<div class="ind{" ind-live" if i < len(keys) else ""}"><h3>{e(ind["name"])}</h3><p>{e(ind["desc"])}</p>{link}</div>'
        inds_html = (f'<section id="industries" class="sec-tight"><div class="wrap stack rv" data-rv="industries" style="gap:32px">'
                     f'<div class="stack" style="gap:12px;max-width:760px"><div class="kicker">{e(t["indK"])}</div><h2 class="h2">{e(t["indH"])}</h2><p class="lead">{e(t["indP"])}</p></div>'
                     f'<div class="grid-auto ind-grid">{inds_html}</div></div></section>')

    cat_field = ''
    if variant == 'main':
        cat_field = f'<div class="field"><label for="demo-cat">{e(t["dCat"])}</label><input id="demo-cat" class="inp-dark" type="text" value="{e(t["catDef"])}"></div>'

    # ROI defaults
    (spend, s_min, s_max, s_step), (guests, g_min, g_max, g_step) = ROI[variant]
    monthly = PRICES[1]
    rev = round(guests * spend * 4.33); net = rev - monthly; mx = max(rev, monthly, 1)
    brk = t['roiBreak'].replace('{n}', str(math.ceil(monthly / (spend * 4.33))))

    faqs = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(f["q"])}<span class="plus" aria-hidden="true">'
                   f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{ACC}" stroke-width="3" stroke-linecap="round"><path d="M12 5v14"/><path d="M5 12h14"/></svg></span></summary>'
                   f'<p>{e(f["a"])}</p></details>' for i, f in enumerate(t['faqs']))

    work = ''.join(f'<div class="wcard"><div class="wlogo" style="background:{bg}" aria-hidden="true"><span class="wtile" style="background:{tile};color:{tfg}">{mono}</span>'
                   f'<span class="wname" style="color:{fg}">{e(nm)}</span></div><div class="pad whost">{host}</div><h3 class="sr">{e(nm)}</h3>'
                   f'<p class="pad">{e(t["wk"][i])}</p><a class="pad" href="{href}" target="_blank" rel="noopener">{e(t["wkVisit"])} ↗</a></div>'
                   for i, (nm, mono, host, href, bg, tile, tfg, fg) in enumerate(WORK))

    mp = {k: t[k] for k in ['dQ', 'dIdle', 'dScan', 'dToday', 'dWith', 'dIntro', 'dNot', 'dYes', 'dScore', 'dOf', 'dNote', 'dOther', 'dYour',
                            'dDesc', 'dAgain', 'dDone', 'dWait', 'dGet', 'dEmailPh', 'btn', 'privT', 'privL', 'tyH', 'tyP', 'tyBtn', 'roiBreak',
                            'perMonth', 'included', 'once', 'setup', 'inclH']}
    mp.update(lang=L, names=NAMES, prices=PRICES, setups=SETUPS, addons=ADDONS, addonNames=[a['name'] for a in t['addons']], cal=CAL,
              catDef=t.get('catDef', ''), mailText=MAIL_TEXT[L], privUrl=rel(path, PRIV_PATH[L]))
    mp_json = json.dumps(mp, ensure_ascii=False).replace('</', '<\\/')
    logo_href = rel(path, main_path(L))

    return f'''<!doctype html>
<html lang="{m['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{redirect}<script>document.documentElement.className+=' js';try{{if(sessionStorage.getItem('mp-intro')){{document.documentElement.className+=' no-intro'}}else{{sessionStorage.setItem('mp-intro','1')}}}}catch(e){{}}</script>
<title>{e(m['title'])}</title>
<meta name="description" content="{e(m['desc'])}">
<link rel="canonical" href="{url}">
{alt}
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="{A}favicon.ico" sizes="any">
<link rel="icon" href="{A}favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="{A}favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{A}favicon-16x16.png">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="manifest" href="{A}site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mr. Picked">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(m['title'])}">
<meta property="og:description" content="{e(m['desc'])}">
<meta property="og:image" content="{SITE}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{m['og']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}assets/style.css">
<script type="application/ld+json">
{ld_json(L, t, path, title, desc)}
</script>
</head>
<body>
<div class="intro" aria-hidden="true"><div class="intro-row"><span class="intro-logo"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#0E1A2B" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></span><span class="intro-word">Mr. Picked</span></div></div>

<header class="dark hero">
<div class="wrap">
<nav class="nav" aria-label="Main">
<a class="logo" href="{logo_href}"><span class="logo-mark">{CK('#0E1A2B', 16, 3)}</span><span class="logo-word">Mr. Picked</span></a>
<div class="nav-links">
<a href="#how">{e(t['navHow'])}</a><a href="#pricing">{e(t['navPricing'])}</a><a href="#roi">{e(t['navRoi'])}</a><a href="#faq">{e(t['navFaq'])}</a>
<div class="langs" role="navigation" aria-label="Language">{langs}</div>
<a class="btn btn-accent" href="#check">{e(t['navCta'])}</a>
</div>
</nav>
<div class="hero-grid">
<div class="hero-copy">
<div class="pill a-up" style="--d:1.35s"><i></i>{e(t['eyebrow'])}</div>
<h1 class="h1">{words}</h1>
<p class="hero-sub a-up" style="--d:2.05s">{e(t['sub'])}</p>
<div class="row-wrap a-up" style="--d:2.2s"><a class="btn btn-accent" href="#check">{e(t['cta1'])}</a><a class="btn btn-ghost" href="#pricing">{e(t['cta2'])}</a></div>
<div class="proof a-up" style="--d:2.35s"><span>{CK(ACC)}{e(t['p1'])}</span><span>{CK(ACC)}{e(t['p2'])}</span><span>{CK(ACC)}{e(t['p3'])}</span></div>
</div>
<div class="demo a-up" style="--d:1.85s">
<div class="demo-top"><div class="dots" aria-hidden="true"><i></i><i></i><i></i></div><div class="demo-label">{e(t['dTitle'])}</div></div>
<div class="demo-fields">
<div class="field"><label for="demo-name">{e(t['dName'])}</label><input id="demo-name" class="inp-dark" type="text" placeholder="{e(t['dNamePh'])}"></div>
<div class="field"><label for="demo-city">{e(t['dCity'])}</label><input id="demo-city" class="inp-dark" type="text" value="Ljubljana"></div>
{cat_field}
</div>
<button type="button" id="demo-run" class="demo-run">{e(t['dRun'])}</button>
<div id="demo-out" aria-live="polite"><div class="demo-idle">{e(t['dIdle'])}</div></div>
</div>
</div>
</div>
</header>

<main>
<section id="service-video" class="sec-tight">
<div class="wrap vid-grid rv" data-rv="service-video">
<div class="stack" style="gap:14px"><div class="kicker">Mr. Picked</div><h2 class="h2">{e(VIDEO[L][0])}</h2><p class="lead">{e(VIDEO[L][1])}</p>
<a class="btn btn-ghost-dark" href="{VIDEO_SRC}" target="_blank" rel="noopener">{e(VIDEO[L][2])} ↗</a></div>
<div class="vid-frame"><video src="{VIDEO_SRC}" poster="{VIDEO_POSTER}" controls playsinline preload="none" width="480" height="854" aria-label="{e(VIDEO[L][0])}"></video></div>
</div>
</section>

<section id="how" class="sec">
<div class="wrap stack rv" data-rv="how" style="gap:40px">
<div class="stack" style="gap:12px;max-width:720px"><div class="kicker">{e(t['howK'])}</div><h2 class="h2">{e(t['howH'])}</h2></div>
<div class="tabs" role="tablist" aria-label="{e(t['howK'])}">{tabs}</div>
{panels}
</div>
</section>

<section class="sec-tight">
<div class="wrap split rv" data-rv="video">
<div class="stack" style="gap:22px">
<div class="kicker">{e(t['vidK'])}</div><h2 class="h2">{e(t['vidH'])}</h2><p class="lead">{e(t['vidP'])}</p>
<div class="stack" style="gap:16px">{vids}</div>
</div>
<div class="phones" aria-hidden="true"><div class="phone">{PLAY}<small>EN · SL · HR</small></div><div class="phone mid">{PLAY}<small>IT · DE · HU</small></div><div class="phone">{PLAY}<small>Reels · TikTok · Shorts</small></div></div>
</div>
</section>

<section id="pricing" class="sec dark">
<div class="wrap stack rv" data-rv="pricing" style="gap:36px">
<div class="stack" style="gap:12px;max-width:760px"><div class="kicker">{e(t['pkK'])}</div><h2 class="h2">{e(t['pkH'])}</h2><p style="font-size:17px;color:var(--t2)">{e(t['pkSub'])}</p></div>
<div class="grid-auto" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{tiers}</div>
<div class="grid-auto" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:start">
<div class="box-d"><div class="box-title" id="incl-title">{e(t['inclH'] + ' ' + NAMES[1])}</div>{incl}</div>
<div class="box-d"><div class="box-title">{e(t['addH'])}</div>{addons}</div>
<div class="sum"><div class="box-title">{e(t['sumH'])}</div>
<div class="sum-lines" id="sum-lines"><div><span>{NAMES[1]}</span><span>{fmt(PRICES[1], L)} {e(t['perMonth'])}</span></div></div>
<div class="hr"></div>
<div class="sum-row"><span style="font-weight:600">{e(t['sumMonthly'])}</span><b id="sum-monthly">{fmt(PRICES[1], L)}</b></div>
<div class="sum-row once" id="sum-once-row" hidden><span style="font-weight:600">{e(t['sumOnce'])}</span><b id="sum-once"></b></div>
<a class="btn btn-navy" href="#check" style="margin-top:6px">{e(t['sumCta'])}</a>
</div>
</div>
</div>
</section>

<section id="compare" class="sec">
<div class="wrap stack rv" data-rv="compare" style="gap:28px">
<div class="stack" style="gap:12px"><div class="kicker">{e(t['cmpK'])}</div><h2 class="h2">{e(t['cmpH'])}</h2></div>
<div class="cmp-wrap" role="region" aria-label="{e(t['cmpH'])}" tabindex="0">
<table class="cmp"><thead><tr><th scope="col"><span class="sr">{e(t['cmpH'])}</span></th>{cmp_head}</tr></thead>
{cmp_rows}</table>
</div>
</div>
</section>

{inds_html}

<section id="roi" class="sec">
<div class="wrap split rv" data-rv="roi" style="gap:40px">
<div class="stack" style="gap:26px">
<div class="stack" style="gap:12px"><div class="kicker">{e(t['roiK'])}</div><h2 class="h2">{e(t['roiH'])}</h2><p class="lead">{e(t['roiP'])}</p></div>
<div class="slider"><div class="slider-top"><label for="roi-spend">{e(t['roiSpend'])}</label><output id="roi-spend-o" for="roi-spend">{fmt(spend, L)}</output></div>
<input id="roi-spend" type="range" min="{s_min}" max="{s_max}" step="{s_step}" value="{spend}"></div>
<div class="slider"><div class="slider-top"><label for="roi-guests">{e(t['roiGuests'])}</label><output id="roi-guests-o" for="roi-guests">{guests}</output></div>
<input id="roi-guests" type="range" min="{g_min}" max="{g_max}" step="{g_step}" value="{guests}"></div>
<p class="note">{e(t['roiNote'])}</p>
</div>
<div class="roi-card">
<div class="stack" style="gap:8px"><div class="roi-line"><span>{e(t['roiRev'])}</span><b id="roi-rev">{fmt(rev, L)}</b></div><div class="roi-bar"><span id="roi-rev-bar" style="width:{round(rev/mx*100)}%"></span></div></div>
<div class="stack" style="gap:8px"><div class="roi-line"><span>{e(t['roiCost'])}</span><b id="roi-cost">{fmt(monthly, L)}</b></div><div class="roi-bar cost"><span id="roi-cost-bar" style="width:{round(monthly/mx*100)}%"></span></div></div>
<div class="hr" style="background:var(--line)"></div>
<div class="roi-net"><span style="font-weight:600">{e(t['roiNet'])}</span><b id="roi-net">+{fmt(net, L)}</b></div>
<div class="roi-break" id="roi-break">{e(brk)}</div>
<a class="btn btn-accent" href="#check">{e(t['roiCta'])}</a>
</div>
</div>
</section>

<section class="sec-tight">
<div class="wrap promise rv" data-rv="promise">
<div class="stack" style="gap:16px"><div class="kicker on-dark">{e(t['proK'])}</div><h2 class="h2">{e(t['proH'])}</h2><p style="font-size:18px;color:var(--t2)">{e(t['proP'])}</p></div>
<div class="mr">{MR_SVG}<div class="mr-quote">{e(t['mrQuote'])}</div><div style="font-size:14px;color:var(--muted)">— Mr. Picked</div></div>
</div>
</section>

<section id="work" class="sec-tight">
<div class="wrap stack rv" data-rv="work" style="gap:40px">
<div class="founder"><div class="avatar" aria-hidden="true">LD</div><div class="stack">
<div class="kicker">{e(t['fdK'])}</div><h2>{e(t['fdH'])}</h2><p class="lead">{e(t['fdP'])}</p><div style="font-weight:600">{e(t['fdName'])}</div></div></div>
<div class="stack" style="gap:12px"><div class="kicker">{e(t['wkK'])}</div><h2 class="h2">{e(t['wkH'])}</h2></div>
<div class="grid-auto">{work}</div>
</div>
</section>

<section id="faq" class="sec-tight">
<div class="faq rv" data-rv="faq">
<div class="stack" style="gap:12px"><div class="kicker">{e(t['faqK'])}</div><h2 class="h2">{e(t['faqH'])}</h2></div>
<div class="faq-list">{faqs}</div>
</div>
</section>

<section id="check" class="sec-tight">
<div class="wrap cta rv" data-rv="check">
<div class="stack" style="gap:14px"><h2 class="h2">{e(t['ctaH'])}</h2><p class="lead">{e(t['ctaP'])}</p></div>
<div>
<form id="check-form" novalidate>
<div class="form-msg" id="check-msg" role="status" aria-live="polite" hidden></div>
<label class="l" for="cta-biz">{e(t['fBiz'])}</label>
<input id="cta-biz" name="business" class="inp-light" type="text" autocomplete="organization" placeholder="{e(t['dNamePh'])}">
<label class="l" for="cta-mail">{e(t['fMail'])}</label>
<input id="cta-mail" name="email" class="inp-light" type="email" autocomplete="email" required placeholder="{e(t['mailPh'])}">
<label class="consent"><input type="checkbox" name="consent" value="yes">{e(t['consent'])}</label>
<div class="priv">{e(t['privT'])} <a href="{rel(path, PRIV_PATH[L])}">{e(t['privL'])}</a></div>
<button type="submit" class="btn btn-navy">{e(t['btn'])}</button>
</form>
<div class="thanks" id="check-thanks" hidden aria-live="polite">
<div class="form-msg warn" id="check-warn" hidden></div>
<span class="logo-mark" style="width:40px;height:40px;border-radius:999px">{CK('#0E1A2B', 18, 3)}</span>
<h3>{e(t['tyH'])}</h3><p>{e(t['tyP'])}</p>
<a class="btn btn-accent" href="{CAL}" target="_blank" rel="noopener">{e(t['tyBtn'])}</a>
</div>
</div>
</div>
</section>
</main>

<a class="mbar" href="#check">{e(t['mbar'])} →</a>

<footer>
<div class="wrap foot">
<div><b>Mr. Picked</b> · Ljubljana · SI · HR · IT · AT · HU</div>
<div class="co"><span style="font-weight:600;color:var(--navy)">Cyberfinance, računalniško programiranje d.o.o.</span>
<span>Celovška cesta 136, 1000 Ljubljana, Slovenia</span>
<span>DŠ: 83314512 · <a href="tel:+38640290963">+386 40 290 963</a> · <a href="mailto:info@mrpicked.eu">info@mrpicked.eu</a></span>
<span><a href="{rel(path, PRIV_PATH[L])}">{e(t['privL'])}</a></span></div>
</div>
</footer>

<script>window.MP = {mp_json};</script>
<script src="{A}assets/app.js" defer></script>
</body>
</html>
'''

def privacy_page(L):
    P = brand(PRIV[L]); t = {**D['T'][L], **D['T2'][L]}
    path = PRIV_PATH[L]; A = '../' * path.count('/'); url = SITE + path; m = META[L]
    alt = '\n'.join(f'<link rel="alternate" hreflang="{META[x]["hl"]}" href="{SITE + PRIV_PATH[x]}">' for x in LANGS)
    alt += f'\n<link rel="alternate" hreflang="x-default" href="{SITE + PRIV_PATH["EN"]}">'
    langs = ''.join(f'<a href="{rel(path, PRIV_PATH[x])}" hreflang="{META[x]["hl"]}" lang="{META[x]["hl"]}" data-lang="{x.lower()}"'
                    + (' aria-current="page"' if x == L else '') + f'>{x}</a>' for x in LANGS)
    body = ''
    for h, blocks in P['sections']:
        body += f'<h2>{e(h)}</h2>'
        for b in blocks:
            body += ('<ul>' + ''.join(f'<li>{e(x)}</li>' for x in b) + '</ul>') if isinstance(b, list) else f'<p>{e(b)}</p>'
    home = rel(path, main_path(L))
    return f"""<!doctype html>
<html lang="{m['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(P['title'])}</title>
<meta name="description" content="{e(P['desc'])}">
<link rel="canonical" href="{url}">
{alt}
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="{A}favicon.ico" sizes="any">
<link rel="icon" href="{A}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="manifest" href="{A}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}assets/style.css">
</head>
<body class="legal-page">
<header class="dark">
<div class="wrap">
<nav class="nav" aria-label="Main">
<a class="logo" href="{home}"><span class="logo-mark">{CK('#0E1A2B', 16, 3)}</span><span class="logo-word">Mr. Picked</span></a>
<div class="langs" role="navigation" aria-label="Language">{langs}</div>
</nav>
</div>
</header>
<main class="legal">
<div class="wrap">
<h1 class="h2">{e(P['h1'])}</h1>
<p class="legal-upd">{e(P['updated'])}</p>
<p class="lead">{e(P['intro'])}</p>
{body}
<p class="legal-back"><a href="{home}">← {e(P['back'])}</a></p>
</div>
</main>
<footer>
<div class="wrap foot">
<div><b>Mr. Picked</b> · Ljubljana · SI · HR · IT · AT · HU</div>
<div class="co"><span style="font-weight:600;color:var(--navy)">Cyberfinance, računalniško programiranje d.o.o.</span>
<span>Celovška cesta 136, 1000 Ljubljana, Slovenia</span>
<span>DŠ: 83314512 · <a href="tel:+38640290963">+386 40 290 963</a> · <a href="mailto:info@mrpicked.eu">info@mrpicked.eu</a></span></div>
</div>
</footer>
<script>document.querySelectorAll('.langs a').forEach(function(a){{a.addEventListener('click',function(){{try{{localStorage.setItem('mp-lang',a.getAttribute('data-lang'))}}catch(e){{}}}})}})</script>
</body>
</html>
"""

PAGES = [(L, 'main') for L in LANGS] + [(L, v) for v in IND_ORDER for L in ('EN', 'SL')]
for L, v in PAGES:
    p = os.path.join(OUT, page_path(L, v), 'index.html')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(page(L, v))
    print('wrote', p)
for L in LANGS:
    p = os.path.join(OUT, PRIV_PATH[L], 'index.html')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(privacy_page(L))
    print('wrote', p)

# sitemap with hreflang alternates
urls = ''
for L, v in PAGES:
    alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{META[x]["hl"]}" href="{SITE + page_path(x, v)}"/>' for x in group(v))
    alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE + page_path("EN", v)}"/>'
    urls += f'  <url>\n    <loc>{SITE + page_path(L, v)}</loc>\n    <lastmod>2026-11-22</lastmod>{alts}\n  </url>\n'
palts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{META[x]["hl"]}" href="{SITE + PRIV_PATH[x]}"/>' for x in LANGS)
for L in LANGS:
    urls += f'  <url>\n    <loc>{SITE + PRIV_PATH[L]}</loc>\n    <lastmod>2026-11-22</lastmod>{palts}\n  </url>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + '</urlset>\n')
print('wrote sitemap')
