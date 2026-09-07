# import streamlit as st

# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="A Birthday Surprise for Brightuuuu",
#     page_icon="🎂",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # ============================================================
# # SECRET PASSWORD
# # ============================================================

# PASSWORD = "T20080209S"

# # ============================================================
# # SESSION STATE
# # ============================================================

# defaults = {
#     "page": "password",
#     "hint_level": 0,
#     "password_attempts": 0,
#     "entry_mode": None,
#     "show_reveal": False,
#     "funny_index": 0,
#     "wish_index": 0
# }

# for key, value in defaults.items():
#     if key not in st.session_state:
#         st.session_state[key] = value


# # ============================================================
# # FUNNY INTRO MESSAGES
# # ============================================================

# funny_messages = [
#     (
#         "😂",
#         "First things first...",
#         "I could have wished you normally."
#     ),
#     (
#         "🤦‍♀️",
#         "But then I thought...",
#         "Where's the fun in being normal?"
#     ),
#     (
#         "🌍",
#         "So I had an idea...",
#     ),
#     (
#         "🌸",
#         "Just enjoy the little surprise.",
#         "You deserve a nice birthday."
#     ),
#     (
#         "🎂",
#         "Okay...",
#         "Let's begin."
#     )
# ]


# # ============================================================
# # LANGUAGE WISHES
# # ============================================================

# wishes = [

#     {
#         "language": "Tamil",
#         "wish": "இனிய பிறந்தநாள் வாழ்த்துக்கள்!",
#         "english": "Happy Birthday!",
#         "emoji": "🌺",
#         "background": "linear-gradient(135deg, #ff512f, #dd2476, #ff9966)"
#     },

#     {
#         "language": "Telugu",
#         "wish": "పుట్టినరోజు శుభాకాంక్షలు!",
#         "english": "Happy Birthday!",
#         "emoji": "🌼",
#         "background": "linear-gradient(135deg, #ff8008, #ffc837, #ff5f6d)"
#     },

#     {
#         "language": "Kannada",
#         "wish": "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು!",
#         "english": "Happy Birthday!",
#         "emoji": "🌿",
#         "background": "linear-gradient(135deg, #11998e, #38ef7d, #a8e063)"
#     },

#     {
#         "language": "Malayalam",
#         "wish": "ജന്മദിനാശംസകൾ!",
#         "english": "Happy Birthday!",
#         "emoji": "🌴",
#         "background": "linear-gradient(135deg, #00b09b, #96c93d, #00c9a7)"
#     },

#     {
#         "language": "Hindi",
#         "wish": "जन्मदिन मुबारक हो!",
#         "english": "Happy Birthday!",
#         "emoji": "🪷",
#         "background": "linear-gradient(135deg, #f12711, #f5af19, #ff512f)"
#     },

#     {
#         "language": "Bengali",
#         "wish": "শুভ জন্মদিন!",
#         "english": "Happy Birthday!",
#         "emoji": "🌸",
#         "background": "linear-gradient(135deg, #c33764, #1d2671, #6a3093)"
#     },

#     {
#         "language": "Marathi",
#         "wish": "वाढदिवसाच्या हार्दिक शुभेच्छा!",
#         "english": "Heartfelt birthday wishes!",
#         "emoji": "🌻",
#         "background": "linear-gradient(135deg, #ee0979, #ff6a00, #f7971e)"
#     },

#     {
#         "language": "Punjabi",
#         "wish": "ਜਨਮਦਿਨ ਮੁਬਾਰਕ!",
#         "english": "Happy Birthday!",
#         "emoji": "🌼",
#         "background": "linear-gradient(135deg, #f7971e, #ffd200, #ff512f)"
#     },

#     {
#         "language": "Gujarati",
#         "wish": "જન્મદિવસની શુભેચ્છાઓ!",
#         "english": "Happy Birthday!",
#         "emoji": "🌺",
#         "background": "linear-gradient(135deg, #8e2de2, #4a00e0, #ff00cc)"
#     },

#     {
#         "language": "English",
#         "wish": "Happy Birthday!",
#         "english": "Wishing you a wonderful birthday!",
#         "emoji": "🎂",
#         "background": "linear-gradient(135deg, #fc466b, #3f5efb, #00c6ff)"
#     },

#     {
#         "language": "French",
#         "wish": "Joyeux anniversaire !",
#         "english": "Happy Birthday!",
#         "emoji": "🌷",
#         "background": "linear-gradient(135deg, #a18cd1, #fbc2eb, #fad0c4)"
#     },

#     {
#         "language": "Spanish",
#         "wish": "¡Feliz cumpleaños!",
#         "english": "Happy Birthday!",
#         "emoji": "🌺",
#         "background": "linear-gradient(135deg, #ff416c, #ff4b2b, #ff9068)"
#     },

#     {
#         "language": "Italian",
#         "wish": "Buon compleanno!",
#         "english": "Happy Birthday!",
#         "emoji": "🌿",
#         "background": "linear-gradient(135deg, #56ab2f, #a8e063, #11998e)"
#     },

#     {
#         "language": "German",
#         "wish": "Alles Gute zum Geburtstag!",
#         "english": "All the best for your birthday!",
#         "emoji": "🌼",
#         "background": "linear-gradient(135deg, #232526, #414345, #f7971e)"
#     },

#     {
#         "language": "Portuguese",
#         "wish": "Feliz aniversário!",
#         "english": "Happy Birthday!",
#         "emoji": "🌊",
#         "background": "linear-gradient(135deg, #00c6ff, #0072ff, #00f2fe)"
#     },

#     {
#         "language": "Chinese",
#         "wish": "生日快乐！",
#         "english": "Happy Birthday!",
#         "emoji": "🌸",
#         "background": "linear-gradient(135deg, #ff0844, #ffb199, #ff416c)"
#     },

#     {
#         "language": "Japanese",
#         "wish": "お誕生日おめでとう！",
#         "english": "Happy Birthday!",
#         "emoji": "🌸",
#         "background": "linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb)"
#     },

#     {
#         "language": "Korean",
#         "wish": "생일 축하해요!",
#         "english": "Happy Birthday!",
#         "emoji": "✨",
#         "background": "linear-gradient(135deg, #667eea, #764ba2, #a18cd1)"
#     },

#     {
#         "language": "Arabic",
#         "wish": "عيد ميلاد سعيد!",
#         "english": "Happy Birthday!",
#         "emoji": "🌙",
#         "background": "linear-gradient(135deg, #141e30, #243b55, #8360c3)"
#     },

