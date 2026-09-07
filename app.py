import streamlit as st
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For Brightuuuu ❤️",
    page_icon="🎂",
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
# ============================================================
# ORDER:
# 1. South Indian languages
# 2. North Indian languages
# 3. Other countries
# ============================================================

wishes = [

    # ========================================================
    # SOUTH INDIA
    # ========================================================

    {
        "language": "Tamil",
        "wish": "இனிய பிறந்தநாள் வாழ்த்துக்கள்!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌺",
        "theme": "theme-tamil"
    },

    {
        "language": "Telugu",
        "wish": "పుట్టినరోజు శుభాకాంక్షలు!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌼",
        "theme": "theme-telugu"
    },

    {
        "language": "Kannada",
        "wish": "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌿",
        "theme": "theme-karnataka"
    },

    {
        "language": "Malayalam",
        "wish": "ജന്മദിനാശംസകൾ!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌴",
        "theme": "theme-kerala"
    },

    # ========================================================
    # NORTH / OTHER INDIAN LANGUAGES
    # ========================================================

    {
        "language": "Hindi",
        "wish": "जन्मदिन मुबारक हो!",
        "subtitle": "Happy Birthday!",
        "emoji": "🪷",
        "theme": "theme-india"
    },

    {
        "language": "Bengali",
        "wish": "শুভ জন্মদিন!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-bengal"
    },

    {
        "language": "Marathi",
        "wish": "वाढदिवसाच्या हार्दिक शुभेच्छा!",
        "subtitle": "Heartfelt birthday wishes!",
        "emoji": "🪔",
        "theme": "theme-marathi"
    },

    {
        "language": "Punjabi",
        "wish": "ਜਨਮਦਿਨ ਮੁਬਾਰਕ!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-punjab"
    },

    {
        "language": "Gujarati",
        "wish": "જન્મદિવસની શુભકામનાઓ!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌼",
        "theme": "theme-gujarat"
    },

    # ========================================================
    # OTHER COUNTRIES
    # ========================================================

    {
        "language": "English",
        "wish": "Happy Birthday!",
        "subtitle": "Wishing you a wonderful birthday!",
        "emoji": "🎂",
        "theme": "theme-birthday"
    },

    {
        "language": "French",
        "wish": "Joyeux anniversaire !",
        "subtitle": "Happy Birthday!",
        "emoji": "🌷",
        "theme": "theme-paris"
    },

    {
        "language": "Japanese",
        "wish": "お誕生日おめでとう！",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-japan"
    },

    {
        "language": "Korean",
        "wish": "생일 축하해요!",
        "subtitle": "Happy Birthday!",
        "emoji": "✨",
        "theme": "theme-korea"
    },

    {
        "language": "Spanish",
        "wish": "¡Feliz cumpleaños!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌺",
        "theme": "theme-fiesta"
    },

    {
        "language": "Italian",
        "wish": "Buon compleanno!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌷",
        "theme": "theme-italy"
    },

    {
        "language": "German",
        "wish": "Alles Gute zum Geburtstag!",
        "subtitle": "All the best for your birthday!",
        "emoji": "🌼",
        "theme": "theme-germany"
    },

    {
        "language": "Portuguese",
        "wish": "Feliz aniversário!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌊",
        "theme": "theme-portugal"
    },

    {
        "language": "Chinese",
        "wish": "生日快乐！",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-china"
    },

    {
        "language": "Arabic",
        "wish": "عيد ميلاد سعيد!",
        "subtitle": "Happy Birthday!",
        "emoji": "✨",
        "theme": "theme-arabic"
    },

    {
        "language": "Turkish",
        "wish": "Doğum günün kutlu olsun!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌷",
        "theme": "theme-turkey"
    },

    {
        "language": "Russian",
        "wish": "С днём рождения!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-russia"
    },

    {
        "language": "Greek",
        "wish": "Χρόνια πολλά!",
        "subtitle": "Many happy returns!",
        "emoji": "🌼",
        "theme": "theme-greece"
    },

    {
        "language": "Dutch",
        "wish": "Gefeliciteerd met je verjaardag!",
        "subtitle": "Congratulations on your birthday!",
        "emoji": "🌷",
        "theme": "theme-netherlands"
    },

    {
        "language": "Swedish",
        "wish": "Grattis på födelsedagen!",
        "subtitle": "Happy Birthday!",
        "emoji": "✨",
        "theme": "theme-sweden"
    },

    {
        "language": "Thai",
        "wish": "สุขสันต์วันเกิด!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌺",
        "theme": "theme-thailand"
    },

    {
        "language": "Vietnamese",
        "wish": "Chúc mừng sinh nhật!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌸",
        "theme": "theme-vietnam"
    },

    {
        "language": "Indonesian",
        "wish": "Selamat ulang tahun!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌴",
        "theme": "theme-indonesia"
    },

    {
        "language": "Filipino",
        "wish": "Maligayang kaarawan!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌺",
        "theme": "theme-philippines"
    },

    {
        "language": "Latin",
        "wish": "Felix natalis!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌿",
        "theme": "theme-latin"
    },

    {
        "language": "Irish",
        "wish": "Lá breithe sona duit!",
        "subtitle": "Happy Birthday!",
        "emoji": "🌿",
        "theme": "theme-ireland"
    }
]


