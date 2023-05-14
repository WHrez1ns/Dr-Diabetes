from sklearn import tree

matriz = [[110, 177, 155], [165, 303, 225], [234, 205, 273], [59, 94, 77], [121, 153, 94], [113, 162, 63], [152, 259, 200], [262, 273, 288], [
    194, 205, 272], [55, 112, 94], [141, 232, 309], [69, 35, 149], [77, 77, 177], [183, 273, 251], [108, 146, 58], [91, 88, 94], [109, 198, 102]]
labels = [1, 2, 2, 0, 1, 1, 2, 2, 2, 0, 2, 0, 0, 2, 1, 0, 1]

classif = tree.DecisionTreeClassifier()
classif.fit(matriz, labels)

while True:
    try:
        print("-----------------------------------------------------------------")
        gen = float(input("Valor em jejum: "))
        tagd = float(input("Valor Pós-Sobrecarga: "))
        dddm = float(input("Valor Glicemia Casual: "))

        x = classif.predict([[gen, tagd, dddm]])
        if x == 0:
            print("-----------------------------------------------------------------")
            print("Seu nível de Glicose está Normal!")
        elif x == 1:
            print("-----------------------------------------------------------------")
            print("Seu nível de Glicose está Baixo!")
        else:
            print("-----------------------------------------------------------------")
            print("Diagnóstico de Diabetes mellitus!")

        print("-----------------------------------------------------------------")
        print("ATENÇÃO! Suas respostas precisam ser analisadas por um médico especialista, essas informações não devem ser usadas como diagnóstico definitivo")
    except ValueError:
        print("-----------------------------------------------------------------")
        print("Erro inesperado")


# dataset link: https://archive.ics.uci.edu/ml/datasets/diabetes
