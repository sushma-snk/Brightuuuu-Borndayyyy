import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For Brightuuuu ✨",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SECRET INFORMATION
# ============================================================

PASSWORD = "T20080209S"

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "password",
    "hint_level": 0,
    "password_attempts": 0,
    "entry_mode": None,
    "show_reveal": False,
    "funny_index": 0,
    "wish_index": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# BIRTHDAY WISHES
# 29 LANGUAGES
#
# ORDER:
# 1. South Indian places
# 2. North / Other Indian places
# 3. Other countries
# ============================================================

wishes = [

    # ========================================================
    # SOUTH INDIA
    # ========================================================

    {
        "place": "Tamil Nadu, India",
        "language": "Tamil",
        "wish": "இனிய பிறந்தநாள் வாழ்த்துக்கள்!",
        "translit": "Iniya pirandhanaal vaazhthukkal!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "Andhra Pradesh, India",
        "language": "Telugu",
        "wish": "పుట్టినరోజు శుభాకాంక్షలు!",
        "translit": "Puttinaroju shubhakankshalu!",
        "meaning": "Happy Birthday!",
        "emoji": "🌼"
    },

    {
        "place": "Karnataka, India",
        "language": "Kannada",
        "wish": "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು!",
        "translit": "Huttuhabbada shubhashayagalu!",
        "meaning": "Happy Birthday!",
        "emoji": "🌷"
    },

    {
        "place": "Kerala, India",
        "language": "Malayalam",
        "wish": "ജന്മദിനാശംസകൾ!",
        "translit": "Janmadinaashamsakal!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    # ========================================================
    # NORTH / OTHER INDIAN LANGUAGES
    # ========================================================

    {
        "place": "Uttar Pradesh, India",
        "language": "Hindi",
        "wish": "जन्मदिन मुबारक हो!",
        "translit": "Janmadin mubarak ho!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "West Bengal, India",
        "language": "Bengali",
        "wish": "শুভ জন্মদিন!",
        "translit": "Shubho jonmodin!",
        "meaning": "Happy Birthday!",
        "emoji": "🌼"
    },

    {
        "place": "Maharashtra, India",
        "language": "Marathi",
        "wish": "वाढदिवसाच्या हार्दिक शुभेच्छा!",
        "translit": "Vaadhdivsachya haardik shubhechha!",
        "meaning": "Heartfelt birthday wishes!",
        "emoji": "🌷"
    },

    {
        "place": "Punjab, India",
        "language": "Punjabi",
        "wish": "ਜਨਮਦਿਨ ਮੁਬਾਰਕ!",
        "translit": "Janamdin mubarak!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    {
        "place": "Gujarat, India",
        "language": "Gujarati",
        "wish": "જન્મદિવસની શુભકામનાઓ!",
        "translit": "Janmadivasni shubhakaamnaao!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    # ========================================================
    # OTHER COUNTRIES
    # ========================================================

    {
        "place": "United Kingdom",
        "language": "English",
        "wish": "Happy Birthday!",
        "translit": "Happy Birthday!",
        "meaning": "Wishing you a wonderful birthday!",
        "emoji": "✨"
    },

    {
        "place": "France",
        "language": "French",
        "wish": "Joyeux anniversaire !",
        "translit": "Joyeux anniversaire!",
        "meaning": "Happy Birthday!",
        "emoji": "🌷"
    },

    {
        "place": "Japan",
        "language": "Japanese",
        "wish": "お誕生日おめでとう！",
        "translit": "Otanjoubi omedetou!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "South Korea",
        "language": "Korean",
        "wish": "생일 축하해요!",
        "translit": "Saengil chukahaeyo!",
        "meaning": "Happy Birthday!",
        "emoji": "✨"
    },

    {
        "place": "Spain",
        "language": "Spanish",
        "wish": "¡Feliz cumpleaños!",
        "translit": "Feliz cumpleaños!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    {
        "place": "Italy",
        "language": "Italian",
        "wish": "Buon compleanno!",
        "translit": "Buon compleanno!",
        "meaning": "Happy Birthday!",
        "emoji": "🌷"
    },

    {
        "place": "Germany",
        "language": "German",
        "wish": "Alles Gute zum Geburtstag!",
        "translit": "Alles Gute zum Geburtstag!",
        "meaning": "All the best for your birthday!",
        "emoji": "🌼"
    },

    {
        "place": "Portugal",
        "language": "Portuguese",
        "wish": "Feliz aniversário!",
        "translit": "Feliz aniversário!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "China",
        "language": "Chinese",
        "wish": "生日快乐！",
        "translit": "Shēngrì kuàilè!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    {
        "place": "Saudi Arabia",
        "language": "Arabic",
        "wish": "عيد ميلاد سعيد!",
        "translit": "Eid milad sa'eed!",
        "meaning": "Happy Birthday!",
        "emoji": "✨"
    },

    {
        "place": "Türkiye",
        "language": "Turkish",
        "wish": "Doğum günün kutlu olsun!",
        "translit": "Dogum gunun kutlu olsun!",
        "meaning": "Happy Birthday!",
        "emoji": "🌷"
    },

    {
        "place": "Russia",
        "language": "Russian",
        "wish": "С днём рождения!",
        "translit": "S dnyom rozhdeniya!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "Greece",
        "language": "Greek",
        "wish": "Χρόνια πολλά!",
        "translit": "Chronia polla!",
        "meaning": "Many happy returns!",
        "emoji": "🌼"
    },

    {
        "place": "Netherlands",
        "language": "Dutch",
        "wish": "Gefeliciteerd met je verjaardag!",
        "translit": "Gefeliciteerd met je verjaardag!",
        "meaning": "Congratulations on your birthday!",
        "emoji": "🌷"
    },

    {
        "place": "Sweden",
        "language": "Swedish",
        "wish": "Grattis på födelsedagen!",
        "translit": "Grattis pa fodelsedagen!",
        "meaning": "Happy Birthday!",
        "emoji": "✨"
    },

    {
        "place": "Thailand",
        "language": "Thai",
        "wish": "สุขสันต์วันเกิด!",
        "translit": "Suk san wan goet!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    {
        "place": "Vietnam",
        "language": "Vietnamese",
        "wish": "Chúc mừng sinh nhật!",
        "translit": "Chuc mung sinh nhat!",
        "meaning": "Happy Birthday!",
        "emoji": "🌸"
    },

    {
        "place": "Indonesia",
        "language": "Indonesian",
        "wish": "Selamat ulang tahun!",
        "translit": "Selamat ulang tahun!",
        "meaning": "Happy Birthday!",
        "emoji": "🌼"
    },

    {
        "place": "Philippines",
        "language": "Filipino",
        "wish": "Maligayang kaarawan!",
        "translit": "Maligayang kaarawan!",
        "meaning": "Happy Birthday!",
        "emoji": "🌺"
    },

    {
        "place": "Ireland",
        "language": "Irish",
        "wish": "Lá breithe sona duit!",
        "translit": "La breithe sona duit!",
        "meaning": "Happy Birthday!",
        "emoji": "🌿"
    }
]


# ============================================================
# FUNNY INTRO
# ============================================================

funny_messages = [

    {
        "emoji": "😂",
        "title": "First things first...",
        "message": "I could have simply wished you Happy Birthday."
    },

    {
        "emoji": "🙃",
        "title": "But obviously...",
        "message": "That would have been far too normal for me."
    },

    {
        "emoji": "🌍",
        "title": "So I had an idea...",
        "message": "Why stop at one birthday wish when we can go around the world?"
    },

    {
        "emoji": "👀",
        "title": "Don't worry...",
        "message": "You don't have to pack your bags. Just keep pressing NEXT."
    },

    {
        "emoji": "🌸",
        "title": "But seriously...",
        "message": "I wanted to make your birthday a little different."
    },

    {
        "emoji": "✨",
        "title": "So here we go...",
        "message": "A little birthday wish, from a lot of different places."
    }
]


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(255, 194, 221, 0.75),
            transparent 28%
        ),

        radial-gradient(
            circle at 95% 8%,
            rgba(194, 224, 255, 0.75),
            transparent 28%
        ),

        radial-gradient(
            circle at 10% 65%,
            rgba(218, 201, 255, 0.72),
            transparent 32%
        ),

        radial-gradient(
            circle at 90% 60%,
            rgba(194, 245, 225, 0.70),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(255, 226, 190, 0.75),
            transparent 35%
        ),

        linear-gradient(
            135deg,
            #fff4fa,
            #f8f4ff,
            #f1f9ff,
            #f4fff9,
            #fff9ef
        );

    background-attachment: fixed;

    color: #55475c;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* =========================================================
   FLOATING FLOWERS + SHINES
   ========================================================= */

.float {
    position: fixed;
    bottom: -60px;

    font-size: 25px;

    opacity: 0;

    pointer-events: none;

    z-index: 0;

    animation: floatUp 11s linear infinite;
}

.f1 {
    left: 5%;
    animation-delay: 0s;
}

.f2 {
    left: 18%;
    animation-delay: 2.2s;
}

.f3 {
    left: 34%;
    animation-delay: 4.5s;
}

.f4 {
    left: 50%;
    animation-delay: 1.3s;
}

.f5 {
    left: 68%;
    animation-delay: 3.5s;
}

.f6 {
    left: 84%;
    animation-delay: 5.5s;
}

.f7 {
    left: 94%;
    animation-delay: 7s;
}

@keyframes floatUp {

    0% {
        transform:
            translateY(0)
            rotate(0deg)
            scale(0.8);

        opacity: 0;
    }

    12% {
        opacity: 0.65;
    }

    50% {
        transform:
            translateY(-55vh)
            rotate(180deg)
            scale(1.1);

        opacity: 0.75;
    }

    88% {
        opacity: 0.5;
    }

    100% {
        transform:
            translateY(-115vh)
            rotate(360deg)
            scale(0.8);

        opacity: 0;
    }
}


/* =========================================================
   MAIN TITLE
   ========================================================= */

.main-title {

    text-align: center;

    font-family: 'Playfair Display', serif;

    font-size: 48px;

    font-weight: 700;

    background:
        linear-gradient(
            90deg,
            #e99abf,
            #e5b77b,
            #a9c9ed,
            #bba4df,
            #9dcfb9,
            #e99abf
        );

    background-size: 400% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: titleGradient 7s linear infinite;

    margin-bottom: 8px;
}

@keyframes titleGradient {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 400% center;
    }
}


