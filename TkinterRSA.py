import tkinter as tk
from tkinter import ttk
import random
from tkinter import PhotoImage
from PIL import Image, ImageTk
import re


def first_primes():
    my_prime_numbers = []
    numb = 0
    range_of_prime= 100 # How big numbers you are looking for #
    while numb < 2:
        prime = random.randrange (1,range_of_prime)
        starting = int(2)

        while (starting*starting) <= prime:
            score = prime % starting
            if score == int(0):
                prime = random.randrange(1,range_of_prime)
                starting = int(2)
            else:
                starting +=1

        if prime not in my_prime_numbers:
            my_prime_numbers.append(prime)
            numb += 1

        if len(my_prime_numbers) == 2:
            break
    return my_prime_numbers

def algorithm_RSA(my_prime_numbers):
    p = my_prime_numbers[0]
    q = my_prime_numbers[1]
    Theta = (p-1) * (q-1) #Euler formula
    n = p * q #Euler modulus
# Euklides Algorithm - GCD - greates common divisor - to find 'e'
    e = 7
# Edtended Euclidean algorithm - d * e mod Theta = 1 //
    u, w, d, z = 1, e, 0, Theta

    while w:
        if z != 0:
            if w < z:
                u, d = d, u
                w, z = z, w
            q = w//z
            u -= q*d
            w -= q*z
        else:
            return algorithm_RSA(first_primes())
    if z == 1:
        if d < 0: d += Theta
        return (e,n), (d,n)

        print(f"PUBLIC KEY: (e={e},n={n})")
        print(f"PRIVATE KEY: (d={d},n={n})")

        return publickeys, privatekeys

    else:
        return algorithm_RSA(first_primes())

def Encryption(t,e,n):
    asci_decrypting = []
    text_decrypted = []
    for x in t:
        asci_decrypting.append(ord(x))
    for y in asci_decrypting:
        if 0<y<n:
            text_decrypted.append((y**e)%n)
        else:
            print("Tej wiadomości nie można zaszyfrować.")
    print(text_decrypted)
    return text_decrypted

def Decryption(t,d,n):
    final=''
    cleaning=t[1:-1]
    y=cleaning.split(', ')
    text_decrypted = []
    #Asci Part Up
    for c in y:
       if 0<int(c)<n:
           c_int=int(c)
           text_decrypted.append(chr(((c_int)**d)%n))
       else:
          print("Tej wiadomości nie można zaszyfrować.")
    for joining in text_decrypted:
        final+=joining
    print(final)
    return final


# Tworzenie głównego okna
root = tk.Tk()
root.title("RSA message generator")

style = ttk.Style()

def generate_keys():
    publickeys, privatekeys = algorithm_RSA(first_primes())
    label_frame3_publickeys.config(text=f"e={publickeys[0]}\nn={publickeys[1]}")
    label_frame4_privatekeys.config(text=f"d={privatekeys[0]}\nn={privatekeys[1]}")

def encode_text():
    t=text_field_encode_input.get("1.0", "end-1c")
    e=int(text_field_encode_e.get("1.0", "end-1c"))
    n=int(text_field_encode_n.get("1.0", "end-1c"))
    encrypted_text = Encryption(t,e,n)

    text_field_encode_output.config(state="normal")
    text_field_encode_output.delete("1.0","end")
    text_field_encode_output.insert("1.0", str(encrypted_text))
    text_field_encode_output.config(state="disabled")

def decode_text():
    t_dirty=text_field_decode_input.get("1.0", "end-1c")
    pattern = r"\[.*\]"
    match = re.search(pattern, t_dirty)
    if match:
        t=match.group()

    d=int(text_field_decode_e.get("1.0", "end-1c"))
    n=int(text_field_decode_n.get("1.0", "end-1c"))
    decrypted_text = Decryption(t,d,n)

    text_field_decode_output.config(state="normal")
    text_field_decode_output.delete("1.0","end")
    text_field_decode_output.insert("1.0", str(decrypted_text))
    text_field_decode_output.config(state="disabled")

def clear_text():
    text_field_encode_input.delete("1.0", "end-1c")
    text_field_encode_output.config(state="normal")
    text_field_encode_output.delete("1.0", "end-1c")
    text_field_encode_output.config(state="disabled")

