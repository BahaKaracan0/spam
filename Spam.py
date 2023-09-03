"""Bu kod, kullanıcıdan alınan girişlere göre belirli bir süre içinde belirtilen
 mesajı belirli sayıda kez otomatik olarak yazan bir programın basit bir arayüzünü oluşturur.
 Kullanıcı, programı başlatabilir veya sonlandırabilir.
 Bu programın çalışma mantığı: kursör nerede ise belirlenen input değerleri oraya yazılır ve enter'a basılır.
"""
import tkinter as tk
import pyautogui
import time


def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"


def start_program(event=None):
    alert_message = alert_entry.get()
    count_value = count_entry.get()
    msg = msg_entry.get()

    if not count_value.isdigit() or int(count_value) <= 0:
        result_label.config(text="Geçersiz bir sayı girdiniz. Lütfen pozitif bir sayı girin.", fg="red")
        return

    count = int(count_value)

    second = 10

    for i in range(second, 0, -1):
        result_label.config(text=f"{alert_message} {i} saniye")
        root.update()
        time.sleep(1)

    result_label.config(text="Program çalışıyor...")
    root.update()

    while count > 0:
        pyautogui.typewrite(msg)
        pyautogui.press("Enter")
        count -= 1

    result_label.config(text="Program tamamlandı.")


def quit_program():
    root.destroy()


# Tkinter arayüzünü oluşturma
root = tk.Tk()
root.title("Program Arayüzü")

# Arka plan rengi
root.configure(bg='#333333')

# Etiketler ve giriş alanları
alert_label = tk.Label(root, text="10 saniye başlama süresinde gösterilecek mesaj (başlamaya .. saniye):", fg='white',
                       bg='#333333')
alert_label.pack(pady=5)

alert_entry = tk.Entry(root)
alert_entry.pack(pady=5)
alert_entry.bind("<Return>", on_enter)

count_label = tk.Label(root, text="Sayı:", fg='white', bg='#333333')
count_label.pack(pady=5)

count_entry = tk.Entry(root)
count_entry.pack(pady=5)
count_entry.bind("<Return>", on_enter)

msg_label = tk.Label(root, text="Mesaj:", fg='white', bg='#333333')
msg_label.pack(pady=5)

msg_entry = tk.Entry(root)
msg_entry.pack(pady=5)
msg_entry.bind("<Return>", on_enter)

# Butonlar
button_frame = tk.Frame(root, bg='#333333')
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Programı Başlat", command=start_program, padx=10)
start_button.pack(side=tk.LEFT, padx=5)

quit_button = tk.Button(button_frame, text="Programı Sonlandır", command=quit_program, padx=10)
quit_button.pack(side=tk.LEFT, padx=5)

# Sonuç etiketi
result_label = tk.Label(root, text="", fg='white', bg='#333333')
result_label.pack(pady=10)

# Arayüzü başlatma
root.mainloop()
