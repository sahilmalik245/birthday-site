import streamlit as st
import datetime
import time

# 1. Page Config Setup (Must be first)
st.set_page_config(page_title="Happy Birthday Space!", page_icon="🎂", layout="centered")

# Custom CSS for Beautiful Dark/Colorful Theme
st.markdown("""
    <style>
    .main-title { font-size: 55px; font-weight: bold; color: #FF4B4B; text-align: center; text-shadow: 2px 2px #FFD700; }
    .sub-title { font-size: 26px; text-align: center; color: #4A4A4A; font-style: italic; }
    .countdown-box { background-color: #FFF0F5; padding: 15px; border-radius: 10px; border: 2px dashed #FF69B4; text-align: center; font-size: 20px; font-weight: bold; color: #FF1493; }
    </style>
""", unsafe_allow_html=True)

# 2. Setup Birthday Date (Yahan apne dost ka birthday saal, mahina, din set karein)
# Example: 2026, December 25th (Change this to your friend's real birthday date!)
birthday_date = datetime.datetime(2026, 12, 25, 0, 0, 0)
current_time = datetime.datetime.now()

# 3. Welcome Header
st.markdown("<div class='main-title'>🎉 HAPPY BIRTHDAY! 🎉</div>", unsafe_allow_html=True)
st.write("")
dost_ka_naam = "Bestie" 
st.markdown(f"<div class='sub-title'>Welcome to your special digital universe, {dost_ka_naam}! 🌟</div>", unsafe_allow_html=True)
st.write("---")

# FEATURE 1: Live Countdown Timer
st.subheader("⏳ Countdown to the Big Day!")
if birthday_date > current_time:
    time_left = birthday_date - current_time
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    st.markdown(f"<div class='countdown-box'>🎁 Only {days} Days, {hours} Hours, and {minutes} Minutes left for the party! 🥳</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='countdown-box'>🔥 IT'S PARTY TIME! THE COUNTDOWN IS OVER! 🍰</div>", unsafe_allow_html=True)
st.write("---")

# FEATURE 2: Super Surprise Button (Balloons + Confetti + Music)
st.subheader("🎁 Open Your Grand Surprise Bundle...")
if st.button("Click to Unlock Magic! 🤩✨"):
    # Streamlit built-in features
    st.balloons()
    st.snow() # Snow flakes overlay as extra glitter effect
    
    st.success(f"Happiest Birthday to the most irreplaceable friend! ✨ May this year bring you endless success, late-night food trips, aur bohot saari khushiyan! 🍗🍿")
    
    # Background Music Track
    st.write("🎵 *Playing Birthday Special Track for you...*")
    st.audio("https://soundhelix.com") 

st.write("---")

# FEATURE 3: Memory Lane Tabs with Dynamic Layout
st.subheader("📸 The Memory Vault (Hamari Yaadein)")
tab1, tab2, tab3 = st.tabs(["Day 1 🎒", "The Epic Trip 🚗", "Pranks & Fun 😂"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("🎈 **Old Times:**")
    with col2:
        st.info("Uncomment standard 'st.image' codes to add real photos here! (e.g., photo1.jpg)")
        # st.image("photo1.jpg", caption="School/College ka pehla din")

with tab2:
    st.warning("✈️ Trip memories blueprint ready! Place your favorite travel picture inside your project folder.")
    # st.image("photo2.jpg", caption="The unforgettable road trip!")

with tab3:
    st.error("🤫 Warning: Don't leak these funny faces to public social media!")
    # st.image("photo3.jpg", caption="Craziest face ever!")

st.write("---")

# FEATURE 4: Interactive Friend Quiz (Mini-Game)
st.subheader("🎮 Quick Friendship Quiz!")
st.write(f"Let's see who knows {dost_ka_naam} best! Answer this secret question:")

quiz_ans = st.radio(
    f"What is {dost_ka_naam}'s absolute favorite thing to do in free time?",
    ["Sleeping like a panda 🐼", "Scrolling endless Reels 📱", "Eating Biryani 🍗", "Studying coding 💻"]
)

if st.button("Submit Answer 🎯"):
    if quiz_ans == "Eating Biryani 🍗":
        st.balloons()
        st.success("🎯 100% CORRECT! Aap sacha yaar ho! Biryani lover is always a winner!")
    else:
        st.error("❌ Wrong! Try again, ya toh apne dost se dosti tod do! 😂")

st.write("---")

# 5. Wishes Box (Data input tracking layer)
st.subheader("💝 Leave a Digital Note!")
wish_text = st.text_input("Apna anonymous ya open message yahan type karein:")
if wish_text:
    st.success(f"Saved: \"{wish_text}\" (Yeh code system back-end me permanently store kar sakta hai!)")
