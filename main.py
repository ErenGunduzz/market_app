import tkinter
import tkinter.messagebox
from tkinter.ttk import *
DEPARTMENTS = ["Book", "Electronics", "Sport Equipments"]
BOOKS = ["War and Peace", "Anna Karenina", "A Tale of 2 cities",
         "The Great Gatsby", "One Hundred Years of Solitude",
         "1984", "Animal Farm", "Don Quixote", "Jane Eyre",
         "Nutuk", "Das Kapital", "Pride and Prejudice",
         "Brave New World", "Crime and Punishment", "The Grapes of Wrath",
         "The Lord of the rings", "Les Miserables", "The Brothers Karamazov",
         "The Time Machine", "The Art of War", "Around The World in 80 days",
         "20.000 Leagues Under the Sea", "Journey to the Center of the World",
         "From the Earth to the Moon"]

ELECTRONICS = ["Computer", "Mobile Phone", "Tablet", "Scooter", "Drone"]

COMPUTER_MODELS = ["HP", "Lenovo", "Acer", "Monster", "Apple", "Samsung", "Toshiba", "Huawei"]
COMPUTER_INFO = [f"Price: 2.000£ Stocks: {2.000}", f"Price: 1.800£ Stocks: {2.000}", f"Price 1.900£ Stocks:{2.000}",
                 f"Price: 1.500£ Stocks: {2.000}", f"Price: 3.000£ Stocks: {2.000}", f"Price 2.300£ Stocks:{2.000}",
                 f"Price: 2.200£ Stocks: {2.000}", f"Price: 2.000£ Stocks: {2.000}"]
PHONE_MODELS = ["Samsung", "Apple", "Xiaomi", "Huawei", "Nokia"]
PHONE_INFO = [f"Price: 400£ Stocks: {2.000}", f"Price: 600£ Stocks: {2.000}", f"Price 300£ Stocks:{2.000}",
              f"Price: 400£ Stocks: {2.000}", f"Price: 100£ Stocks: {2.000}"]
SCOOTER_MODELS = ["Xiaomi"]

SPORTS = ["Cycling", "Swimming", "Basketball", "Football"]

BOOKS_INFO = ["War and Peace by Leo Tolstoy: 10£", "Anna Karenina by Leo Tolstoy: 10£",
              "A Tale of 2 cities by Charles Dickens: 8£", "The Great Gatsby by F. Scott Fitzgerald: 6£",
              "One Hundred Years of Solitude by Gabriel García Márquez: 7£",
              "1984 by George Orwell: 10£", "Animal Farm by George Orwell: 9£",
              "Don Quixote by Cervantes: 2£", "Jane Eyre by Charlotte Brontë: 4£",
              "Nutuk by M.Kemal Atatürk: 3£", "Das Kapital by Karl Marx: 1£",
              "Pride and Prejudice by Jane Austen: 3£", "Brave New World by Aldous Huxley: 2£",
              "Crime and Punishment by Fyodor Dostoyevski: 6£", "The Grapes of Wrath by John Steinbeck: 4£",
              "The Lord of The Rings by J.R.R Tolkien: 10£", "Les Miserables by Victor Hugo: 4£",
              "The Brothers Karamazov by Fyodor Dostoyevski: 7£", "The Time Machine by H.G.Wells: 3£",
              "The Art of War by Sun Tzu: 4£", "Around The World in 80 days by Jules Verne: 2£",
              "20.000 Leagues Under The Sea by Jules Verne: 2£", "Journey to the Center of the World by Jules Verne: 2£",
              "From the Earth to the Moon by Jules Verne: 2£"]
stocks = [7143, 2203, 869, 5175, 3128, 1591, 1253, 7043, 7536, 1336, 5945, 6792, 9226, 6561, 7282, 1034, 5975, 3329, 3000, 8064, 3701, 206, 2010, 9671]



