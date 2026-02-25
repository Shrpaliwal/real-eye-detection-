import random

R_EATING = "I dont like to eat anything because i am a bot obviously!"
R_FESTIVAL="ohh wow, thats great thing, btw which festival"
R_FEST="Ohh! Happy Krishna Janamashtmi to you and your your family. May Lord Shri Krishna bless you."
R_GANESH="Ohh! Happy Ganesh Chaturthi to you and your whole family. May Ganpati Bappa bless you."
R_WEATHER="i think it is raining outiside, because it is monsson season."
R_RAM="JAY JAY SHRI RAM"
R_QUES="let me think.....as per the theories and the researches we found that hen come from the egg and the egg come from the hen so we cant decide who came first."
R_JOKE="One joke, coming up! What is a sea monster’s favorite snack? Ships and dip."
def unknown():
    response = ['could you please rephrase that?',
                "...",
                "sounds about right",
                "what does that mean?"][random.randrange(4)]
    return response