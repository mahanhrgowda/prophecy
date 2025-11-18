import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime  # Still used for positive years where possible, but avoided for extremes
import random

# Emojis for fun - even more added for engagement! 🎉😄
yuga_emojis = {
    "Descending Satya Yuga": "🌟✨😇",  # Golden age sparkle with angel
    "Descending Treta Yuga": "🏹🛡️⚔️",   # Heroic age with shield and sword
    "Descending Dwapara Yuga": "⚔️🔥🤝", # Age of conflict fire with handshake
    "Descending Kali Yuga": "🌑😈💥",    # Dark age devil with explosion
    "Ascending Kali Yuga": "🌒🌱📈",     # Rising from dark growth with up arrow
    "Ascending Dwapara Yuga": "🛡️🚀🤖", # Rising conflict resolution rocket with robot
    "Ascending Treta Yuga": "🦸‍♂️💥🌟",    # Rising heroes boom with star
    "Ascending Satya Yuga": "✨🌈🕊️",     # Rising golden rainbow with dove
    "End of Ascending Satya Yuga": "🏁🎉🔄"  # End of cycle party with recycle
}

# Hindu Yuga Explanations - Made more engaging! 😎📖
yuga_explanations = {
    "Descending Satya Yuga": "🌟✨ The Ultimate Golden Age! 😇 Truth shines like the sun, everyone lives super long (think centuries!), and harmony is everywhere. Pure dharma vibes – no lies, no fights, just enlightenment party! 🎉🧘‍♂️ Imagine a world where everyone's a wise sage chilling in paradise! 🌈",
    "Descending Treta Yuga": "🏹🛡️ The Heroic Silver Age! ⚖️ Virtue dips a bit (75% dharma left), heroes rise with epic quests and rituals. Sacrifices start, but life's still awesome! 💪 Think Ramayana adventures – bows, arrows, and moral dilemmas! 🏹🔥 Exciting times with a touch of drama! 🎭",
    "Descending Dwapara Yuga": "⚔️🔥 The Bronze Age of Balance! 🔄 Half virtue, half vice – conflicts brew, but knowledge from scriptures saves the day. Tech and wars mix! 🤖⚔️ Like Mahabharata battles – Krishna guiding through the chaos! 🛡️😲 A thrilling tug-of-war between good and evil! 🕺",
    "Descending Kali Yuga": "🌑😈 The Iron Age of Darkness! 😔 Only 25% dharma – short lives, greed, strife everywhere. Materialism rules, but it's the plot twist before the comeback! 💥🌪️ Think modern hustle with ancient warnings – time to wake up! ⏰ But hey, every storm passes! 🌧️➡️🌤️",
    "Ascending Kali Yuga": "🌒🌱 Rising from the Shadows! 📈 Slow recovery from chaos – seeds of hope planted, small improvements spark. Dharma starts climbing! 🌱😊 Like emerging from a long night, fresh starts and subtle shifts towards better days! 🌅 Exciting turnaround ahead! 🚀",
    "Ascending Dwapara Yuga": "🛡️🚀 Rising Balance & Tech Boom! 🤝 Halfway to harmony – technology advances, conflicts resolve, knowledge explodes! 📚💡 We're in this now (2025 vibes!) – think AI, space, but with growing wisdom! 🤖🌌 Super engaging era of innovation! 🎨",
    "Ascending Treta Yuga": "🦸‍♂️💥 Rising Heroes & Strength! 💪 Virtue at 75% – great leaders, discoveries, epic comebacks. Dharma strengthens! 🏆 Like future legends rising – adventures, breakthroughs, and moral wins! 🌟😄 Can't wait for this heroic upgrade! 🦸‍♀️",
    "Ascending Satya Yuga": "✨🌈 Rising Back to Golden Bliss! 🕊️ Full dharma restored – long lives, universal peace, spiritual highs. Enlightenment for all! 😇🌍 Imagine a utopian future where harmony reigns supreme! 🎊 Pure joy and cosmic connection! 🔮",
    "End of Ascending Satya Yuga": "🏁🎉 Cycle Wrap-Up! 🔄 End of the full precession swing – ready for cosmic renewal. Party time before the next loop! 🥳🌌 Like finishing a grand adventure, only to start an even better one! 📖➡️📖"
}

