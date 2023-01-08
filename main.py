import tkinter as tk
import pyautogui
from tkinter import filedialog


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Wyszukiwarka obrazu na ekranie")

        self.label = tk.Label(self.root, text="Wyszukiwarka obrazu na ekranie")
        self.label.pack()

        self.button = tk.Button(self.root, text="Wybierz obrazek", command=self.choose_image, bg='#fff', fg='#f00')
        self.button.pack()

        self.confidence_scale = tk.Scale(self.root, from_=0.7, to=1.0, resolution=0.1, orient="horizontal",
                                         label="Wartość podobieństwa", bg='#fff', fg='black')
        self.confidence_scale.pack(ipadx=30)

        self.start_button = tk.Button(self.root, text="Start", state="disabled", command=self.start_search)
        self.start_button.pack()

        self.is_searching = False
        self.image_path = ""

        self.exit_button = tk.Button(self.root, text="Wyjście", fg="red", bg="black", command=self.root.destroy)
        self.exit_button.pack(ipadx=22, ipady=22, side=tk.BOTTOM)

        self.info_label = tk.Label(self.root, text="Wybierz obrazek, ustaw wartość podobieństwa,\n a następnie uruchom funkcje: Start", fg="yellow", bg="gray")
        self.info_label.pack(ipadx=22, ipady=22)



    def choose_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=(("JPG obrazy", "*.jpg"), ("IMG obrazy", "*.img"), ("PNG obrazy", "*.png")))
        if self.image_path:
            self.button.config(bg="yellow", text="Wybrano plik")
            self.start_button.config(state="normal")

    def start_search(self):
        if not self.is_searching:
            # rozpoczęcie szukania obrazka
            self.is_searching = True
            self.start_button.config(text="Stop")
            self.button.config(bg="yellow", text="Wybrano plik")
            while True:
                pos = pyautogui.locateOnScreen(self.image_path, confidence=self.confidence_scale.get())
                if pos is not None:
                    print(f"Znaleziono obrazek na pozycji: {pos}")
                    found_label = tk.Label(root, text="Znaleziono obrazek", font=("", 11), fg="green")
                    found_label.pack()
                    self.button.config(bg="white", text="Wybierz obrazek")
                    pyautogui.moveTo(pos)  ##Przenosi kursor na znaleziony obrazek
                    root.after(2000, found_label.destroy)
                    self.start_button.config(text="Start", state="disabled")

                    break
                self.root.update()  # odświeżenie GUI tkinter
            self.is_searching = False
            self.start_button.config(text="Start")
        else:
            # zatrzymanie szukania obrazka
            self.button.config(bg="white", text="Wybierz obrazek")
            self.is_searching = False
            self.start_button.config(text="Start", state="disabled")
            print("Nie znaleziono obrazka")


root = tk.Tk()
root.resizable(width=False, height=False)
root.attributes('-topmost',True)
app = App(root)
root.mainloop()