import streamlit as st

from academy.catalog import QUIZZES
from academy.ui import heading, navigate


def quiz_cards(quizzes):
    columns = st.columns(3, gap="medium")
    for col, quiz in zip(columns, quizzes):
        with col:
            with st.container(border=True, key="card_" + quiz["id"]):
                st.html(f'''<div class="quiz-card"><div class="card-top"><span class="quiz-icon {quiz['tone']}">{quiz['symbol']}</span>
                    <span class="level {quiz['tone']}">{quiz['level']}</span></div>
                    <div class="quiz-topic">{quiz['topic']}</div><h3>{quiz['title']}</h3>
                    <p>{quiz['description']}</p><div class="quiz-meta"><span>◉ {quiz['questions']} sual</span><span>◷ {quiz['minutes']} dəqiqə</span></div></div>''')
                st.button(
                    "Tezliklə · Testə başla →", disabled=True,
                    key="start_" + quiz["id"], use_container_width=True,
                    help="Testlərin cavablandırılması 3-cü mərhələdə aktivləşdiriləcək.",
                )


def home():
    heading(
        "Böyük biliklər kiçik addımlarla başlayır.",
        "Oracle SQL və PL/SQL biliklərinizi sınayın, nəticələrinizi izləyin və inkişaf edin.",
    )
    st.html('''<section class="hero"><div class="hero-copy"><div class="hero-kicker">✧ BİLİYİNİZİ NÖVBƏTİ SƏVİYYƏYƏ DAŞIYIN</div>
        <h2>Sadəcə sorğu yazmayın.<br><span>SQL-ə hakim olun.</span></h2>
        <p>Hər test yeni bir bacarıqdır. Mövzunuzu seçin,<br>biliklərinizi yoxlayın və fərqinizi görün.</p>
        <div class="hero-note">✓ Oracle SQL və PL/SQL üzrə praktik suallar</div></div>
        <div class="hero-art"><div class="orbit"></div><div class="code-window"><div class="code-header"><i></i><i></i><i></i><span>your_next_level.sql</span></div>
        <div class="hero-code"><div><small>01</small> <b>SELECT</b> success</div><div><small>02</small> <b>FROM</b> your_future</div><div><small>03</small> <b>WHERE</b> practice = <em>'daily'</em>;</div></div>
        <div class="code-success">● Öyrənməyə davam et <span>✓</span></div></div><div class="floating-db">▤</div></div></section>''')
    st.button("Testləri kəşf et →", type="primary", key="discover_tests", on_click=navigate, args=("tests",))
    st.html('''<div class="stats-grid">
        <div class="stat"><span>Mövzu üzrə testlər</span><strong>3</strong><small>Nümunə kataloq</small><i class="purple">▤</i></div>
        <div class="stat"><span>Tamamlanan testlər</span><strong>—</strong><small>Girişdən sonra göstəriləcək</small><i class="blue">✓</i></div>
        <div class="stat"><span>Orta nəticəniz</span><strong>—</strong><small>İlk nəticənizi gözləyir</small><i class="green">◎</i></div>
        <div class="stat"><span>Ən yüksək nəticəniz</span><strong>—</strong><small>Hər cəhd irəliyə bir addımdır</small><i class="orange">♧</i></div></div>
        <div class="section-heading"><h2>Biliklərinizi sınayın <span>3 mövzu</span></h2><p>Səviyyənizə uyğun mövzunu seçin və ilk addımı atın.</p></div>''')
    quiz_cards(QUIZZES)
    a, b = st.columns([1.3, 1], gap="medium")
    with a:
        st.html('''<section class="bottom-panel"><h3>Son nəticələriniz</h3><div class="empty-result"><span>↗</span><div><h4>İlk nəticəniz üçün hazırsınız?</h4><p>Testləri tamamladıqdan sonra inkişafınızı burada izləyəcəksiniz.</p></div></div></section>''')
    with b:
        st.html('''<section class="tip-panel"><div class="eyebrow">GÜNÜN SQL İPUCU</div><h3>NULL adi bir dəyər deyil.</h3><p>NULL yoxlanışı üçün <code>= NULL</code> əvəzinə <code>IS NULL</code> istifadə edin.</p></section>''')


