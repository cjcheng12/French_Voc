
import streamlit as st
import random
import json
import os
from gtts import gTTS
from io import BytesIO

# ==========================================
# 1. ONTARIO GRADE 2 FRENCH IMMERSION VOCABULARY LIST
# ==========================================
VOCABULARY = [
    # School & Classroom
    {"fr": "le crayon", "en": "the pencil"},
    {"fr": "le livre", "en": "the book"},
    {"fr": "la gomme", "en": "the eraser"},
    {"fr": "le pupitre", "en": "the desk"},
    {"fr": "la chaise", "en": "the chair"},
    {"fr": "les ciseaux", "en": "the scissors"},
    {"fr": "la colle", "en": "the glue"},
    {"fr": "le sac à dos", "en": "the backpack"},
    {"fr": "le professeur", "en": "the teacher (male)"},
    {"fr": "l'école", "en": "the school"},
    {"fr": "le cahier", "en": "the notebook"},
    {"fr": "la règle", "en": "the ruler"},
    {"fr": "le tableau", "en": "the board"},
    
    # Family & People
    {"fr": "la mère", "en": "the mother"},
    {"fr": "le père", "en": "the father"},
    {"fr": "la sœur", "en": "the sister"},
    {"fr": "le frère", "en": "the brother"},
    {"fr": "la grand-mère", "en": "the grandmother"},
    {"fr": "le grand-père", "en": "the grandfather"},
    {"fr": "le bébé", "en": "the baby"},
    {"fr": "l'ami", "en": "the friend (male)"},
    {"fr": "la famille", "en": "the family"},

    # Animals
    {"fr": "le chien", "en": "the dog"},
    {"fr": "le chat", "en": "the cat"},
    {"fr": "l'oiseau", "en": "the bird"},
    {"fr": "le poisson", "en": "the fish"},
    {"fr": "le cheval", "en": "the horse"},
    {"fr": "la vache", "en": "the cow"},
    {"fr": "le cochon", "en": "the pig"},
    {"fr": "le lapin", "en": "the rabbit"},
    {"fr": "le lion", "en": "the lion"},
    {"fr": "l'ours", "en": "the bear"},
    {"fr": "la souris", "en": "the mouse"},
    {"fr": "le canard", "en": "the duck"},

    # Body Parts
    {"fr": "la tête", "en": "the head"},
    {"fr": "le bras", "en": "the arm"},
    {"fr": "la jambe", "en": "the leg"},
    {"fr": "la main", "en": "the hand"},
    {"fr": "le pied", "en": "the foot"},
    {"fr": "les yeux", "en": "the eyes"},
    {"fr": "le nez", "en": "the nose"},
    {"fr": "la bouche", "en": "the mouth"},
    {"fr": "les cheveux", "en": "the hair"},
    {"fr": "l'oreille", "en": "the ear"},

    # Food
    {"fr": "la pomme", "en": "the apple"},
    {"fr": "la banane", "en": "the banana"},
    {"fr": "le pain", "en": "the bread"},
    {"fr": "le fromage", "en": "the cheese"},
    {"fr": "l'eau", "en": "the water"},
    {"fr": "le lait", "en": "the milk"},
    {"fr": "le poulet", "en": "the chicken"},
    {"fr": "le gâteau", "en": "the cake"},
    {"fr": "l'œuf", "en": "the egg"},
    {"fr": "la pizza", "en": "the pizza"},
    {"fr": "le jus", "en": "the juice"},
    {"fr": "les légumes", "en": "the vegetables"},

    # House & Home
    {"fr": "la maison", "en": "the house"},
    {"fr": "la chambre", "en": "the bedroom"},
    {"fr": "la cuisine", "en": "the kitchen"},
    {"fr": "le salon", "en": "the living room"},
    {"fr": "le lit", "en": "the bed"},
    {"fr": "la porte", "en": "the door"},
    {"fr": "la fenêtre", "en": "the window"},
    {"fr": "la salle de bain", "en": "the bathroom"},
    {"fr": "le jardin", "en": "the garden"},

    # Nature & Weather
    {"fr": "le soleil", "en": "the sun"},
    {"fr": "la lune", "en": "the moon"},
    {"fr": "l'étoile", "en": "the star"},
    {"fr": "le nuage", "en": "the cloud"},
    {"fr": "la pluie", "en": "the rain"},
    {"fr": "la neige", "en": "the snow"},
    {"fr": "l'arbre", "en": "the tree"},
    {"fr": "la fleur", "en": "the flower"},
    {"fr": "il fait beau", "en": "it is nice out"},
    {"fr": "il fait froid", "en": "it is cold"},

    # Clothing
    {"fr": "le pantalon", "en": "the pants"},
    {"fr": "le t-shirt", "en": "the t-shirt"},
    {"fr": "la robe", "en": "the dress"},
    {"fr": "la jupe", "en": "the skirt"},
    {"fr": "les chaussures", "en": "the shoes"},
    {"fr": "le manteau", "en": "the coat"},
    {"fr": "le chapeau", "en": "the hat"},
    {"fr": "les chaussettes", "en": "the socks"},

    # Verbs (Action words)
    {"fr": "manger", "en": "to eat"},
    {"fr": "boire", "en": "to drink"},
    {"fr": "dormir", "en": "to sleep"},
    {"fr": "jouer", "en": "to play"},
    {"fr": "courir", "en": "to run"},
    {"fr": "marcher", "en": "to walk"},
    {"fr": "écouter", "en": "to listen"},
    {"fr": "regarder", "en": "to watch/look"},
    {"fr": "parler", "en": "to speak"},
    {"fr": "lire", "en": "to read"},
    {"fr": "écrire", "en": "to write"},
    {"fr": "nager", "en": "to swim"},
    {"fr": "sauter", "en": "to jump"},
    {"fr": "danser", "en": "to dance"},
    {"fr": "chanter", "en": "to sing"},

    # Colors & Numbers
    {"fr": "rouge", "en": "red"},
    {"fr": "bleu", "en": "blue"},
    {"fr": "vert", "en": "green"},
    {"fr": "jaune", "en": "yellow"},
    {"fr": "noir", "en": "black"},
    {"fr": "blanc", "en": "white"},
    {"fr": "orange", "en": "orange"},
    {"fr": "violet", "en": "purple"},
    {"fr": "un", "en": "one"},
    {"fr": "deux", "en": "two"},
    {"fr": "trois", "en": "three"},
    {"fr": "quatre", "en": "four"},
    {"fr": "cinq", "en": "five"},
    {"fr": "six", "en": "six"},
    {"fr": "sept", "en": "seven"},
    {"fr": "huit", "en": "eight"},
    {"fr": "neuf", "en": "nine"},
    {"fr": "dix", "en": "ten"}
]