#     {
#         "language": "Turkish",
#         "wish": "Doğum günün kutlu olsun!",
#         "english": "Happy Birthday!",
#         "emoji": "🌷",
#         "background": "linear-gradient(135deg, #ed213a, #93291e, #ff416c)"
#     },

#     {
#         "language": "Russian",
#         "wish": "С днём рождения!",
#         "english": "Happy Birthday!",
#         "emoji": "❄️",
#         "background": "linear-gradient(135deg, #2193b0, #6dd5ed, #7f7fd5)"
#     },

#     {
#         "language": "Greek",
#         "wish": "Χρόνια πολλά!",
#         "english": "Many happy returns!",
#         "emoji": "🌊",
#         "background": "linear-gradient(135deg, #36d1dc, #5b86e5, #00c6ff)"
#     },

#     {
#         "language": "Dutch",
#         "wish": "Gefeliciteerd met je verjaardag!",
#         "english": "Congratulations on your birthday!",
#         "emoji": "🌷",
#         "background": "linear-gradient(135deg, #f953c6, #b91d73, #ff6a88)"
#     },

#     {
#         "language": "Swedish",
#         "wish": "Grattis på födelsedagen!",
#         "english": "Happy Birthday!",
#         "emoji": "✨",
#         "background": "linear-gradient(135deg, #4facfe, #00f2fe, #43e97b)"
#     },

#     {
#         "language": "Thai",
#         "wish": "สุขสันต์วันเกิด!",
#         "english": "Happy Birthday!",
#         "emoji": "🌺",
#         "background": "linear-gradient(135deg, #ff758c, #ff7eb3, #fa709a)"
#     },

#     {
#         "language": "Vietnamese",
#         "wish": "Chúc mừng sinh nhật!",
#         "english": "Happy Birthday!",
#         "emoji": "🌸",
#         "background": "linear-gradient(135deg, #f83600, #f9d423, #ff8008)"
#     },

#     {
#         "language": "Indonesian",
#         "wish": "Selamat ulang tahun!",
#         "english": "Happy Birthday!",
#         "emoji": "🌴",
#         "background": "linear-gradient(135deg, #00b09b, #96c93d, #38ef7d)"
#     },

#     {
#         "language": "Filipino",
#         "wish": "Maligayang kaarawan!",
#         "english": "Happy Birthday!",
#         "emoji": "🌼",
#         "background": "linear-gradient(135deg, #12c2e9, #c471ed, #f64f59)"
#     },

#     {
#         "language": "Irish",
#         "wish": "Lá breithe sona duit!",
#         "english": "Happy Birthday!",
#         "emoji": "☘️",
#         "background": "linear-gradient(135deg, #11998e, #38ef7d, #00c9a7)"
#     }
# ]


# # ============================================================
# # GLOBAL CSS
# # ============================================================

# st.markdown(
#     """
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700;800&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Noto Sans', sans-serif;
# }

# .stApp {
#     min-height: 100vh;

#     background:
#         radial-gradient(
#             circle at 10% 10%,
#             rgba(255, 0, 128, 0.55),
#             transparent 28%
#         ),
#         radial-gradient(
#             circle at 90% 15%,
#             rgba(0, 220, 255, 0.45),
#             transparent 30%
#         ),
#         radial-gradient(
#             circle at 50% 55%,
#             rgba(255, 190, 0, 0.30),
#             transparent 32%
#         ),
#         radial-gradient(
#             circle at 80% 90%,
#             rgba(150, 0, 255, 0.45),
#             transparent 30%
#         ),
#         linear-gradient(
#             135deg,
#             #ff006e 0%,
#             #8338ec 35%,
#             #3a86ff 65%,
#             #06d6a0 100%
#         );

#     background-attachment: fixed;
#     color: white;
#     overflow-x: hidden;
# }

# /* Hide Streamlit chrome */

# #MainMenu {
#     visibility: hidden;
# }

# header {
#     visibility: hidden;
# }

# footer {
#     visibility: hidden;
# }

# .block-container {
#     max-width: 900px;
#     padding-top: 2.5rem;
#     padding-bottom: 4rem;
# }

# /* Floating decoration */

# .floating {
#     position: fixed;
#     bottom: -60px;
#     pointer-events: none;
#     z-index: 0;
#     animation: floatUp 10s linear infinite;
#     opacity: 0.75;
# }

# .float1 {
#     left: 6%;
#     font-size: 27px;
#     animation-delay: 0s;
# }

# .float2 {
#     left: 20%;
#     font-size: 20px;
#     animation-delay: 2s;
# }

# .float3 {
#     left: 38%;
#     font-size: 25px;
#     animation-delay: 4s;
# }

# .float4 {
#     left: 57%;
#     font-size: 22px;
#     animation-delay: 1s;
# }

# .float5 {
#     left: 75%;
#     font-size: 28px;
#     animation-delay: 3s;
# }

# .float6 {
#     left: 91%;
#     font-size: 20px;
#     animation-delay: 5s;
# }

# @keyframes floatUp {

#     0% {
#         transform:
#             translateY(0)
#             rotate(0deg)
#             scale(0.7);
#         opacity: 0;
#     }

#     15% {
#         opacity: 0.8;
#     }

#     80% {
#         opacity: 0.8;
#     }

#     100% {
#         transform:
#             translateY(-115vh)
#             rotate(360deg)
#             scale(1.15);
#         opacity: 0;
#     }
# }

# /* Main title */

# .main-title {
#     font-family: 'Playfair Display', serif;
#     text-align: center;
#     font-size: 48px;
#     font-weight: 800;
#     color: white;
#     text-shadow: 0 4px 18px rgba(0,0,0,0.25);
#     margin-bottom: 8px;
# }

# .subtitle {
#     text-align: center;
#     font-size: 18px;
#     color: rgba(255,255,255,0.92);
#     margin-bottom: 30px;
# }

# /* Glass card */

# .glass-card {
#     background: rgba(255,255,255,0.16);
#     border: 1px solid rgba(255,255,255,0.32);
#     border-radius: 30px;
#     padding: 40px 32px;

#     backdrop-filter: blur(18px);
#     -webkit-backdrop-filter: blur(18px);

#     box-shadow: 0 20px 60px rgba(0,0,0,0.20);

#     animation: cardIn 0.65s ease;
# }

# @keyframes cardIn {

#     from {
#         opacity: 0;
#         transform:
#             translateY(25px)
#             scale(0.97);
#     }

#     to {
#         opacity: 1;
#         transform:
#             translateY(0)
#             scale(1);
#     }
# }

# /* Emoji */

# .big-emoji {
#     text-align: center;
#     font-size: 72px;
#     margin-bottom: 12px;

