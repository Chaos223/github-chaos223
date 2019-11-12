from tkinter import *
from generator import generate
from config import *

# window setup
window = Tk()
window.title('Empty files generator')
variable = StringVar(window)
optionMenu = OptionMenu(window, variable, *ledgers)

ledgerLabel = Label(window, text="Ledger")
businessDateLabel = Label(window, text="Business Date YYYYMMDD")
timeStampDate = Label(window, text="TimeStamp Date YYYYMMDD")
sequenceNumberLabel = Label(window, text='Sequence number')
generateButton = Button(window, text='Generate', command=lambda: generate(variable.get()))

sequenceNumberEntry = Entry(window)
businessDateLabelEntry = Entry(window)
timeStampDateEntry = Entry(window)

ledgerLabel.grid(row=0, sticky=E)
businessDateLabel.grid(row=1, sticky=E)
timeStampDate.grid(row=2, sticky=E)
sequenceNumberLabel.grid(row=3, sticky=E)
optionMenu.grid(row=0, column=1)
businessDateLabelEntry.grid(row=1, column=1)
timeStampDateEntry.grid(row=2, column=1)
sequenceNumberEntry.grid(row=3, column=1)
generateButton.grid(row=4, columnspan=2)
window.mainloop()
