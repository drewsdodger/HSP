import os; os.system("pip install ollama unratedwriting speechrecognition pyttsx3 pyaudio --break-system-packages")
from unratedwriting import typewrite as type; import os, pyttsx3, speech_recognition as talk, ollama as AI, argparse, time # type: ignore
messages = []
USER = 'user'
ASSISTANT = 'assistant'
engine = pyttsx3.init()
rate = engine.getProperty('rate')   
engine.setProperty('rate', 130)     
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)   
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = talk.Recognizer()
mic = talk.Microphone()
parser = argparse.ArgumentParser()
parser.add_argument('arg')  # positional argument

try:
    args = parser.parse_args()
    model = args.arg
except:
    print("What AI core should be used?")
    model = input() 
    if model == "":
        model = "llama2-uncensored"
type(f"HSP | By LAMBDA | R4 V1 MB | Core: {model}")

time.sleep(5)
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def logo(task):
    print(f"""
################################
-- λ Human Simulation Project --      
################################
1.B --{task}--""")
    if os.name == "nt":
        os.system(f"title {task}")
    else:
        #sys.stdout.write(f"\33]0;{title}\a")
        #sys.stdout.flush()
        print("[x] Terminal does not allow renaming!")
messages = []
USER = 'user'
ASSISTANT = 'assistant'
def add_history(content, role):
        messages.append({'role': role, 'content': content})
def chat(message):
    add_history(message, USER)
    response = AI.chat(model=model, messages=messages, stream=True)
    complete_message = ''
    for line in response:
        complete_message += line['message']['content']
        print(line['message']['content'], end='', flush=True)
        add_history(complete_message, ASSISTANT)
    engine.say(complete_message)
    engine.runAndWait()
while True:

    with mic as source:
        clear()
        r.adjust_for_ambient_noise(source,duration=0.2)
        logo("Listening")
        audio = r.listen(source)
    try:
        clear()
        logo("Checking input")
        text = r.recognize_google(audio)
        clear()
        prompt = True
    except:
        clear()
        prompt = False
    while prompt == True:
        clear()
        logo("Generating prompt")
        try:
            response = chat(text)
        except:
            AI.pull(model)
            response = chat(text)
        engine.say(response)
        type(response)    
        engine.runAndWait()
        prompt = False
# /\/\ 
# \  /   λ if i try hard enough λ
#  \/    λ it'll end up working λ