#     animation:
#         gentleFloat 2.8s ease-in-out infinite;
# }

# @keyframes gentleFloat {

#     0%, 100% {
#         transform: translateY(0);
#     }

#     50% {
#         transform: translateY(-9px);
#     }
# }

# /* Password input */

# .stTextInput input {
#     background: rgba(255,255,255,0.18) !important;
#     color: white !important;

#     border:
#         1px solid rgba(255,255,255,0.40) !important;

#     border-radius: 17px !important;

#     text-align: center !important;

#     font-size: 20px !important;
# }

# .stTextInput input::placeholder {
#     color: rgba(255,255,255,0.70) !important;
# }

# /* Buttons */

# .stButton > button {
#     width: 100%;

#     border: none;
#     border-radius: 18px;

#     padding: 13px 20px;

#     font-size: 18px;
#     font-weight: 700;

#     color: white;

#     background:
#         linear-gradient(
#             90deg,
#             #ff006e,
#             #8338ec,
#             #3a86ff
#         );

#     box-shadow:
#         0 8px 25px rgba(70,0,160,0.30);

#     transition:
#         all 0.25s ease;
# }

# .stButton > button:hover {
#     transform:
#         translateY(-3px)
#         scale(1.01);

#     box-shadow:
#         0 12px 32px rgba(255,0,110,0.40);
# }

# /* Hint */

# .hint-box {
#     margin-top: 18px;

#     padding: 20px;

#     border-radius: 20px;

#     text-align: center;

#     background:
#         linear-gradient(
#             135deg,
#             rgba(255,215,0,0.25),
#             rgba(255,105,180,0.18)
#         );

#     border:
#         1px solid rgba(255,235,150,0.45);

#     color: white;

#     box-shadow:
#         0 8px 25px rgba(0,0,0,0.12);

#     animation:
#         cardIn 0.5s ease;
# }

# /* Reaction */

# .reaction {
#     text-align: center;
#     font-size: 23px;
#     line-height: 1.8;
#     color: white;
# }

# /* Wishes */

# .wish-wrapper {
#     animation:
#         wishIn 0.85s cubic-bezier(.2,.8,.2,1);
# }

# @keyframes wishIn {

#     0% {
#         opacity: 0;

#         transform:
#             scale(0.80)
#             translateY(25px)
#             rotateX(10deg);
#     }

#     100% {
#         opacity: 1;

#         transform:
#             scale(1)
#             translateY(0)
#             rotateX(0);
#     }
# }

# .wish-card {
#     min-height: 460px;

#     border-radius: 38px;

#     padding: 55px 25px;

#     display: flex;

#     flex-direction: column;

#     align-items: center;

#     justify-content: center;

#     text-align: center;

#     border:
#         2px solid rgba(255,255,255,0.30);

#     box-shadow:
#         0 25px 70px rgba(0,0,0,0.25);

#     position: relative;

#     overflow: hidden;
# }

# .wish-card::before {
#     content: "";

#     position: absolute;

#     width: 250px;
#     height: 250px;

#     border-radius: 50%;

#     background:
#         rgba(255,255,255,0.16);

#     filter: blur(10px);

#     top: -120px;
#     right: -100px;
# }

# .wish-card::after {
#     content: "";

#     position: absolute;

#     width: 180px;
#     height: 180px;

#     border-radius: 50%;

#     background:
#         rgba(255,255,255,0.13);

#     filter: blur(12px);

#     bottom: -100px;
#     left: -70px;
# }

# .language-label {
#     font-family:
#         'Playfair Display',
#         serif;

#     font-size: 22px;
#     font-weight: 700;

#     color:
#         rgba(255,255,255,0.95);

#     margin-bottom: 25px;

#     position: relative;
#     z-index: 2;
# }

# .wish-emoji {
#     font-size: 78px;

#     margin-bottom: 25px;

#     position: relative;
#     z-index: 2;

#     animation:
#         wishEmoji 2.5s ease-in-out infinite;
# }

# @keyframes wishEmoji {

#     0%, 100% {
#         transform:
#             translateY(0)
#             rotate(-3deg);
#     }

#     50% {
#         transform:
#             translateY(-10px)
#             rotate(3deg);
#     }
# }

# .wish-main {
#     font-family:
#         'Noto Sans',
#         sans-serif;

#     font-size: 37px;

#     font-weight: 800;

#     line-height: 1.5;

#     color: white;

#     text-shadow:
#         0 5px 20px rgba(0,0,0,0.25);

#     position: relative;
#     z-index: 2;

#     margin-bottom: 22px;
# }

# .wish-english {
#     font-family:
#         'Playfair Display',
#         serif;

#     font-size: 21px;

#     font-style: italic;

#     color:
#         rgba(255,255,255,0.92);

#     position: relative;
#     z-index: 2;
# }

# /* Final card */

# .final-card {
#     text-align: center;

#     padding: 55px 25px;

#     border-radius: 38px;

#     background:
#         linear-gradient(
#             135deg,
#             rgba(255,0,110,0.30),
#             rgba(131,56,236,0.30),
#             rgba(58,134,255,0.30),
#             rgba(6,214,160,0.30)
#         );

#     border:
#         1px solid rgba(255,255,255,0.35);

#     box-shadow:
#         0 25px 70px rgba(0,0,0,0.25);

#     position: relative;

#     overflow: hidden;

#     animation:
#         finalAppear 1s ease;
# }

# @keyframes finalAppear {

#     from {
#         opacity: 0;
#         transform: scale(0.75);
#     }

#     to {
#         opacity: 1;
#         transform: scale(1);
#     }
# }

# .final-title {
#     font-family:
#         'Playfair Display',
#         serif;

#     font-size: 45px;

#     font-weight: 800;

#     color: white;

#     animation:
#         finalGlow 1.6s ease-in-out infinite alternate;
# }

# @keyframes finalGlow {

#     from {
#         text-shadow:
#             0 0 10px rgba(255,255,255,0.4);
#     }

#     to {
#         text-shadow:
#             0 0 25px rgba(255,255,255,0.9),
#             0 0 50px rgba(255,0,150,0.7);
#     }
# }

# .final-message {
#     font-size: 19px;

#     line-height: 1.9;

#     color:
#         rgba(255,255,255,0.95);

#     margin-top: 25px;
# }

# /* Sparkles */

# .sparkle-field {
#     height: 120px;
#     position: relative;
#     margin-bottom: 15px;
# }

# .spark {
#     position: absolute;

#     font-size: 28px;

#     animation:
#         sparkle 1.8s ease-in-out infinite;
# }

