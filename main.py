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
                labels.insert(0, 0)
    elif 100 < label[0] < 126:
        if 140 < label[1] < 200:
            if label[2] < 200:
                labels.insert(0, 1)
    elif label[0] >= 126:
        if label[1] >= 200:
            if label[2] >= 200:
                labels.insert(0, 2)
    else:
        labels.insert(0, 3)

print(labels)
print(matriz)

classif = tree.DecisionTreeClassifier()
classif.fit(matriz, labels)
gen = float(input("Valor em jejum: "))
tagd = float(input("Valor Pós-Sobrecarga: "))
dddm = float(input("Valor Glicemia Casual: "))
x = classif.predict([[gen, tagd, dddm]])
if x == 0:
    print("Seu nível de Glicose está Normal!")
elif x == 1:
     print("Seu nível de Glicose está Diminuída")
# else:
#     print("Diagnóstico de Diabetes mellitus")

# print("Suas respostas precisam ser analisadas por um médico especialista e que essas informações não devem ser usadas como diagnóstico definitivo")

# dataset link: https://archive.ics.uci.edu/ml/datasets/diabetes

# Hipoglicemia (baixa de açucar) [4] | valores a baixo de < 70
# Glicemia está Normal [0] | Em jejum: < 100 | Pós-Sobrecarga: < 140 | Glicemia Casual: < 200
# Tolerância à glicose diminuída [1] | Em jejum: 100 < 126 | Pós-Sobrecarga: 140 < 200 | Glicemia Casual: < 200
# Diagnóstico de Diabetes mellitus [2] | Em jejum: >= 126 | Pós-Sobrecarga: >= 200 | Glicemia Casual: >= 200
