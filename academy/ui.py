from pathlib import Path

import streamlit as st


def load_style():
    css = (Path(__file__).parent / "style.css").read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


def heading(title, description, eyebrow="SİZİN SQL SƏYAHƏTİNİZ"):
    from html import escape

    st.html(
        f'<div class="page-heading"><div class="eyebrow">{escape(eyebrow)}</div>'
        f'<h1>{escape(title)}</h1><p>{escape(description)}</p></div>'
    )


def navigate(page):
    st.session_state.page = page


def sidebar():
    with st.sidebar:
        st.html('''<div class="brand"><div class="brand-mark">▤</div>
            <div>SQL Quiz<span>ACADEMY</span></div></div>
            <div class="sidebar-label">ÖYRƏNMƏ MƏKANINIZ</div>''')
        for page, label, icon in (
            ("home", "İcmal", ":material/dashboard:"),
            ("tests", "Testlər", ":material/menu_book:"),
            ("results", "Nəticələrim", ":material/monitoring:"),
        ):
            st.button(
                label,
                icon=icon,
                key="nav_" + page,
                type="primary" if st.session_state.page == page else "tertiary",
                use_container_width=True,
                on_click=navigate,
                args=(page,),
            )
        st.html('''<div class="sidebar-note"><div class="note-code">&lt;/&gt; ✧</div>
            <h4>Hər sual bir addımdır.</h4><p>SQL biliklərinizi hər gün bir az daha inkişaf etdirin.</p>
            <span>Öyrən. Sına. İnkişaf et.</span></div>''')
        st.button(
            "Hesaba daxil ol",
            icon=":material/login:",
            key="sidebar_login",
            type="tertiary",
            use_container_width=True,
            on_click=navigate,
            args=("login",),
        )


def topbar():
    labels = {"home": "İcmal", "tests": "Testlər", "results": "Nəticələrim", "login": "Hesaba giriş"}
    left, right = st.columns([4, 1], vertical_alignment="center")
    with left:
        st.html(f'<div class="breadcrumb">Platforma <span>/</span> <b>{labels.get(st.session_state.page, "İcmal")}</b></div>')
    with right:
        st.button(
            "Daxil ol ↗", key="header_login", use_container_width=True,
            on_click=navigate, args=("login",),
        )


def footer():
    st.html('<div class="site-footer"><span>SQL Quiz Academy</span><span>Bilikdən bacarığa · Oracle SQL &amp; PL/SQL</span></div>')
