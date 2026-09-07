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
    page_title="A Birthday Surprise for Brightuuuu 🎂",
    page_icon="💗",
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

defaults = {
    "page": "password",
    "hint_level": 0,
    "password_attempts": 0,
    "entry_mode": None,
    "show_reveal": False,
    "funny_index": 0,
    "wish_index": 0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# PASTEL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       IMPORT FONTS
       ======================================================== */

    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Quicksand:wght@400;500;600;700&family=Pacifico&display=swap');


    /* ========================================================
       GLOBAL
       ======================================================== */

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, #fce4ec 0%, transparent 28%),
            radial-gradient(circle at 90% 15%, #e8eaf6 0%, transparent 30%),
            radial-gradient(circle at 20% 90%, #e0f2f1 0%, transparent 30%),
            radial-gradient(circle at 85% 85%, #fff3e0 0%, transparent 30%),
            #fffaf7;

        min-height: 100vh;
    }


    /* ========================================================
       HIDE STREAMLIT DEFAULT ELEMENTS
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* ========================================================
       MAIN CONTAINER
       ======================================================== */

    .block-container {
        max-width: 760px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       PASTEL CARD
       ======================================================== */

    .pastel-card {
        background: rgba(255, 255, 255, 0.78);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        padding: 38px 34px;
        box-shadow:
            0 15px 45px rgba(180, 160, 180, 0.16),
            inset 0 1px 0 rgba(255,255,255,0.8);

        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);

        text-align: center;
        margin: 10px auto 25px auto;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    .main-title {
        font-family: 'DM Serif Display', serif;
        font-size: 3.4rem;
        line-height: 1.15;
        color: #8e7d9a;
        margin-bottom: 10px;
    }

    .script-title {
        font-family: 'Pacifico', cursive;
        font-size: 2.8rem;
        color: #c58ca8;
        margin: 10px 0;
    }

    .section-title {
        font-family: 'DM Serif Display', serif;
        font-size: 2.4rem;
        color: #8d8295;
        margin-bottom: 15px;
    }

    .subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #9a919b;
        line-height: 1.7;
    }


    /* ========================================================
       SMALL TEXT
       ======================================================== */

    .soft-text {
        color: #aaa0a8;
        font-size: 0.95rem;
        line-height: 1.7;
    }

    .cute-text {
        color: #b18ca2;
        font-size: 1.05rem;
        font-weight: 600;
    }


    /* ========================================================
       BIG HEART
       ======================================================== */

    .big-heart {
        font-size: 5rem;
        animation: heartbeat 1.8s infinite;
        margin: 5px;
    }

    @keyframes heartbeat {

        0% {
            transform: scale(1);
        }

        25% {
            transform: scale(1.12);
        }

        40% {
            transform: scale(1);
        }

        60% {
            transform: scale(1.08);
        }

        100% {
            transform: scale(1);
        }
    }


    /* ========================================================
       FLOATING DECORATIONS
       ======================================================== */

    .floating {
        position: fixed;
        font-size: 25px;
        opacity: 0.45;
        pointer-events: none;
        z-index: 0;
    }

    .flower1 {
        top: 12%;
        left: 5%;
        animation: float1 6s ease-in-out infinite;
    }

    .flower2 {
        top: 28%;
        right: 5%;
        animation: float2 7s ease-in-out infinite;
    }

    .flower3 {
        bottom: 12%;
        left: 8%;
        animation: float1 8s ease-in-out infinite;
    }

    .flower4 {
        bottom: 20%;
        right: 7%;
        animation: float2 6s ease-in-out infinite;
    }

    @keyframes float1 {
        0%, 100% {
            transform: translateY(0px) rotate(0deg);
        }

        50% {
            transform: translateY(-18px) rotate(8deg);
        }
    }

    @keyframes float2 {
        0%, 100% {
            transform: translateY(0px) rotate(0deg);
        }

        50% {
            transform: translateY(15px) rotate(-8deg);
        }
    }


    /* ========================================================
       PASSWORD BOX
       ======================================================== */

    .password-title {
        font-family: 'Pacifico', cursive;
        color: #b7839d;
        font-size: 2rem;
    }


    /* ========================================================
       WISH CARD
       ======================================================== */

    .wish-card {
        background: linear-gradient(
            135deg,
            rgba(252, 228, 236, 0.75),
            rgba(232, 234, 246, 0.75)
        );

        border-radius: 25px;
        padding: 28px;
        margin: 20px 0;

        border: 1px solid rgba(255,255,255,0.9);

        box-shadow:
            0 10px 30px rgba(190,170,190,0.14);
    }

    .wish-text {
        font-family: 'DM Serif Display', serif;
        font-size: 1.65rem;
        color: #81768a;
        line-height: 1.6;
    }


    /* ========================================================
       FUNNY CARD
       ======================================================== */

    .funny-card {
        background: linear-gradient(
            135deg,
            #fff3e0,
            #fce4ec
        );

        border-radius: 28px;
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.9);

        box-shadow:
            0 10px 30px rgba(200,170,180,0.15);

        margin: 20px 0;
    }

    .funny-text {
        font-size: 1.25rem;
        color: #8d7d84;
        line-height: 1.7;
        font-weight: 600;
    }


    /* ========================================================
       FINAL CARD
       ======================================================== */

    .final-card {
        background:
            linear-gradient(
                145deg,
                rgba(252,228,236,0.88),
                rgba(232,234,246,0.88),
                rgba(224,242,241,0.88)
            );

        border-radius: 35px;
        padding: 45px 35px;

        border: 2px solid rgba(255,255,255,0.8);

        box-shadow:
            0 20px 60px rgba(170,150,180,0.18);

        text-align: center;
    }

    .final-name {
        font-family: 'Pacifico', cursive;
        font-size: 3.5rem;
        color: #c18ca5;
        margin: 15px 0;
    }

    .final-message {
        font-family: 'DM Serif Display', serif;
        font-size: 1.5rem;
        line-height: 1.8;
        color: #7f7482;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {

        width: 100%;

        border-radius: 18px;

        border: 1px solid rgba(255,255,255,0.9);

        background:
            linear-gradient(
                135deg,
                #f8dce7,
                #e4e1f4
            );

        color: #806f7b;

        font-family: 'Quicksand', sans-serif;

        font-weight: 700;

        font-size: 1rem;

        padding: 0.7rem 1rem;

        box-shadow:
            0 6px 18px rgba(170,150,170,0.12);

        transition: all 0.25s ease;
    }


    .stButton > button:hover {

        transform: translateY(-3px);

        box-shadow:
            0 10px 25px rgba(170,150,170,0.18);

        border-color: #f0d9e4;
    }


    /* ========================================================
       INPUT
       ======================================================== */

    .stTextInput input {

        border-radius: 17px !important;

        border: 2px solid #eadde6 !important;

        background: rgba(255,255,255,0.75) !important;

        color: #786e77 !important;

        text-align: center;

        font-family: 'Quicksand', sans-serif;

        font-weight: 600;

        padding: 14px !important;
    }

    .stTextInput input:focus {

        border-color: #d8b9ca !important;

        box-shadow:
            0 0 0 3px rgba(220,190,210,0.15) !important;
    }


    /* ========================================================
       PROGRESS BAR
       ======================================================== */

    .progress-text {

        text-align: center;

        font-size: 0.85rem;

        color: #aaa0a8;

        margin-bottom: 8px;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    .soft-divider {

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                #eadde6,
                transparent
            );

        margin: 25px 0;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 600px) {

        .block-container {
            padding: 1rem;
        }

        .pastel-card {
            padding: 28px 20px;
            border-radius: 25px;
        }

        .main-title {
            font-size: 2.5rem;
        }

        .script-title {
            font-size: 2.1rem;
        }

        .section-title {
            font-size: 2rem;
        }

        .final-name {
            font-size: 2.6rem;
        }

        .wish-text {
            font-size: 1.3rem;
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
    <div class="floating flower1">🌸</div>
    <div class="floating flower2">🦋</div>
    <div class="floating flower3">🌷</div>
    <div class="floating flower4">✨</div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# BIRTHDAY WISHES
# ============================================================

wishes = [

    "இனிய பிறந்தநாள் வாழ்த்துக்கள்! 💗",

    "పుట్టినరోజు శుభాకాంక్షలు! 🎂",

    "ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು! 🌸",

    "ജന്മദിനാശംസകൾ! 💕",

    "जन्मदिन की शुभकामनाएँ! ✨",

    "শুভ জন্মদিন! 🌷",

    "वाढदिवसाच्या हार्दिक शुभेच्छा! 💫",

    "ਜਨਮਦਿਨ ਮੁਬਾਰਕ! 💗",

    "જન્મદિવસની શુભકામનાઓ! 🌸",

    "Happy Birthday! 🎂",

    "Joyeux anniversaire! 🌷",

    "¡Feliz cumpleaños! 💕",

    "Buon compleanno! ✨",

    "Alles Gute zum Geburtstag! 🌸",

    "Feliz aniversário! 💗",

    "生日快乐！🎂",

    "お誕生日おめでとう！🌸",

    "생일 축하해! 💕",

    "عيد ميلاد سعيد! ✨",

    "Doğum günün kutlu olsun! 🌷",

    "С днём рождения! 💗",

    "Χρόνια πολλά! 🎂",

    "Fijne verjaardag! 🌸",

    "Grattis på födelsedagen! 💕",

    "สุขสันต์วันเกิด! ✨",

    "Chúc mừng sinh nhật! 🌷",

    "Selamat ulang tahun! 💗",

    "Maligayang kaarawan! 🎂",

]


# ============================================================
# FUNNY MESSAGES
# ============================================================

funny_messages = [

    "Congratulations! 🎉 You have successfully unlocked another year of being older... but hopefully not wiser. 😂",

    "Age is just a number. Unfortunately, yours is starting to look like a password. 😌",

    "Don't worry about getting older. You're still young enough to make questionable decisions. 😂",

    "Another year older, another year of pretending you know what you're doing. 😎",

    "Happy Birthday! May your phone battery last longer than your patience. 🔋😂",

    "You're not getting old... you're becoming a limited edition. ✨",

    "Today is your special day. So yes, you are officially allowed to be extra dramatic. 😌",

]


# ============================================================
# PAGE 1 — PASSWORD
# ============================================================

if st.session_state.page == "password":

    st.markdown(
        """
        <div class="pastel-card">

            <div class="big-heart">💗</div>

            <div class="password-title">
                Waittt... 👀
            </div>

            <div class="main-title">
                Something Special
            </div>

            <p class="subtitle">
                There is a tiny secret hiding here...
                <br>
                But only one very special person can unlock it. ✨
            </p>

            <div class="soft-divider"></div>

            <p class="cute-text">
                🔐 Enter the secret code
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Password",
        type="password",
        label_visibility="collapsed",
        placeholder="Enter the secret code..."
    )

    if st.button("✨ Unlock the surprise ✨"):

        if password == PASSWORD:

            st.session_state.page = "entry_reaction"

            st.rerun()

        else:

            st.session_state.password_attempts += 1

            if st.session_state.password_attempts == 1:

                st.warning("Hmmmm... nope 😌 Try again.")

            elif st.session_state.password_attempts == 2:

                st.info("Okay okay... think carefully 👀")

            else:

                st.error("Aiyo! Wrong again 😂")


# ============================================================
# PAGE 2 — ENTRY REACTION
# ============================================================

elif st.session_state.page == "entry_reaction":

    st.markdown(
        """
        <div class="pastel-card">

            <div class="big-heart">🥹</div>

            <div class="script-title">
                You actually made it!
            </div>

            <p class="subtitle">
                I was wondering if you would figure that out...
            </p>

            <div class="soft-divider"></div>

            <p class="soft-text">
                Okay fine.
                <br>
                Since you are here...
                <br><br>
                I have something to tell you. 💗
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Okay... tell me 👀"):

        st.session_state.page = "welcome"

        st.rerun()


# ============================================================
# PAGE 3 — WELCOME
# ============================================================

elif st.session_state.page == "welcome":

    st.markdown(
        """
        <div class="pastel-card">

            <div class="script-title">
                Helloooo Brightuuuu 💗
            </div>

            <div class="big-heart">
                🫶
            </div>

            <p class="subtitle">
                Today isn't just another day.
            </p>

            <p class="soft-text">
                Because today happens to be the day
                <br>
                one very special human came into this world. 🌸
            </p>

            <div class="soft-divider"></div>

            <p class="cute-text">
                And yes...
                <br>
                this little surprise is for YOU. ✨
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue the surprise 🌷"):

        st.session_state.page = "funny"

        st.rerun()


# ============================================================
# PAGE 4 — FUNNY
# ============================================================

elif st.session_state.page == "funny":

    message = funny_messages[
        st.session_state.funny_index
    ]

    st.markdown(
        f"""
        <div class="pastel-card">

            <div class="section-title">
                Before we get emotional...
            </div>

            <p class="soft-text">
                Let's address the important things first. 😌
            </p>

            <div class="funny-card">

                <div class="big-heart">
                    😂
                </div>

                <div class="funny-text">
                    {message}
                </div>

            </div>

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

        if st.button("Okay okay 😌"):

            st.session_state.page = "wishes"

            st.rerun()


# ============================================================
# PAGE 5 — WISHES
# ============================================================

elif st.session_state.page == "wishes":

    wish = wishes[
        st.session_state.wish_index
    ]

    progress = (
        st.session_state.wish_index + 1
    )

    total = len(wishes)

    st.markdown(
        f"""
        <div class="pastel-card">

            <div class="section-title">
                A little birthday magic 🌸
            </div>

            <p class="progress-text">
                Wish {progress} of {total}
            </p>

            <div class="wish-card">

                <div class="wish-text">
                    {wish}
                </div>

            </div>

            <p class="soft-text">
                Because one birthday wish
                <br>
                is obviously not enough. 💗
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.wish_index < total - 1:

        if st.button("🌷 Next wish"):

            st.session_state.wish_index += 1

            st.rerun()

    else:

        if st.button("💗 There's more..."):

            st.session_state.page = "final_intro"

            st.rerun()


# ============================================================
# PAGE 6 — FINAL INTRO
# ============================================================

elif st.session_state.page == "final_intro":

    st.markdown(
        """
        <div class="pastel-card">

            <div class="big-heart">
                🥹
            </div>

            <div class="script-title">
                Okay Brightuuuu...
            </div>

            <p class="subtitle">
                Enough of the jokes.
            </p>

            <div class="soft-divider"></div>

            <p class="soft-text">

                There is one last thing.

                <br><br>

                And this one is a little more
                <br>
                from the heart. 💗

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Open the last surprise ✨"):

        st.session_state.page = "final"

        st.rerun()


# ============================================================
# PAGE 7 — FINAL
# ============================================================

elif st.session_state.page == "final":

    st.markdown(
        """
        <div class="final-card">

            <div style="font-size:4rem;">
                🎂
            </div>

            <div class="final-name">
                Brightuuuu
            </div>

            <div class="big-heart">
                💗
            </div>

            <div class="final-message">

                Happy Birthday! 🌷

                <br><br>

                I hope this year brings you
                <br>
                more happiness,
                more laughter,
                more beautiful memories,
                and plenty of reasons to smile.

                <br><br>

                Stay exactly the way you are...
                <br>
                because honestly,
                <br>
                you're pretty special. ✨

                <br><br>

                And yes...

                <br>

                <span style="
                    font-family:'Pacifico', cursive;
                    color:#c18ca5;
                    font-size:1.8rem;
                ">
                    Happy Birthday, Brightuuuu 💕
                </span>

            </div>

            <div class="soft-divider"></div>

            <p class="soft-text">
                Made with a little bit of madness,
                <br>
                a lot of affection,
                <br>
                and way too many birthday wishes. 🌸
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🌸 Start again"):

        for key, value in defaults.items():
            st.session_state[key] = value

        st.rerun()