def clear_text2():
    text_field_decode_input.delete("1.0", "end-1c")
    text_field_decode_output.config(state="normal")
    text_field_decode_output.delete("1.0", "end-1c")
    text_field_decode_output.config(state="disabled")

def open_popup():
    popup = tk.Toplevel()  # Tworzymy nowe okno
    popup.title("Introduction to RSA generator")  # Tytuł okna pop-up
    #popup.minsize(200,150)  # Ustawienie rozmiaru okna

    # Tworzenie etykiety w oknie pop-up
    label_popup = ttk.Label(popup, text="ENCODING\n     If you want to encode the message, first copy 'Public keys'\n     Than enter your text to UPPER field on the right. \n\nDECODING: \n     If you want to decode message, first copy 'Private keys', paste code (e.g [1, 232, 24] and decode!", font=("Arial", 11))
    label_popup.pack(pady=50)  # Umieszczamy etykietę i ustawiamy jej pozycję

    # Tworzenie przycisku do zamknięcia okna pop-up
    close_button = ttk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()  # Umieszczamy przycisk w oknie pop-up

# Zmiana koloru wewnętrznego (tła) przycisku w stylu
style.configure("label_nameRSA.TLabel",
                background="white",  # Kolor tła przycisku
                foreground="black",  # Kolor tekstu przycisku
                padding=10)

style.configure("label_introduction.TLabel",
                background="#C0C0C0",  # Kolor tła przycisku
                foreground="black",  # Kolor tekstu przycisku
                padding=10)

# Definicja stylu dla przycisku
style.configure('create.TButton', relief="raised", borderwidth=3, foreground="black", font=('Helwetica', 9))

# Zmiana koloru tła w różnych stanach na ten sam kolor
style.map('create.TButton',
          background=[('active', '#C0C0C0'), ('!active', '#C0C0C0')])  #


style.configure('TButton', font=('Helvetica', 9))


# Ustawienie rozmiaru okna na 800x600 pikseli
#root.geometry("800x600")

root.rowconfigure(0,weight=0)
root.rowconfigure(1,weight=0)
root.rowconfigure(2,weight=0)
root.rowconfigure(3,weight=0)
root.rowconfigure(4,weight=0)
root.rowconfigure(5,weight=0)
root.rowconfigure(6,weight=0)
root.rowconfigure(7,weight=0)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)
root.columnconfigure(5,weight=1)
root.columnconfigure(6,weight=1)
root.columnconfigure(7,weight=1)
root.columnconfigure(8,weight=1)
root.columnconfigure(9,weight=1)
root.columnconfigure(10,weight=1)
root.columnconfigure(11,weight=1)
root.columnconfigure(12,weight=1)
root.columnconfigure(13,weight=1)
# root.columnconfigure(1,weight=1)

#1-FIRST ROW - NAME "RSA"
frame_nameRSA = ttk.Frame(root,relief="solid", borderwidth=5)
frame_nameRSA.grid(row=0, column=0, sticky="ew", padx=5, pady=5,columnspan=6)

frame_nameRSA.columnconfigure(0, weight=1)
frame_nameRSA.rowconfigure(0, weight=1)

#logo
path_point1 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\rsa_logo1.png"
img = Image.open(path_point1)  # Otwórz obrazek
img = img.resize((90,47))  # Zmień rozmiar na np. 50x50 pikseli

# Konwertuj obrazek do formatu Tkinter
point1 = ImageTk.PhotoImage(img)

label_nameRSA = ttk.Label(frame_nameRSA,
                          text="Click below to get your private and public keys.\n Private keys are only for You, so keep them safe!"
                          ,anchor="center",justify="center",image=point1, compound="top",style="label_nameRSA.TLabel")

# Umieszczanie widgetu na siatce
label_nameRSA.grid(row=0, column=0,sticky="nsew", padx=5, pady=5)

#1.2- Arrow down
frame_introduction = ttk.Frame(root)
frame_introduction.grid(row=1, column=2,columnspan=2, sticky="ew", padx=5, pady=0)

frame_introduction.columnconfigure(0, weight=1)
frame_introduction.rowconfigure(0, weight=1)

