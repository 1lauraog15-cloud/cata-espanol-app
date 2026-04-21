import streamlit as st


def load_css() -> None:
    """Inyecta en la página todos los estilos globales de la app."""
    st.markdown("""
<style>
    /* ── Fonts ─────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=DM+Sans:wght@300;400;500;600&display=swap');

    /* ── Design tokens ──────────────────────────────────── */
    :root {
        --bg:           #f7f3ed;
        --bg-card:      #ffffff;
        --txt:          #1c1007;
        --txt2:         #7a6e60;
        --border:       #e4ddd3;
        --red:          #b5432a;
        --red-soft:     #faeee9;
        --gold:         #c07a18;
        --gold-soft:    #fdf3dc;
        --green:        #2e6b47;
        --green-soft:   #e6f4ee;
        --navy:         #1e3a5f;
        --navy-soft:    #e6ecf5;
        --purple:       #5b3a9e;
        --purple-soft:  #ede8f8;
        --amber:        #b45309;
        --amber-soft:   #fef3c7;
        --shadow:       0 2px 14px rgba(28,16,7,.07);
        --shadow-lg:    0 8px 32px rgba(28,16,7,.10);
        --r:            14px;
        --r-lg:         20px;
    }

    /* ── Base ───────────────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background: var(--bg);
        color: var(--txt);
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2.5rem;
        max-width: 1320px;
    }

    /* ── Sidebar ────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: #fff !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }

    /* ── Brand block ─────────────────────────────────────── */
    .brand {
        padding: 1.4rem 1.2rem 1rem;
        border-bottom: 1px solid var(--border);
        margin-bottom: 0.4rem;
    }
    .brand-name {
        font-family: 'Fraunces', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: var(--txt);
        letter-spacing: -0.02em;
        line-height: 1;
    }
    .brand-tagline {
        font-size: 0.76rem;
        color: var(--txt2);
        margin-top: 0.25rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* ── Nav sections ────────────────────────────────────── */
    .nav-section {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.10em;
        text-transform: uppercase;
        color: var(--txt2);
        padding: 0.9rem 1.2rem 0.3rem;
    }
    .nav-item {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.55rem 1.2rem;
        margin: 0.05rem 0.5rem;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 500;
        color: var(--txt);
        cursor: pointer;
        transition: background 0.12s;
        text-decoration: none;
    }
    .nav-item:hover { background: var(--bg); }
    .nav-item.active {
        background: var(--red-soft);
        color: var(--red);
        font-weight: 600;
    }
    .nav-item .ni-icon { font-size: 1rem; width: 1.3rem; text-align: center; }
    .nav-divider { height: 1px; background: var(--border); margin: 0.6rem 1.2rem; }

    /* ── Module header ───────────────────────────────────── */
    .mod-header {
        border-radius: var(--r-lg);
        padding: 1.4rem 1.8rem;
        margin-bottom: 1.4rem;
        display: flex;
        align-items: center;
        gap: 1.2rem;
    }
    .mod-header-icon {
        font-size: 2.4rem;
        line-height: 1;
    }
    .mod-header-text h2 {
        font-family: 'Fraunces', serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0 0 0.2rem;
        line-height: 1.1;
    }
    .mod-header-text p {
        margin: 0;
        font-size: 0.88rem;
        opacity: 0.8;
    }

    /* ── Home cards ──────────────────────────────────────── */
    .home-hero {
        background: linear-gradient(135deg, var(--txt) 0%, #2d1a0a 100%);
        border-radius: var(--r-lg);
        padding: 2.4rem 2rem;
        margin-bottom: 2rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    .home-hero::before {
        content: "";
        position: absolute;
        top: -40px; right: -40px;
        width: 220px; height: 220px;
        background: var(--red);
        border-radius: 50%;
        opacity: 0.12;
    }
    .home-hero h1 {
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 0.5rem;
        color: white;
        position: relative;
    }
    .home-hero p {
        margin: 0;
        font-size: 1rem;
        color: rgba(255,255,255,0.72);
        position: relative;
    }
    .home-hero .stat-row {
        display: flex;
        gap: 2rem;
        margin-top: 1.4rem;
        position: relative;
    }
    .home-stat { text-align: left; }
    .home-stat-n {
        font-family: 'Fraunces', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        line-height: 1;
    }
    .home-stat-l {
        font-size: 0.78rem;
        color: rgba(255,255,255,0.6);
        margin-top: 0.1rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .module-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 1.2rem;
        transition: box-shadow 0.15s, transform 0.15s;
        height: 100%;
        cursor: pointer;
        box-shadow: var(--shadow);
    }
    .module-card:hover {
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    .mc-top {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.7rem;
    }
    .mc-icon {
        font-size: 1.4rem;
        width: 2.4rem;
        height: 2.4rem;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    .mc-title {
        font-family: 'Fraunces', serif;
        font-size: 1rem;
        font-weight: 700;
        color: var(--txt);
        line-height: 1.2;
    }
    .mc-desc {
        font-size: 0.82rem;
        color: var(--txt2);
        line-height: 1.5;
        margin-bottom: 0.8rem;
    }
    .mc-badge {
        display: inline-block;
        font-size: 0.74rem;
        font-weight: 600;
        border-radius: 999px;
        padding: 0.2rem 0.6rem;
    }

    /* ── Metric cards ────────────────────────────────────── */
    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 0.9rem 1rem;
        text-align: center;
        box-shadow: var(--shadow);
    }
    .metric-value {
        font-family: 'Fraunces', serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: var(--txt);
        line-height: 1;
    }
    .metric-label {
        font-size: 0.78rem;
        color: var(--txt2);
        margin-top: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* ── Cards & quiz boxes ──────────────────────────────── */
    .card-box, .quiz-box {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--r);
        padding: 1.3rem;
        box-shadow: var(--shadow);
        margin-bottom: 0.6rem;
    }
    .card-chip {
        display: inline-block;
        background: var(--purple-soft);
        color: var(--purple);
        border-radius: 999px;
        padding: 0.25rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }
    .nivel-badge {
        display: inline-block;
        border-radius: 999px;
        padding: 0.18rem 0.55rem;
        font-size: 0.74rem;
        font-weight: 700;
        color: white;
        margin-left: 0.4rem;
    }
    .card-title {
        font-family: 'Fraunces', serif;
        color: var(--navy);
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.55rem;
        line-height: 1.2;
    }
    .card-line { color: var(--txt); margin-bottom: 0.4rem; font-size: 0.95rem; }
    .section-title {
        font-family: 'Fraunces', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--txt);
        margin-bottom: 0.2rem;
    }
    .section-sub { color: var(--txt2); margin-bottom: 0.8rem; font-size: 0.87rem; }

    /* ── Example / nota blocks ───────────────────────────── */
    .example-block {
        background: var(--navy-soft);
        border-left: 3px solid var(--navy);
        border-radius: 0 10px 10px 0;
        padding: 0.5rem 0.85rem;
        margin: 0.3rem 0;
        font-style: italic;
        color: var(--navy);
        font-size: 0.91rem;
    }
    .nota-box {
        background: var(--amber-soft);
        border: 1px solid #fcd34d;
        border-radius: 10px;
        padding: 0.5rem 0.85rem;
        font-size: 0.85rem;
        color: var(--amber);
        margin-top: 0.6rem;
    }

    /* ── Feedback ────────────────────────────────────────── */
    .feedback-ok {
        background: var(--green-soft);
        border-left: 4px solid var(--green);
        color: var(--green);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-bad {
        background: var(--red-soft);
        border-left: 4px solid var(--red);
        color: var(--red);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-neutral {
        background: var(--bg);
        border-left: 4px solid var(--border);
        color: var(--txt);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }
    .feedback-ai {
        background: var(--gold-soft);
        border-left: 4px solid var(--gold);
        color: var(--amber);
        padding: 0.85rem 1rem;
        border-radius: 0 var(--r) var(--r) 0;
        margin-top: 0.75rem;
        white-space: pre-wrap;
        font-size: 0.92rem;
    }

    /* ── Doble prep cards ────────────────────────────────── */
    .double-prep-card {
        background: var(--gold-soft);
        border: 1px solid #fde68a;
        border-radius: var(--r);
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .dp-verb { font-family: 'Fraunces', serif; font-size: 1.05rem; color: var(--amber); font-weight: 700; }
    .dp-row { margin: 0.4rem 0; }
    .dp-prep { display: inline-block; background: var(--amber-soft); color: var(--amber); border-radius: 6px; padding: 0.12rem 0.4rem; font-weight: 700; font-size: 0.85rem; }
    .dp-sig { color: var(--txt); font-size: 0.88rem; }
    .dp-ex { color: var(--amber); font-style: italic; font-size: 0.85rem; margin-top: 0.1rem; }
    .weak-tag { background: var(--red-soft); color: var(--red); border-radius: 6px; padding: 0.12rem 0.5rem; font-size: 0.76rem; font-weight: 700; }

    /* ── Conectores ──────────────────────────────────────── */
    .con-card-chip {
        display: inline-block;
        background: var(--gold-soft);
        color: var(--amber);
        border-radius: 999px;
        padding: 0.25rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }
    .con-card-title {
        font-family: 'Fraunces', serif;
        color: var(--amber);
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.55rem;
    }
    .con-example-block {
        background: var(--gold-soft);
        border-left: 3px solid var(--gold);
        border-radius: 0 10px 10px 0;
        padding: 0.5rem 0.85rem;
        margin: 0.3rem 0;
        font-style: italic;
        color: var(--amber);
        font-size: 0.91rem;
    }

    /* ── Streamlit overrides ─────────────────────────────── */
    /* Sidebar nav buttons — clean, no border */
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        padding: 0.42rem 0.8rem !important;
        font-size: 0.87rem !important;
        font-weight: 400 !important;
        color: var(--txt) !important;
        box-shadow: none !important;
        margin: 1px 0 !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: var(--bg) !important;
        color: var(--txt) !important;
        border: none !important;
    }
    /* Main content area buttons — keep bordered */
    .block-container .stButton > button {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        color: var(--txt) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        transition: all 0.12s !important;
        padding: 0.45rem 1rem !important;
    }
    .block-container .stButton > button:hover {
        background: var(--bg) !important;
        border-color: var(--txt2) !important;
    }
    div[data-testid="stTabs"] button {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
    }
    .stRadio label { font-size: 0.88rem !important; }
    .stSelectbox label, .stMultiSelect label {
        font-size: 0.82rem !important;
        color: var(--txt2) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    .stProgress > div > div {
        background: var(--red) !important;
        border-radius: 999px !important;
    }
    .stProgress { border-radius: 999px !important; }

    /* ── Module badge (for home cards) ──────────────────── */
    .module-badge {
        display: inline-block;
        border-radius: 10px;
        padding: 0.4rem 1rem;
        font-weight: 700;
        font-size: 0.9rem;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)
