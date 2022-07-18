#un fonzione per rechiamare automaticamente il codice dopo la fine di un operazione
def perimetro():
    print("Il programma calcola il perimetro di una figura geometrica")
    print("""
    - Quadrato >>1
    - Rettangolo >>2
    - Cerchio >>3
    _ Triangolo >>4
    _ Esci >>5""")
#Il valore iniziale del variabile scelta per essere leggibile dal controllo while.
    scelta = 0   
#Controllo di codice condizionale a scelta del' utente.
    while scelta !=5:
        print("Inserisce la scelta: ")
        scelta=int(input(">>> "))
#if, elif, else sono controlli condizional a base dell scelta ma operano sotto il controllo while.
        if scelta == 1:
            print("Hai selezionato il perimetro del quadrato")
            lato = float(input("Inserisci il valore del lato del quadrato: "))
            print("Il valore del perimetro del quadrato, avente lato", lato, "e :", lato*4)
        elif scelta == 2:
            print("Hai selezionato il perimetro del rettangolo")
            base = float(input("Inserisci il valore del base: "))
            altezza = float(input("Inserisci il valore dell'altezza: "))
            print("Il valore del rettangolo avente base", base, "e altezza ",altezza, "e :", base*2 + altezza*2)
        elif scelta == 3:
            print("Hai scelto il perimetro dl cerchio")
            diametro = float(input("Inserisci il diametro del cerchio: "))
            print("Il valore del perimetro avente diametro ", diametro, "e: ", 3.14 * diametro)
        elif scelta == 4:
            print("Hai scelto il perimetro del Triangolo")
            lato1 = float(input("Inserisci il valore del primo lato: "))
            lato2 = float(input("Inserisci il valore del secondo lato: "))
            lato3 = float(input("Inserisci il valore del terzo lato: "))
            print("Il valore del perimetro avente valori dei lati 1:",lato1,"2:",lato2,"3:",lato3," e: ", lato1+lato2+lato3)
#Termine del condizione del while.
        elif scelta == 5:
             print("Ciaoo")
        else:
            print("Inserisci una scelta valida")
perimetro()
#Termine del  definizione.
