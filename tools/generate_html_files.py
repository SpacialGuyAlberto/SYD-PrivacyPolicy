import json

with open("policy_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Quick summary card translations
summary_cards = {
    "de": [
        {"title": "Verantwortlicher", "text": "SNAPYOURDATE UG (haftungsbeschränkt)<br>Hamburg, Deutschland"},
        {"title": "Datenschutzkontakt", "text": "Johnny Jonat<br><a href='mailto:info@monalisaentertainment.com'>info@monalisaentertainment.com</a>"},
        {"title": "Wesentliche Dienste", "text": "Supabase (Datenbank), Google Maps, RevenueCat (In-App-Käufe)"},
        {"title": "Aufsichtsbehörde", "text": "Hamburgischer Beauftragter für Datenschutz und Informationsfreiheit"}
    ],
    "en": [
        {"title": "Data Controller", "text": "SNAPYOURDATE UG (haftungsbeschränkt)<br>Hamburg, Germany"},
        {"title": "Data Protection Contact", "text": "Johnny Jonat<br><a href='mailto:info@monalisaentertainment.com'>info@monalisaentertainment.com</a>"},
        {"title": "Key Cloud Services", "text": "Supabase (Database), Google Maps, RevenueCat (In-App Purchases)"},
        {"title": "Supervisory Authority", "text": "Hamburg Commissioner for Data Protection and Freedom of Information"}
    ],
    "es": [
        {"title": "Responsable del tratamiento", "text": "SNAPYOURDATE UG (haftungsbeschränkt)<br>Hamburgo, Alemania"},
        {"title": "Contacto de protección de datos", "text": "Johnny Jonat<br><a href='mailto:info@monalisaentertainment.com'>info@monalisaentertainment.com</a>"},
        {"title": "Servicios técnicos clave", "text": "Supabase (Base de datos), Google Maps, RevenueCat (Compras integradas)"},
        {"title": "Autoridad de control", "text": "Comisionado de Hamburgo para la Protección de Datos y Libertad de Información"}
    ]
}

lang_names = {
    "de": {"label": "Deutsch", "flag": "🇩🇪", "orig": "(Original)"},
    "en": {"label": "English", "flag": "🇬🇧", "orig": ""},
    "es": {"label": "Español", "flag": "🇪🇸", "orig": ""}
}

toc_titles = {
    "de": "Inhaltsverzeichnis",
    "en": "Table of Contents",
    "es": "Índice de contenidos"
}

search_placeholders = {
    "de": "Abschnitte durchsuchen...",
    "en": "Search policy sections...",
    "es": "Buscar en los apartados..."
}

# --- 1. Generate standalone pages (privacy-de.html, privacy-en.html, privacy-es.html) ---
for lang in ["de", "en", "es"]:
    meta_title = data["meta"]["title"][lang]
    meta_subtitle = data["meta"]["subtitle"][lang]
    meta_date = data["meta"]["date"][lang]
    meta_intro = data["meta"]["intro"][lang]
    
    toc_html = ""
    sections_html = ""
    
    for sec in data["sections"]:
        s_id = sec["id"]
        s_num = sec["num"]
        s_title = sec["title"][lang]
        s_content = sec["content"][lang]
        
        toc_html += f'<li><a href="#{s_id}" class="toc-link"><span style="color:var(--primary);font-weight:700;">{s_num}.</span> {s_title}</a></li>\n'
        
        sections_html += f"""
        <article id="{s_id}" class="policy-section">
            <header class="section-header">
                <span class="section-num">{s_num}</span>
                <h2 class="section-title">{s_title}</h2>
            </header>
            <div class="section-body">
                {s_content}
            </div>
        </article>
        """
        
    cards_html = ""
    for card in summary_cards[lang]:
        cards_html += f"""
        <div class="quick-card">
            <h4>{card['title']}</h4>
            <p>{card['text']}</p>
        </div>
        """

    # Language switcher links for standalone page
    switcher_html = f"""
    <div class="lang-switcher">
        <a href="privacy-de.html" class="lang-btn {'active' if lang=='de' else ''}">🇩🇪 DE</a>
        <a href="privacy-en.html" class="lang-btn {'active' if lang=='en' else ''}">🇬🇧 EN</a>
        <a href="privacy-es.html" class="lang-btn {'active' if lang=='es' else ''}">🇪🇸 ES</a>
    </div>
    """

    page_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta_title}</title>
    <meta name="description" content="{meta_subtitle} - SNAPYOURDATE">
    <link rel="icon" type="image/png" href="SYD_App_Icon_Transparent.png">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <div class="header-container">
            <a href="index.html" class="brand">
                <img src="SYD_App_Icon_Transparent.png" alt="SNAPYOURDATE Logo">
                <div class="brand-text">
                    <h1>SNAPYOURDATE</h1>
                    <span>{meta_subtitle}</span>
                </div>
            </a>
            {switcher_html}
        </div>
    </header>

    <div class="main-layout">
        <aside class="sidebar">
            <div class="search-box">
                <input type="text" class="search-input" id="searchInput" placeholder="{search_placeholders[lang]}">
            </div>
            <h3>{toc_titles[lang]}</h3>
            <ul class="toc-list" id="tocList">
                {toc_html}
            </ul>
        </aside>

        <main class="content-area">
            <div class="hero-banner">
                <div class="badge-row">
                    <span class="badge">SNAPYOURDATE Legal</span>
                    <span class="badge badge-date">{meta_date}</span>
                </div>
                <h1>{meta_title.split('–')[0].strip()}</h1>
                <p class="intro-lead">{meta_intro}</p>
            </div>

            <div class="quick-cards">
                {cards_html}
            </div>

            <div id="sectionsContainer">
                {sections_html}
            </div>
        </main>
    </div>

    <footer class="footer">
        <div class="footer-links">
            <a href="index.html">Multilingual Hub</a>
            <a href="privacy-de.html">🇩🇪 Deutsch</a>
            <a href="privacy-en.html">🇬🇧 English</a>
            <a href="privacy-es.html">🇪🇸 Español</a>
            <a href="Datenschutz.pdf" target="_blank">PDF (Original DE)</a>
        </div>
        <p>&copy; 2026 SNAPYOURDATE UG (haftungsbeschränkt). Meiendorfer Straße 72, 22145 Hamburg, Deutschland.</p>
    </footer>

    <script>
        // Simple search filter
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {{
            searchInput.addEventListener('input', function() {{
                const filter = this.value.toLowerCase().trim();
                const sections = document.querySelectorAll('.policy-section');
                const tocLinks = document.querySelectorAll('.toc-link');
                
                sections.forEach((sec, idx) => {{
                    const text = sec.innerText.toLowerCase();
                    const matches = text.includes(filter);
                    sec.style.display = matches ? 'block' : 'none';
                    if (tocLinks[idx]) {{
                        tocLinks[idx].parentElement.style.display = matches ? 'block' : 'none';
                    }}
                }});
            }});
        }}

        // Highlight TOC on scroll
        const sections = document.querySelectorAll('.policy-section');
        const tocLinks = document.querySelectorAll('.toc-link');
        window.addEventListener('scroll', () => {{
            let current = '';
            sections.forEach(section => {{
                const sectionTop = section.offsetTop - 120;
                if (pageYOffset >= sectionTop) {{
                    current = section.getAttribute('id');
                }}
            }});
            tocLinks.forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) {{
                    link.classList.add('active');
                }}
            }});
        }});
    </script>
