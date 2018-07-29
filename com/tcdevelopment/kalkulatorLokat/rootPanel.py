from tkinter import *

NUMBER_TO_PERCENT = 100
TAX_OPTIONS = ["pomiń podatek", "na koniec okresu", "na koniec"]
CAP_OPTIONS = ["dzień","tydzień","miesiąc","kwartał","pół roku","rok"]
iterations_per_year = [365,51,12,4,2,1]

root = Tk()
root.title("Kalkulator Lokat")

# Labels
Label(text="Kwota").grid(row=0,column=0,sticky=W)
Label(text="Oprocentowanie").grid(row=1,column=0,sticky=W)
Label(text="Kapitalizacja co").grid(row=2,column=0,sticky=W)
Label(text="Dopłaty co okres").grid(row=3,column=0,sticky=W)
Label(text="Lata Oszczędzania").grid(row=4,column=0,sticky=W)
Label(text="Podatek Belki").grid(row=5,column=0,sticky=W)

# Text Entry
initialAmount = DoubleVar()
annual_percentage = DoubleVar()
capitalization = StringVar()
add_amount_per_interval = DoubleVar()
years = IntVar()
tax = StringVar()

capitalization.set(CAP_OPTIONS[5])
tax.set(TAX_OPTIONS[1])

Spinbox(textvariable=initialAmount,from_=0.0,to=999999999999).grid(row=0,column=1,sticky=W)
Spinbox(textvariable=annual_percentage,from_=0,to=999999999999,increment=.1).grid(row=1,column=1,sticky=W)
OptionMenu(root,capitalization,*CAP_OPTIONS).grid(row=2,column=1,sticky=W)
Spinbox(textvariable=add_amount_per_interval,from_=0,to=999999999999).grid(row=3,column=1,sticky=W)
Spinbox(textvariable=years,from_=0,to=200).grid(row=4,column=1,sticky=W)
OptionMenu(root, tax, *TAX_OPTIONS).grid(row=5, column=1,sticky=W)

def calculate():
    initial_money = initialAmount.get()
    annual_perc = annual_percentage.get()
    liczba_okresow = iterations_per_year[CAP_OPTIONS.index(capitalization.get())]
    doplata = add_amount_per_interval.get()
    time = years.get()
    tax_option = tax.get()
    percentage_per_okres = annual_perc/liczba_okresow/NUMBER_TO_PERCENT


    for t in range(time):
        for liczba_w_roku in range(liczba_okresow):
            initial_money = initial_money*(1+percentage_per_okres)+doplata

    print(initial_money)



# action button
Button(text="Przelicz",command=calculate).grid(row=6, column=1,sticky=W)




# run program
root.mainloop()
