# SQL Quiz Academy

Azərbaycan dilində Oracle SQL və PL/SQL test platforması. **Ayrıca Streamlit layihəsidir.**

## Cari mərhələ: 1 — görünüş və naviqasiya

Hazırdır:

- Ağ, tünd-göy və bənövşəyi rənglərdə responsiv dashboard.
- Sol menyu və səhifələr arasında keçid.
- Üç nümunə mövzudan ibarət test kataloqu.
- Oracle SQL / PL/SQL mövzu filtri və mətn axtarışı.
- Giriş ekranının önbaxışı və nəticələr üçün boş vəziyyət.

**Hələ aktiv deyil:** real qeydiyyat/giriş, testlərin cavablandırılması, vaxt sayğacı, qiymətləndirmə, müəllim paneli və daimi verilənlər bazası. Giriş formasında real şifrə istifadə etməyin. Test başlatma düymələri bu mərhələdə bilərəkdən deaktivdir. Göstəricilər uydurma tələbə nəticələri göstərmir.

## Quruluş

```text
app.py                    Streamlit giriş faylı
requirements.txt          Python asılılıqları
.streamlit/config.toml    Rənglər və tətbiq konfiqurasiyası
academy/catalog.py        Açıq nümunə test metadatası
academy/ui.py             Menyu, başlıq və ümumi elementlər
academy/views.py          Ana səhifə, kataloq, giriş və nəticə ekranları
academy/style.css         Responsiv dizayn
tests/test_app.py          Streamlit səhifə və naviqasiya yoxlamaları
```

## Yerli işə salma

Python 3.12 tövsiyə olunur. Layihəni ayrıca qovluğa çıxarın:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Mac / Linux:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Brauzerdə terminalın göstərdiyi ünvanı **serverin işlədiyi kompüterdə** açın. Bulud mühitinin `localhost` ünvanı sizin Windows kompüterinizin ünvanı deyil. Onu açıq internet linki kimi paylaşmaq olmaz.

## Sonrakı mərhələlər

1. **Hazırkı mərhələ:** ana səhifə və giriş ekranının görünüşü.
2. **Qeydiyyat və giriş:** Supabase Auth, ad-soyad, e-poçt təsdiqi, yalnız müəllimə verilən admin rolu.
3. **Test mühərriki:** sualların bir-bir göstərilməsi, geri/irəli keçid, cavab saxlama, server vaxtı və serverdə qiymətləndirmə.
4. **Müəllim paneli:** test/sual CRUD, müddət/bal və Excel/CSV idxalı.
5. **Statistika:** şəxsi nəticələr, müəllim hesabatları, çətin suallar və Excel ixracı.
6. **Yayım:** ayrıca GitHub reposu + Streamlit Community Cloud + Supabase Free. Xidmətlərin pulsuz limitləri daxilində istifadə.

Düzgün cavablar açıq kataloqa və brauzer koduna daxil edilməyəcək. Müəllim menyusunu gizlətmək təkbaşına təhlükəsizlik sayılmayacaq: hər müəllim əməliyyatında serverdə rol yoxlanacaq.

## GitHub və Streamlit Community Cloud

Bu qovluğun məzmunu ayrıca `sql-quiz-academy` reposunun kökündə olmalıdır. Python faylları ilə birlikdə `academy/` qovluğunu, `requirements.txt` və `.streamlit/config.toml` faylını da yükləyin. Streamlit Cloud əsas faylı: **`app.py`**. Python: **3.12**.

İlk mərhələ üçün Supabase açarı lazım deyil. Növbəti mərhələdə məxfi açarlar Streamlit Cloud → **Secrets** bölməsinə daxil ediləcək; GitHub-a və çata yazılmayacaq. Sayt hələ internetdə yayımlanmayıb. Canlı `…streamlit.app` linki yalnız deploy tamamlanandan sonra yaranacaq.

## Yoxlama

Layihə qovluğunda:

```bash
python -m unittest discover -s tests -v
```

Sınaqlar Streamlit-in `AppTest` aləti ilə ayrıca sessiyalarda işləyir; səhifələrin render olunmasını, naviqasiyanı, kataloq axtarışını və giriş önbaxışının hesab yaratmamasını yoxlayır.