/* =========================================================
   SUBTITLE
   ========================================================= */

.subtitle {

    text-align: center;

    color: #806d82;

    font-size: 18px;

    margin-bottom: 30px;

    font-weight: 500;
}


/* =========================================================
   GLASS CARD
   ========================================================= */

.glass-card {

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.82),
            rgba(255,255,255,0.55)
        );

    border:
        1px solid rgba(255,255,255,0.9);

    border-radius: 30px;

    padding: 38px;

    backdrop-filter: blur(18px);

    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 15px 45px rgba(145,120,160,0.15),
        0 0 35px rgba(190,160,210,0.10);

    animation: cardIn 0.7s ease;
}

@keyframes cardIn {

    from {
        opacity: 0;
        transform: translateY(25px) scale(0.97);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}


/* =========================================================
   EMOJI
   ========================================================= */

.big-emoji {

    text-align: center;

    font-size: 68px;

    margin-bottom: 12px;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {

    width: 100%;

    border:
        1px solid rgba(255,255,255,0.8);

    border-radius: 18px;

    padding: 13px 20px;

    font-size: 18px;

    font-weight: 700;

    color: #66546a;

    background:
        linear-gradient(
            90deg,
            #ffd1e3,
            #ded1f7,
            #c8e6fa,
            #c9eedf
        );

    box-shadow:
        0 7px 22px rgba(160,140,180,0.18);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 30px rgba(150,130,180,0.25);
}


/* =========================================================
   TEXT INPUT
   ========================================================= */

.stTextInput input {

    background:
        rgba(255,255,255,0.65) !important;

    color: #594d5e !important;

    border:
        1px solid rgba(180,160,190,0.35) !important;

    border-radius: 16px !important;

    text-align: center !important;

    font-size: 21px !important;

    font-family:
        'DM Sans',
        sans-serif !important;
}


/* =========================================================
   HINT
   ========================================================= */

.hint-box {

    margin-top: 18px;

    padding: 20px;

    border-radius: 20px;

    text-align: center;

    background:
        linear-gradient(
            135deg,
            rgba(255,226,181,0.65),
            rgba(255,214,230,0.55)
        );

    border:
        1px solid rgba(230,190,150,0.35);

    color: #76604e;

    animation: cardIn 0.5s ease;
}


/* =========================================================
   REACTION
   ========================================================= */

.reaction {

    text-align: center;

    font-size: 23px;

    line-height: 1.7;

    padding: 25px;

    color: #65576a;
}


/* =========================================================
   WISH CARD
   ========================================================= */

.wish-card {

    min-height: 450px;

    border-radius: 35px;

    padding: 50px 30px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    border:
        1px solid rgba(255,255,255,0.95);

    background:
        linear-gradient(
            135deg,
            rgba(255,211,229,0.72),
            rgba(224,213,250,0.70),
            rgba(205,232,249,0.65),
            rgba(211,242,226,0.60),
            rgba(255,235,202,0.68)
        );

    box-shadow:
        0 18px 50px rgba(140,120,160,0.18);

    animation: wishAppear 0.75s ease;
}

@keyframes wishAppear {

    0% {
        opacity: 0;

        transform:
            scale(0.86)
            rotateX(10deg);
    }

    100% {
        opacity: 1;

        transform:
            scale(1)
            rotateX(0deg);
    }
}


/* =========================================================
   PLACE
   ========================================================= */

.destination {

    font-family: 'DM Sans', sans-serif;

    font-size: 15px;

    text-transform: uppercase;

    letter-spacing: 3px;

    color: #806b82;

    margin-bottom: 12px;
}


/* =========================================================
   LANGUAGE
   ========================================================= */

.wish-language {

    font-size: 18px;

    color: #8b7089;

    margin-bottom: 25px;

    font-weight: 600;
}


/* =========================================================
   WISH EMOJI
   ========================================================= */

.wish-emoji {

    font-size: 70px;

    margin-bottom: 22px;

    animation: emojiFloat 2.5s ease-in-out infinite;
}

@keyframes emojiFloat {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-9px);
    }
}


