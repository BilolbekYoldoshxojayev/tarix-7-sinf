"""Topic catalogue: id, book, title, printed page range (PDF page == printed page)."""

BOOKS = {
    "uz": {"title": "O‘zbekiston tarixi", "pdf": "Ozbekiston_tarixi_7_uzb_2022 (1).pdf"},
    "jh": {"title": "Jahon tarixi", "pdf": "jahon_tarixi_7_uzb_2022.pdf"},
}

TOPICS = [
    ("uz01", "uz", "Ajdodlarimizning ma’naviy qadriyatlari – jahon sivilizatsiyasi asoslaridan biri", 3, 7),
    ("uz02", "uz", "IV–VII asrlarda mamlakatimiz xalqlarining turmush tarzi", 8, 9),
    ("uz03", "uz", "IV–VII asrlarda Xorazm", 10, 14),
    ("uz04", "uz", "IV–V asrlarda xioniylar va kidariylar", 15, 17),
    ("uz05", "uz", "Eftaliylar", 18, 23),
    ("uz06", "uz", "Turk xoqonligi", 24, 31),
    ("uz07", "uz", "G‘arbiy Turk xoqonligi", 32, 38),
    ("uz08", "uz", "Mahalliy hokimliklarning tashkil topishi", 39, 47),
    ("uz09", "uz", "Turon xalqlarining harbiy san’ati", 48, 53),
    ("uz10", "uz", "VI–VII asrlarda Turon xalqlari madaniy hayoti", 54, 61),
    ("jh01", "jh", "German qabilalari va Rim imperiyasi", 6, 11),
    ("jh02", "jh", "Franklar davlati: qirollikdan imperiya sari", 12, 21),
    ("jh03", "jh", "Britaniyadan – Angliyaga", 22, 29),
    ("jh04", "jh", "Muqaddas Rim imperiyasi", 30, 35),
    ("jh05", "jh", "Vizantiya: G‘arb va Sharq orasida", 36, 41),
    ("jh06", "jh", "Slavyan davlatlarining tashkil topishi", 42, 49),
    ("jh07", "jh", "Yangi din beshigi", 50, 55),
    ("jh08", "jh", "Arab xalifaligi: islom dunyosining barpo etilishi", 56, 61),
]
