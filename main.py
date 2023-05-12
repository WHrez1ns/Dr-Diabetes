from sklearn import tree

matriz = []
labels = []

jejum = []
sobrecarga = []
casual = []

with open('dados_em_jejum.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        jejum.append(int(linha.strip()))

with open('dados_pos_sobrecarga.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        sobrecarga.append(int(linha.strip()))

with open('dados_glicemia_casual.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        casual.append(int(linha.strip()))

for i in range(len(jejum)):
    linha = [jejum[i], sobrecarga[i], casual[i]]
    matriz.append(linha)

for label in matriz:
    if label[0] < 100:
        if label[1] < 140:
            if label[2] < 200:
                print("separando label", label, "0")
                labels.append(0)
            else:
                print("separando label", label, "3")
                labels.append(3) 
        else:
            print("separando label", label, "3")
            labels.append(3)
    elif 100 < label[0] < 126:
        if 140 < label[1] < 200:
            if label[2] < 200:
                print("separando label", label, "1")
                labels.append(1)
            else:
                print("separando label", label, "3")
                labels.append(3)
        else:
            print("separando label", label, "3")
            labels.append(3)
    elif label[0] >= 126:
        if label[1] >= 200:
            if label[2] >= 200:
                print("separando label", label, "2")
                labels.append(2)
            else:
                print("separando label", label, "3")
                labels.append(3)
        else:
            print("separando label", label, "3")
            labels.append(3)
    elif label == matriz[-1]:
        print("separando label", label, "3")
        labels.append(3)

matriz.reverse()
print(labels)
print(matriz)

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
        elif x == 2:
            print("-----------------------------------------------------------------")
            print("Diagnóstico de Diabetes mellitus")
        elif x == 3:
            print("-----------------------------------------------------------------")
            print("Exame inválido")

        print("-----------------------------------------------------------------")
        print("Suas respostas precisam ser analisadas por um médico especialista e que essas informações não devem ser usadas como diagnóstico definitivo")
    except ValueError:
        print("-----------------------------------------------------------------")
        print("Erro inesperado")


# dataset link: https://archive.ics.uci.edu/ml/datasets/diabetes