# Data from chat history
yuga_data = [
    {"Yuga Phase": "Descending Satya Yuga", "Start Date": "14699 BCE-09-25"},
    {"Yuga Phase": "Descending Treta Yuga", "Start Date": "9545 BCE-02-18"},
    {"Yuga Phase": "Descending Dwapara Yuga", "Start Date": "5679 BCE-12-07"},
    {"Yuga Phase": "Descending Kali Yuga", "Start Date": "3102 BCE-02-18"},
    {"Yuga Phase": "Ascending Kali Yuga", "Start Date": "1813 BCE-09-25"},
    {"Yuga Phase": "Ascending Dwapara Yuga", "Start Date": "525 BCE-05-01"},
    {"Yuga Phase": "Ascending Treta Yuga", "Start Date": "2053 CE-07-14"},
    {"Yuga Phase": "Ascending Satya Yuga", "Start Date": "5919 CE-05-02"},
    {"Yuga Phase": "End of Ascending Satya Yuga", "Start Date": "11074 CE-09-25"}
]

# Image URLs for comparisons (public domain) - added Zuni
comparison_images = {
    "Mayan": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Mayancalender1.JPG",
    "Aztec": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Aztec_calendar.jpeg",
    "Inca": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Inca_Quipu.jpg",
    "Egyptian": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Sirius_A_and_B_Hubble_photo.jpg",
    "Hopi": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Hopi_prophecy_rock.jpg",
    "Zuni": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Zuni_Pueblo%2C_New_Mexico_IMG_5595.JPG"  # Zuni Pueblo image as proxy
}

# Fun facts for random generation - added more with Zuni! 🎲
fun_facts = [
    "Did you know? The Mayan Long Count starts around 3114 BCE, just 12 years before Kali Yuga! 🗓️🎉😲",
    "Aztec Five Suns mythology involves world destructions, similar to Yuga cycles' renewals! 💥🔥🌋",
    "Inca used quipus for timekeeping – knotted strings as calendars! 🪢🏔️🤓",
    "Egyptian Sothic cycle resets every ~1460 years, tied to Sirius rising! ⭐🐶✨",
    "We're currently in Ascending Dwapara Yuga – tech boom ahead? 🚀🛡️🤖",
    "Hopi prophecies speak of Four Worlds destroyed by corruption, like Yuga descents! 🌍😱🪶",
    "Zuni myths: Emerge from four underworlds – slimy starts to daylight harmony! 🕳️➡️☀️😄",
    "Satya Yuga is the age of pure truth – imagine no lies, just bliss! 🌟🤩😇",
    "Kali Yuga: Chaos central, but ascent brings epic comebacks! 🌑➡️🌒💫🚀"
]

# Parse year to numerical float (BCE negative, with fractional for month/day)
def parse_year_num(date_str):
    if "BCE" in date_str:
        year_str = date_str.split(" BCE")[0]
        year = -int(year_str)
        month_day = date_str.split("-")[1:]
    else:
        parts = date_str.split(" CE-")
        year = int(parts[0])
        month_day = parts[1].split("-")
    month = int(month_day[0])
    day = int(month_day[1])
    fractional = (month - 1) / 12 + day / 365.25
    return year + fractional if year > 0 else year - fractional

df = pd.DataFrame(yuga_data)
df['Year Num'] = df['Start Date'].apply(parse_year_num)

# Function to find Yuga for a given numerical year
def find_yuga(input_year_num):
    for i in range(len(df) - 1):
        if df['Year Num'][i] <= input_year_num < df['Year Num'][i+1]:
            return df['Yuga Phase'][i], yuga_emojis.get(df['Yuga Phase'][i], "🔄")
    return "Beyond the Cycle", "❓"