def tests():
    heading("Testlər", "Oracle SQL və PL/SQL üzrə mövzuları kəşf edin.", "BİLİKDƏN BACARIĞA")
    topic = st.segmented_control("Mövzu", ["Hamısı", "Oracle SQL", "PL/SQL"], default="Hamısı")
    search = st.text_input("Test axtar", placeholder="Mövzu və ya test adı…", icon=":material/search:")
    rows = [q for q in QUIZZES if (topic in (None, "Hamısı") or q["topic"] == topic) and search.casefold() in (q["title"] + q["description"]).casefold()]
    if rows:
        quiz_cards(rows)
    else:
        st.info("Uyğun test tapılmadı. Başqa açar söz və ya mövzu seçin.")
    st.caption("Bu mərhələdə test kataloqu təqdim olunur. Cavablandırma və vaxt sayğacı 3-cü mərhələdə aktivləşdiriləcək.")


def login():
    heading("Öyrənmə məkanınıza daxil olun", "Şəxsi nəticələrinizə və test tarixçənizə bir yerdən baxın.", "SQL QUIZ ACADEMY")
    left, right = st.columns([1.05, 1], gap="large")
    with left:
        st.html('''<div class="auth-story"><div class="auth-badge">✧ ÖYRƏNMƏK ÜÇÜN DOĞRU YER</div><h2>Gələcəyinizi<br><span>biliklə qurun.</span></h2><p>Hər yeni sual bir fürsətdir. Praktika edin, özünüzü sınayın və inkişafınızı izləyin.</p>
            <div>✓ Mövzular üzrə praktiki testlər</div><div>✓ Serverdə obyektiv qiymətləndirmə</div><div>✓ Şəxsi nəticələr və inkişaf tarixçəsi</div>
            <pre><b>SELECT</b> knowledge<br><b>FROM</b> academy<br><b>WHERE</b> learner = 'you';</pre></div>''')
    with right:
        with st.container(border=True, key="login_panel"):
            st.html('<div class="auth-title"><span>▤</span><h2>Yenidən xoş gəlmisiniz</h2><p>Hesabınıza giriş üçün məlumatlarınızı daxil edin.</p></div>')
            st.info("Bu, giriş ekranının önbaxışıdır. Hələlik real şifrənizi daxil etməyin.")
            with st.form("login_form", clear_on_submit=True):
                st.text_input("E-poçt ünvanı", placeholder="siz@example.com", max_chars=254)
                st.text_input("Şifrə", type="password", placeholder="Şifrənizi daxil edin", max_chars=128)
                submitted = st.form_submit_button("Daxil ol →", type="primary", use_container_width=True)
            if submitted:
                st.info("Giriş hələ aktiv deyil. Hesabların təhlükəsiz qeydiyyatı və girişi növbəti mərhələdə qoşulacaq. Hesabınıza giriş edilmədi.")
            st.caption("Giriş ekranının önbaxışı · Hesabların aktivləşdirilməsi növbəti mərhələdədir.")
            st.html('<div class="auth-security">♧ Təhlükəsiz giriş · Ayrı müəllim və tələbə hesabları</div>')


def results():
    heading("Nəticələrim", "Şəxsi test tarixçənizi və inkişafınızı burada izləyəcəksiniz.")
    st.html('''<section class="results-empty"><span>↗</span><h3>Nəticələriniz üçün şəxsi məkan</h3><p>Hesabınıza daxil olub test tamamladıqdan sonra balınız, faiziniz və cavab təhliliniz burada görünəcək.</p></section>''')
    st.button("Giriş ekranına keç →", key="results_login", type="primary", on_click=navigate, args=("login",))