# ============================================================
# FUNNY INTRO MESSAGES
# ============================================================

funny_messages = [

    {
        "emoji": "😂",
        "title": "First things first...",
        "message": "I could have simply wished you Happy Birthday."
    },

    {
        "emoji": "🤦‍♀️",
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
        "emoji": "❤️",
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

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Quicksand:wght@400;500;600;700&family=Satisfy&display=swap');

* {
    font-family: 'Quicksand', sans-serif;
}


/* =========================================================
   VIBRANT BACKGROUND
   ========================================================= */

.stApp {

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(255, 120, 180, 0.42),
            transparent 27%
        ),

        radial-gradient(
            circle at 95% 8%,
            rgba(100, 180, 255, 0.38),
            transparent 28%
        ),

        radial-gradient(
            circle at 15% 55%,
            rgba(190, 130, 255, 0.35),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 50%,
            rgba(90, 220, 190, 0.25),
            transparent 30%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(255, 175, 100, 0.30),
            transparent 35%
        ),

        linear-gradient(
            135deg,
            #170026,
            #250038,
            #12002b,
            #061c35
        );

    background-attachment: fixed;

    color: white;
}


/* =========================================================
   HIDE STREAMLIT DEFAULTS
   ========================================================= */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =========================================================
   MAIN CONTAINER
   ========================================================= */

.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* =========================================================
   FLOATING FLOWERS + SHINES ONLY
   ========================================================= */

.float {
    position: fixed;

    bottom: -60px;

    font-size: 25px;

    opacity: 0;

    pointer-events: none;

    z-index: 0;

    animation:
        floatUp 10s linear infinite;
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
        opacity: 0.75;
    }

    50% {
        transform:
            translateY(-55vh)
            rotate(180deg)
            scale(1.1);

        opacity: 0.8;
    }

    88% {
        opacity: 0.65;
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
            #ff9fd2,
            #ffd59a,
            #a8dfff,
            #d6a7ff,
            #ff9fd2
        );

    background-size: 300% auto;

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    animation:
        titleGradient 5s linear infinite;

    margin-bottom: 8px;
}

@keyframes titleGradient {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 300% center;
    }
}


/* =========================================================
   SUBTITLE
   ========================================================= */

.subtitle {

    text-align: center;

    color: #f6d8ed;

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
            rgba(255,255,255,0.12),
            rgba(255,255,255,0.055)
        );

    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 30px;

    padding: 38px;

    backdrop-filter: blur(18px);

    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 10px 45px rgba(0,0,0,0.35),
        0 0 35px rgba(180,100,255,0.10);

    animation:
        cardIn 0.7s ease;
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

    font-size: 70px;

    margin-bottom: 12px;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {

    width: 100%;

    border: 1px solid rgba(255,255,255,0.16);

    border-radius: 18px;

    padding: 13px 20px;

    font-size: 18px;

    font-weight: 700;

    color: white;

    background:
        linear-gradient(
            90deg,
            #d86aa9,
            #9567d9,
            #5e9edc
        );

    box-shadow:
        0 7px 25px rgba(160,80,190,0.28);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 35px rgba(200,100,220,0.40);
}


/* =========================================================
   TEXT INPUT
   ========================================================= */

