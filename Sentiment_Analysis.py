import tkinter
from tkinter import *
from tkinter import messagebox
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sent_analyze():
    text = e1.get()
    tokenized_text = nltk.sent_tokenize(text)
    analyzer = SentimentIntensityAnalyzer()
    print(tokenized_text)
    for sent in tokenized_text:
        scores = analyzer.polarity_scores(sent)
        print(scores)
        if scores['compound'] >= 0.05:
            messagebox.showinfo('Sentiment Result', 'Positive Text')
            e1.delete(0, END)
        elif scores['compound'] <= -0.05:
            messagebox.showinfo('Sentiment Result', 'Negative Text')
            e1.delete(0, END)
        else:
            messagebox.showinfo('Sentiment Result', 'Neutral Text')
            e1.delete(0, END)


win = tkinter.Tk()
win.geometry("800x300")
win.title("NLP Mini Project")
win.configure(background="#000000")

lbl = Label(
    win,
    text=("Sentiment Analysis from Text"),
    font=("Verdana", 18),
    bg=("#000000"),
    fg=("#ffffff")
)
lbl.pack(pady=20)

lbl2 = Label(
    win,
    text=("Please Enter your Text"),
    font=("Comic sans ms", 14),
    bg=("#000000"),
    fg=("#ffffff")
)
lbl2.pack()

e1 = Entry(
    win,
    font=("Verdana")
)
e1.pack(pady=20, ipadx=10, ipady=10)

b1 = Button(
    win,
    text=("Analyze"),
    font=("Comic sans ms", 12),
    width=14,
    bg=("#4C4B4B"),
    fg=("#6ab04c"),
    relief="raised",
    command=sent_analyze
)
b1.pack(pady=15)

win.mainloop()