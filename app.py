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
    {"fr": "noir",
     