#logo
path_point1_2 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\arrow_down1_plus.png"
img = Image.open(path_point1_2)  # Otwórz obrazek
img = img.resize((68, 51))  # Zmień rozmiar na np. 50x50 pikseli

# Konwertuj obrazek do formatu Tkinter
point1_2 = ImageTk.PhotoImage(img)
label_introduction = ttk.Label(frame_introduction,anchor="center",justify="center",image=point1_2)

# Umieszczanie widgetu na siatce
label_introduction.grid(row=0, column=0,sticky="ew", padx=5, pady=0)

#2-SECOND - CREATE KEYS BUTTON
frame2_create_button = ttk.Frame(root)
frame2_create_button.grid(row=2, column=2, padx=5, pady=0,columnspan=2)

path_point2 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\generate1.png"
img = Image.open(path_point2)  # Otwórz obrazek
img = img.resize((125, 49))  # Zmień rozmiar na np. 50x50 pikseli

# Konwertuj obrazek do formatu Tkinter
point2 = ImageTk.PhotoImage(img)

label_frame2_create_button = ttk.Button(frame2_create_button,image=point2, command=generate_keys,style="create.TButton")

# Umieszczanie widgetu na siatce
label_frame2_create_button.grid(row=0, column=0, padx=5, pady=0)

#3-THIRD  - CREATE PUBLIC KEYS
frame3_publickeys = ttk.Frame(root)
frame3_publickeys.grid(row=3, column=2, padx=5, pady=5)

frame3_publickeys.columnconfigure(0, weight=1)
frame3_publickeys.rowconfigure(0, weight=1)

#logo
path_point3 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\PUBLIC.png"
img = Image.open(path_point3)  # Otwórz obrazek
img = img.resize((66,47))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
point3 = ImageTk.PhotoImage(img)

label_frame3_publickeys = ttk.Button(frame3_publickeys,image=point3,compound="top")

# Umieszczanie widgetu na siatce
label_frame3_publickeys.grid(row=0, column=0, padx=5, pady=5)

#4- CREATE PRIVATE KEYS
frame4_privatekeys = ttk.Frame(root)
frame4_privatekeys.grid(row=3, column=3, padx=5, pady=5)

frame4_privatekeys.columnconfigure(0, weight=1)
frame4_privatekeys.rowconfigure(0, weight=1)

#logo
path_point4 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\PRIVATE.png"
img = Image.open(path_point4)  # Otwórz obrazek
img = img.resize((66,47))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
point4 = ImageTk.PhotoImage(img)

label_frame4_privatekeys = ttk.Button(frame4_privatekeys,image=point4,compound="top")

# Umieszczanie widgetu na siatce
label_frame4_privatekeys.grid(row=0, column=0, padx=5, pady=5)


#6- Encryption and decryption
#frame_introduction = ttk.Frame(root,relief="solid", borderwidth=3)
#frame_introduction.grid(row=6, column=1, sticky="ew", padx=5, pady=5,columnspan=4)
#
#frame_introduction.columnconfigure(0, weight=1)
#frame_introduction.rowconfigure(0, weight=1)
#label_introduction = ttk.Label(frame_introduction,
#                          text="Enter your primary sentence to encrypt or coded sentence to decrypt ",anchor="center",justify="center",style="label_introduction.TLabel")

# Umieszczanie widgetu na siatce
#label_introduction.grid(row=0, column=0,sticky="ew", padx=5, pady=5)

#logo
path_point6 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\touch.png"
img = Image.open(path_point6)  # Otwórz obrazek
img = img.resize((40, 40))  # Zmień rozmiar na np. 50x50 pikseli

# Konwertuj obrazek do formatu Tkinter
point6 = ImageTk.PhotoImage(img)

# Przycisk do otwarcia okna pop-up i logo

open_button = ttk.Button(root, text="How it works ?", command=open_popup, image=point6,compound="right")
open_button.grid(row=5,column=1,columnspan=4)  # Umieszczamy przycisk w głównym oknie

#7- Arrow right
frame_introduction = ttk.Frame(root)
frame_introduction.grid(row=4, column=1, sticky="ew", padx=5, pady=5,columnspan=4)

