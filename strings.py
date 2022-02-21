
i = "s"

while i == "s":
    i = int(input("Index (1), (2) (3) (4) (5) --> "))

    if i == 1:
        #Detectar cuál cadena es más larga
        cadena1 = input("\nPrimera cadena --> ")
        cadenta2 = input("Segunda cadena --> ")
        if len(cadena1) > len(cadenta2):
            print(f"{cadena1} Tiene más caracteres")
        elif len(cadenta2) > len(cadena1):
            print(f"{cadenta2} Tiene más caracteres")
        else:
            print("Ambas son iguales")
    elif i == 2:
        #Detectar si finaliza con "."
        userP = input("\nIntroducir palabra/cadena --> ")
        if userP.endswith("."):
            print('Termina con un "."')
        else:
            print('No termina con un punto "."')
    elif i == 3:
        #Detectar si una palabra es palíndroma
        word = input("\nPalabra o frase --> ")
        word = word.replace(" ","")
        wordPal = word[::-1]
        print(f"Invertida: {wordPal}")

        if word == wordPal:
            print("Es palíndroma")
        else:
            print("No es palíndroma")
    elif i == 4:
        #retornar frase con una uppercase en cada nueva palabra, y reemplazar los " " por "*"
        phrase = input("\nFrase --> ")
        phrase = phrase.replace(" ", "*")
        phrase = phrase.title()
        print(f"Nueva frase --> {phrase}")
    elif i == 5:
        #detectar vocales
        vocales = input("\nTextee algo --> ")
        print(f"""
        Vocales a = {vocales.count("a")}
        Vocales e = {vocales.count("e")}
        Vocales i = {vocales.count("i")}
        Vocales o = {vocales.count("o")}
        Vocales u = {vocales.count("u")}
        """)
        
    i = input("\nSeguir (s) Detener (n) --> ")