# .s1 {
#     left: 10%;
#     top: 40%;
# }

# .s2 {
#     left: 25%;
#     top: 10%;
#     animation-delay: .3s;
# }

# .s3 {
#     left: 45%;
#     top: 50%;
#     animation-delay: .6s;
# }

# .s4 {
#     left: 65%;
#     top: 15%;
#     animation-delay: .9s;
# }

# .s5 {
#     left: 82%;
#     top: 45%;
#     animation-delay: 1.2s;
# }

# @keyframes sparkle {

#     0%, 100% {
#         opacity: 0.25;

#         transform:
#             scale(0.6)
#             rotate(0deg);
#     }

#     50% {
#         opacity: 1;

#         transform:
#             scale(1.5)
#             rotate(180deg);
#     }
# }

# /* Mobile */

# @media (max-width: 600px) {

#     .main-title {
#         font-size: 35px;
#     }

#     .wish-main {
#         font-size: 27px;
#     }

#     .wish-card {
#         min-height: 400px;
#         padding: 40px 18px;
#     }

#     .wish-emoji {
#         font-size: 65px;
#     }

#     .final-title {
#         font-size: 34px;
#     }

# }

# </style>
# """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # FLOATING DECORATIONS
# # ============================================================

# st.markdown(
#     """
# <div class="floating float1">🌸</div>
# <div class="floating float2">✨</div>
# <div class="floating float3">🌺</div>
# <div class="floating float4">✦</div>
# <div class="floating float5">🌼</div>
# <div class="floating float6">✨</div>
# """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # PASSWORD PAGE
# # ============================================================

# if st.session_state.page == "password":

#     st.markdown(
#         """
# <div class="main-title">
# 🎂 Something Special for Brightuuuu
# </div>

# <div class="subtitle">
# Before the birthday wishes begin... there's one little challenge.
# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         """
# <div class="glass-card">

#     <div class="big-emoji">
#     🌸✨🎂✨🌸
#     </div>

#     <h2 style="text-align:center;">
#     Hey Brightuuuu..!!
#     </h2>

#     <p style="
#         text-align:center;
#         font-size:19px;
#         line-height:1.8;
#         color:white;
#     ">

#     There's something waiting for you here.

#     <br><br>

#     But first...

#     <br>

#     <b>Enter the password. 😌</b>

#     </p>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     password = st.text_input(
#         "Password",
#         type="password",
#         placeholder="Enter the secret password...",
#         label_visibility="collapsed"
#     )

#     if st.button("🔓 Unlock"):

#         if password == PASSWORD:

#             st.session_state.entry_mode = (
#                 st.session_state.hint_level
#             )

#             st.session_state.page = "entry_reaction"

#             st.rerun()

#         else:

#             st.session_state.password_attempts += 1

#             st.error(
#                 "❌ Nope! That's not it. Try again 😂"
#             )

#     # --------------------------------------------------------
#     # HINT BUTTON
#     # --------------------------------------------------------

#     if st.session_state.hint_level < 2:

#         if st.button("💡 Give me a hint"):

#             st.session_state.hint_level += 1

#             st.rerun()

#     # --------------------------------------------------------
#     # HINT 1
#     # --------------------------------------------------------

#     if st.session_state.hint_level >= 1:

#         st.markdown(
#             """
# <div class="hint-box">

# 💡 <b>HINT 1</b>

# <br><br>

# It has exactly <b>6 characters</b>
# followed by <b>4 digits</b>.

# <br><br>

# That's it. I'm done helping. 😌

# </div>
# """,
#             unsafe_allow_html=True
#         )

#     # --------------------------------------------------------
#     # HINT 2
#     # --------------------------------------------------------

#     if st.session_state.hint_level >= 2:

#         st.markdown(
#             """
# <div class="hint-box">

# 💡 <b>HINT 2</b>

# <br><br>

# Think of something you type
# to unlock your laptop. 💻

# <br><br>

# <b>Your laptop PIN.</b>

# </div>
# """,
#             unsafe_allow_html=True
#         )

#         st.markdown(
#             """
# <p style="
#     text-align:center;
#     color:white;
#     margin-top:18px;
#     font-size:16px;
# ">
# Two hints already... really? 😑😂
# </p>
# """,
#             unsafe_allow_html=True
#         )

#         if st.button("🚨 I give up — Reveal"):

#             st.session_state.show_reveal = True

#             st.rerun()

#     # --------------------------------------------------------
#     # REVEAL
#     # --------------------------------------------------------

#     if st.session_state.show_reveal:

#         st.markdown(
#             """
# <div class="final-card">

#     <div class="big-emoji">
#     🎂✨🌸✨🎂
#     </div>

#     <div class="final-title">
#     HAPPY BIRTHDAY, BRIGHTUUUU!!
#     </div>

#     <div class="final-message">

#     Okay, no more guessing. 😂

#     <br><br>

#     I hope you have a genuinely wonderful birthday.

#     <br><br>

#     Enjoy your day, smile a lot,
#     eat something nice,
#     and have a beautiful year ahead. ❤️

#     <br><br>

#     <b>Happy Birthday! 🎂✨</b>

#     </div>

# </div>
# """,
#             unsafe_allow_html=True
#         )


# # ============================================================
# # PASSWORD REACTION
# # ============================================================

# elif st.session_state.page == "entry_reaction":

#     mode = st.session_state.entry_mode

#     if mode == 0:

#         st.markdown(
#             """
# <div class="glass-card">

#     <div class="big-emoji">
#     🎉✨🎉
#     </div>

#     <div class="reaction">

#     <b>WAITTT... YOU GOT IT?!</b>

#     <br><br>

#     And you didn't even use a hint?!

#     <br><br>

#     Okay Brightuuuu...

#     <br>

#     <b>I'm genuinely impressed. 👏😂</b>

#     <br><br>

#     You may proceed. 😌

#     </div>

# </div>
# """,
#             unsafe_allow_html=True
#         )

#     elif mode == 1:

#         st.markdown(
#             """
# <div class="glass-card">

#     <div class="big-emoji">
#     😌✨
#     </div>

#     <div class="reaction">

#     <b>Okayyy... acceptable.</b>

#     <br><br>

#     One hint isn't too bad.

#     <br><br>

#     I'll let that one slide. 😌

#     <br><br>

#     <b>Welcome, Brightuuuu! ❤️</b>

#     </div>

# </div>
# """,
#             unsafe_allow_html=True
#         )

#     else:

#         st.markdown(
#             """
# <div class="glass-card">

#     <div class="big-emoji">
#     😑🌸😂
#     </div>