class MainScreen:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x600")
        self.main_window.title("Eren Store")

        # Create a Menu widget.
        self.listbox = tkinter.Listbox(self.main_window, width=80, height=20)
        self.listbox.pack(padx=10, pady=10)

        # Create a list with the names of departments.
        for department in range(len(DEPARTMENTS)):
            self.listbox.insert(department, DEPARTMENTS[department])


        self.get_item(self.main_window, self.choose_item)




        # start the main loop.
        tkinter.mainloop()


    def get_item(self,window, function):
        # Create a button to get the selected item.
        self.get_button = tkinter.Button(
            window,text="Get Item",
            command=function)
        self.get_button.pack(padx=50, pady=30)

    def __buy_item(self):
        # Display the cost of the selected item.
        selected_item = self.choose_item()

    def choose_item(self):
        selected_item = self.listbox.curselection()
        if len(selected_item) > 0:
            if selected_item[0] == 0:
                self.display_books()
            elif selected_item[0] == 1:
                self.display_electronics()
            elif selected_item[0] == 2:
                self.display_sport_eq()
        else:
            tkinter.messagebox.showinfo(
                message="No item selected.")
    def choose_book(self):
        selected_item = self.book_list.curselection()
        if len(selected_item) > 0:
            for book in range(len(BOOKS)+1):
                if selected_item[0] == book:
                    tkinter.messagebox.showinfo(BOOKS[book], BOOKS_INFO[book])
                    tkinter.messagebox.showinfo("Stock", f"Stock of {BOOKS[book]} : {stocks[book]}")
                    buy_status = tkinter.messagebox.askyesno(
                        message="Do you want to buy it?")
                    if buy_status == True:
                        stocks[book] -= 1
         
        else:
            tkinter.messagebox.showinfo(
                message="No item selected.")



    def display_books(self):
        ok_cancel = tkinter.messagebox.askokcancel(
            message="You are redirecting to Books page...")

        if ok_cancel == True:
            self.new_window = self.openNewWindow(self.main_window, "Books", "red")
            self.book_list = tkinter.Listbox(self.new_window, width=50, height=20)
            self.book_list.pack(padx=10, pady=10)
            for book in range(len(BOOKS)):
                self.book_list.insert(book, BOOKS[book])


            self.get_item(self.new_window, self.choose_book)
        else:
            pass

    def choose_electro(self):
        selected_item = self.electro_list.curselection()
        if len(selected_item) > 0:
            if selected_item[0] == 0:
                self.computer_window = self.openNewWindow(self.new_window, "Computer")
                self.computer_list = tkinter.Listbox(self.computer_window, width=50, height=20)
                self.computer_list.pack(padx=10, pady=10)
                for computer in range(len(COMPUTER_MODELS)):
                    self.computer_list.insert(computer, COMPUTER_MODELS[computer])
                self.get_item(self.computer_window, self.display_computer)
            elif selected_item[0] == 1:
                self.phone_window = self.openNewWindow(self.new_window, "Phone")
                self.phone_list = tkinter.Listbox(self.phone_window, width=50, height=20)
                self.phone_list.pack(padx=10, pady=10)
                for phone in range(len(PHONE_MODELS)):
                    self.phone_list.insert(phone, PHONE_MODELS[phone])
                self.get_item(self.phone_window, self.display_phone)
            elif selected_item[0] == 2:
                self.tablet_window = self.openNewWindow(self.new_window, "Tablet")
                self.tablet_list = tkinter.Listbox(self.tablet_window, width=50, height=20)
                self.tablet_list.pack(padx=10, pady=10)
                for tablet in range(len(PHONE_MODELS) - 1):
                    self.tablet_list.insert(tablet, PHONE_MODELS[tablet])
                self.get_item(self.tablet_window, self.display_tablet)
            else:
                tkinter.messagebox.showwarning("Warning", "There is no stock.")
    def choose_sport(self):
        selected_item = self.sport_list.curselection()
        if len(selected_item) > 0:
            tkinter.messagebox.showwarning("Warning", "There is no stock!")


    def display_computer(self):
        selected_pc = self.computer_list.curselection()
        for j in range(len(COMPUTER_MODELS)+1):
            if selected_pc[0] == j:
                tkinter.messagebox.showinfo(COMPUTER_MODELS[j], COMPUTER_INFO[j])

    def display_phone(self):
        selected_phone = self.phone_list.curselection()
        for k in range(len(PHONE_MODELS)+1):
            if selected_phone[0] == k:
                tkinter.messagebox.showinfo((PHONE_MODELS[k]), PHONE_INFO[k])

    def display_tablet(self):
        selected_tablet = self.tablet_list.curselection()
        for t in range(len(PHONE_MODELS)):
            if selected_tablet[0] == t:
                tkinter.messagebox.showinfo((PHONE_MODELS[t]), PHONE_INFO[t])


    def display_electronics(self):
        ok_cancel = tkinter.messagebox.askokcancel(
            message="You are redirecting to Electronics page...")
        if ok_cancel == True:
            self.new_window = self.openNewWindow(self.main_window, "Electronics")
            self.electro_list = tkinter.Listbox(self.new_window, width=50, height=20)
            self.electro_list.pack(padx=10, pady=10)
            for electro in range(len(ELECTRONICS)):
                self.electro_list.insert(electro, ELECTRONICS[electro])

            self.get_item(self.new_window, self.choose_electro)
           

        else:
            pass



    def display_sport_eq(self):
        ok_cancel = tkinter.messagebox.askokcancel(
            message="You are redirecting to Electronics page...")
        if ok_cancel == True:
            self.new_window = self.openNewWindow(self.main_window, "Sports")
            self.sport_list = tkinter.Listbox(self.new_window, width=50, height=20)
            self.sport_list.pack(padx=10, pady=10)
            for sport in range(len(SPORTS)):
                self.sport_list.insert(sport, SPORTS[sport])
            self.get_item(self.new_window, self.choose_sport)
        else:
            pass



    # method to open a new window
    # on a button click.
    def openNewWindow(self, window, window_name, background_color="white"):

        newWindow = tkinter.Toplevel(window, background=background_color)
        newWindow.geometry("500x500")
        newWindow.title(window_name)
        return newWindow



if __name__ == "__main__":
    MainScreen = MainScreen()

