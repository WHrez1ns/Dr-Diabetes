from sklearn import tree  # importa o módulo "tree" do Sklearn Árvore de Decisão
features = [[7, 0.6, 40], [7, 0.6, 41], [6, 0.4, 42], [7, 0.6, 35],
            [32, 600, 37], [33, 620, 38], [38, 615, 35], [35, 550, 34]]
# labels = [galinha, galinha, cavalo, cavalo]
# Uma galinha será representada por 0, enquanto um cavalo será representado por 1
labels = [0, 0, 0, 0, 1, 1, 1, 1]  # número de classes
classif = tree.DecisionTreeClassifier()  # Classificador
classif.fit(features, labels)
gen = float(input("Valor em jejum: "))
tagd = float(input("Valor Pós-Sobrecarga: "))
dddm = float(input("Valor Glicemia Casual: "))
x = classif.predict([[gen, tagd, dddm]])
if x == 0:
    print("Seu nível de Glicose está Normal!")
elif x == 1:
    print("Seu nível de Glicose está Diminuída")
else:
    print("Diagnóstico de Diabetes mellitus")

print("Suas respostas precisam ser analisadas por um médico especialista e que essas informações não devem ser usadas como diagnóstico definitivo")
# Hipoglicemia (baixa de açucar) [4] | valores a baixo de < 70
# Glicemia está Normal [0] | Em jejum: < 100 | Pós-Sobrecarga: < 140 | Glicemia Casual: < 200
# Tolerância à glicose diminuída [1] | Em jejum: 100 < 126 | Pós-Sobrecarga: 140 < 200 | Glicemia Casual: < 200
# Diagnóstico de Diabetes mellitus [2] | Em jejum: >= 126 | Pós-Sobrecarga: >= 200 | Glicemia Casual: >= 200