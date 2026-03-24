#19/03/2026
traducciones = {
    "colores": {
        "rojo":     {"en": "Red",    "es": "Rojo",     "ja": "赤 (Aka)"},
        "azul":     {"en": "Blue",   "es": "Azul",     "ja": "青 (Ao)"},
        "verde":    {"en": "Green",  "es": "Verde",    "ja": "緑 (Midori)"},
        "amarillo": {"en": "Yellow", "es": "Amarillo", "ja": "黄色 (Kiiro)"},
        "negro":    {"en": "Black",  "es": "Negro",    "ja": "黒 (Kuro)"},
        "blanco":   {"en": "White",  "es": "Blanco",   "ja": "白 (Shiro)"},
        "naranja":  {"en": "Orange", "es": "Naranja",  "ja": "橙 (Daidai)"},
        "morado":   {"en": "Purple", "es": "Morado",   "ja": "紫 (Murasaki)"},
    },
    "palabras": {
        "hola":    {"en": "Hello",     "es": "Hola",    "ja": "こんにちは (Konnichiwa)"},
        "gracias": {"en": "Thank you", "es": "Gracias", "ja": "ありがとう (Arigatou)"},
        "si":      {"en": "Yes",       "es": "Si",      "ja": "はい (Hai)"},
        "no":      {"en": "No",        "es": "No",      "ja": "いいえ (Iie)"},
        "agua":    {"en": "Water",     "es": "Agua",    "ja": "水 (Mizu)"},
        "casa":    {"en": "House",     "es": "Casa",    "ja": "家 (Ie)"},
        "perro":   {"en": "Dog",       "es": "Perro",   "ja": "犬 (Inu)"},
        "gato":    {"en": "Cat",       "es": "Gato",    "ja": "猫 (Neko)"},
    }
}
T = str(input("Bienvenido al traductor, en que idioma desea traducir: \nIngles(1) \nEspañol(2) \nJapones(3)"))

if T == "1":
    idioma = "en"
elif T == "2":
    idioma = "es"
elif T == "3":
    idioma = "ja"
else:
    print("Opcion no valida.")
    idioma = None

if idioma:
    I = input("\nQue deseas traducir? \nColor(1) \nPalabra(2)\n> ")
 
    if I == "1":
        categoria = "colores"
        print("\nColores disponibles:", ", ".join(traducciones["colores"].keys()))
        I1 = input("Escribe el color: ").strip().lower()
        if I1 in traducciones["colores"]:
            print(f"\nTraduccion: {traducciones['colores'][I1][idioma]}")
        else:
            print("Color no encontrado en el diccionario.")
 
    elif I == "2":
        categoria = "palabras"
        print("\nPalabras disponibles:", ", ".join(traducciones["palabras"].keys()))
        I2 = input("Escribe la palabra: ").strip().lower()
        if I2 in traducciones["palabras"]:
            print(f"\nTraduccion: {traducciones['palabras'][I2][idioma]}")
        else:
            print("Palabra no encontrada en el diccionario.")
 
    else:
        print("Opcion no valida.")