/* =========================================================
   NATIVE LANGUAGE WISH
   ========================================================= */

.wish-text {

    font-family:
        'Noto Sans',
        'Noto Sans Tamil',
        'Noto Sans Telugu',
        'Noto Sans Kannada',
        'Noto Sans Malayalam',
        'Noto Sans Devanagari',
        'Noto Sans Bengali',
        'Noto Sans Gujarati',
        'Noto Sans Gurmukhi',
        'Noto Sans Arabic',
        'Noto Sans CJK SC',
        'Noto Sans JP',
        'Noto Sans KR',
        sans-serif;

    font-size: 38px;

    font-weight: 700;

    color: #574c60;

    line-height: 1.55;

    margin-bottom: 12px;

    text-shadow:
        0 2px 10px rgba(255,255,255,0.7);
}


/* =========================================================
   TRANSLITERATION
   ========================================================= */

.transliteration {

    font-family:
        'DM Sans',
        sans-serif;

    font-size: 20px;

    font-style: italic;

    color: #826f83;

    margin-bottom: 14px;

    line-height: 1.5;
}


/* =========================================================
   ENGLISH MEANING
   ========================================================= */

.meaning {

    font-family:
        'DM Sans',
        sans-serif;

    font-size: 18px;

    color: #706273;

    font-weight: 500;
}


