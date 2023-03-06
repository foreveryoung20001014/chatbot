import openai
import tkinter as tk
from tkinter import simpledialog

API = ""
Model = "gpt-3.5-turbo"
Messages = []

def initializ(prompt):
    Messages.clear
    Messages.append({"role": "system", "content": prompt})

def chatbot(sentence):
    Messages.append({"role": "user", "content": sentence})
    response = openai.ChatCompletion.create(model=Model, messages=Messages)
    result = ""
    for choice in response.choices:
        result += choice.message.content
    Messages.append({"role": "assistant", "content": result})
    return result

def close(root):
    Messages.clear()
    root.quit()
    

def enterkey():
    root = tk.Tk()
    root.withdraw()
    key = simpledialog.askstring(title="Input API", 
                                 prompt="Please enter your key:", 
                                 initialvalue="https://platform.openai.com/account/api-keys",)
    return key

def myClick(root, enter, b2):
    ans_me = "Me: " + enter.get()
    ans_chatbot = "Chatbot: " + chatbot(enter.get())
    b2.insert(tk.END, ans_me)
    b2.insert(tk.END, ans_chatbot)
    b2.insert(tk.END, "")

def chatroom():
    root = tk.Tk(className="chatbot")
    lab = tk.Label(root, text="enter the message", )
    lab.pack()
    ent = tk.Entry(root, width=50)
    ent.pack()

    b1=tk.Scrollbar(root,width=40)
    b1.pack(side = tk.RIGHT, fill = tk.Y)
    b2 = tk.Listbox(root, yscrollcommand = b1.set, width=40, height=16)
    b2.pack( side = tk.LEFT, fill = tk.BOTH )
    b1.config( command = b2.yview )

    myButton = tk.Button(root, text="Send", command=lambda: myClick(root, ent, b2), width=5, height=8)
    myButton.pack()
    clearButton = tk.Button(root, text="Close", command=lambda: close(root), width=5, height=8)
    clearButton.pack()
    root.mainloop()
    
API = enterkey()
openai.api_key = API
initializ("you are an AI assistant.")
chatroom()