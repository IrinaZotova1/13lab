
import tkinter as tk
import requests

class CatFacts:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat Facts")
        self.root.geometry("800x400")
        self.root.configure(bg="lightblue")

        self.get_fact_button = tk.Button(self.root, text="Получить факт о котах", font=('Arial', 20),  command=self.display_fact, bg='lavender', fg='black')
        self.get_fact_button.pack()

        self.fact_label = tk.Label(self.root, text="", font=('Arial', 16), padx=10, pady=50, fg='darkblue', bg="lightblue")
        self.fact_label.pack()

    def get_cat_fact(self):
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        return data['fact']

    def display_fact(self):
        self.cat_fact_data = self.get_cat_fact()
        self.fact_label.config(text=self.cat_fact_data)

def main():
    root = tk.Tk()
    app = CatFacts(root)
    root.mainloop()

if __name__ == "__main__":
    main()


