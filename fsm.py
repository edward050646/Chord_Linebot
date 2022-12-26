from transitions.extensions import GraphMachine

from utils import send_text_message
chord = ""
note = ""
dchord = ""
notename = {"c":0, "c#":1, "d":2, "d#":3, "e":4, "f":5, "f#":6, "g":7, "g#":8, "a":9, "a#":10, "b":11}
chordnum = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_chord(self, event):
        text = event.message.text
        return text.lower() == "和弦"

    def is_going_to_chordtone(self, event):
        text = event.message.text
        return text.lower() == "組成音"

    def is_going_to_diachord(self, event):
        text = event.message.text
        return text.lower() == "音階"

    def is_going_to_rechord(self, event):
        global chord 
        text = event.message.text
        chord = text.lower()
        return True

    def is_going_to_rechordtone(self, event):
        global note
        text = event.message.text
        note = text.lower()
        return True

    def is_going_to_rediachord(self, event):
        global dchord
        text = event.message.text
        dchord = text.lower()
        return True

    def on_enter_chord(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入和弦代號")

    def on_enter_chordtone(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入和弦組成音")

    def on_enter_diachord(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入調性代號")

    def on_enter_rechord(self, event):
        print("I'm entering state1")
        text = event.message.text.lower()
        if '#' in text:
            name =text[0:1]
        else :
            name =text[0]

        if '7' in text : 

            if 'M' in text :

                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+4)%12]
                sendback += " " + chordnum[(root+7)%12]
                sendback += " " + chordnum[(root+11)%12]
            elif 'm' in text :

                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+3)%12]
                sendback += " " + chordnum[(root+7)%12]
                sendback += " " + chordnum[(root+10)%12]
            else :

                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+4)%12]
                sendback += " " + chordnum[(root+7)%12]
                sendback += " " + chordnum[(root+10)%12]
        else : 
            if 'm' in text :
                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+3)%12]
                sendback += " " + chordnum[(root+7)%12]
            else :
                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+4)%12]
                sendback += " " + chordnum[(root+7)%12] 

        reply_token = event.reply_token
        send_text_message(reply_token, sendback)
        self.go_back()

    def on_enter_rechordtone(self, event):
        global notename
        print("I'm entering state1")
        text = event.message.text.lower()
        notelist = list(text.split(" "))
        notenum = []
        for elem in notelist :
            notenum.append(notename[elem])
        if len(notename) == 4 :
            if (notenum[1]-notenum[0]+12)%12 == 3 : 
                replychord = notename[0] + "m7"
            else :
                if (notenum[3]-notenum[0]+12)%12 == 10 :
                    replychord = notename[0] + "7"
                else : 
                    replychord = notename[0] + "M7"
        else : 
            if (notenum[1]-notenum[0]+12)%12 == 3 : 
                replychord = notename[0] + "m"
            else : 
                replychord = notename[0]

        reply_token = event.reply_token
        send_text_message(reply_token, replychord)
        self.go_back()

    def on_enter_rediachord(self, event):
        print("I'm entering state1")
        text = event.message.text.lower()
        if '#' in text:
            name =text[0:1]
        else :
            name =text[0]

        if 'm' in text:  
                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+2)%12]
                sendback += " " + chordnum[(root+3)%12]
                sendback += " " + chordnum[(root+5)%12]
                sendback += " " + chordnum[(root+7)%12]
                sendback += " " + chordnum[(root+8)%12]
                sendback += " " + chordnum[(root+10)%12]
        else :
                root = notename[name]
                sendback = chordnum[root]
                sendback += " " + chordnum[(root+2)%12]
                sendback += " " + chordnum[(root+4)%12]
                sendback += " " + chordnum[(root+5)%12]
                sendback += " " + chordnum[(root+7)%12]
                sendback += " " + chordnum[(root+9)%12]
                sendback += " " + chordnum[(root+11)%12]
                
        reply_token = event.reply_token
        send_text_message(reply_token, sendback)
        self.go_back()