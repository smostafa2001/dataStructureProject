from Trie import Trie
from tkinter import *


fileDescriptor = open("words.txt")
words = fileDescriptor.read().split()
trie = Trie()
trie.formTrie(words)

window = Tk()
window.geometry("510x400")
window.title("پروژه ساختمان داده")
font = ("Times", 14, 'bold')
label = Label(text="Enter your query", font=font)
label.grid(row=0, column=1)


def onSelection(frame):
    dialog = frame.widget
    position = int(dialog.curselection()[0])
    selectedValue = dialog.get(position)
    entryString.set(selectedValue)
    listBox.delete(0, END)


def downArrowIsClicked(frame):
    listBox.focus()
    listBox.selection_set(0)


entryString = StringVar()
entry = Entry(window, textvariable=entryString, font=font)
entry.grid(row=1, column=1, padx=10, pady=0)
listBox = Listbox(window, height=6, font=font, relief='flat',
                  bg='SystemButtonFace', highlightcolor='SystemButtonFace')
listBox.grid(row=2, column=1)


def getData(*args):
    searchString = entry.get()
    if searchString == '':
        listBox.delete(0, END)
        return
    else:
        listBox.delete(0, END)
        trie.clearSuggestions()
        compare = trie.autoSuggestions(searchString)
        suggestions = trie.getSuggestions()
        for suggestion in suggestions:
            listBox.insert(END, suggestion)
        if compare == -1:
            listBox.insert(END, searchString)
        elif compare == 0:
            listBox.insert(END, "No string found with this prefix")


entry.bind('<Down>', downArrowIsClicked)
listBox.bind('<Right>', onSelection)
listBox.bind('<Return>', onSelection)
entryString.trace('w', getData)
window.mainloop()