/* =========================================================
   FINAL CARD
   ========================================================= */

.final-card {

    text-align: center;

    padding: 55px 30px;

    border-radius: 35px;

    background:
        linear-gradient(
            135deg,
            rgba(255,211,229,0.75),
            rgba(225,214,249,0.75),
            rgba(205,232,250,0.70),
            rgba(211,242,226,0.70),
            rgba(255,235,204,0.75)
        );

    border:
        1px solid rgba(255,255,255,0.95);

    box-shadow:
        0 20px 60px rgba(135,115,155,0.20);
}


/* =========================================================
   FINAL TITLE
   ========================================================= */

.final-title {

    font-family:
        'Playfair Display',
        serif;

    font-size: 43px;

    font-weight: 700;

    color: #66536b;

    margin-bottom: 22px;

    animation: finalGlow 2s ease-in-out infinite alternate;
}

@keyframes finalGlow {

    from {
        text-shadow:
            0 0 5px rgba(235,170,200,0.35);
    }

    to {
        text-shadow:
            0 0 18px rgba(210,170,220,0.50),
            0 0 30px rgba(180,210,230,0.40);
    }
}


/* =========================================================
   FINAL MESSAGE
   ========================================================= */

.final-message {

    font-family:
        'DM Sans',
        sans-serif;

    font-size: 19px;

    line-height: 1.9;

    color: #685b6d;
}


