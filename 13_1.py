import requests
import tkinter as tk

# Функция для загрузки данных с API и вывода на экран
def get_weather():
    api_key = 'db0f91d6df687d044dfe0dcc944bd034'
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    weather_data = f'Город: {data["name"]}\nТемпература: {round(data["main"]["temp"]-273)}°C\nПогода: {data["weather"][0]["description"]}'

    weather_label.config(text=weather_data)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Погода")
root.geometry("600x400")
root.configure(background='cyan')

city_label = tk.Label(root, text="Введите город:", bg='cyan', font=('Arial', 30), padx=10, pady=50)
city_label.pack()


city_entry = tk.Entry(root, bg='white', font=('Arial', 20))
city_entry.pack()

get_weather_button = tk.Button(root, text="Узнать погоду", bg='white', font=('Arial', 15), padx=10, pady=10, command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", bg='cyan', font=('Arial', 12), padx=10, pady=50)
weather_label.pack()

root.mainloop()