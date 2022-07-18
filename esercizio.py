def perimetro():
    print("Il programma calcola il perimetro di una figura geometrica")
    print("""
    - Quadrato >>1
    - Rettangolo >>2
    - Cerchio >>3""")
    
    print("Inserisce la scelta")
    scelta=int(input(">>> "))
    if scelta == 1:
        print("Hai selezionato il perimetro del quadrato")
        lato = float(input("Inserisci il valore del lato del quadrato: "))
        print("Il valore del perimetro del quadrato, avente lato", lato, "e :", lato*4)
    elif scelta == 2:
        print("Hai selezionato il perimetro del rettangolo")
        base = float(input("Inserisci il valore del base: "))
        altezza = float(input("Inserisci il valore dell'altezza: "))
        print("Il valore del rettangolo avente base", base, "e altezza ",altezza, "e :", (base + altezza)*2)
    elif scelta == 3:
        print("Hai scelto il perimetro dl cerchio")
        diametro = float(input("Inserisci il diametro del cerchio: "))
        print("Il valore del perimetro avente diametro ", diametro, "e: ", 3.14 * diametro)    
    else:
          print("Inserisci una scelta valida")
perimetro();