frame_introduction.columnconfigure(0, weight=1)
frame_introduction.rowconfigure(0, weight=1)

#logo
path_point7 = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\arrow_right2_plus.png"
img = Image.open(path_point7)  # Otwórz obrazek
img = img.resize((130, 52))  # Zmień rozmiar na np. 50x50 pikseli

# Konwertuj obrazek do formatu Tkinter
point7 = ImageTk.PhotoImage(img)


label_introduction = ttk.Label(frame_introduction,anchor="center",justify="center",image=point7)

# Umieszczanie widgetu na siatce
label_introduction.grid(row=0, column=0,sticky="ew", padx=5, pady=5)

#logo
frame_logo = ttk.Frame(root)
frame_logo.grid(row=0, column=7,columnspan=6, padx=5, pady=5)
path_background = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\cipher2.png"
img = Image.open(path_background)  # Otwórz obrazek
img = img.resize((237, 120))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
background = ImageTk.PhotoImage(img)
label_logo = ttk.Button(frame_logo,image=background,style="create.TButton")
# Umieszczanie widgetu na siatce
label_logo.grid(row=0, column=0, padx=5, pady=0,sticky="e")

#8  - INPUT FRAME
frame7_inputframe = ttk.Frame(root)
frame7_inputframe.grid(row=1, column=7,columnspan=6, padx=5, pady=5)

frame7_inputframe.columnconfigure(0, weight=1)
frame7_inputframe.columnconfigure(1, weight=1)
frame7_inputframe.rowconfigure(0, weight=1)

label_input = ttk.Label(frame7_inputframe, text="Enter your message:")
label_input.grid(row=0, column=0, padx=5, pady=5)
# Pole tekstowe do wprowadzania danych (Text)
text_field_encode_input = tk.Text(frame7_inputframe,height=4,width=30)  # Można dostosować szerokość i wysokość
text_field_encode_input.grid(row=1, column=0, padx=5, pady=5,sticky="ew")

label_encode = ttk.Label(frame7_inputframe, text="Your encoded text:")
label_encode.grid(row=0, column=1, padx=5, pady=5)
# Pole tekstowe do wprowadzania danych (Text)
text_field_encode_output = tk.Text(frame7_inputframe,height=4,state="disabled",width=30)  # Można dostosować szerokość i wysokość
text_field_encode_output.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

#9  - Input e and n
frame9_inputframe = ttk.Frame(root)
frame9_inputframe.grid(row=2, column=7, padx=5, pady=5)

frame9_inputframe.columnconfigure(0, weight=1)
frame9_inputframe.columnconfigure(1, weight=1)
frame9_inputframe.columnconfigure(2, weight=1)
frame9_inputframe.columnconfigure(3, weight=1)
frame9_inputframe.columnconfigure(4, weight=1)
frame9_inputframe.columnconfigure(5, weight=1)
frame9_inputframe.rowconfigure(0, weight=1)

label_inpute = ttk.Label(frame9_inputframe, text="Enter e")
label_inpute.grid(row=0, column=0, sticky="w", padx=5, pady=5)
text_field_encode_e = tk.Text(frame9_inputframe,height=1,width=5)  # Można dostosować szerokość i wysokość
text_field_encode_e.grid(row=0, column=1,columnspan=1, padx=5, pady=5)

label_inputn = ttk.Label(frame9_inputframe, text="Enter n")
label_inputn.grid(row=0, column=2, sticky="w", padx=5, pady=5)
text_field_encode_n = tk.Text(frame9_inputframe,height=1,width=5)  # Można dostosować szerokość i wysokość
text_field_encode_n.grid(row=0, column=3,columnspan=1, padx=5, pady=5)
#10 ENCODE THE THE TEXT
path_encode = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\encode.png"
img = Image.open(path_encode)  # Otwórz obrazek
img = img.resize((80, 32))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
encode = ImageTk.PhotoImage(img)
label_frame9_encode = ttk.Button(frame9_inputframe,command=encode_text,image=encode,style="create.TButton")
# Umieszczanie widgetu na siatce
label_frame9_encode.grid(row=0, column=4, padx=5, pady=0,sticky="e")