#     <div class="reaction">

#     <b>Seriously, Brightuuuu?!</b>

#     <br><br>

#     You used BOTH hints?!

#     <br><br>

#     I gave you TWO chances. 😂

#     <br><br>

#     <span style="font-size:18px;">
#     Fine. I'm slightly offended.
#     </span>

#     <br><br>

#     But okay...

#     <br>

#     <b>Welcome. 😌</b>

#     </div>

# </div>
# """,
#             unsafe_allow_html=True
#         )

#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.button("✨ Continue"):

#         st.session_state.page = "welcome"

#         st.rerun()


# # ============================================================
# # WELCOME PAGE
# # ============================================================

# elif st.session_state.page == "welcome":

#     st.markdown(
#         """
# <div class="main-title">
# Welcome Brightuuuu..!! 🎂
# </div>

# <div class="subtitle">
# Okay... now we're getting somewhere. ✨
# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         """
# <div class="glass-card">

#     <div class="big-emoji">
#     🌸🎂✨🌼
#     </div>

#     <h2 style="text-align:center;">
#     I could have just sent you a message.
#     </h2>

#     <p style="
#         text-align:center;
#         font-size:20px;
#         line-height:1.9;
#         color:white;
#     ">

#     Something simple like...

#     <br><br>

#     <b>“Happy Birthday!”</b>

#     <br><br>

#     But somehow that felt a little too ordinary.

#     <br><br>

#     So I decided to make you
#     travel a little today. 🌍

#     <br><br>

#     <b>Ready?</b>

#     </p>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     if st.button("🌍 Let's go"):

#         st.session_state.page = "funny"

#         st.rerun()


# # ============================================================
# # FUNNY INTRO
# # ============================================================

# elif st.session_state.page == "funny":

#     emoji, title, message = funny_messages[
#         st.session_state.funny_index
#     ]

#     st.markdown(
#         """
# <div class="subtitle">
# Before the actual surprise...
# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f"""
# <div class="glass-card">

#     <div class="big-emoji">
#     {emoji}
#     </div>

#     <h2 style="text-align:center;">
#     {title}
#     </h2>

#     <p style="
#         text-align:center;
#         font-size:23px;
#         line-height:1.8;
#         color:white;
#     ">
#     {message}
#     </p>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.session_state.funny_index < len(funny_messages) - 1:

#         if st.button("Next 👉"):

#             st.session_state.funny_index += 1

#             st.rerun()

#     else:

#         if st.button("🌎 Begin the wishes"):

#             st.session_state.page = "wishes"

#             st.rerun()


# # ============================================================
# # LANGUAGE WISHES
# # ============================================================

# elif st.session_state.page == "wishes":

#     current = wishes[
#         st.session_state.wish_index
#     ]

#     st.markdown(
#         """
# <div class="subtitle">
# 🌍 A little birthday journey...
# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f"""
# <div class="wish-wrapper">

#     <div
#         class="wish-card"
#         style="background:{current['background']};"
#     >

#         <div class="language-label">
#         🌍 {current['language']}
#         </div>

#         <div class="wish-emoji">
#         {current['emoji']}
#         </div>

#         <div class="wish-main">
#         {current['wish']}
#         </div>

#         <div class="wish-english">
#         {current['english']}
#         </div>

#     </div>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.session_state.wish_index < len(wishes) - 1:

#         if st.button("Next 🌸"):

#             st.session_state.wish_index += 1

#             st.rerun()

#     else:

#         if st.button("✨ One last thing..."):

#             st.session_state.page = "final_intro"

#             st.rerun()


# # ============================================================
# # FINAL INTRO
# # ============================================================

# elif st.session_state.page == "final_intro":

#     st.markdown(
#         """
# <div class="glass-card">

#     <div class="big-emoji">
#     🌍✨🌸✨🌍
#     </div>

#     <div class="reaction">

#     <b>And that's the little journey.</b>

#     <br><br>

#     So many different ways to say it...

#     <br><br>

#     But here's the one I really wanted you to hear.

#     <br><br>

#     <span style="font-size:18px;">
#     ❤️ From me to you.
#     </span>

#     </div>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.button("🎂 Open your birthday wish"):

#         st.session_state.page = "final"

#         st.rerun()


# # ============================================================
# # FINAL BIRTHDAY SCREEN
# # ============================================================

# elif st.session_state.page == "final":

#     st.markdown(
#         """
# <div class="final-card">

#     <div class="sparkle-field">

#         <div class="spark s1">✦</div>
#         <div class="spark s2">✨</div>
#         <div class="spark s3">✧</div>
#         <div class="spark s4">✨</div>
#         <div class="spark s5">✦</div>

#     </div>

#     <div class="big-emoji">
#     🎂🌸✨🌼
#     </div>

#     <div class="final-title">
#     HAPPY BIRTHDAY, BRIGHTUUUU!!
#     </div>

#     <div class="final-message">

#     I hope your day is filled with
#     happiness, laughter, good food,
#     good people and lots of little moments
#     that make you smile.

#     <br><br>

#     I hope the year ahead brings you
#     wonderful memories, exciting things,
#     and plenty of reasons to be happy.

#     <br><br>

#     Have a really wonderful birthday,
#     Brightuuuu. ❤️

#     <br><br>

#     <b>Enjoy your day! 🎂✨</b>

#     </div>

# </div>
# """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         """
# <div style="
#     text-align:center;
#     margin-top:28px;
#     color:rgba(255,255,255,0.90);
#     font-family:'Playfair Display',serif;
#     font-size:17px;
# ">
# Made specially for you. 🌸
# </div>
# """,
#         unsafe_allow_html=True
#     )


import streamlit as st
import time
import random

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="A Birthday Surprise for Brightuuuu 💗",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PASSWORD
# ============================================================

PASSWORD = "T20080209S"

# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "password",
    "password_attempts": 0,
    "funny_index": 0,
    "wish_index": 0,
    "secret_clicks": 0,
    "music_started": False,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# CUSTOM CSS
