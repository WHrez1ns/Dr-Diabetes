from sklearn import tree
import time
from functions import limpar_terminal

matriz = [[110, 177, 155], [165, 303, 225], [234, 205, 273], [59, 94, 77], [121, 153, 94], [113, 162, 63], [152, 259, 200], [262, 273, 288], [
    194, 205, 272], [55, 112, 94], [141, 232, 309], [69, 35, 149], [77, 77, 177], [183, 273, 251], [108, 146, 58], [91, 88, 94], [109, 198, 102], [39, 39, 39], [69, 69, 69], [99, 139, 199], [70, 70, 70], [100, 140, 199], [125, 199, 199], [126, 200, 200], [700, 700, 700], [600, 600, 600]]

labels = [1, 2, 2, 0, 1, 1, 2, 2, 2, 0, 2,
          0, 0, 2, 1, 0, 1, 3, 3, 0, 0, 1, 1, 2, 4, 2]
# 0 - Seu nível de Glicose está Normal
# 1 - Seu nível de Glicose está Baixo
# 2 - Diagnóstico de Diabetes Mellitus
# 3 - Quadro de Hipoglicemia
# 4 - Exame inválido

resp = 'S'

classif = tree.DecisionTreeClassifier()
classif.fit(matriz, labels)

while resp == 'S':
    try:
        print(
            "\033[36m-----------------------------------------------------------------")
        print("|                     D R.  D I A B E T E S                     |")
        print(
            "\033[36m-----------------------------------------------------------------")
        gen = float(input("|\033[35m Valor do exame em jejum:\033[36m "))
        tagd = float(
            input("|\033[35m Valor do exame Pós-Sobrecarga:\033[36m "))
        dddm = float(
            input("|\033[35m Valor do exame de Glicemia Casual:\033[36m "))

        x = classif.predict([[gen, tagd, dddm]])
        if x == 0:
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[32m| Seu nível de Glicose está Normal!")
        elif x == 1:
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[33m| Seu nível de Glicose está Baixo!")
        elif x == 2:
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[31m| Diagnóstico de Diabetes mellitus!")
        elif x == 3:
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[34m| Quadro de Hipoglicemia!")
        else:
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[37m| Exame inválido!")

        print(
            "\033[36m-----------------------------------------------------------------")
        print("\033[33m| ATENÇÃO! Suas respostas precisam ser analisadas por um médico especialista, essas informações não devem ser usadas como diagnóstico definitivo")
        print(
            "\033[36m-----------------------------------------------------------------")
        resp = input("\033[36m| Deseja continuar \033[37m[S/N]: ").upper()
        if resp == 'N' or resp != 'S':
            print(
                "\033[36m-----------------------------------------------------------------")
            print("\033[36m| Encerrando...")
            time.sleep(1.5)
            print(
                "\033[36m-----------------------------------------------------------------")
            exit()
        limpar_terminal()
    except ValueError:
        print(
            "\033[36m-----------------------------------------------------------------")
        print("\033[31m| Erro inesperado!")

# dataset link: https://archive.ics.uci.edu/ml/datasets/diabetes