/* =========================================================
   FINAL FLOWER + SHINE CELEBRATION
   ========================================================= */

.celebration {

    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: 999;

    overflow: hidden;
}

.celebration span {

    position: absolute;

    top: -60px;

    font-size: 27px;

    opacity: 0;

    animation:
        celebrationFall 5s linear infinite;
}

.c1  { left: 4%;  animation-delay: 0s; }
.c2  { left: 13%; animation-delay: 0.7s; }
.c3  { left: 23%; animation-delay: 1.5s; }
.c4  { left: 34%; animation-delay: 0.3s; }
.c5  { left: 45%; animation-delay: 1.9s; }
.c6  { left: 57%; animation-delay: 0.9s; }
.c7  { left: 68%; animation-delay: 2.2s; }
.c8  { left: 78%; animation-delay: 1.2s; }
.c9  { left: 88%; animation-delay: 2.7s; }
.c10 { left: 96%; animation-delay: 1.7s; }

@keyframes celebrationFall {

    0% {
        transform:
            translateY(-80px)
            rotate(0deg)
            scale(0.7);

        opacity: 0;
    }

    12% {
        opacity: 0.9;
    }

    50% {
        transform:
            translateY(50vh)
            translateX(30px)
            rotate(180deg)
            scale(1.1);

        opacity: 0.8;
    }

    85% {
        opacity: 0.6;
    }

    100% {
        transform:
            translateY(115vh)
            translateX(-25px)
            rotate(360deg)
            scale(0.8);

        opacity: 0;
    }
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 600px) {

    .main-title {
        font-size: 34px;
    }

    .wish-text {
        font-size: 28px;
    }

    .transliteration {
        font-size: 17px;
    }

    .meaning {
        font-size: 16px;
    }

    .wish-card {
        min-height: 420px;
        padding: 35px 20px;
    }

    .glass-card {
        padding: 28px 20px;
    }

    .final-title {
        font-size: 34px;
    }
}

</style>

<div class="float f1">🌸</div>
<div class="float f2">✨</div>
<div class="float f3">🌷</div>
<div class="float f4">✨</div>
<div class="float f5">🌺</div>
<div class="float f6">✨</div>
<div class="float f7">🌼</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# PASSWORD PAGE
# ============================================================