.stTextInput input {

    background:
        rgba(255,255,255,0.10) !important;

    color: white !important;

    border:
        1px solid rgba(255,255,255,0.25) !important;

    border-radius: 16px !important;

    text-align: center !important;

    font-size: 21px !important;

    font-family:
        'Quicksand',
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
        rgba(255,210,120,0.11);

    border:
        1px solid rgba(255,220,150,0.28);

    color: #ffe8bd;

    animation:
        cardIn 0.5s ease;
}


/* =========================================================
   REACTION
   ========================================================= */

.reaction {

    text-align: center;

    font-size: 24px;

    line-height: 1.7;

    padding: 25px;

    color: #ffe8f7;
}


/* =========================================================
   WISH CARD
   ========================================================= */

.wish-card {

    min-height: 430px;

    border-radius: 35px;

    padding: 55px 30px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    border:
        1px solid rgba(255,255,255,0.22);

    background:
        linear-gradient(
            135deg,
            rgba(255,120,190,0.20),
            rgba(125,100,230,0.18),
            rgba(90,180,230,0.15)
        );

    box-shadow:
        0 15px 50px rgba(0,0,0,0.35),
        0 0 40px rgba(255,130,200,0.12);

    animation:
        wishAppear 0.75s ease;
}


/* =========================================================
   WISH ANIMATION
   ========================================================= */

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
   DESTINATION
   ========================================================= */

.destination {

    font-family:
        'Quicksand',
        sans-serif;

    font-size: 15px;

    text-transform: uppercase;

    letter-spacing: 4px;

    color: #f5c9e8;

    margin-bottom: 28px;
}


/* =========================================================
   WISH EMOJI
   ========================================================= */

.wish-emoji {

    font-size: 78px;

    margin-bottom: 25px;

    animation:
        emojiFloat 2.5s ease-in-out infinite;
}

@keyframes emojiFloat {

    0%, 100% {
        transform:
            translateY(0);
    }

    50% {
        transform:
            translateY(-10px);
    }
}


/* =========================================================
   WISH LANGUAGE
   ========================================================= */

.wish-language {

    font-family:
        'Quicksand',
        sans-serif;

    font-size: 19px;

    color: #f9c9e8;

    margin-bottom: 14px;

    font-weight: 600;
}


/* =========================================================
   WISH TEXT
   IMPORTANT:
   This is deliberately plain HTML text.
   No code formatting.
   ========================================================= */

.wish-text {

    font-family:
        'Playfair Display',
        serif;

    font-size: 36px;

    font-weight: 700;

    color: #ffffff;

    text-shadow:
        0 0 18px rgba(255,130,205,0.45);

    margin-bottom: 20px;

    line-height: 1.5;

    word-break: normal;

    white-space: normal;
}


/* =========================================================
   WISH SUBTITLE
   ========================================================= */

.wish-subtitle {

    font-family:
        'Quicksand',
        sans-serif;

    font-size: 20px;

    color: #f7ddeb;

    font-style: italic;
}


/* =========================================================
   FINAL CARD
   ========================================================= */

.final-card {

    text-align: center;

    padding: 50px 30px;

    border-radius: 32px;

    background:
        linear-gradient(
            135deg,
            rgba(255,120,190,0.18),
            rgba(90,180,235,0.13),
            rgba(165,105,230,0.20)
        );

    border:
        1px solid rgba(255,255,255,0.22);

    box-shadow:
        0 0 50px rgba(255,120,200,0.18);
}


/* =========================================================
   FINAL TITLE
   ========================================================= */

.final-title {

    font-family:
        'Playfair Display',
        serif;

    font-size: 42px;

    font-weight: 700;

    margin-bottom: 20px;

    animation:
        finalGlow 1.8s ease-in-out infinite alternate;
}

@keyframes finalGlow {

    from {
        text-shadow:
            0 0 8px rgba(255,140,205,0.45);
    }

    to {
        text-shadow:
            0 0 20px rgba(255,140,205,0.75),
            0 0 45px rgba(160,110,230,0.50);
    }
}


/* =========================================================
   FINAL MESSAGE
   ========================================================= */

.final-message {

    font-family:
        'Quicksand',
        sans-serif;

    font-size: 19px;

    line-height: 1.9;

    color: #ffe9f7;
}


