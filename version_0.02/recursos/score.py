from io import open

score = []
cadena = "\n".join(score)

def score_Escribir(username):
    score_txt = open(f"bd/facil/{username}_score.txt","w")
    score_txt = open(f"bd/medio/{username}_score.txt","w")
    score_txt = open(f"bd/dificil/{username}_score.txt","w")
    score_txt.write(cadena)
    score_txt.close()
    
def score_Leer(username):
    score_txt = open(f"bd/facil/{username}_score.txt","r")
    score_txt = open(f"bd/medio/{username}_score.txt","r")
    score_txt = open(f"bd/dificil/{username}_score.txt","r")
    lista_recuperada = [linea.strip() for linea in score_txt]
    score.extend(lista_recuperada)
    
def score_Sobreescribir(username):
    score_txt = open(f"bd/{username}_score.txt","a")
    score_txt.write(f"\n{cadena}")
    score_txt.close()
    
if __name__ == "__main__":
    #score_Escribir()
    score_Leer()
    #score_Sobreescribir()