if st.session_state.page == "password":

    st.markdown(
        '<div class="main-title">✨ Something Made Just For You ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">There is something waiting here for you.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass-card">

            <div class="big-emoji">
                🌸✨🌼
            </div>

            <h2 style="
                text-align:center;
                font-family:'Playfair Display', serif;
                color:#66566b;
            ">
                Hey Brightuuuu..!!
            </h2>

            <p style="
                text-align:center;
                color:#756578;
                font-size:18px;
                line-height:1.8;
            ">
                Before you enter, there's just one tiny problem...
                <br><br>
                <b>You need the secret password.</b>
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Enter the secret password",
        type="password",
        placeholder="Enter password..."
    )

    if st.button("🔓 Unlock"):

        if password == PASSWORD:

            st.session_state.entry_mode = st.session_state.hint_level
            st.session_state.page = "entry_reaction"

            st.rerun()

        else:

            st.session_state.password_attempts += 1

            st.error(
                "❌ Nope! That's not it. Try again, birthday boy. 😂"
            )

    # ========================================================
    # HINT BUTTON
    # ========================================================

    if st.session_state.hint_level < 2:

        if st.button("💡 Give me a hint"):

            st.session_state.hint_level += 1

            st.rerun()

    # ========================================================
    # HINT 1
    # ========================================================

    if st.session_state.hint_level >= 1:

        st.markdown(
            """
            <div class="hint-box">

                💡 <b>HINT 1</b>

                <br><br>

                It contains exactly
                <b>2 letters/characters</b>
                and
                <b>8 digits</b>.

                <br><br>

                I know you got it. 😌

            </div>
            """,
            unsafe_allow_html=True
        )

    # ========================================================
    # HINT 2
    # ========================================================

    if st.session_state.hint_level >= 2:

        st.markdown(
            """
            <div class="hint-box">

                💡 <b>HINT 2</b>

                <br><br>

                Seriously!! You want the second hint?
                That's bad!! 👀

                <br><br>

                <b>Laptop PIN.</b> 💻

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                margin-top:20px;
                color:#9b7388;
                font-size:16px;
            ">

                Okay... you have used BOTH hints.
                I'm slightly disappointed now. 😑😂

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🚨 I give up — Reveal"):

            st.session_state.show_reveal = True

            st.rerun()

    # ========================================================
    # REVEAL
    # ========================================================

    if st.session_state.show_reveal:

        st.markdown(
            """
            <div class="final-card">

                <div class="big-emoji">
                    🌸✨🌼
                </div>

                <div class="final-title">
                    HAPPY BIRTHDAY, BRIGHTUUUU!!
                </div>

                <div class="final-message">

                    I was going to make you work for it... 😂

                    <br><br>

                    But fine.

                    <br>

                    No password. No clues. No more tests.

                    <br><br>

                    Just have an absolutely wonderful birthday! ✨

                    <br><br>

                    Enjoy your day, birthday boy. 🌸

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ENTRY REACTION
# ============================================================

elif st.session_state.page == "entry_reaction":

    mode = st.session_state.entry_mode

    # --------------------------------------------------------
    # NO HINT
    # --------------------------------------------------------

    if mode == 0:

        st.markdown(
            """
            <div class="glass-card">

                <div class="big-emoji">
                    🌸✨🌸
                </div>

                <div class="reaction">

                    <b>WAITTTT... YOU GOT IT?!</b>

                    <br><br>

                    No hints?!

                    <br>

                    Okayyy... I'm impressed. 👏😂

                    <br><br>

                    That's exactly how I wanted you to enter.

                    <br><br>

                    <b>Welcome, Brightuuuu!! ✨</b>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # ONE HINT
    # --------------------------------------------------------

    elif mode == 1:

        st.markdown(
            """
            <div class="glass-card">

                <div class="big-emoji">
                    🌷✨
                </div>

                <div class="reaction">

                    <b>Okayyy... acceptable.</b>

                    <br><br>

                    You needed one hint.

                    <br>

                    I'll allow it. 😌

                    <br><br>

                    At least you figured it out.

                    <br><br>

                    <b>Welcome, Brightuuuu!! ✨</b>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # TWO HINTS
    # --------------------------------------------------------

    else:

        st.markdown(
            """
            <div class="glass-card">

                <div class="big-emoji">
                    😑🌸😂
                </div>

                <div class="reaction">

                    <b>Seriously, Brightuuuu?</b>

                    <br><br>

                    You used BOTH hints?!

                    <br><br>

                    I literally gave you two clues
                    and you still made me do all the work. 😂

                    <br><br>

                    I'm mildly offended.

                    <br><br>

                    But fine...

                    <br>

                    <b>Welcome. 😌✨</b>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("✨ Continue"):

        st.session_state.page = "welcome"

        st.rerun()


# ============================================================
# WELCOME PAGE
# ============================================================

elif st.session_state.page == "welcome":

    st.markdown(
        """
        <div class="main-title">
            ✨ Welcome Brightuuuu..!! ✨
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass-card">

            <div class="big-emoji">
                🌸✨🌼
            </div>

            <h2 style="
                text-align:center;
                font-family:'Playfair Display', serif;
                color:#66566b;
            ">
                You made it!
            </h2>

            <p style="
                text-align:center;
                color:#756578;
                font-size:20px;
                line-height:1.9;
            ">

                I could have just typed
                <b>"Happy Birthday!"</b>
                and sent it to you.

                <br><br>

                But apparently that was not enough. 😂

                <br><br>

                So I made you something a little different.

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🌍 Let's see it"):

        st.session_state.page = "funny"

        st.rerun()


# ============================================================
# FUNNY INTRO
# ============================================================

elif st.session_state.page == "funny":

    item = funny_messages[
        st.session_state.funny_index
    ]

    st.markdown(
        """
        <div class="subtitle">
            Made with you in mind... 🌸
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="glass-card">

            <div class="big-emoji">
                {item["emoji"]}
            </div>

            <h2 style="
                text-align:center;
                font-family:'Playfair Display', serif;
                color:#66566b;
            ">
                {item["title"]}
            </h2>

            <p style="
                text-align:center;
                font-size:23px;
                color:#756578;
                line-height:1.7;
            ">
                {item["message"]}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.funny_index < len(funny_messages) - 1:

        if st.button("Next 👉"):

            st.session_state.funny_index += 1

            st.rerun()

    else:

        if st.button("🌎 Okay, let's travel"):

            st.session_state.page = "wishes"

            st.rerun()


# ============================================================
# LANGUAGE WISHES
# ============================================================

elif st.session_state.page == "wishes":

    current = wishes[
        st.session_state.wish_index
    ]

    total = len(wishes)
    current_number = st.session_state.wish_index + 1

    st.markdown(
        f"""
        <div class="subtitle">
            🌎 Birthday trip — {current_number} of {total}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # IMPORTANT:
    # Use st.html() instead of markdown so multilingual text
    # is rendered as HTML rather than appearing as code.
    # ========================================================

    wish_html = f"""
    <div class="wish-card">

        <div class="destination">
            📍 {current["place"]}
        </div>

        <div class="wish-language">
            {current["language"]}
        </div>

        <div class="wish-emoji">
            {current["emoji"]}
        </div>

        <div class="wish-text">
            {current["wish"]}
        </div>

        <div class="transliteration">
            {current["translit"]}
        </div>

        <div class="meaning">
            {current["meaning"]}
        </div>

    </div>
    """

    st.html(wish_html)

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================
    # NEXT
    # ========================================================

    if st.session_state.wish_index < len(wishes) - 1:

        if st.button("Next 🌍"):

            st.session_state.wish_index += 1

            st.rerun()

    else:

        if st.button("✨ One last thing..."):

            st.session_state.page = "final_intro"

            st.rerun()


# ============================================================
# FINAL INTRO
# ============================================================

elif st.session_state.page == "final_intro":

    st.markdown(
        """
        <div class="glass-card">

            <div class="big-emoji">
                🌎✨🌸
            </div>

            <div class="reaction">

                <b>And after travelling all this way...</b>

                <br><br>

                I think it's time for the one wish
                that actually matters.

                <br><br>

                <span style="font-size:19px;">
                    No more destinations.
                </span>

                <br>

                <span style="font-size:19px;">
                    Just one birthday wish from me to you.
                </span>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🎂 Open your birthday wish"):

        st.session_state.page = "final"

        st.rerun()


# ============================================================
# FINAL BIRTHDAY MESSAGE
# ============================================================

elif st.session_state.page == "final":

    # ========================================================
    # FLOWER + SHINE CELEBRATION
    # ========================================================

    st.html(
        """
        <div class="celebration">

            <span class="c1">🌸</span>
            <span class="c2">✨</span>
            <span class="c3">🌷</span>
            <span class="c4">✨</span>
            <span class="c5">🌺</span>
            <span class="c6">✨</span>
            <span class="c7">🌼</span>
            <span class="c8">✨</span>
            <span class="c9">🌸</span>
            <span class="c10">🌷</span>

        </div>
        """
    )

    # ========================================================
    # FINAL CARD
    # ========================================================

    st.html(
        """
        <div class="final-card">

            <div class="big-emoji">
                🌸✨🌼
            </div>

            <div class="final-title">
                HAPPY BIRTHDAY, BRIGHTUUUU!!
            </div>

            <div class="final-message">

                I hope your day is filled with
                happiness, laughter, good food,
                good people and lots of little moments
                that make you smile.

                <br><br>

                I hope the year ahead brings you
                wonderful memories, exciting things,
                and plenty of reasons to be happy.

                <br><br>

                Have a really, really wonderful birthday. ✨

                <br><br>

                <b>Enjoy your day, Brightuuuu! 🌸</b>

            </div>

        </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:30px;
            color:#8b758a;
            font-size:16px;
            line-height:1.8;
        ">

            🌸 Some wishes are better left as little memories. ✨

            <br>

            And this one was meant just for you.

        </div>
        """,
        unsafe_allow_html=True
    )