</body>
</html>"""

    filename = f"privacy-{lang}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_html.strip())
    print(f"{filename} generated!")

# --- 2. Generate unified interactive index.html ---
# index.html includes all three languages in tab sections with JS switching
languages = ["de", "en", "es"]

lang_sections_json = json.dumps(data, ensure_ascii=False)
summary_cards_json = json.dumps(summary_cards, ensure_ascii=False)
toc_titles_json = json.dumps(toc_titles, ensure_ascii=False)
search_placeholders_json = json.dumps(search_placeholders, ensure_ascii=False)

index_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SNAPYOURDATE – Privacy Policy / Datenschutzerklärung</title>
    <meta name="description" content="Official Privacy Policy for SNAPYOURDATE native app in German, English, and Spanish.">
    <link rel="icon" type="image/png" href="SYD_App_Icon_Transparent.png">
    <link rel="stylesheet" href="style.css">
    <style>
        .lang-pane {{
            display: none;
        }}
        .lang-pane.active {{
            display: block;
        }}
        .pdf-link-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--bg-card-alt);
            border: 1px solid var(--border-color);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: 0.82rem;
            color: var(--text-muted);
            transition: all 0.15s;
        }}
        .pdf-link-btn:hover {{
            color: var(--primary);
            border-color: var(--primary-border);
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-container">
            <a href="index.html" class="brand">
                <img src="SYD_App_Icon_Transparent.png" alt="SNAPYOURDATE Logo">
                <div class="brand-text">
                    <h1>SNAPYOURDATE</h1>
                    <span id="headerSubtitle">Datenschutzhinweise für die native App</span>
                </div>
            </a>
            
            <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap;">
                <div class="lang-switcher" role="tablist">
                    <button class="lang-btn active" id="btn-de" onclick="setLanguage('de')" role="tab" aria-selected="true">🇩🇪 Deutsch</button>
                    <button class="lang-btn" id="btn-en" onclick="setLanguage('en')" role="tab" aria-selected="false">🇬🇧 English</button>
                    <button class="lang-btn" id="btn-es" onclick="setLanguage('es')" role="tab" aria-selected="false">🇪🇸 Español</button>
                </div>
                <a href="Datenschutz.pdf" target="_blank" class="pdf-link-btn" title="Download Original PDF">
                    📄 PDF (DE)
                </a>
            </div>
        </div>
    </header>

    <div class="main-layout">
        <aside class="sidebar">
            <div class="search-box">
                <input type="text" class="search-input" id="searchInput" placeholder="Abschnitte durchsuchen..." oninput="handleSearch()">
            </div>
            <h3 id="tocHeading">Inhaltsverzeichnis</h3>
            <ul class="toc-list" id="dynamicToc">
                <!-- Populated dynamically via JS -->
            </ul>
        </aside>

        <main class="content-area">
            <!-- German Pane -->
            <div id="pane-de" class="lang-pane active">
                <div class="hero-banner">
                    <div class="badge-row">
                        <span class="badge">SNAPYOURDATE Legal</span>
                        <span class="badge badge-date">{data['meta']['date']['de']}</span>
                    </div>
                    <h1>Datenschutzerklärung</h1>
                    <p class="intro-lead">{data['meta']['intro']['de']}</p>
                </div>
                <div class="quick-cards" id="cards-de"></div>
                <div class="policy-sections-wrapper" id="sections-de"></div>
            </div>

            <!-- English Pane -->
            <div id="pane-en" class="lang-pane">
                <div class="hero-banner">
                    <div class="badge-row">
                        <span class="badge">SNAPYOURDATE Legal</span>
                        <span class="badge badge-date">{data['meta']['date']['en']}</span>
                    </div>
                    <h1>Privacy Policy</h1>
                    <p class="intro-lead">{data['meta']['intro']['en']}</p>
                </div>
                <div class="quick-cards" id="cards-en"></div>
                <div class="policy-sections-wrapper" id="sections-en"></div>
            </div>

            <!-- Spanish Pane -->
            <div id="pane-es" class="lang-pane">
                <div class="hero-banner">
                    <div class="badge-row">
                        <span class="badge">SNAPYOURDATE Legal</span>
                        <span class="badge badge-date">{data['meta']['date']['es']}</span>
                    </div>
                    <h1>Política de Privacidad</h1>
                    <p class="intro-lead">{data['meta']['intro']['es']}</p>
                </div>
                <div class="quick-cards" id="cards-es"></div>
                <div class="policy-sections-wrapper" id="sections-es"></div>
            </div>
        </main>
    </div>

    <footer class="footer">
        <div class="footer-links">
            <a href="javascript:void(0)" onclick="setLanguage('de')">🇩🇪 Deutsch (Original)</a>
            <a href="javascript:void(0)" onclick="setLanguage('en')">🇬🇧 English</a>
            <a href="javascript:void(0)" onclick="setLanguage('es')">🇪🇸 Español</a>
            <span style="color:var(--border-color);">|</span>
            <a href="privacy-de.html">Direct DE Link</a>
            <a href="privacy-en.html">Direct EN Link</a>
            <a href="privacy-es.html">Direct ES Link</a>
            <span style="color:var(--border-color);">|</span>
            <a href="Datenschutz.pdf" target="_blank">📄 Original PDF</a>
        </div>
        <p>&copy; 2026 SNAPYOURDATE UG (haftungsbeschränkt) · Meiendorfer Straße 72, 22145 Hamburg, Deutschland.</p>
        <p style="margin-top:0.4rem; font-size:0.8rem; color:var(--text-muted);">Vertreten durch / Represented by / Representada por: Liroy Johnny Ilian Jonat · E-Mail: info@monalisaentertainment.com</p>
    </footer>

    <script>
        const policyData = {lang_sections_json};
        const summaryCards = {summary_cards_json};
        const tocHeadings = {toc_titles_json};
        const searchPlaceholders = {search_placeholders_json};

        let currentLang = 'de';

        function renderLanguageContent(lang) {{
            // Render Quick Cards
            const cardsContainer = document.getElementById('cards-' + lang);
            if (cardsContainer && cardsContainer.children.length === 0) {{
                let cardsHtml = '';
                summaryCards[lang].forEach(card => {{
                    cardsHtml += `
                    <div class="quick-card">
                        <h4>${{card.title}}</h4>
                        <p>${{card.text}}</p>
                    </div>`;
                }});
                cardsContainer.innerHTML = cardsHtml;
            }}

            // Render Sections
            const sectionsContainer = document.getElementById('sections-' + lang);
            if (sectionsContainer && sectionsContainer.children.length === 0) {{
                let sHtml = '';
                policyData.sections.forEach(sec => {{
                    sHtml += `
                    <article id="${{sec.id}}-${{lang}}" class="policy-section" data-sec-num="${{sec.num}}">
                        <header class="section-header">
                            <span class="section-num">${{sec.num}}</span>
                            <h2 class="section-title">${{sec.title[lang]}}</h2>
                        </header>
                        <div class="section-body">
                            ${{sec.content[lang]}}
                        </div>
                    </article>`;
                }});
                sectionsContainer.innerHTML = sHtml;
            }}
        }}

        function updateToc(lang) {{
            document.getElementById('tocHeading').innerText = tocHeadings[lang] || 'Table of Contents';
            document.getElementById('searchInput').placeholder = searchPlaceholders[lang] || 'Search...';
            
            const tocList = document.getElementById('dynamicToc');
            let tocHtml = '';
            policyData.sections.forEach(sec => {{
                tocHtml += `
                <li>
                    <a href="#${{sec.id}}-${{lang}}" class="toc-link" data-target="${{sec.id}}-${{lang}}">
                        <span style="color:var(--primary);font-weight:700;">${{sec.num}}.</span> ${{sec.title[lang]}}
                    </a>
                </li>`;
            }});
            tocList.innerHTML = tocHtml;
        }}

        function setLanguage(lang, updateUrl = true) {{
            if (!['de', 'en', 'es'].includes(lang)) lang = 'de';
            currentLang = lang;
            document.documentElement.lang = lang;

            // Render content if not already rendered
            renderLanguageContent(lang);

            // Toggle panes
            ['de', 'en', 'es'].forEach(l => {{
                const pane = document.getElementById('pane-' + l);
                const btn = document.getElementById('btn-' + l);
                if (l === lang) {{
                    pane.classList.add('active');
                    btn.classList.add('active');
                    btn.setAttribute('aria-selected', 'true');
                }} else {{
                    pane.classList.remove('active');
                    btn.classList.remove('active');
                    btn.setAttribute('aria-selected', 'false');
                }}
            }});

            // Update Header Subtitle
            document.getElementById('headerSubtitle').innerText = policyData.meta.subtitle[lang];
            document.title = policyData.meta.title[lang];

            // Update TOC & Search placeholder
            updateToc(lang);

            // Clear search filter
            const searchInput = document.getElementById('searchInput');
            if (searchInput) searchInput.value = '';

            // Update URL hash/query
            if (updateUrl) {{
                try {{
                    const url = new URL(window.location);
                    url.searchParams.set('lang', lang);
                    window.history.replaceState({{}}, '', url);
                }} catch (e) {{}}
            }}

            try {{
                localStorage.setItem('syd_pref_lang', lang);
            }} catch(e) {{}}
        }}

        function handleSearch() {{
            const filter = document.getElementById('searchInput').value.toLowerCase().trim();
            const activePane = document.getElementById('pane-' + currentLang);
            const sections = activePane.querySelectorAll('.policy-section');
            const tocLinks = document.querySelectorAll('#dynamicToc .toc-link');

            sections.forEach((sec, idx) => {{
                const text = sec.innerText.toLowerCase();
                const matches = text.includes(filter);
                sec.style.display = matches ? 'block' : 'none';
                if (tocLinks[idx]) {{
                    tocLinks[idx].parentElement.style.display = matches ? 'block' : 'none';
                }}
            }});
        }}

        // Initialize from URL or LocalStorage
        window.addEventListener('DOMContentLoaded', () => {{
            const urlParams = new URLSearchParams(window.location.search);
            const hash = window.location.hash.replace('#', '').toLowerCase();
            const savedLang = localStorage.getItem('syd_pref_lang');

            let initialLang = 'de';
            if (['de', 'en', 'es'].includes(urlParams.get('lang'))) {{
                initialLang = urlParams.get('lang');
            }} else if (['de', 'en', 'es'].includes(hash)) {{
                initialLang = hash;
            }} else if (savedLang && ['de', 'en', 'es'].includes(savedLang)) {{
                initialLang = savedLang;
            }} else if (navigator.language) {{
                const prefix = navigator.language.slice(0, 2).toLowerCase();
                if (['de', 'en', 'es'].includes(prefix)) {{
                    initialLang = prefix;
                }}
            }}

            // Pre-render all languages
            ['de', 'en', 'es'].forEach(renderLanguageContent);
            setLanguage(initialLang, false);

            // Scrollspy for TOC
            window.addEventListener('scroll', () => {{
                const activePane = document.getElementById('pane-' + currentLang);
                const sections = activePane.querySelectorAll('.policy-section');
                const tocLinks = document.querySelectorAll('#dynamicToc .toc-link');
                let currentSecId = '';

                sections.forEach(sec => {{
                    if (sec.style.display !== 'none') {{
                        const top = sec.offsetTop - 140;
                        if (pageYOffset >= top) {{
                            currentSecId = sec.getAttribute('id');
                        }}
                    }}
                }});

                tocLinks.forEach(link => {{
                    link.classList.remove('active');
                    if (link.getAttribute('data-target') === currentSecId) {{
                        link.classList.add('active');
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html.strip())
print("index.html generated successfully!")