#11 Clear button
path_clear = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\clear.png"
img = Image.open(path_clear)  # Otwórz obrazek
img = img.resize((125, 33))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
clear= ImageTk.PhotoImage(img)
label_frame11_clear = ttk.Button(frame9_inputframe,command=clear_text,image=clear,text="clear")
# Umieszczanie widgetu na siatce
label_frame11_clear.grid(row=0, column=5, padx=5, pady=0,sticky="e")

# Separator object
separator = ttk.Frame(root, height=5, relief="raised")
separator.grid(row=3,column=7, padx=5, pady=10,sticky="ew")

#12  - OUTPUT FRAME
frame12_inputframe = ttk.Frame(root)
frame12_inputframe.grid(row=4, column=7,columnspan=6, padx=5, pady=5)

frame12_inputframe.columnconfigure(0, weight=1)
frame12_inputframe.columnconfigure(1, weight=1)
frame12_inputframe.rowconfigure(0, weight=1)

label_input = ttk.Label(frame12_inputframe, text="Enter your message:")
label_input.grid(row=0, column=0, padx=5, pady=5)
# Pole tekstowe do wprowadzania danych (Text)
text_field_decode_input = tk.Text(frame12_inputframe,height=4,width=30)  # Można dostosować szerokość i wysokość
text_field_decode_input.grid(row=1, column=0, padx=5, pady=5,sticky="ew")

label_decode = ttk.Label(frame12_inputframe, text="Your decoded text:")
label_decode.grid(row=0, column=1, padx=5, pady=5)
# Pole tekstowe do wprowadzania danych (Text)
text_field_decode_output = tk.Text(frame12_inputframe,height=4,state="disabled",width=30)  # Można dostosować szerokość i wysokość
text_field_decode_output.grid(row=1, column=1, padx=5, pady=5,sticky="ew")

#13  - Input e and d
frame13_inputframe = ttk.Frame(root)
frame13_inputframe.grid(row=5, column=7, padx=5, pady=5)

frame13_inputframe.columnconfigure(0, weight=1)
frame13_inputframe.columnconfigure(1, weight=1)
frame13_inputframe.columnconfigure(2, weight=1)
frame13_inputframe.columnconfigure(3, weight=1)
frame13_inputframe.columnconfigure(4, weight=1)
frame13_inputframe.columnconfigure(5, weight=1)
frame13_inputframe.rowconfigure(0, weight=1)

label_inpute = ttk.Label(frame13_inputframe, text="Enter d")
label_inpute.grid(row=0, column=0, sticky="w", padx=5, pady=5)
text_field_decode_e = tk.Text(frame13_inputframe,height=1,width=5)  # Można dostosować szerokość i wysokość
text_field_decode_e.grid(row=0, column=1,columnspan=1, padx=5, pady=5)

label_inputn = ttk.Label(frame13_inputframe, text="Enter n")
label_inputn.grid(row=0, column=2, sticky="w", padx=5, pady=5)
text_field_decode_n = tk.Text(frame13_inputframe,height=1,width=5)  # Można dostosować szerokość i wysokość
text_field_decode_n.grid(row=0, column=3,columnspan=1, padx=5, pady=5)
#13 ENCODE THE THE TEXT
path_decode = r"C:\Users\Paweł\Desktop\Paweł\IT\RSA\Tkinter_photos\decode.png"
img = Image.open(path_decode)  # Otwórz obrazek
img = img.resize((80, 32))  # Zmień rozmiar na np. 50x50 pikseli
# Konwertuj obrazek do formatu Tkinter
decode = ImageTk.PhotoImage(img)
label_frame13_decode = ttk.Button(frame13_inputframe,command=decode_text,image=decode,style="create.TButton")
# Umieszczanie widgetu na siatce
label_frame13_decode.grid(row=0, column=4, padx=5, pady=0,sticky="e")

#14 Clear button

label_frame13_clear = ttk.Button(frame13_inputframe,command=clear_text2,image=clear,text="clear")
# Umieszczanie widgetu na siatce
label_frame13_clear.grid(row=0, column=5, padx=5, pady=0,sticky="e")



# Uruchomienie aplikacji
root.mainloop()

