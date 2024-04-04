import tkinter as tk
from tkinter import ttk
import random
import os

# Emotion dictionary with origins
emotions = {
    'happy': {
        'english': [{'word': 'joy', 'origin': 'Middle English: from Old French joie, based on Latin gaudium, from gaudere ‘rejoice’'},
                    {'word': 'delight', 'origin': 'Middle English: from Old French delitier, from Latin delectare ‘to charm’'},
                    {'word': 'ecstasy', 'origin': 'Late Middle English: from Old French extasie, via late Latin from Greek ekstasis ‘standing outside oneself’'},
                    {'word': 'cheerful', 'origin': 'Late Middle English: from cheer + -ful'},
                    {'word': 'bliss', 'origin': 'Middle English: perhaps related to bliss'},
                    {'word': 'jubilant', 'origin': 'Late Middle English: from Latin jubilant- ‘shouting for joy’'},
                    {'word': 'euphoria', 'origin': 'Late 18th century: from Greek euphoria, from euphoros ‘borne well, cheerful’, from eu ‘well’ + pherein ‘to bear’'},
                    {'word': 'mirth', 'origin': 'Old English: from mirth ‘pleasure, joy’, of Germanic origin; related to Dutch and German Mirth'},
                    {'word': 'exhilaration', 'origin': 'Late Middle English: from late Latin exhilaratio(n-), from exhilarare ‘gladden’'},
                    {'word': 'gleeful', 'origin': 'Old English glēoful (see glee, -ful)'},
                    {'word': 'rapture', 'origin': 'Late Middle English: from French, from medieval Latin raptura ‘seizure, rape’, from Latin rapt- ‘snatched away’, from the verb rapere'},
                    {'word': 'upbeat', 'origin': 'Late 19th century: from up + beat in the musical sense'}],
        'spanish': [{'word': 'alegría', 'origin': 'Latin: from alacritas, from alacer ‘brisk, cheerful’'},
                    {'word': 'felicidad', 'origin': 'Latin: from felicitas, from felix, felic- ‘happy’'},
                    {'word': 'contento', 'origin': 'Old Spanish: from Latin contentus ‘satisfied’'},
                    {'word': 'regocijo', 'origin': 'Latin: from re- (expressing intensive force) + gaudere ‘rejoice’'},
                    {'word': 'euforia', 'origin': 'Late Middle English: from late Latin euphoria, from Greek, from euphoros'},
                    {'word': 'júbilo', 'origin': 'Late Middle English: from late Latin jubilare, from Latin jubilum ‘song of rejoicing’'},
                    {'word': 'entusiasmo', 'origin': 'Mid 17th century: from Greek enthousiasmos, from enthousiazein ‘be inspired or possessed by a god, be rapturous’'},
                    {'word': 'alegrón', 'origin': 'Derived from "alegre"'},
                    {'word': 'felicidad', 'origin': 'Derived from "feliz"'},
                    {'word': 'alborozo', 'origin': 'From Arabic'},
                    {'word': 'jolgorio', 'origin': 'From jolgorio, from jolgorio'}],
        'french': [{'word': 'joie', 'origin': 'Latin: gaudium, from gaudere ‘rejoice’'},
                   {'word': 'bonheur', 'origin': 'Latin: bonum '},
                   {'word': 'allégresse', 'origin': 'Latin: ad lætitiam ‘toward happiness’'},
                   {'word': 'heureux', 'origin': 'Latin: augurium, from augur ‘augur’'},
                   {'word': 'béatitude', 'origin': 'Late Middle English: from Old French beatitude, from ecclesiastical Latin beatitudo, from Latin beatus ‘happy’'},
                   {'word': 'émerveillement', 'origin': 'Late Middle English: from Old French, from merveiller ‘to marvel at’'},
                   {'word': 'épanouissement', 'origin': 'Middle English: from Old French espandre ‘pour out’, from Latin expandere ‘expand’'},
                   {'word': 'jubilation', 'origin': 'Late Middle English: from late Latin jubilatio(n-), from Latin jubilare ‘to shout for joy’'},
                   {'word': 'béatitude', 'origin': 'From "beatitude"'},
                   {'word': 'réjouissance', 'origin': 'From "réjouir"'},
                   {'word': 'enchantement', 'origin': 'From "enchantement"'},
                   {'word': 'exultation', 'origin': 'From "exultation"'}],
        'japanese': [{'word': 'shiawase', 'origin': 'Derived from the verb "shiawaseru," meaning "to be happy"'},
                     {'word': 'yorokobi', 'origin': 'Derived from the verb "yorokobu," meaning "to rejoice"'},
                     {'word': 'tanoshii', 'origin': 'Derived from the adjective "tanoshii," meaning "pleasant"'},
                     {'word': 'ureshii', 'origin': 'Derived from the verb "ureshimeru," meaning "to delight"'},
                     {'word': 'kōfuku', 'origin': 'Derived from "kōfuku," meaning "happiness"'},
                     {'word': 'kangei', 'origin': 'Derived from "kangei," meaning "welcome"'},
                     {'word': 'hokorashige', 'origin': 'Derived from "hokorashige," meaning "proud"'},
                     {'word': 'manzoku', 'origin': 'Derived from "manzoku," meaning "satisfaction"'},
                     {'word': 'yokan', 'origin': 'Derived from "yokan," meaning "premonition"'},
                     {'word': 'tanjun', 'origin': 'Derived from "tanjun," meaning "simple"'},
                     {'word': 'kansha', 'origin': 'Derived from "kansha," meaning "gratitude"'},
                     {'word': 'yūjō', 'origin': 'Derived from "yūjō," meaning "friendship"'}]
    },
    'sad': {
        'english': [{'word': 'sadness', 'origin': 'Old English: sædnesse, from sæd ‘sated, weary’'},
                    {'word': 'grief', 'origin': 'Old French: grief, gref, from grever ‘to burden’'},
                    {'word': 'despair', 'origin': 'Middle English: from Old French despeir, from desperer ‘despair’'},
                    {'word': 'melancholy', 'origin': 'Late Middle English: from Old French melancolie, via late Latin from Greek melankholia, from melas, melan- ‘black’ + kholē ‘bile’'},
                    {'word': 'depression', 'origin': 'Late Middle English: from Latin depressio(n-), from deprimere ‘press down’'},
                    {'word': 'heartbreak', 'origin': 'Late Middle English: from heart + break in the sense ‘sudden pain’'},
                    {'word': 'woe', 'origin': 'Old English wā, of Germanic origin; related to Dutch wee and German Weh, also to wail'},
                    {'word': 'misery', 'origin': 'Middle English: from Old French misere, from Latin miseria, from miser ‘wretched’'},
                    {'word': 'sorrow', 'origin': 'Old English sorg, of Germanic origin; related to Dutch zorg and German Sorge'},
                    {'word': 'anguish', 'origin': 'Middle English: from Old French anguisse, angoisse, from Latin angustiae ‘tightness, distress’'},
                    {'word': 'desolation', 'origin': 'Late Middle English: via Latin from desolare, from de- (expressing reversal) + solus ‘alone’'},
                    {'word': 'disconsolate', 'origin': 'Late Middle English: from medieval Latin disconsolatus, from dis- (expressing reversal) + consolatus ‘comforted’'}],
        'spanish': [{'word': 'tristeza', 'origin': 'Latin: tristitia, from tristis ‘sad’'},
                    {'word': 'pena', 'origin': 'Old Spanish: from Latin poena ‘punishment’'},
                    {'word': 'desesperación', 'origin': 'Latin: desperatio(n-), from desperare ‘despair’'},
                    {'word': 'melancolía', 'origin': 'Latin: melancholia, from Greek melankholia, from melas, melan- ‘black’ + kholē ‘bile’'},
                    {'word': 'depresión', 'origin': 'Latin: depressio(n-), from deprimere ‘press down’'},
                    {'word': 'pesar', 'origin': 'Latin pesar, from pensum ‘weight’'},
                    {'word': 'aflicción', 'origin': 'From "aflicción"'},
                    {'word': 'angustia', 'origin': 'From "angustia"'},
                    {'word': 'soledad', 'origin': 'Derived from "solo"'},
                    {'word': 'desolación', 'origin': 'From "desolación"'},
                    {'word': 'abatimiento', 'origin': 'Derived from "abatido"'},
                    {'word': 'desánimo', 'origin': 'Derived from "desánimo"'}],
        'french': [{'word': 'tristesse', 'origin': 'Latin: tristitia, from tristis ‘sad’'},
                   {'word': 'chagrin', 'origin': 'Latin: caccabus, from Greek kakkabos ‘pot’'},
                   {'word': 'désespoir', 'origin': 'Latin: desperatio(n-), from desperare ‘despair’'},
                   {'word': 'mélancolie', 'origin': 'Latin: melancholia, from Greek melankholia, from melas, melan- ‘black’ + kholē ‘bile’'},
                   {'word': 'dépression', 'origin': 'Latin: depressio(n-), from deprimere ‘press down’'},
                   {'word': 'peine', 'origin': 'Latin poena, from pensum ‘weight’'},
                   {'word': 'chagrin', 'origin': 'From "chagrin"'},
                   {'word': 'détresse', 'origin': 'From "détresse"'},
                   {'word': 'solitude', 'origin': 'From "solitude"'},
                   {'word': 'dévastation', 'origin': 'From "dévastation"'},
                   {'word': 'découragement', 'origin': 'From "découragement"'},
                   {'word': 'déconvenue', 'origin': 'From "déconvenue"'}],
        'japanese': [{'word': 'kanashimi', 'origin': 'Derived from the verb "kanashimu," meaning "to be sad"'},
                     {'word': 'hihō', 'origin': 'From Old Japanese'},
                     {'word': 'zetsubō', 'origin': 'From Old Japanese'},
                     {'word': 'merankorī', 'origin': 'From English "melancholy"'},
                     {'word': 'shitsurēshimai', 'origin': 'Derived from the verb "shitsurēshimau," meaning "to be disheartened"'},
                     {'word': 'bakabakashī', 'origin': 'Derived from the verb "bakabakashī," meaning "to be foolish"'},
                     {'word': 'sabishisa', 'origin': 'Derived from "sabishisa," meaning "loneliness"'},
                     {'word': 'kanbō', 'origin': 'Derived from "kanbō," meaning "gloom"'},
                     {'word': 'shikkari', 'origin': 'Derived from "shikkari," meaning "solid"'},
                     {'word': 'gūzen', 'origin': 'Derived from "gūzen," meaning "coincidence"'},
                     {'word': 'samishii', 'origin': 'Derived from "samishii," meaning "lonely"'},
                     {'word': 'shigatsu', 'origin': 'Derived from "shigatsu," meaning "April"'}]
    },
    'anger': {
        'english': [{'word': 'anger', 'origin': 'Old Norse: angr, from Old Norse angr ‘grief’'},
                    {'word': 'rage', 'origin': 'Middle English: from Old French, from Latin rabies ‘madness’'},
                    {'word': 'outrage', 'origin': 'Middle English: from Old French, based on Latin ultra ‘beyond’ + French -age ‘-age’'},
                    {'word': 'fury', 'origin': 'Middle English: from Old French furie, from Latin furia, from furere ‘to rage’'},
                    {'word': 'ire', 'origin': 'Old English īr(e), īg(e)r(e), of Germanic origin; related to Dutch ijver, also to early Scandinavian īrar ‘ire’'},
                    {'word': 'resentment', 'origin': 'Middle English: from Old French, from resentir ‘feel resentment’, based on Latin sentire ‘feel’'},
                    {'word': 'indignation', 'origin': 'Middle English: via Old French from Latin indignatio(n-), from indignari ‘consider as unworthy’'},
                    {'word': 'exasperation', 'origin': 'Late 16th century: from Latin exasperatio(n-), from exasperare ‘irritate to the highest degree’'},
                    {'word': 'wrath', 'origin': 'Old English wrǣththo, from wrāth ‘angry’'},
                    {'word': 'hostility', 'origin': 'Middle English: from Old French hostilite, from Latin hostilitas, from hostis ‘enemy’'},
                    {'word': 'animosity', 'origin': 'Late Middle English: from late Latin animositas, from Latin animosus ‘spirited, bold’'},
                    {'word': 'pique', 'origin': 'Mid 16th century: from French, literally ‘prick’, from piquer ‘prick, sting’, from late Latin piccare, related to picus ‘woodpecker’'}],
        'spanish': [{'word': 'enojo', 'origin': 'Latin: inodiare, based on odium ‘hatred’'},
                    {'word': 'ira', 'origin': 'Latin: ira ‘anger’'},
                    {'word': 'indignación', 'origin': 'Latin: indignatio(n-), from indignari ‘consider as unworthy’'},
                    {'word': 'furia', 'origin': 'Latin: furia, from furere ‘to rage’'},
                    {'word': 'cólera', 'origin': 'Latin: cholera ‘cholera’'},
                    {'word': 'resentimiento', 'origin': 'From "resentimiento"'},
                    {'word': 'furioso', 'origin': 'From "furioso"'},
                    {'word': 'exasperación', 'origin': 'From "exasperación"'},
                    {'word': 'rabia', 'origin': 'From "rabia"'},
                    {'word': 'hostilidad', 'origin': 'Derived from "hostilidad"'},
                    {'word': 'animosidad', 'origin': 'From "animosidad"'},
                    {'word': 'pique', 'origin': 'From "pique"'}],
        'french': [{'word': 'colère', 'origin': 'Latin: cholera ‘cholera’'},
                   {'word': 'rage', 'origin': 'Latin: rabies, from rabere ‘be mad’'},
                   {'word': 'indignation', 'origin': 'Latin: indignatio(n-), from indignari ‘consider as unworthy’'},
                   {'word': 'fureur', 'origin': 'Latin: furor, from furere ‘to rage’'},
                   {'word': 'haine', 'origin': 'Old French haïne, from hair ‘to hate’, of Germanic origin; related to Dutch haan ‘rooster’'},
                   {'word': 'ressentiment', 'origin': 'From "ressentiment"'},
                   {'word': 'rageux', 'origin': 'Derived from "rageux"'},
                   {'word': 'exaspération', 'origin': 'From "exaspération"'},
                   {'word': 'courroux', 'origin': 'From "courroux"'},
                   {'word': 'hostilité', 'origin': 'Derived from "hostilité"'},
                   {'word': 'animosité', 'origin': 'From "animosité"'},
                   {'word': 'pique', 'origin': 'From "pique"'}],
        'japanese': [{'word': 'ikari', 'origin': 'Derived from the verb "ikaru," meaning "to get angry"'},
                     {'word': 'gekido', 'origin': 'Derived from the verb "gekidōsuru," meaning "to rage"'},
                     {'word': 'unabara', 'origin': 'Derived from "unabara," meaning "sea of anger"'},
                     {'word': 'fyūrī', 'origin': 'From English "fury"'},
                     {'word': 'jigoku', 'origin': 'Derived from "jigoku," meaning "hell"'},
                     {'word': 'tekihatsu', 'origin': 'Derived from "tekihatsu," meaning "antagonism"'},
                     {'word': 'kyōfu', 'origin': 'Derived from "kyōfu," meaning "terror"'},
                     {'word': 'shūen', 'origin': 'Derived from "shūen," meaning "ruin"'},
                     {'word': 'enken', 'origin': 'Derived from "enken," meaning "grudge"'},
                     {'word': 'enrage', 'origin': 'From English "enrage"'},
                     {'word': 'bōfū', 'origin': 'Derived from "bōfū," meaning "storm"'},
                     {'word': 'fukigen', 'origin': 'Derived from "fukigen," meaning "sullen"'}]
    },
    'fear': {
        'english': [{'word': 'fear', 'origin': 'Old English fǣr, of Germanic origin; related to Dutch gevaar and German Gefahr ‘danger’'},
                    {'word': 'anxiety', 'origin': 'Late Middle English: from Old French anxiete or Latin anxietas, from anxius ‘anxious’'},
                    {'word': 'dread', 'origin': 'Old English: from a Germanic base meaning ‘to fear’; related to Dutch dreaden'},
                    {'word': 'terror', 'origin': 'Late Middle English: from Old French terreur, from Latin terror, from terrere ‘frighten’'},
                    {'word': 'phobia', 'origin': 'Late 18th century: from Greek, ‘fear’'},
                    {'word': 'apprehension', 'origin': 'Late Middle English: from French, or from medieval Latin apprehensio(n-), from apprehendere ‘seize, grasp’'},
                    {'word': 'panic', 'origin': 'Mid 17th century: from French panique, from modern Latin panicus, from Greek panikos, from Pan ‘Pan’ (from the belief that he caused terror)'},
                    {'word': 'horror', 'origin': 'Old English: via Latin from Greek; related to hirsute'},
                    {'word': 'alarm', 'origin': 'Late Middle English (as a noun): from Old French alarme, from Italian all’arme! ‘to arms!’'},
                    {'word': 'dismay', 'origin': 'Middle English (originally in the sense ‘unconsciousness’): from Old French desmai (noun), desmaier (verb), from Latin ex- ‘completely’ + machina ‘contrivance’'},
                    {'word': 'foreboding', 'origin': 'Middle English: from fore- ‘before’ + bode + -ing'},
                    {'word': 'phobic', 'origin': 'Mid 19th century: from Greek -phobos, from phobos ‘fear’'}],
        'spanish': [{'word': 'miedo', 'origin': 'Old Spanish: from Latin metus ‘fear’'},
                    {'word': 'ansiedad', 'origin': 'Late Middle English: via Old French from Latin anxietas, from anxius ‘anxious’'},
                    {'word': 'temor', 'origin': 'Old Spanish: from Latin timor ‘fear’'},
                    {'word': 'terror', 'origin': 'Late Middle English: from Old French terreur, from Latin terror, from terrere ‘frighten’'},
                    {'word': 'fobia', 'origin': 'Late 18th century: from Greek, ‘fear’'},
                    {'word': 'aprensión', 'origin': 'Derived from "aprensión"'},
                    {'word': 'pánico', 'origin': 'From "pánico"'},
                    {'word': 'horror', 'origin': 'Derived from "horror"'},
                    {'word': 'alarma', 'origin': 'From "alarma"'},
                    {'word': 'desmayo', 'origin': 'Derived from "desmayo"'},
                    {'word': 'presentimiento', 'origin': 'From "presentimiento"'},
                    {'word': 'fóbico', 'origin': 'From "fóbico"'}],
        'french': [{'word': 'peur', 'origin': 'Latin: pavere ‘be afraid’'},
                   {'word': 'anxiété', 'origin': 'Latin: anxietas, from anxius ‘anxious’'},
                   {'word': 'crainte', 'origin': 'Latin: crenta, from crentare ‘to fear’'},
                   {'word': 'terreur', 'origin': 'Latin: terror, from terrere ‘frighten’'},
                   {'word': 'phobie', 'origin': 'From "phobie"'},
                   {'word': 'inquiétude', 'origin': 'Derived from "inquiétude"'},
                   {'word': 'panique', 'origin': 'Derived from "panique"'},
                   {'word': 'horreur', 'origin': 'Derived from "horreur"'},
                   {'word': 'alarme', 'origin': 'From "alarme"'},
                   {'word': 'consternation', 'origin': 'Derived from "consternation"'},
                   {'word': 'prémonition', 'origin': 'Derived from "prémonition"'},
                   {'word': 'phobique', 'origin': 'Derived from "phobique"'}],
        'japanese': [{'word': 'koware', 'origin': 'From Old Japanese'},
                     {'word': 'fuan', 'origin': 'Derived from "fuan," meaning "uneasiness"'},
                     {'word': 'kyōfu', 'origin': 'Derived from "kyōfu," meaning "terror"'},
                     {'word': 'terā', 'origin': 'From English "terror"'},
                     {'word': 'shitsubō', 'origin': 'Derived from "shitsubō," meaning "disappointment"'},
                     {'word': 'dokushin', 'origin': 'Derived from "dokushin," meaning "loneliness"'},
                     {'word': 'kyūso', 'origin': 'Derived from "kyūso," meaning "shock"'},
                     {'word': 'keiken', 'origin': 'Derived from "keiken," meaning "experience"'},
                     {'word': 'kizen', 'origin': 'Derived from "kizen," meaning "omission"'},
                     {'word': 'shōdoku', 'origin': 'Derived from "shōdoku," meaning "disinfection"'},
                     {'word': 'hakkyō', 'origin': 'Derived from "hakkyō," meaning "fume"'},
                     {'word': 'shindō', 'origin': 'Derived from "shindō," meaning "quake"'}]
    }
}