# App title with fun emoji and animation 🎈
st.title("Cosmic Yuga Explorer: Precession Edition! 🚀🌌✨😄 With Calculations, Prophecies & More! 🎉🔮")
st.balloons()  # Fun animation on load! 🎊

st.write("Blast off into the refactored Yuga cycles! 🌟 Now with detailed math breakdowns, Zuni prophecies, Krishna's date detective story, tons of emojis, and super engaging tales! 😎📖 Current date (Nov 18, 2025) is in Ascending Dwapara Yuga 🛡️🚀🤖 – tech vibes strong, 29 years till heroic Treta! 🦸💥🎊")

# Section 0: Hindu Yuga Explanations - Already engaging! 📖
st.header("Hindu Yuga Explanations: Epic Cosmic Stories! 📖🌟😲")
st.write("Dive into each Yuga like a thrilling adventure novel – with emojis, fun facts, and why they rock! 🕺✨ Click to expand the magic! 🔮")
for phase, expl in yuga_explanations.items():
    emoji = yuga_emojis.get(phase, "🔄")
    with st.expander(f"{emoji} {phase} – Click for the Full Scoop! 🎉"):
        st.write(expl)
        st.write("---")  # Separator for readability

# New Section: Detailed Yuga Duration Calculations 🔢✨
st.header("Yuga Math Magic: How We Crunched the Numbers! 🔢🚀😄")
st.write("Ever wonder how we shrunk ancient Yugas to fit Earth's wobbly spin? 🌍🎢 Let's break it down like a cosmic recipe – step by step, with emojis and excitement! 📏💥 No boring lectures, just fun facts and formulas! 🤓🎉")

with st.expander("Step 1: Base Precession Cycle 🌌🌀"):
    st.write("Earth's axis wobbles like a top! Full cycle: **25,772 years** 😲 (astronomy fact!). Half arc (descending swing): **12,886 years** – our Mahayuga base! 🎾💨")

with st.expander("Step 2: Ratio Division – 4:3:2:1 Magic! ⚖️✨"):
    st.write("Ratios add up to 10 parts! Unit: **12,886 ÷ 10 = 1,288.6 years** 🔢. Then: Satya (4) = **5,154.4 yrs** 🌟, Treta (3) = **3,865.8 yrs** 🏹, Dwapara (2) = **2,577.2 yrs** ⚔️, Kali (1) = **1,288.6 yrs** 🌑. Boom – descending done! 💥")

with st.expander("Step 3: Sandhi Twilights – Buffer Zones! 🌗🕰️"):
    st.write("Sandhi = 10% pure length each end! Total = Pure × 1.2 📈. E.g., Kali Pure: **1,073.8 yrs** 😈, Sandhi: **107.4 yrs** each 🎥. Like smooth fades in a movie – blending eras! 🌅")

with st.expander("Step 4: Big Picture – Manvantara & Kalpa! 📚🌌"):
    st.write("Manvantara: 71 Mahayugas = **914,906 yrs** 😱. Kalpa: 1,000 Mahayugas = **12,886,000 yrs** ☕. Cosmic seasons for the soul – winter to spring vibes! ❄️➡️🌸")

st.write("These calcs tie ancient wisdom to real stars – flexible and fascinating! 🔭😄 If precession tweaks, so do we! 📐")

# New Section: Krishna's Death Date – Start of Desc Kali! 🕵️‍♂️📜
st.header("Detective Mode: How We Pinned Krishna's Death Date! 🕵️‍♂️🔮😎")
st.write("Buckle up for a cosmic whodunit – anchoring Descending Kali Yuga to Feb 18, 3102 BCE! 🌑💥 Based on Mahabharata clues, astronomy, and epic math. No time machine needed – just stars and shlokas! ⭐📜🎉")