/* =========================================================
   FINAL FLOWER + SHINE SHOWER
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

    font-size: 26px;

    opacity: 0;

    animation:
        celebrationFall 5s linear infinite;
}

.c1 { left: 4%;  animation-delay: 0s; }
.c2 { left: 13%; animation-delay: 0.7s; }
.c3 { left: 23%; animation-delay: 1.5s; }
.c4 { left: 34%; animation-delay: 0.3s; }
.c5 { left: 45%; animation-delay: 1.9s; }
.c6 { left: 57%; animation-delay: 0.9s; }
.c7 { left: 68%; animation-delay: 2.2s; }
.c8 { left: 78%; animation-delay: 1.2s; }
.c9 { left: 88%; animation-delay: 2.7s; }
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

        opacity: 0.85;
    }

    85% {
        opacity: 0.7;
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
        font-size: 27px;
    }

    .wish-card {
        min-height: 390px;
        padding: 35px 20px;
    }

    .glass-card {
        padding: 28px 20px;
    }

}

</style>

<!-- ONLY FLOWERS AND SHINES FLOATING -->

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
        🎂🌸✨
        </div>

        <h2 style="
            text-align:center;
            font-family:'Playfair Display', serif;
        ">
        Hey Brightuuuu..!!
        </h2>

        <p style="
            text-align:center;
            color:#ffe1f3;
            font-size:18px;
            line-height:1.8;
        ">

        Before you enter, there's just one tiny problem...
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

            st.session_state.entry_mode = (
                st.session_state.hint_level
            )

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

            It contains exactly <b>2 letters/characters</b>
            and <b>8 digits</b>.

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

            Seriously!! You want the second hint. Thats bad!!. 👀

            <b> Laptop PIN.</b> 💻

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                margin-top:20px;
                color:#ffb6d9;
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
            🎂🌸✨
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

            Just have an absolutely wonderful birthday! ❤️

            <br><br>

            Enjoy your day, birthday boy. 🎂✨

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
            🎉🥳🎉
            </div>

            <div class="reaction">

            <b>WAITTTT... YOU GOT IT?!</b>

            <br><br>

            No hints?!

            <br>

            Okayyy... I'm impressed. 👏😂

            <span style="font-size:19px;">
            That's exactly how I wanted you to enter.
            </span>

            <br><br>

            <b>Welcome, Brightuuuu!! ❤️</b>

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
            😌✨
            </div>

            <div class="reaction">

            <b>Okayyy... acceptable.</b>

            <br><br>

            You needed one hint.

            I'll allow it. 😌

            At least you figured it out.

            <br><br>

            <b>Welcome, Brightuuuu!! ❤️</b>

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
            😑👉😂
            </div>

            <div class="reaction">

            <b>Seriously, Brightuuuu?</b>

            <br><br>

            You used BOTH hints?!

            I literally gave you two clues
            and you still made me do all the work. 😂

            I'm mildly offended.

            But fine...

            <br>

            <b>Welcome. 😌❤️</b>

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
        🥳🎂✨
        </div>

        <h2 style="
            text-align:center;
            font-family:'Playfair Display', serif;
        ">
        You made it!
        </h2>

        <p style="
            text-align:center;
            color:#ffe4f4;
            font-size:20px;
            line-height:1.9;
        ">

        I could have just typed "Happy Birthday!" and sent it to you.

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
        Made with you in mind...
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
        ">
        {item["title"]}
        </h2>

        <p style="
            text-align:center;
            font-size:23px;
            color:#ffe8f6;
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

    # --------------------------------------------------------
    # SUBTITLE
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="subtitle">
        🌎 A little birthday trip begins...
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # LANGUAGE-SPECIFIC BACKGROUNDS
    # --------------------------------------------------------

    backgrounds = {

        "Tamil":
            "linear-gradient(135deg, #ff512f, #dd2476, #ff9966)",

        "Telugu":
            "linear-gradient(135deg, #ff8008, #ffc837, #ff5f6d)",

        "Kannada":
            "linear-gradient(135deg, #11998e, #38ef7d)",

        "Malayalam":
            "linear-gradient(135deg, #00b09b, #96c93d)",

        "Hindi":
            "linear-gradient(135deg, #f12711, #f5af19)",

        "Bengali":
            "linear-gradient(135deg, #c33764, #1d2671)",

        "Marathi":
            "linear-gradient(135deg, #ee0979, #ff6a00)",

        "Punjabi":
            "linear-gradient(135deg, #f7971e, #ffd200)",

        "Gujarati":
            "linear-gradient(135deg, #8e2de2, #4a00e0)",

        "English":
            "linear-gradient(135deg, #fc466b, #3f5efb, #00c6ff)",

        "French":
            "linear-gradient(135deg, #a18cd1, #fbc2eb)",

        "Japanese":
            "linear-gradient(135deg, #ff9a9e, #fad0c4)",

        "Korean":
            "linear-gradient(135deg, #667eea, #764ba2)",

        "Spanish":
            "linear-gradient(135deg, #ff416c, #ff4b2b)",

        "Italian":
            "linear-gradient(135deg, #56ab2f, #a8e063)",

        "German":
            "linear-gradient(135deg, #232526, #414345, #f7971e)",

        "Portuguese":
            "linear-gradient(135deg, #00c6ff, #0072ff)",

        "Chinese":
            "linear-gradient(135deg, #ff0844, #ffb199)",

        "Arabic":
            "linear-gradient(135deg, #141e30, #243b55)",

        "Turkish":
            "linear-gradient(135deg, #ed213a, #93291e)",

        "Russian":
            "linear-gradient(135deg, #2193b0, #6dd5ed)",

        "Greek":
            "linear-gradient(135deg, #36d1dc, #5b86e5)",

        "Dutch":
            "linear-gradient(135deg, #f953c6, #b91d73)",

        "Swedish":
            "linear-gradient(135deg, #4facfe, #00f2fe)",

        "Thai":
            "linear-gradient(135deg, #ff758c, #ff7eb3)",

        "Vietnamese":
            "linear-gradient(135deg, #f83600, #f9d423)",

        "Indonesian":
            "linear-gradient(135deg, #00b09b, #96c93d)",

        "Filipino":
            "linear-gradient(135deg, #12c2e9, #c471ed)",

        "Latin":
            "linear-gradient(135deg, #8360c3, #2ebf91)",

        "Irish":
            "linear-gradient(135deg, #11998e, #38ef7d)"
    }

    background = backgrounds.get(
        current["language"],
        "linear-gradient(135deg, #667eea, #764ba2)"
    )

    # --------------------------------------------------------
    # IMPORTANT:
    # USE st.html() FOR THIS CARD.
    # This prevents Streamlit Cloud from displaying the HTML
    # source instead of rendering it.
    # --------------------------------------------------------

    st.html(
        f"""
        <style>

        .birthday-wish-card {{
            min-height: 430px;

            border-radius: 35px;

            padding: 55px 30px;

            display: flex;

            flex-direction: column;

            justify-content: center;

            align-items: center;

            text-align: center;

            border: 1px solid rgba(255,255,255,0.30);

            background: {background};

            box-shadow:
                0 20px 60px rgba(0,0,0,0.35),
                0 0 45px rgba(255,130,200,0.18);

            animation:
                birthdayWishAppear 0.75s ease;

            position: relative;

            overflow: hidden;

            box-sizing: border-box;
        }}


        .birthday-wish-card::before {{

            content: "";

            position: absolute;

            width: 250px;

            height: 250px;

            border-radius: 50%;

            background: rgba(255,255,255,0.13);

            filter: blur(12px);

            top: -130px;

            right: -100px;
        }}


        .birthday-wish-card::after {{

            content: "";

            position: absolute;

            width: 200px;

            height: 200px;

            border-radius: 50%;

            background: rgba(255,255,255,0.10);

            filter: blur(12px);

            bottom: -100px;

            left: -80px;
        }}


        .birthday-destination {{

            font-family:
                'Quicksand',
                'Noto Sans',
                sans-serif;

            font-size: 14px;

            font-weight: 600;

            letter-spacing: 4px;

            text-transform: uppercase;

            color: rgba(255,255,255,0.82);

            margin-bottom: 22px;

            position: relative;

            z-index: 2;
        }}


        .birthday-language {{

            font-family:
                'Quicksand',
                'Noto Sans',
                sans-serif;

            font-size: 20px;

            font-weight: 700;

            color: rgba(255,255,255,0.95);

            margin-bottom: 22px;

            position: relative;

            z-index: 2;
        }}


        .birthday-wish-emoji {{

            font-size: 76px;

            line-height: 1;

            margin-bottom: 28px;

            position: relative;

            z-index: 2;

            animation:
                birthdayEmojiFloat 2.5s ease-in-out infinite;
        }}


        .birthday-wish-text {{

            font-family:
                'Noto Sans',
                'Noto Sans Devanagari',
                'Noto Sans Telugu',
                'Noto Sans Kannada',
                'Noto Sans Malayalam',
                'Noto Sans Bengali',
                'Noto Sans Tamil',
                sans-serif;

            font-size: 36px;

            font-weight: 800;

            line-height: 1.55;

            color: white;

            text-shadow:
                0 4px 20px rgba(0,0,0,0.25);

            margin-bottom: 22px;

            position: relative;

            z-index: 2;

            word-break: normal;

            white-space: normal;
        }}


        .birthday-wish-subtitle {{

            font-family:
                'Quicksand',
                sans-serif;

            font-size: 20px;

            font-style: italic;

            color: rgba(255,255,255,0.92);

            position: relative;

            z-index: 2;
        }}


        @keyframes birthdayWishAppear {{

            0% {{

                opacity: 0;

                transform:
                    scale(0.85)
                    translateY(25px);
            }}

            100% {{

                opacity: 1;

                transform:
                    scale(1)
                    translateY(0);
            }}
        }}


        @keyframes birthdayEmojiFloat {{

            0%, 100% {{

                transform:
                    translateY(0)
                    rotate(-3deg);
            }}

            50% {{

                transform:
                    translateY(-10px)
                    rotate(3deg);
            }}
        }}


        @media (max-width: 600px) {{

            .birthday-wish-card {{

                min-height: 390px;

                padding: 40px 18px;
            }}

            .birthday-wish-text {{

                font-size: 27px;

                line-height: 1.55;
            }}

            .birthday-wish-emoji {{

                font-size: 62px;
            }}

            .birthday-language {{

                font-size: 18px;
            }}

        }}

        </style>


        <div class="birthday-wish-card">

            <div class="birthday-destination">
                🌍 DESTINATION
            </div>

            <div class="birthday-language">
                {current["language"]}
            </div>

            <div class="birthday-wish-emoji">
                {current["emoji"]}
            </div>

            <div class="birthday-wish-text">
                {current["wish"]}
            </div>

            <div class="birthday-wish-subtitle">
                {current["subtitle"]}
            </div>

        </div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # NEXT BUTTON
    # --------------------------------------------------------

    if st.session_state.wish_index < len(wishes) - 1:

        if st.button("Next 🌍"):

            st.session_state.wish_index += 1

            st.rerun()

    else:

        if st.button("✨ One last thing..."):

            st.session_state.page = "final_intro"

            st.rerun()


    # # ========================================================
    # # IMPORTANT:
    # # The multilingual text is rendered directly as HTML.
    # # It is NOT placed inside a code block.
    # # ========================================================

    # st.markdown(
    #     f"""
    #     <div class="wish-card {current["theme"]}">

    #         <div class="destination">
    #             🌍 DESTINATION
    #         </div>

    #         <div class="wish-language">
    #             {current["language"]}
    #         </div>

    #         <div class="wish-emoji">
    #             {current["emoji"]}
    #         </div>

    #         <div class="wish-text">
    #             {current["wish"]}
    #         </div>

    #         <div class="wish-subtitle">
    #             {current["subtitle"]}
    #         </div>

    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )


    # st.markdown("<br>", unsafe_allow_html=True)


    # # ========================================================
    # # NEXT
    # # ========================================================

    # if st.session_state.wish_index < len(wishes) - 1:

    #     if st.button("Next 🌍"):

    #         st.session_state.wish_index += 1

    #         st.rerun()

    # else:

    #     if st.button("✨ One last thing..."):

    #         st.session_state.page = "final_intro"

    #         st.rerun()


# ============================================================
# FINAL INTRO
# ============================================================

elif st.session_state.page == "final_intro":

    st.markdown(
        """
        <div class="glass-card">

        <div class="big-emoji">
        🌎✨❤️
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
    # NEW CELEBRATION:
    # FLOWERS + SHINES INSTEAD OF BALLOONS
    # ========================================================

    st.markdown(
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
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="final-card">

        <div class="big-emoji">
        🎂🌸✨
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

        Have a really, really wonderful birthday. ❤️

        <br><br>

        <b>Enjoy your day, Brightuuuu! 🎂✨</b>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================================
    # NO "ALL WISHES TOGETHER" SECTION
    # ========================================================

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:30px;
            color:#f2c9e2;
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