def display_random_word(emotion):
    language = random.choice(list(emotions[emotion].keys())) # Choose a random language
    word_obj = random.choice(emotions[emotion][language]) # Choose a random word object from the selected language
    word = word_obj['word']
    origin = word_obj['origin']
    result_label.config(text=f"A word related to {emotion} in {language}: {word}\nOrigin: {origin}")

def on_emotion_select(emotion):
    display_random_word(emotion)

# Create main application window
root = tk.Tk()
root.title("Emotion Dictionary")

# Change background color
root.configure(bg="white")

# Get the directory path of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create buttons with images for emotions
def create_emotion_button(emotion):
    img = tk.PhotoImage(file=os.path.join(script_directory, f"{emotion}.png"))  # Change path to your images
    btn = tk.Button(root, image=img, command=lambda emotion=emotion: on_emotion_select(emotion),
                    width=100, height=100)  # Adjust width and height as needed
    btn.image = img
    return btn

emotion_buttons = {}
for index, emotion in enumerate(emotions.keys()):
    emotion_buttons[emotion] = create_emotion_button(emotion)
    emotion_buttons[emotion].grid(row=0, column=index, padx=5, pady=5)

# Label to display result with background color
result_label = tk.Label(root, text="", bg="white")  # Set background color to white
result_label.grid(row=1, column=0, columnspan=len(emotions), pady=50)

root.mainloop()