with st.expander("Clue 1: Mahabharata Astro References! 🌌⚔️"):
    st.write("Vyasa's epic drops planetary hints during Kurukshetra War: Saturn in Rohini 😠, Jupiter in Shravana 🌟, Mars retro in Jyeshta-Anuradha 🔄, eclipses close together 🌑☀️, comet at Pushya ☄️. Like a celestial puzzle! 🧩")

with st.expander("Clue 2: Krishna's Death – 36 Years Post-War! ⏳😔"):
    st.write("Krishna dips out 36 years after the battle – Moon in Revati Nakshatra Pada 4 🌙, with a solar eclipse! 🔭 Anchors the timeline – war in ~3138 BCE, death in 3102 BCE. Epic link! 📅💔")

with st.expander("Clue 3: Precession & Yuga Tie-In! 🌀🔗"):
    st.write("We refactor Yugas to precession (25,772 yrs) – but date stays fixed via astro matches. Software sims (like Planetarium) confirm positions! 🤖⭐ Other dates (e.g., 3067 BCE war) don't fit Revati eclipse perfectly. Winner: Feb 18, 3102 BCE! 🏆😄")

st.write("This blend of ancient texts, modern astronomy, and math magic makes history alive! 📖🚀 Questions? Dive deeper! 🔍")

# Section 1: Yuga Timeline - Enhanced with numerical years! 📅
st.header("Yuga Cycle Timeline: Visual Cosmic Journey! 📅✨🔄😄")
st.write("Zoom through time with emojis galore! 🕰️🎨 Current spot marked – feel the vibes! 🌟 (BCE years negative for epic scale!)")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df['Year Num'], [1] * len(df), 'o-', color='purple')
ax.set_yticks([])
for i, row in df.iterrows():
    ax.text(row['Year Num'], 1.05, f"{yuga_emojis.get(row['Yuga Phase'], '🔄')} {row['Yuga Phase']}", rotation=45, ha='right', va='bottom')
plt.title("Yuga Cycle Timeline 🌟💫🎉")
plt.xlabel("Year (BCE negative, CE positive) ⏳😎")
st.pyplot(fig)

# Interactive Date Checker with spinner animation 🔍
st.header("Time Portal: Find Your Yuga Spot! ⏳🔍✨😲")
st.write("Punch in a date – zap to its Yuga! Negative years for BCE (e.g., -3102). Let's time travel! 🚀🕰️")

col1, col2, col3 = st.columns(3)
with col1:
    year = st.number_input("Year 📆😄", min_value=-15000, max_value=12000, value=2025)
with col2:
    month = st.number_input("Month 🌙✨", min_value=1, max_value=12, value=11)
with col3:
    day = st.number_input("Day ☀️🌟", min_value=1, max_value=31, value=18)

if st.button("Zap to Yuga! 🔮💥"):
    with st.spinner("Warping through cosmic time... ⏳✨🚀"):
        user_year_num = year + ((month - 1) / 12 + day / 365.25) if year > 0 else year - ((month - 1) / 12 + day / 365.25)
        yuga_phase, emoji = find_yuga(user_year_num)
        st.success(f"Whoosh! On {year}-{month:02d}-{day:02d}, you're in **{yuga_phase}** {emoji}! 🎉💥 Epic era alert! 😄")
        st.balloons()  # Animation on success! 🎈

# Section 2: Cultural Comparisons with Images - added Zuni! 🌍
st.header("Global Cosmic Party: Cultural Comparisons! 🌍🤝🎭✨😄")
st.write("Pick a culture for mind-blowing parallels, pics, and prophecy fun! 🖼️😲 Now with Zuni emergence tales! 🕳️☀️🔥")

culture = st.selectbox("Choose Your Cosmic Buddy: 🌐😎", ["Mayan", "Aztec", "Inca", "Egyptian", "Hopi", "Zuni"])

if culture == "Mayan":
    st.subheader("Mayan Long Count: Time Wizards! 🗿📜🌌😲")
    st.write("Starts ~3114 BCE (Kali twin!) 🌑😈, 5,125-yr cycles match Dwapara vibes 🔄⚔️. 2012 rollover bash! 🎉🥳 Emoji: 🌀💫 – Spin through worlds! 🌀")
    st.image(comparison_images["Mayan"], caption="Mayan Calendar Magic! 🗓️✨", use_column_width=True)

