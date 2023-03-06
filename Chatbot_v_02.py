import openai
import tkinter as tk
from tkinter import simpledialog

API = ""
Model = "gpt-3.5-turbo"
Messages = []
prom = "you are an AI assistant."

def initializ():
    Messages.clear
    Messages.append({"role": "system", "content": prom})

def chatbot(sentence):
    Messages.append({"role": "user", "content": sentence})
    response = openai.ChatCompletion.create(model=Model, messages=Messages)
    result = ""
    for choice in response.choices:
        result += choice.message.content
    Messages.append({"role": "assistant", "content": result})
    return result

def clear(b2):
    Messages.clear()
    b2.delete(0, "end")
    initializ()

def close(root):
    root.quit()

def enterkey():
    root = tk.Tk()
    root.withdraw()
    key = simpledialog.askstring(title="Input API", 
                                 prompt="Please enter your key:", 
                                 initialvalue="https://platform.openai.com/account/api-keys")
    if key == None:
        exit()
    if len(key) == 0:
        exit()
    return key

def myClick(root, enter, b2):
    ans_me = "Me: " + enter.get()
    ans_chatbot = "Chatbot: " + chatbot(enter.get())
    b2.insert(tk.END, ans_me)
    b2.insert(tk.END, ans_chatbot)
    b2.insert(tk.END, "")

def chatroom():
    h = 2 
    w = 5

    root = tk.Tk(className="Chatbot")
    lab = tk.Label(root, text="Enter the message")
    lab.pack()
    ent = tk.Entry(root, width=89)
    ent.pack()

    b1=tk.Scrollbar(root,width=20)
    b1.pack(side = tk.RIGHT, fill = tk.Y)
    b2 = tk.Listbox(root, yscrollcommand = b1.set, width=80, height=h*3)
    b2.pack( side = tk.LEFT, fill = tk.BOTH )
    b1.config( command = b2.yview )

    myButton = tk.Button(root, text="Send", command=lambda: myClick(root, ent, b2), width=w, height=h)
    myButton.pack()
    clearButton = tk.Button(root, text="Clear", command=lambda: clear(b2), width=w, height=h)
    clearButton.pack()
    closeButton = tk.Button(root, text="Close", command=lambda: close(root), width=w, height=h)
    closeButton.pack()
    root.resizable(0, 0)
    root.mainloop()

def chat():
    API = enterkey()
    openai.api_key = API
    initializ()
    chatroom()

chat()