# PASTEL ONLY
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GOOGLE FONTS
       ======================================================== */

    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Quicksand:wght@400;500;600;700&family=Pacifico&display=swap');


    /* ========================================================
       GLOBAL BACKGROUND
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 5% 10%,
                rgba(248, 215, 228, 0.70),
                transparent 25%
            ),
            radial-gradient(
                circle at 95% 15%,
                rgba(218, 218, 242, 0.75),
                transparent 28%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(213, 237, 232, 0.70),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 90%,
                rgba(250, 232, 210, 0.70),
                transparent 27%
            ),
            #fffaf7;

        min-height: 100vh;
    }


    /* ========================================================
       HIDE STREAMLIT CHROME
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       MAIN WIDTH
       ======================================================== */

    .block-container {
        max-width: 820px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }


    /* ========================================================
       FONT CLASSES
       ======================================================== */

    .serif {
        font-family: 'DM Serif Display', serif;
    }

    .script {
        font-family: 'Pacifico', cursive;
    }

    .body-font {
        font-family: 'Quicksand', sans-serif;
    }


    /* ========================================================
       GLASS CARD
       ======================================================== */

    .glass-card {
        background: rgba(255, 255, 255, 0.72);

        border: 1px solid rgba(255, 255, 255, 0.90);

        border-radius: 34px;

        padding: 42px 38px;

        margin: 12px auto 25px auto;

        box-shadow:
            0 20px 55px rgba(174, 155, 174, 0.14),
            inset 0 1px 1px rgba(255,255,255,0.9);

        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);

        text-align: center;
    }


    /* ========================================================
       TOP DECORATION
       ======================================================== */

    .top-decoration {
        font-size: 1.7rem;
        letter-spacing: 12px;
        opacity: 0.75;
        margin-bottom: 15px;
    }


    /* ========================================================
       TITLES
       ======================================================== */

    .main-title {
        font-family: 'DM Serif Display', serif;
        font-size: 3.5rem;
        line-height: 1.15;
        color: #8d7c91;
        margin: 10px 0;
    }

    .script-title {
        font-family: 'Pacifico', cursive;
        font-size: 2.9rem;
        line-height: 1.3;
        color: #c58ca8;
        margin: 10px 0 18px 0;
    }

    .small-script {
        font-family: 'Pacifico', cursive;
        font-size: 1.55rem;
        color: #c18da5;
    }

    .subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: 1.08rem;
        line-height: 1.8;
        font-weight: 600;
        color: #958a94;
    }

    .soft-text {
        font-family: 'Quicksand', sans-serif;
        color: #a1979f;
        font-size: 0.98rem;
        line-height: 1.85;
    }

    .cute-text {
        font-family: 'Quicksand', sans-serif;
        color: #b3889f;
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1.8;
    }


    /* ========================================================
       HEART
       ======================================================== */

    .heart {
        font-size: 5rem;
        display: inline-block;
        animation: heartbeat 2s ease-in-out infinite;
    }

    @keyframes heartbeat {

        0%, 100% {
            transform: scale(1);
        }

        15% {
            transform: scale(1.10);
        }

        30% {
            transform: scale(1);
        }

        45% {
            transform: scale(1.08);
        }

        60% {
            transform: scale(1);
        }
    }


    /* ========================================================
       FLOATING DECORATIONS
       ======================================================== */

    .floating {
        position: fixed;
        z-index: 0;
        pointer-events: none;
        opacity: 0.45;
        font-size: 24px;
    }

    .f1 {
        top: 8%;
        left: 4%;
        animation: floatA 7s ease-in-out infinite;
    }

    .f2 {
        top: 20%;
        right: 4%;
        animation: floatB 8s ease-in-out infinite;
    }

    .f3 {
        top: 55%;
        left: 2%;
        animation: floatB 9s ease-in-out infinite;
    }

    .f4 {
        bottom: 12%;
        right: 4%;
        animation: floatA 7s ease-in-out infinite;
    }

    .f5 {
        bottom: 7%;
        left: 10%;
        animation: floatB 8s ease-in-out infinite;
    }

    @keyframes floatA {

        0%, 100% {
            transform: translateY(0) rotate(-5deg);
        }

        50% {
            transform: translateY(-20px) rotate(8deg);
        }
    }

    @keyframes floatB {

        0%, 100% {
            transform: translateY(0) rotate(5deg);
        }

        50% {
            transform: translateY(18px) rotate(-8deg);
        }
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    .divider {
        height: 1px;

        margin: 28px 0;

        background:
            linear-gradient(
                90deg,
                transparent,
                #e9dce5,
                transparent
            );
    }


    /* ========================================================
       PASSWORD AREA
       ======================================================== */

    .lock {
        font-size: 3.5rem;
        margin-bottom: 5px;
    }


    /* ========================================================
       FUNNY CARD
       ======================================================== */

    .funny-card {

        background:
            linear-gradient(
                135deg,
                rgba(255, 238, 222, 0.80),
                rgba(250, 224, 235, 0.80)
            );

        border-radius: 28px;

        border: 1px solid rgba(255,255,255,0.9);

        padding: 30px;

        margin: 25px 0;

        box-shadow:
            0 12px 35px rgba(180,160,170,0.12);
    }

    .funny-number {
        font-family: 'Pacifico', cursive;
        color: #c394a8;
        font-size: 1.2rem;
        margin-bottom: 15px;
    }

    .funny-message {
        font-family: 'Quicksand', sans-serif;
        color: #887b83;
        font-size: 1.18rem;
        line-height: 1.8;
        font-weight: 600;
    }


    /* ========================================================
       WISH CARD
       ======================================================== */

    .wish-card {

        background:
            linear-gradient(
                135deg,
                rgba(237, 228, 245, 0.82),
                rgba(222, 240, 236, 0.80)
            );

        border-radius: 30px;

        padding: 34px 25px;

        margin: 25px 0;

        border: 1px solid rgba(255,255,255,0.9);

        box-shadow:
            0 14px 38px rgba(160,150,175,0.12);
    }

    .wish-language {
        font-family: 'Quicksand', sans-serif;
        color: #a18c9e;
        font-size: 0.88rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }

    .wish-message {
        font-family: 'DM Serif Display', serif;
        color: #817589;
        font-size: 1.7rem;
        line-height: 1.65;
    }


    /* ========================================================
       MEMORY / EMOTIONAL CARD
       ======================================================== */

    .memory-card {

        background:
            linear-gradient(
                145deg,
                rgba(252, 230, 238, 0.82),
                rgba(232, 230, 245, 0.82)
            );

        border-radius: 32px;

        padding: 36px 30px;

        border: 1px solid rgba(255,255,255,0.95);

        box-shadow:
            0 18px 45px rgba(180,155,175,0.13);

        margin: 25px 0;
    }

    .memory-line {
        font-family: 'DM Serif Display', serif;
        font-size: 1.35rem;
        line-height: 1.9;
        color: #837682;
    }


    /* ========================================================
       FINAL CARD
       ======================================================== */

    .final-card {

        background:
            linear-gradient(
                145deg,
                rgba(249, 220, 232, 0.88),
                rgba(228, 224, 244, 0.88),
                rgba(219, 238, 233, 0.88)
            );

        border-radius: 40px;

        padding: 50px 35px;

        border: 2px solid rgba(255,255,255,0.9);

        box-shadow:
            0 25px 70px rgba(165,145,170,0.17);

        text-align: center;

        overflow: hidden;
    }

    .cake {
        font-size: 4.5rem;
        margin-bottom: 10px;
    }

    .final-name {
        font-family: 'Pacifico', cursive;
        color: #bf88a3;
        font-size: 3.6rem;
        line-height: 1.4;
    }

    .final-heading {
        font-family: 'DM Serif Display', serif;
        color: #827486;
        font-size: 2rem;
        margin: 18px 0;
    }

    .final-message {
        font-family: 'Quicksand', sans-serif;
        color: #807580;
        font-size: 1.12rem;
        line-height: 2;
        font-weight: 500;
    }

    .signature {
        font-family: 'Pacifico', cursive;
        color: #c18ca5;
        font-size: 1.6rem;
        margin-top: 25px;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {

        width: 100%;

        min-height: 48px;

        border-radius: 18px;

        border: 1px solid rgba(255,255,255,0.95);

        background:
            linear-gradient(
                135deg,
                #f4d9e5,
                #e2def2
            );

        color: #806f7b;

        font-family: 'Quicksand', sans-serif;

        font-weight: 700;

        font-size: 1rem;

        box-shadow:
            0 7px 20px rgba(170,150,170,0.12);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
    }

    .stButton > button:hover {

        transform: translateY(-3px);

        box-shadow:
            0 12px 28px rgba(170,150,170,0.18);
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    .stTextInput input {

        background: rgba(255,255,255,0.78) !important;

        border: 2px solid #eadde6 !important;

        border-radius: 18px !important;

        padding: 14px !important;

        text-align: center;

        color: #796f78 !important;

        font-family: 'Quicksand', sans-serif !important;

        font-weight: 700;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 600px) {

        .block-container {
            padding: 1rem 0.8rem 3rem 0.8rem;
        }

        .glass-card {
            padding: 30px 20px;
            border-radius: 28px;
        }

        .main-title {
            font-size: 2.6rem;
        }

        .script-title {
            font-size: 2.25rem;
        }

        .heart {
            font-size: 4rem;
        }

        .wish-message {
            font-size: 1.4rem;
        }

        .final-name {
            font-size: 2.7rem;
        }

        .final-card {
            padding: 40px 20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FLOATING DECORATIONS
# ============================================================

st.markdown(
    """
    <div class="floating f1">🌸</div>
    <div class="floating f2">🦋</div>
    <div class="floating f3">🌷</div>
    <div class="floating f4">✨</div>
    <div class="floating f5">💗</div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# BIRTHDAY WISHES
# ============================================================

wishes = [
    ("Tamil", "இனிய பிறந்தநாள் வாழ்த்துக்கள்! 💗"),
    ("Telugu", "పుట్టినరోజు శుభాకాంక్షలు! 🎂"),
    ("Kannada", "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು! 🌸"),
    ("Malayalam", "ജന്മദിനാശംസകൾ! 💕"),
    ("Hindi", "जन्मदिन की शुभकामनाएँ! ✨"),
    ("Bengali", "শুভ জন্মদিন! 🌷"),
    ("Marathi", "वाढदिवसाच्या हार्दिक शुभेच्छा! 💫"),
    ("Punjabi", "ਜਨਮਦਿਨ ਮੁਬਾਰਕ! 💗"),
    ("Gujarati", "જન્મદિવસની શુભકામનાઓ! 🌸"),
    ("English", "Happy Birthday! 🎂"),
    ("French", "Joyeux anniversaire! 🌷"),
    ("Spanish", "¡Feliz cumpleaños! 💕"),
    ("Italian", "Buon compleanno! ✨"),
    ("German", "Alles Gute zum Geburtstag! 🌸"),
    ("Portuguese", "Feliz aniversário! 💗"),
    ("Chinese", "生日快乐！🎂"),
    ("Japanese", "お誕生日おめでとう！🌸"),
    ("Korean", "생일 축하해! 💕"),
    ("Arabic", "عيد ميلاد سعيد! ✨"),
    ("Turkish", "Doğum günün kutlu olsun! 🌷"),
    ("Russian", "С днём рождения! 💗"),
    ("Greek", "Χρόνια πολλά! 🎂"),
    ("Dutch", "Fijne verjaardag! 🌸"),
    ("Swedish", "Grattis på födelsedagen! 💕"),
    ("Thai", "สุขสันต์วันเกิด! ✨"),
    ("Vietnamese", "Chúc mừng sinh nhật! 🌷"),
    ("Indonesian", "Selamat ulang tahun! 💗"),
    ("Filipino", "Maligayang kaarawan! 🎂"),
]


# ============================================================
# FUNNY MESSAGES
# ============================================================

funny_messages = [
    "Congratulations! 🎉 You have successfully unlocked another year of being older... but hopefully not wiser. 😂",

    "Age is just a number. Unfortunately, yours is starting to look suspiciously like a password. 😌",

    "Don't worry about getting older. You're still young enough to make questionable decisions. 😂",

    "Another year older. Another year of pretending you know exactly what you're doing. 😎",

    "Happy Birthday! May your phone battery last longer than your patience. 🔋😂",

    "You're not getting old... you're becoming a limited edition. ✨",

    "Today is your special day, so you are officially allowed to be extra dramatic. 😌",

    "At this point, cake is basically a personality trait. 🎂😂",

    "One more year of existence and still no instruction manual. Impressive. 😂",

    "Don't count the candles. Just enjoy the cake before someone else does. 👀🎂",
]


# ============================================================
# PAGE 1 — PASSWORD
# ============================================================

if st.session_state.page == "password":

    st.markdown(
        """
        <div class="glass-card">

            <div class="top-decoration">
                🌸 ✨ 🌷
            </div>

            <div class="lock">
                🔐
            </div>

            <div class="script-title">
                Psssst...
            </div>

            <div class="main-title">
                Something Special
            </div>

            <p class="subtitle">
                There is a tiny little surprise hiding here.
                <br>
                But obviously...
                <br>
                I can't just let anyone open it. 👀
            </p>

            <div class="divider"></div>

            <p class="cute-text">
                Only one person knows the secret code. 💗
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Secret password",
        type="password",
        placeholder="Enter the secret code...",
        label_visibility="collapsed"
    )

    if st.button("🔓 Unlock the surprise"):

        if password == PASSWORD:

            st.session_state.page = "entry_reaction"

            st.rerun()

        else:

            st.session_state.password_attempts += 1

            attempts = st.session_state.password_attempts

            if attempts == 1:
                st.warning("Hmmmm... nope 😌 Think again.")

            elif attempts == 2:
                st.info("You're getting closer... maybe. 👀")

            elif attempts == 3:
                st.warning("Okay Brightuuuu... seriously? 😂")

            else:
                st.error(
                    "Wrong again! I'm starting to question whether "
                    "you deserve this surprise. 😭😂"
                )


# ============================================================
# PAGE 2 — ENTRY REACTION
# ============================================================

elif st.session_state.page == "entry_reaction":

    st.markdown(
        """
        <div class="glass-card">

            <div class="top-decoration">
                ✨ 🌸 ✨
            </div>

            <div class="heart">
                🥹
            </div>

            <div class="script-title">
                You actually made it!
            </div>

            <p class="subtitle">
                I knew you would figure it out...
                <br>
                eventually. 😌
            </p>

            <div class="divider"></div>

            <div class="soft-text">

                Okay.

                <br><br>

                No more secrets.

                <br><br>

                Well...

                <br>

                maybe one or two more. 👀

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Okay... what is this? 👀"):

        st.session_state.page = "welcome"

        st.rerun()


# ============================================================
# PAGE 3 — WELCOME
# ============================================================

elif st.session_state.page == "welcome":

    st.markdown(
        """
        <div class="glass-card">

            <div class="top-decoration">
                🌷 💗 🌷
            </div>

            <div class="script-title">
                Helloooo Brightuuuu
            </div>

            <div class="heart">
                🫶
            </div>

            <p class="subtitle">
                Today isn't just another ordinary day.
            </p>

            <div class="memory-card">

                <div class="memory-line">

                    Today is the day
                    <br>
                    one very special human
                    <br>
                    decided to show up in this world. 🌸

                </div>

            </div>

            <p class="cute-text">

                And yes...

                <br>

                this ridiculously unnecessary little website
                <br>
                is completely for YOU. 💗

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue... 🌸"):

        st.session_state.page = "funny"

        st.rerun()


# ============================================================
# PAGE 4 — FUNNY
# ============================================================

elif st.session_state.page == "funny":

    index = st.session_state.funny_index

    message = funny_messages[index]

    st.markdown(
        f"""
        <div class="glass-card">

            <div class="top-decoration">
                😂 🌷 😂
            </div>

            <div class="script-title">
                But first...
            </div>

            <p class="subtitle">
                Before this gets unnecessarily emotional,
                <br>
                we need to discuss some important facts.
            </p>

            <div class="funny-card">

                <div class="funny-number">
                    Important Birthday Fact #{index + 1}
                </div>

                <div class="funny-message">
                    {message}
                </div>

            </div>

            <p class="soft-text">
                Don't worry. There are more. 😌
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("😂 Another one"):

            st.session_state.funny_index = (
                st.session_state.funny_index + 1
            ) % len(funny_messages)

            st.rerun()

    with col2:

        if st.button("Okay enough 😂"):

            st.session_state.page = "wishes"

            st.rerun()


# ============================================================
# PAGE 5 — MULTILINGUAL WISHES
# ============================================================

elif st.session_state.page == "wishes":

    index = st.session_state.wish_index

    language, message = wishes[index]

    total = len(wishes)

    st.markdown(
        f"""
        <div class="glass-card">

            <div class="top-decoration">
                🌍 ✨ 🌸
            </div>

            <div class="script-title">
                One birthday...
            </div>

            <p class="subtitle">
                So many languages.
                <br>
                Because apparently one wish wasn't enough. 💗
            </p>

            <div class="wish-card">

                <div class="wish-language">
                    {language}
                </div>

                <div class="wish-message">
                    {message}
                </div>

            </div>

            <p class="soft-text">
                Wish {index + 1} of {total}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if index < total - 1:

        if st.button("🌷 Next birthday wish"):

            st.session_state.wish_index += 1

            st.rerun()

    else:

        if st.button("💗 One last thing..."):

            st.session_state.page = "final_intro"

            st.rerun()


# ============================================================
# PAGE 6 — EMOTIONAL INTRO
# ============================================================

elif st.session_state.page == "final_intro":

    st.markdown(
        """
        <div class="glass-card">

            <div class="top-decoration">
                ✨ 🌸 ✨
            </div>

            <div class="heart">
                🥹
            </div>

            <div class="script-title">
                Okay Brightuuuu...
            </div>

            <p class="subtitle">
                That's enough teasing.
            </p>

            <div class="divider"></div>

            <div class="memory-card">

                <div class="memory-line">

                    Jokes apart...

                    <br><br>

                    I really hope this new year of your life
                    <br>
                    gives you beautiful things.

                    <br><br>

                    More smiles.
                    <br>
                    More memories.
                    <br>
                    More reasons to be happy.

                </div>

            </div>

            <p class="cute-text">
                And now...
                <br>
                the actual birthday message. 💗
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Open it... 💌"):

        st.session_state.page = "final"

        st.rerun()


# ============================================================
# PAGE 7 — FINAL
# ============================================================

elif st.session_state.page == "final":

    st.markdown(
        """
        <div class="final-card">

            <div class="cake">
                🎂
            </div>

            <div class="top-decoration">
                🌸 ✨ 🌷
            </div>

            <div class="final-name">
                Brightuuuu
            </div>

            <div class="final-heading">
                Happy Birthday! 💗
            </div>

            <div class="heart">
                🫶
            </div>

            <div class="divider"></div>

            <div class="final-message">

                I hope this year brings you
                <br>
                countless little moments
                <br>
                that make you genuinely happy.

                <br><br>

                I hope you laugh a little louder,
                <br>
                smile a little more,
                <br>
                worry a little less,
                <br>
                and create memories
                <br>
                you'll want to keep forever. 🌷

                <br><br>

                May the things you wish for
                <br>
                slowly find their way to you.

                <br><br>

                And whenever life gets a little difficult,
                <br>
                I hope you remember
                <br>
                that there are people
                <br>
                who are genuinely happy
                <br>
                that you exist. 💗

            </div>

            <div class="divider"></div>

            <div class="small-script">
                Stay happy. Stay crazy.
                <br>
                Stay Brightuuuu. ✨
            </div>

            <div class="signature">
                Happy Birthday 💕
            </div>

            <div class="top-decoration">
                🌸 💗 🌸
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🌷 Start the surprise again"):

        for key, value in DEFAULTS.items():
            st.session_state[key] = value

        st.rerun()

        st.rerun()
