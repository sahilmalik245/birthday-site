import streamlit as st
import random
import time

# 1. Page Config Setup (Must be first)
st.set_page_config(page_title="Happy Birthday Amna Malik!", page_icon="🎂", layout="centered")

# Custom CSS for Beautiful Extended Theme & Single Entry Animation
st.markdown("""
    <style>
    @keyframes entryAnimation {
        0% { transform: translateY(-50px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    .animated-title { 
        font-size: 52px; 
        font-weight: bold; 
        color: #FF4B4B; 
        text-align: center; 
        text-shadow: 2px 2px #FFD700;
        animation: entryAnimation 1.5s ease-out forwards;
    }
    .sub-title { font-size: 24px; text-align: center; color: #4A4A4A; font-style: italic; }
    .memory-text { font-size: 18px; line-height: 1.6; color: #333333; background-color: #FFF5F5; padding: 15px; border-radius: 10px; border-left: 5px solid #FF4B4B; }
    .timeline-box { background-color: #F0F2F6; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- AUTO ACTION: Website khulne par instant welcome poppers ---
st.balloons()
st.toast("🎉 Amna's Grand Birthday Matrix Fully Loaded! 🥳")

# --- TOP HEADING ---
st.markdown("<div class='animated-title'>🎈 HAPPY BIRTHDAY! 🎈</div>", unsafe_allow_html=True)
st.write("")
st.markdown("<div class='sub-title'>Welcome to your special digital space, Bestie! 🌟</div>", unsafe_allow_html=True)
st.write("---")


# 2. Grand Surprise Bundle
st.header("🎁 1. Grand Surprise Bundle")
if st.button("Click to Unlock Magic! 🤩✨", key="magic_btn"):
    st.balloons()
    st.toast("🍰 Cake cutting sequence enabled!")
    st.success("Happiest Birthday to the most irreplaceable friend! ✨ Having you as my female bestie is a flex. May this year bring you endless success, happiness, aur bohot saari khushiyan! 👑🍿")
    st.write("🎵 **Playing Your Favorite Song: Happy Birthday To You Amna Malik**")
    
    # Audio Setup (Audio file named 'birthday_song.mp3' must be in the folder)
    st.audio("birthday_song.mp3")

st.write("---")


# 3. The Memory Vault
st.header("📸 2. The Memory Vault (Hamari Yaadein)")
tab1, tab2 = st.tabs(["Day 1 🎒", "Fun Moments 😂"])

with tab1:
    st.markdown("""
    <div class='memory-text'>
Pehle din ham dono hi random the, aur aaj hamare darmiyan bht distance hai.
Lekin is distance ne hamari dosti ko kam nahi, balkay aur mazboot kiya hai.
Ap door reh kar bhi mere sab se qareeb hai.Allah se dua hai ke hamari
yeh Dosti hamesha aisa hi qaim rahe.Ameen!"  🤲❤️
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("🤫 **Pranks & Fun Layout:** Click below for a side surprise:")
    if st.button("Trigger Fun Pop-Up! 💥", key="popup_btn"):
        st.snow()
        st.toast("🤪 Caught on camera! Memories are locked.")

st.write("---")


# NEW SECTION 1: Our Friendship Timeline
st.header("⏳ 3. Our Journey Timeline")
st.write("Hum dono waqt ke sath kaise badle, ek choti si nazar:")

st.markdown("""
    <div style="background-color: #F0F2F6; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 12px; color: #333333; font-size: 16px;">
        <b>Phase 1: The Stranger Era 👤</b><br>Ek doosre ko na janna, bas normal randomly kahi dikh jana. Koi idea nahi tha ke hum best friends banenge!
    </div>
    <div style="background-color: #F0F2F6; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 12px; color: #333333; font-size: 16px;">
        <b>Phase 2: The 'Closer Than Ever' Era 🤝</b><br>Baatein shuru huin, vibe match hui, aur dheere dheere sab secrets share hone lage.
    </div>
    <div style="background-color: #F0F2F6; padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 12px; color: #333333; font-size: 16px;">
        <b>Phase 3: The Flex Era 👑</b><br>Now officially: <i>"Having you as my female bestie is a flex!"</i> Hamesha sath rehne ka pakka waada.
    </div>
""", unsafe_allow_html=True)

st.write("---")


# NEW SECTION 2: Interactive Bestie Mood Board
st.header("🎭 4. Amna's Birthday Mood Check")
st.write("Amna, aaj aapka mood kaisa hai? Choose karke screen badlo:")
mood = st.selectbox("Select Your Current Mood:", ["Super Excited 🥰", "Hungry for Cake 🍰", "Lazy Panda 🐼", "Emotional (Khushi ke aansu) 😭"])

if mood == "Super Excited 🥰":
    st.balloons()
    st.success("Yesss! Party ka josh full high hona chahiye! 🎉")
elif mood == "Hungry for Cake 🍰":
    st.snow()
    st.warning("Pehle cake cut hoga, fir sabko milega! 😂")
elif mood == "Lazy Panda 🐼":
    st.info("Utho panda! Aaj sone ka din nahi, enjoy karne ka din hai! 🎒")
elif mood == "Emotional (Khushi ke aansu) 😭":
    st.success("Aansu saaf karo aur smile karo, we are besties forever! ❤️")

st.write("---")


# 4. Friendship Quiz! (Balloons only on correct answer)
st.header("🎮 5. Quick Friendship Quiz!")
st.write("Let's see who knows Amna's routine best. Answer this:")

quiz_ans = st.radio(
    "What is your absolute favorite thing to do in free time?",
    [
        "Sleeping like a panda 🐼", 
        "Scrolling endless Reels 📱", 
        "Chatting with me 💬", 
        "Time spend with other friends 👥"
    ],
    key="quiz_radio"
)

if st.button("Submit Answer 🎯", key="quiz_submit"):
    if quiz_ans == "Chatting with me 💬":
        st.balloons()
        st.success("🎯 100% CORRECT! Ye hui na sacchi dosti! Muje pata tha aap yahi select karoge! 😂")
    else:
        st.error("❌ Oho! Galat jawab! Sacha dost kabhi ye option choose nahi karta! Dubara socho! 😜")

st.write("---")


# NEW SECTION 3: Bestie Rapid Fire (Mini-Game)
st.header("⚡ 6. Bestie Rapid Fire Round")
st.write("In teeno me se apni favorite cheez choose kare:")
choice1 = st.checkbox("Chai over Coffee ☕")
choice2 = st.checkbox("Late Night Chats over Early Morning Talks 🦉")
choice3 = st.checkbox("Sending your sweet and cutest streaks✨")

if st.button("Analyze Choices 🧠"):
    st.snow()
    st.info("Result: Amna Malik is certified 100% A Cool Bestie! 😎")

st.write("---")


# NEW SECTION 4: The Friendly Roast Section (FIXED GLITCH)
st.header("🔥 7. The Friendly Roast Zone")
st.write("Birthday hai toh kya hua, thodi bht masti toh banti hai! Click to read a roast:")

if st.button("Generate a Friendly Roast 💣"):
    roasts = [
        "Amna dunya ki pehli aisi larki hai jo sote sote bhi thak jati hai! 🐼😂",
        "Inki memory itni tez hai ke subah kya khaya tha, shaam ko bhool jati hain! 🧠❌",
        "Reels scroll karne ka counter lagaya jaye toh Amna har saal world record toregi! 📱🏆",
        "Reply chahe 2 ghante baad aaye, par dosti me nakhre pure 24 ghante rehte hain! 😜"
    ]
    selected_roast = random.choice(roasts)
    st.markdown(f"""
        <div style="
            background-color: #FFF0F5; 
            padding: 15px; 
            border-radius: 10px; 
            border: 2px dashed #FF69B4; 
            color: #333333; 
            font-size: 18px; 
            font-weight: bold;
            margin-top: 10px;">
            🔥 {selected_roast}
        </div>
    """, unsafe_allow_html=True)

st.write("---")


# EXTRA FEATURE 1: Virtual Cake Cutting Interaction
st.header("🎂 8. Virtual Cake Cutting")
st.write("Chalo, pehle digital cake cut karte hain! Niche diye gaye button par click karo:")
if st.button("Blow Candles & Cut Cake 🕯️🔪", key="cake_btn"):
    st.snow()
    st.markdown("### 🍰 *OM NOM NOM! Cake successfully cut by Amna Malik!* 🎉")
    st.toast("✨ Sweetest wishes deployed!")

st.write("---")


# NEW SECTION 5: Virtual Gift Shop
st.header("🛍️ 9. Amna's Virtual Gift Shop")
st.write("Aaj aapka birthday hai, toh aap niche diye gaye vouchers me se kuch bhi claim kar sakti hain:")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Your Day 🎂"):
        st.balloons()
        st.success("Claimed! Aj apka birthday hai to jo ap kahe gi mai sab mano ga! 🎟️")
with col2:
    if st.button("No-Argument Pass 🤫"):
        st.snow()
        st.warning("Claimed! Aaj pure din main aap se kisi baat par behes nahi karunga! 😂")
with col3:
    if st.button("Free Unlimited Chai ☕"):
        st.balloons()
        st.info("Claimed! Chai ki chuskiyan hamesha free hain aapke liye!")

st.write("---")


# NEW SECTION 6: Our Future Bucket List
st.header("🗺️ 10. Our Future Bucket List")
st.write("Cheezein jo hamein aage life me sath karni chahiye (Tick if you agree!):")
st.checkbox("Ek Doosre ke sath kabi naraz nhi hona chahiye ✨", value=True)
st.checkbox("Hamesha 1 sath rehna chahiye ❤️", value=True)
st.checkbox("Buddhe hone tak ek doosre ko aise hi tang karna 🧓👵", value=True)
st.checkbox("Kabi bi doosro ko bato me nhi ana 🧠", value=True)

st.write("---")


# EXTRA FEATURE 2: Friendship Certificate Generator
st.header("📜 11. Friendship Certificate")
if st.button("Generate Official Best Friend Certificate 🎖️", key="cert_btn"):
    st.balloons()
    st.info("📜 **CERTIFICATE OF AWESOMENESS**\n\nThis certifies that **Amna Malik** is officially declared as the *Most Caring, Sweetest, and Best Friend in the World* for life! Issued with love on 29th September. ❤️")

st.write("---")


# EXTRA FEATURE 3: Fun Compliment Generator
st.header("💖 12. Click for an Instant Smile")
compliments = [
    "Amna jaisa dost milna dunya me sabse mushkil kaam hai! 🔥",
    "Aapki smile dunya ki sabse best cheez hai, hamesha haste raho! 😁",
    "Puri dunya ek taraf, aur dosto me Amna jaisa heera ek taraf! 💎",
    "Allah hamari dosti ko hamesha har buri nazar se bachaye. Ameen! 🌟"
]
if st.button("Get a Bestie Compliment ✨", key="comp_btn"):
    selected = random.choice(compliments)
    st.snow()
    st.warning(selected)

st.write("---")


# NEW SECTION 7: Top Secret Password Box
st.header("🔒 13. Top Secret Bestie Message")
st.write("Sirf Amna ke liye ek hidden message. Isko kholne ke liye secret key 'bestie123' type karo:")
password = st.text_input("Enter Secret Password:", type="password")

if password == "bestie123":
    st.balloons()
    st.markdown("### 🤫 **SECRET NOTE:**")
    st.write("Agar aapne ye box khol liya hai toh yaad rakhna—Aap meri life ki sabse badi blessing ho. No matter life hume kahan le jaye, ye dosti kabhi kam nahi hogi. Happy Birthday again, Amna! 🌸✨")
elif password:
    st.error("Wrong Password! Sirf sachay bestie ko hi password pata hota hai! 😉")

st.write("---")


# 6. Wishes Box
st.header("💝 14. Leave a Digital Note!")
wish_text = st.text_input("Apna anonymous ya open message yahan type karein:", key="wish_input")
if wish_text:
    st.success(f"Saved: \"{wish_text}\"")
