import cv2
from pathlib import *

sciezka=input("Podaj scieżkę z katologiem ze zdjęciami: ")
typ=input("Podaj typ pliku (np. png): ")
sciezka_wyjscia=sciezka+"\\podpisOutput"
path_pliki=Path(sciezka)
if path_pliki.exists():
    piki_list=list(path_pliki.glob("*."+typ))
    text=input("Wypisz podpis: ")
    path_folderu=Path(sciezka_wyjscia)
    path_folderu.mkdir(parents=True, exist_ok=True)
    sciezka_wyjscia=sciezka_wyjscia+"\\"
    for plik in piki_list:
        obraz=cv2.imread(plik)
        cv2.putText(obraz, text, (10,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255),3) 
        pom=str(plik).split("\\")
        print(sciezka_wyjscia+pom[-1])
        cv2.imwrite(sciezka_wyjscia+pom[-1], obraz)
else:
    print("Nie istnieje taka scieżka")