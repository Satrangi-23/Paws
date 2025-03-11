import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
from PIL import Image
import base64
import io
import random

# Page configuration
st.set_page_config(
    page_title="Happy Birthday Nikita🐽!",
    page_icon="🎂🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #ff6b6b, #6b6bff);
            color: white;
        }
        .st-emotion-cache-16txtl3 h1, h2, h3 {
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .birthday-title {
            font-size: 3.5rem;
            text-align: center;
            margin-bottom: 1rem;
            font-family: 'Comic Sans MS', cursive;
            animation: rainbow 5s infinite;
        }
        .message-box {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            backdrop-filter: blur(5px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            background-color: #f00;
            border-radius: 50%;
            animation: fall 5s linear infinite;
        }
        @keyframes rainbow {
            0% { color: red; }
            14% { color: orange; }
            28% { color: yellow; }
            42% { color: green; }
            57% { color: blue; }
            71% { color: indigo; }
            85% { color: violet; }
            100% { color: red; }
        }
        @keyframes fall {
            0% { transform: translateY(-100px) rotate(0deg); }
            100% { transform: translateY(100vh) rotate(360deg); }
        }
        .birthday-cake {
            text-align: center;
            font-size: 6rem;
            margin: 20px 0;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
        }
        .gift-box {
            cursor: pointer;
            font-size: 5rem;
            display: inline-block;
            margin: 0 10px;
            transition: transform 0.3s ease;
        }
        .gift-box:hover {
            transform: scale(1.2);
        }
        .st-emotion-cache-16txtl3 button {
            background-color: #ff6b6b;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .st-emotion-cache-16txtl3 button:hover {
            background-color: #ff4f4f;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Add confetti elements
    confetti_html = ""
    for i in range(50):
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        color = f"hsl({random.randint(0, 360)}, 100%, 50%)"
        confetti_html += f"""
        <div class="confetti" style="left: {left}vw; 
                                     animation-delay: {delay}s; 
                                     background-color: {color};">
        </div>
        """
    st.markdown(confetti_html, unsafe_allow_html=True)

# Apply custom CSS
local_css()

# Sidebar
st.sidebar.markdown("<h2 style='text-align: center; color: Black;'>Birthday Menu</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["🏠 Home", "🎁 Gifts", "📸 Photo Gallery", "🎮 Birthday Games", "✉️ Leave a Message"])

# Home page
if menu == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 class='birthday-title'>Happy Birthday Nikita! 🎉</h1>", unsafe_allow_html=True)
        
        # Countdown if birthday is in the future, otherwise celebration
        today = datetime.now()
        
        # You can set Nikita's birthday here - for demonstration, using a date
        # Format: year, month, day
        birthday = datetime(today.year, 7, 15)  # Change to actual birthday
        
        # If birthday has passed this year, set to next year
        if today.date() > birthday.date():
            birthday = datetime(today.year + 1, birthday.month, birthday.day)
            
        # Calculate days until birthday
        delta = birthday - today
        
        if delta.days > 0:
            st.markdown(f"<h3 style='text-align: center;'>🎂 Countdown to your special day: {delta.days} days!</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='text-align: center;'>🎂 Today is your day! Have an amazing birthday!</h3>", unsafe_allow_html=True)
            st.balloons()
        
        # Birthday cake
        st.markdown("<div class='birthday-cake'>🎂</div>", unsafe_allow_html=True)
        
        # Birthday wish
        st.markdown("<div class='message-box'>", unsafe_allow_html=True)
        st.markdown("""
        <h2 style='text-align: center;'>Wishing You...</h2>
        <p style='text-align: center; font-size: 1.2rem;'>
        A day filled with happiness and a year filled with joy.<br>
        May your life be painted with colors of happiness, success, and good health!<br>
        Thank you for being such an amazing person!
        </p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Birthday music
        st.markdown("<h3 style='text-align: center;'>🎵 Birthday Music 🎵</h3>", unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Gifts page
elif menu == "🎁 Gifts":
    st.markdown("<h1 class='birthday-title'>Special Gifts For You!</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Click on a gift to unwrap it!</p>", unsafe_allow_html=True)
    
    # Create gift rows
    col1, col2, col3 = st.columns(3)
    
    # Gift 1
    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        gift1 = st.button("🎁 Motivational Quote")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if gift1:
            st.markdown("<div class='message-box'>", unsafe_allow_html=True)
            st.markdown("""
            <h3 style='text-align: center;'>Just For You:</h3>
            <p style='text-align: center; font-size: 1.5rem; font-style: italic;'>
            "The future belongs to those who believe in the beauty of their dreams."<br>
            - Eleanor Roosevelt
            </p>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Gift 2
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        gift2 = st.button("🎁 Virtual Cake")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if gift2:
            st.markdown("<div class='message-box' style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<h3>Your Virtual Cake:</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div style='font-size: 3rem; line-height: 1.2;'>
            🍰🍰🍰<br>
            🍰🎂🍰<br>
            🍰🍰🍰
            </div>
            <p>Make a wish and blow out the candles! 🕯️</p>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Gift 3
    with col3:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        gift3 = st.button("🎁 Birthday Poem")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if gift3:
            st.markdown("<div class='message-box'>", unsafe_allow_html=True)
            st.markdown("""
            <h3 style='text-align: center;'>A Birthday Poem For Nikita:</h3>
            <p style='text-align: center; font-size: 1.2rem;'>
            Another year of laughter and joy,<br>
            Another year of memories to deploy.<br>
            Happy Birthday, Nikita, you're one of a kind,<br>
            A better friend, one could never find.<br><br>
            May your day be as wonderful as you,<br>
            Filled with happiness and dreams come true!
            </p>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Additional virtual gifts
    st.markdown("<h3 style='text-align: center; margin-top: 30px;'>More Virtual Gifts!</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div style='text-align: center;' class='gift-box' title='Virtual Flowers'>💐</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align: center;' class='gift-box' title='Virtual Chocolate'>🍫</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div style='text-align: center;' class='gift-box' title='Virtual Gift Card'>🎟️</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div style='text-align: center;' class='gift-box' title='Virtual Balloon'>🎈</div>", unsafe_allow_html=True)

# Photo Gallery
elif menu == "📸 Photo Gallery":
    st.markdown("<h1 class='birthday-title'>Birthday Memories</h1>", unsafe_allow_html=True)
    
    st.info("Upload photos to create a personalized birthday gallery for Nikita!")
    
    # Photo upload feature
    uploaded_files = st.file_uploader("Upload Birthday Photos", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} photos uploaded successfully!")
        
        # Display uploaded photos in a grid
        cols = st.columns(3)
        for i, uploaded_file in enumerate(uploaded_files):
            with cols[i % 3]:
                st.image(uploaded_file, caption=f"Photo {i+1}", use_column_width=True)
    
    # Sample gallery (replace with actual photos of Nikita)
    st.markdown("<h3 style='text-align: center;'>Sample Birthday Themes</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div style='text-align: center; font-size: 5rem;'>🎂</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Cake Theme</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='text-align: center; font-size: 5rem;'>🎉</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Party Theme</p>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div style='text-align: center; font-size: 5rem;'>🎁</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Gift Theme</p>", unsafe_allow_html=True)

# Birthday Games
elif menu == "🎮 Birthday Games":
    st.markdown("<h1 class='birthday-title'>Fun Birthday Games</h1>", unsafe_allow_html=True)
    
    game_selection = st.selectbox("Choose a game to play:", 
                                 ["Birthday Trivia", "Fortune Teller", "Birthday Word Scramble"])
    
    if game_selection == "Birthday Trivia":
        st.markdown("<div class='message-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Birthday Trivia Quiz</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Test your knowledge about birthdays!</p>", unsafe_allow_html=True)
        
        q1 = st.radio("1. What is the most common birth month in the US?",
                     ["January", "July", "August", "September"])
        
        q2 = st.radio("2. Which famous person shares Nikita's birthday?",
                     ["Albert Einstein", "Add actual celebrity", "Leonardo da Vinci", "Marie Curie"])
        
        q3 = st.radio("3. The 'Happy Birthday' song was first published in what year?",
                     ["1893", "1912", "1924", "1938"])
        
        if st.button("Check Answers"):
            score = 0
            if q1 == "September":
                score += 1
            if q2 == "Add actual celebrity":  # Change to actual answer
                score += 1
            if q3 == "1893":
                score += 1
            
            st.success(f"You got {score} out of 3 correct!")
            
            if score == 3:
                st.balloons()
                st.markdown("<p style='text-align: center; font-size: 1.5rem;'>Perfect Score! 🎉</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif game_selection == "Fortune Teller":
        st.markdown("<div class='message-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Birthday Fortune Teller</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Discover what your new year of life has in store!</p>", unsafe_allow_html=True)
        
        if st.button("Reveal My Fortune"):
            fortunes = [
                "This year will bring you unexpected joy and success in your endeavors!",
                "A new friendship will blossom into something extraordinary!",
                "Adventure awaits you - be ready to embark on an exciting journey!",
                "Your creativity will reach new heights this year!",
                "Good health and prosperity are coming your way!",
                "A long-held wish will finally come true this year!",
                "You will discover a hidden talent that will amaze everyone!",
                "This year will be filled with laughter and memorable moments!"
            ]
            
            fortune = random.choice(fortunes)
            
            # Animation effect
            with st.spinner("Reading the stars... 🔮"):
                time.sleep(2)
            
            st.markdown(f"<h2 style='text-align: center;'>Your Birthday Fortune:</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 1.5rem; font-style: italic;'>{fortune}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif game_selection == "Birthday Word Scramble":
        st.markdown("<div class='message-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Birthday Word Scramble</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Unscramble these birthday-related words!</p>", unsafe_allow_html=True)
        
        words = {
            "AETKBIYHCDARP": "BIRTHDAYCAKE",
            "RSTNEEPS": "PRESENTS",
            "ASRBTYLALOCINEE": "CELEBRATIONDAY",
            "IHSWES": "WISHES",
            "ITARSYHEANNPVR": "HAPPYANNIVERSARY"
        }
        
        # Select a random word
        scrambled_word = random.choice(list(words.keys()))
        correct_word = words[scrambled_word]
        
        st.markdown(f"<h2 style='text-align: center;'>Unscramble this word:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 2rem; letter-spacing: 3px;'>{scrambled_word}</p>", unsafe_allow_html=True)
        
        user_guess = st.text_input("Your answer:", "").upper().strip()
        
        if st.button("Check Answer"):
            if user_guess == correct_word:
                st.success("Correct! 🎉")
                st.balloons()
            else:
                st.error("Not quite. Try again!")
                if st.button("Show Hint"):
                    st.info(f"Hint: The first three letters are {correct_word[:3]}")
        st.markdown("</div>", unsafe_allow_html=True)

# Leave a Message
elif menu == "✉️ Leave a Message":
    st.markdown("<h1 class='birthday-title'>Leave Nikita a Birthday Message</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='message-box'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Write a special birthday wish for Nikita!</p>", unsafe_allow_html=True)
    
    name = st.text_input("Your Name:")
    relation = st.text_input("How do you know Nikita?")
    message = st.text_area("Your Birthday Message:", height=150)
    rating = st.slider("Rate how awesome Nikita is:", 1, 10, 10)
    
    if st.button("Send Birthday Wish"):
        if name and message:
            st.success("Your message has been sent! 🎉")
            st.markdown("<div style='background-color: rgba(255, 255, 255, 0.2); border-radius: 10px; padding: 15px; margin-top: 20px;'>", unsafe_allow_html=True)
            st.markdown(f"<h3>From: {name}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p><strong>Relationship:</strong> {relation}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><strong>Message:</strong> {message}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><strong>Awesomeness Rating:</strong> {'⭐' * rating}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><em>Sent on {datetime.now().strftime('%B %d, %Y at %H:%M')}</em></p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Add confetti celebration
            st.balloons()
        else:
            st.warning("Please fill in your name and message.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Display some sample messages
    st.markdown("<h3 style='text-align: center; margin-top: 30px;'>Birthday Message Wall</h3>", unsafe_allow_html=True)
    
    sample_messages = [
        {"name": "Friend1", "relation": "Friend", "message": "Happy Birthday! Have an amazing day!", "rating": 10},
        {"name": "Family1", "relation": "Family", "message": "Wishing you all the best on your special day!", "rating": 10}
    ]
    
    for msg in sample_messages:
        st.markdown("<div style='background-color: rgba(255, 255, 255, 0.2); border-radius: 10px; padding: 15px; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<h4>From: {msg['name']}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Relationship:</strong> {msg['relation']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Message:</strong> {msg['message']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Awesomeness Rating:</strong> {'⭐' * msg['rating']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 50px; padding: 20px; background-color: rgba(0, 0, 0, 0.2); border-radius: 10px;'>
    <p>Made with ❤️ for Nikita's Birthday</p>
    <p>© 2025 Birthday Celebration App</p>
</div>
""", unsafe_allow_html=True)