elif culture == "Aztec":
    st.subheader("Aztec Calendars: Sun Warriors! ☀️🗡️🔥💥")
    st.write("Five Suns with epic ends 💥🌋, like Yuga drops. 52-yr ritual resets 🕯️🙏. Sacrifices for sun power! 🔥😤 Emoji: 🌞🌅 – Blaze on! ☀️")
    st.image(comparison_images["Aztec"], caption="Aztec Sun Stone Epic! ☀️😄", use_column_width=True)

elif culture == "Inca":
    st.subheader("Inca Timekeeping: Mountain Mystics! 🏔️🌌🦙🤓")
    st.write("Pachakuti ~1,000-yr flips 🔄🌀, echo Yuga shifts. Solstice parties 🎊🥳 with quipus! 🪢 Fun: Knot your calendar! 😅 Emoji: 🦙🏞️ – Llama stars! 🦙")
    st.image(comparison_images["Inca"], caption="Inca Quipu Knots! 🪢✨", use_column_width=True)

elif culture == "Egyptian":
    st.subheader("Egyptian Sothic: Star Flood Party! 🐶⭐💦🌊")
    st.write("~1,460-yr resets 🔄🗓️, Nile vibes 💦. ~4242 BCE starts! ⭐ Sirius as Isis pup! 🐕✨🤩 Emoji: 🐚🌟 – River renewal! 🌊")
    st.image(comparison_images["Egyptian"], caption="Sirius Star Glow! ⭐😲", use_column_width=True)

elif culture == "Hopi":
    st.subheader("Hopi Prophecies: World Hoppers! 🌎🔥🪶😱")
    st.write("Four Worlds zapped by bad vibes 😱💥, like Yuga falls. Fifth coming with blue star! 🌍➡️🌈 Emoji: 🪶🌟 – Feather visions! 🪶")
    st.image(comparison_images["Hopi"], caption="Hopi Prophecy Rock! 🪨✨", use_column_width=True)

elif culture == "Zuni":
    st.subheader("Zuni Prophecies: Emergence Adventures! 🕳️☀️🪶😄")
    st.write("Four underworlds: Dark slime to daylight harmony! 🕳️➡️☀️💦 Adapt with divine tweaks (tails off!) 🍿😲 Like Yuga evolutions – kachina dances renew! 🕺🌌 Emoji: 🪶💫 – Spirit spins! 🌀")
    st.image(comparison_images["Zuni"], caption="Zuni Pueblo Vibes! 🏘️✨", use_column_width=True)

# Fun Random Fact Generator with animation 🎲
st.header("Cosmic Fact Blaster: Random Surprises! 🎲😄💥🤯")
if st.button("Blast a Fact! 🌟🚀"):
    with st.spinner("Charging the fact cannon... 🎡✨💥"):
        fact = random.choice(fun_facts)
        st.info(f"Boom! {fact} 😲🎉 Epic, right? Share with friends! 👯‍♂️")
        st.snow()  # Snow animation for fun! ❄️

# Birth Year Interactive 👶
st.header("Birth Yuga Quest: Your Origin Story! 👶⏳✨😎")
user_birth_year = st.slider("Slide to your birth year: 📅🎂", 1900, 2100, 2000)
user_birth_year_num = user_birth_year  # Approximate, no fractional needed for year-only
yuga_phase, emoji = find_yuga(user_birth_year_num)
st.write(f"Zap! Born in {user_birth_year}? Your cosmic home: **{yuga_phase}** {emoji}! BCE? Use date checker. 🕰️😄 Destiny unlocked! 🔑🌟")

st.write("Launch this cosmic app with `streamlit run app.py` – explore, learn, and vibe! 🌈🚀😄 Integrated research, new sections, emojis everywhere – pure fun! 🎊💫🔮")
