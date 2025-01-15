import tkinter as tk
import pyautogui
import time


class YandexMusicWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Yandex Music Widget")

        self.track_label = tk.Label(root, text="Текущий трек: ", font=("Arial", 14))
        self.track_label.pack(pady=20)

        self.next_button = tk.Button(root, text="Следующий трек", command=self.next_track)
        self.next_button.pack(pady=10)

        self.update_track()

    def update_track(self):
        # Здесь Вы можете добавить код для получения текущего трека
        # Например, используя API Яндекс Музыки, если он доступен
        current_track = "Название трека"  # Замените на реальное название трека
        self.track_label.config(text=f"Текущий трек: {current_track}")
        self.root.after(5000, self.update_track)  # Обновление каждые 5 секунд

    def next_track(self):
        # Команда для переключения на следующий трек
        pyautogui.hotkey('ctrl', 'right')  # Замените на нужную комбинацию клавиш


if __name__ == "__main__":
    root = tk.Tk()
    widget = YandexMusicWidget(root)
    root.mainloop()