# ==========================================
# 2. FILE & STATE MANAGEMENT
# ==========================================
MASTERY_FILE = "word_mastery.json"
MAX_TURNS = 20
MASTERY_THRESHOLD = 5

def load_mastery_data():
    if os.path.exists(MASTERY_FILE):
        with open(MASTERY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_mastery_data(data):
    with open(MASTERY_FILE, "w") as f:
        json.dump(data, f)

def get_valid_question():
    mastery_data = st.session_state.mastery_data
    
    available_pool = [
        w for w in VOCABULARY 
        if mastery_data.get(w["fr"], 0) < MASTERY_THRESHOLD
        and w["fr"] not in st.session_state.session_history
    ]
    
    if not available_pool:
        return None
        
    target_word = random.choice(available_pool)
    
    all_english = [w["en"] for w in VOCABULARY if w["en"] != target_word["en"]]
    distractors = random.sample(all_english, 3)
    
    options = distractors + [target_word["en"]]
    random.shuffle(options)
    
    return {"word": target_word, "options": options}

# --- NEW FUNCTION FOR AUDIO ---
@st.cache_data(show_spinner=False)
def get_pronunciation(text_fr):
    """Generates audio bytes for the given French text."""
    try:
        tts = gTTS(text=text_fr, lang='fr')
        fp = BytesIO()
        tts.write_to_fp(fp)
        return fp
    except Exception as e:
        return None

# ==========================================
# 3. GAME LOGIC & UI
# ==========================================

st.set_page_config(page_title="French Vocab Fun", page_icon="🇫🇷")

if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.score = 0
    st.session_state.turn_count = 0
    st.session_state.session_history = [] 
    st.session_state.game_over = False
    st.session_state.current_q = None
    st.session_state.feedback = None 
    st.session_state.mastery_data = load_mastery_data()
    
    st.session_state.current_q = get_valid_question()

# --- HEADER ---
st.title("🇫🇷 French Vocabulary Adventure")
st.markdown("Listen to the word and choose the English meaning!")

# --- GAME OVER SCREEN ---
if st.session_state.game_over:
    st.success(f"🎉 Game Over! Great job!")
    st.metric(label="Final Score", value=f"{st.session_state.score} / {MAX_TURNS}")
    
    if st.session_state.score >= 15:
        st.balloons()
    
    st.write("---")
    st.write("Words you have mastered (Score 5+) will be removed from future games so you can learn new ones!")
    
    if st.button("Play Again (Start New Game)"):
        st.session_state.score = 0
        st.session_state.turn_count = 0
        st.session_state.session_history = []
        st.session_state.game_over = False
        st.session_state.feedback = None
        st.session_state.current_q = get_valid_question()
        st.rerun()

# --- ACTIVE GAME SCREEN ---
elif st.session_state.current_q is None:
    st.warning("Wow! You have mastered all the words in this list!")
    if st.button("Reset All Progress"):
        save_mastery_data({})
        st.session_state.mastery_data = {}
        st.rerun()

else:
    progress = st.session_state.turn_count / MAX_TURNS
    st.progress(progress, text=f"Question {st.session_state.turn_count + 1} of {MAX_TURNS}")
    st.write(f"**Current Score:** {st.session_state.score}")

    q = st.session_state.current_q
    word_fr = q["word"]["fr"]
    correct_en = q["word"]["en"]
    
    # --- WORD & AUDIO DISPLAY ---
    st.markdown(f"""
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px; text-align:center; margin-bottom:10px;">
        <h1 style="color:#2c3e50;">{word_fr}</h1>
    </div>
    """, unsafe_allow_html=True)

    # Generate Audio
    audio_bytes = get_pronunciation(word_fr)
    if audio_bytes:
        # We center the audio player using columns
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.audio(audio_bytes, format='audio/mp3')

    # --- FEEDBACK STAGE ---
    if st.session_state.feedback:
        is_correct, msg = st.session_state.feedback
        
        if is_correct:
            st.success(msg)
        else:
            st.error(msg)
            st.info(f"The correct answer was: **{correct_en}**")
            
        if st.button("Next Word ➡️"):
            st.session_state.turn_count += 1
            st.session_state.feedback = None
            
            if st.session_state.turn_count >= MAX_TURNS:
                st.session_state.game_over = True
            else:
                st.session_state.current_q = get_valid_question()
            
            st.rerun()

    # --- INPUT STAGE ---
    else:
        st.write("What does this mean in English?")
        
        cols = st.columns(2)
        for i, option in enumerate(q["options"]):
            with cols[i % 2]:
                if st.button(option, use_container_width=True):
                    
                    st.session_state.session_history.append(word_fr)
                    
                    if option == correct_en:
                        st.session_state.score += 1
                        
                        current_mastery = st.session_state.mastery_data.get(word_fr, 0)
                        new_mastery = current_mastery + 1
                        st.session_state.mastery_data[word_fr] = new_mastery
                        save_mastery_data(st.session_state.mastery_data)
                        
                        st.session_state.feedback = (True, "✅ Correct! Great job!")
                    else:
                        st.session_state.feedback = (False, "❌ Oops! That's not quite right.")
                    
                    st.rerun()

st.write("---")
st.caption("Press the 'Play' button ▶️ above to hear the pronunciation.")
                        
