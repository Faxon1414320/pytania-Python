


## import
import random, time


##### funkcje

def inputAnswer(answerL) : # wybierz odpowieć na postawie kolejność list
    answer_abcd = {'a': answerL[0], 'b': answerL[1], 'c': answerL[2], 'd': answerL[3]}
    while True:   
        print(f"""{qs[qsNum][0]}
    a) {qs[qsNum][1][0]}    
    b) {qs[qsNum][1][1]}    
    c) {qs[qsNum][1][2]}
    d) {qs[qsNum][1][3]}""")


        letter = input("\n> ")
        
        if letter in answer_abcd:
            return answer_abcd.get(letter)
        else:
            print("nie podano 'a'/'b'/'c'/'d' podaj jeszcze raz (pamiętaj mała litera bez spaci)")


##### kod 
qs = [ # [ pytanie,[a,b,c,d] ] razy ileść

    [ "Czy Python to język interpretowany ? ", 
    [
    "tak ", # poprawne odpowiedz
    "nie ",
    "nie do kończa ",
    "Niewiem ",
    ],],

    [ "Co to jest PEP 8?",
    [
    "Zbiór zaleceń dotyczących stylu kodowania w Pythonie",
    "Standard dokumentacji w języku Python.",
    "Framework do tworzenia aplikacji webowych w Pythonie.",
    "Lista propozycji zmian dla języka Python."
    ],],

    [ "Ile bitów ma jeden bajt ?",
    [
    "8",  # poprawne odpowiedz
    "2",
    "16",
    "64"
    ],],
    
    [ "Jakie słowo kluczowe używamy do definiowania funkcji w Pythonie ?", 
    [
    "def", # poprawne odpowiedz
    "function",
    "define",
    "fun"
    ],],

    [ "Co to jest lista w Pythonie ?",
    [
    "Kolekcja elementów w Pythonie", # poprawne odpowiedz
    "Funkcja matematyczna.",
    "Typ danych numerycznych.",
    "Instrukcja warunkowa."
    ],],
    
    [ "Jaka jest różnica między '==' a 'is' w Pythonie ?",
    [
    "Porównuje obiekty pod kątem identyczności", # poprawne odpowiedz
    "Porównuje wartości.",
    "Służy do sprawdzania równości obiektów.",
    "Porównuje obiekty pod kątem wartości i identyczności."
    ],],

    [ "Co to jest PEP 484 ?",
    [
    "Specyfikacja dla adnotacji typów", # poprawne odpowiedz
    "Dokumentacja standardowa Pythona.",
    "Zbiór zaleceń dotyczących stylu kodowania.",
    "Nazwa dla wersji 2.7 Pythona."
    ],],

    [ "Jakie są różnice między listą a krotką w Pythonie ?", #
    [
    "Lista jest mutowalna, a krotka jest niemutowalna", # poprawne odpowiedz
    "Lista jest niemutowalna, a krotka jest mutowalna.",
    "Obie są mutowalne.",
    "Obie są niemutowalne."
    ],],
    
    [ "Co to jest Comprehension w Pythonie ?", #
    [
    "Składnia do tworzenia nowych obiektów", # poprawne odpowiedz
    "Sposób zrozumienia kodu źródłowego.",
    "Specyfikacja dla funkcji lambda.",
    "Biblioteka do testowania jednostkowego."
    ],],
    
    ["Jakie są korzyści z korzystania z wirtualnego środowiska (virtualenv) w Pythonie ?", #
    [
    "Unikanie konfliktów wersji pakietów między projektami", # poprawne odpowiedz
    "Możliwość korzystania z wersji Pythona dostępnej globalnie.",
    "Brak korzyści z korzystania z wirtualnego środowiska.",
    "Zwiększenie prędkości działania programów."
    ],],

    [ "Jakie są zalety programowania obiektowego w Pythonie ?", #
    [
    "Hermetyzacja danych, polimorfizm, dziedziczenie", # poprawne odpowiedz
    "Zwiększona złożoność kodu.",
    "Brak możliwości hermetyzacji danych.",
    "Brak możliwości tworzenia klas."
    ],],

    [ "Co oznacza termin 'duck typing' w kontekście Pythona ?", #
    [
    "Przyjęcie obiektu na podstawie jego zachowania, a nie konkretnego typu", # poprawne odpowiedz
    "Typowanie statyczne w Pythonie.",
    "Typowanie dynamiczne w Pythonie.",
    "Oznacza kaczki w Pythonie."
    ],],
    
    [ "Co to jest GIL (Global Interpreter Lock) w Pythonie ?", #
    [
    "Mechanizm blokujący jednoczesny dostęp do obiektów w interpreterze Pythona", # poprawne odpowiedz
    "Znak graficzny używany w kodzie źródłowym.",
    "Błąd interpretacji w Pythonie.",
    "Nazwa dla wersji 4.0 Pythona."
    ],],

    [ "Jakie są różnice między Pythonem 2 a Pythonem 3 ?", #
    [
    "Python 3 jest rozwijany, a Python 2 nie", # poprawne odpowiedz
    "Brak różnic, to te same wersje.",
    "Python 3 ma składnię bardziej zgodną z zasadami Pythona.",
    "Python 2 jest nowszą werszą Pythona 3."
    ],],

    [ "Co to jest moduł w Pythonie ?", #
    [
    "Fragment kodu, który można importować do innych programów ", # poprawne odpowiedz
    "Błąd podczas wykonywania programu.",
    "Zmienna o zasięgu globalnym.",
    "Specjalna klasa w Pythonie."
    ],],
]

goodAnswer = [] # pytanie: odpowiedz # elemety dodawane w nastepn linice
for i in range( len(qs) ) :
    goodAnswer += [ qs[i][1][0] ]

qsNum = -1 # numer pytanie 
qsNumList = []
for i in range( len(qs) ) : # lista z numeremi listy # elemety dodawane w nastepn linice
    qsNumList += [i]

givenAnswer = 0 # numer odpowiedzi podajnej
givenSumGoodAnswer = 0 # ile prawidłowych odpwiedzi
roundQuestion = [0,len(qs)] # która runda jest, max round


 

for i in range(len(qs)) : # mieszanie odpowiedz odpowiedzi qs (poprawna pytania są w goodAnswer)
    random.shuffle(qs[i][1])


print("\n wybierz literę odpowiedz po tym znaku '>' (pamiętaj mała litera bez spaci i enteru)         \n \n ") # informacje jak podać odpowiedz i zadanie pytanie



while not roundQuestion[0] == roundQuestion[1] : # czy runda jest równa max rund
    roundQuestion[0] += 1

  
    
    qsNum = random.choice(qsNumList)
    qsNumList.remove(qsNum)

    giveAnswer = inputAnswer(qs[qsNum][1]) # pytanie o odpowiedz
    

    if giveAnswer in goodAnswer[qsNum] :  # Czy podano dobrą odpowiedz
        print(f"  brawo udało ci się odpowiedzieć prawidłowo na pytanie\n\n")
        givenSumGoodAnswer += 1  
    else: # nie podano poprawnej odpowiedzi
        print(f"  niestety nie prawidłowa odpowiedz na pytanie \n  dobra odpowiedz: {goodAnswer[qsNum]}\n\n")
    time.sleep(0.5) 



rating = round( (givenSumGoodAnswer/roundQuestion[1]*100), 1 )
time.sleep(0.6)
print(f"""
test zdany na {rating}%
pytań {roundQuestion[0]}, ile podano prawidłowych odpoiedzi {givenSumGoodAnswer}.
""")




