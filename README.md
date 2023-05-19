
<br>

<a href="https://www.fiap.com.br/">
<img src="img/fiap.png" width="140" height="50">
</a> <br>

<a href="https://www.instagram.com/fiapoficial/">
<img src="img/ig.png">
</a>
<a href="https://www.youtube.com/@FiapBrasil">
<img src="img/yt.png">
</a>

<br>

# Dr-Diabetes

## Checkpoint - Coding for Security

<br>

### Objetivo:
<br>
Desenvolver um programa baseado na técnica de aprendizagem de 
máquina supervisionada.


<br>

- Editor Utilizado: <a href="https://code.visualstudio.com/"> Visual Studio Code</a>.

- Video Explicativo: <a href="https://youtu.be/OZp1oKiIYVw"> link </a>.


- <a href="https://www.canva.com/design/DAFjTtvWsqA/_ej5ZV8C2Qi83CCx0x2umQ/view?utm_content=DAFjTtvWsqA&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"> Slides
  </a><br>


<br>



<br>

#  Explicação

Neste conjunto de códigos em Python, foi apresentado um programa de previsão de níveis de glicose baseado em aprendizado de máquina. Através da biblioteca `sklearn`, especificamente utilizando a classe `DecisionTreeClassifier`, foi criado um modelo que aprende a partir de um conjunto de dados fornecido para prever a condição de saúde de um indivíduo em relação aos seus níveis de glicose.

Os dados de treinamento consistem em uma matriz contendo valores numéricos de testes de glicose e uma lista de rótulos que categorizam cada conjunto de dados em um de cinco possíveis estados: nível normal de glicose, nível baixo de glicose, diagnóstico de Diabetes Mellitus, quadro de hipoglicemia ou exame inválido.

O programa é executado em um loop, onde solicita ao usuário para inserir valores para três exames diferentes. O modelo treinado então prevê a categoria de saúde com base nestes valores e apresenta ao usuário uma mensagem correspondente.

Para melhorar a experiência do usuário, o código também inclui uma função `limpar_terminal` para limpar o terminal após cada iteração e usa o módulo `time` para pausar a execução do programa antes de fechar.

Note-se que, embora o programa forneça uma previsão baseada em aprendizado de máquina, ele destaca que seus resultados devem ser analisados por um médico e não devem ser usados como um diagnóstico definitivo.

<br>

##  Functions:

<br>

````
import os

def limpar_terminal():
    os.system('clear')
````

<br>

O código em questão possui uma função chamada `limpar_terminal()`, que é usada para limpar o conteúdo do terminal. 


1. `import os`: Este comando importa o módulo `os` em Python. Este módulo fornece uma variedade de funções úteis para interagir diretamente com o sistema operacional, incluindo a execução de comandos no terminal ou prompt de comando.

2. `def limpar_terminal():`: Nesta linha, está sendo criada uma função chamada `limpar_terminal()`. A palavra-chave `def` em Python é usada para iniciar a definição de uma função.

3. `os.system('clear')`: Aqui, dentro da função `limpar_terminal()`, é usado o método `system()` do módulo `os`. Esse método permite a execução de comandos do sistema operacional diretamente do código Python. Neste caso, o comando 'clear' (um comando Unix) é passado como argumento para o método `system()`. Este comando limpa o terminal. Caso o sistema operacional fosse Windows, o comando seria 'cls'.

Portanto, sempre que a função `limpar_terminal()` for invocada no código Python, ela irá limpar o conteúdo do terminal.

<br>

## Main:

<br>

````
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
````

<br>

Este código, cria um programa interativo simples que pode receber valores de exames médicos de um usuário e fazer uma previsão baseada nesses valores usando um modelo de aprendizado de máquina. Ele então retorna uma mensagem apropriada com base na previsão.

1. Importações: As bibliotecas `sklearn`, `time` e uma função personalizada `limpar_terminal` são importadas. A `sklearn` é uma biblioteca de aprendizado de máquina em Python, `time` é usada para operações relacionadas ao tempo, e a função `limpar_terminal` foi definida no código anterior.

2. Dados: Duas listas, `matriz` e `labels`, são definidas. A `matriz` contém dados numéricos enquanto `labels` contém categorias correspondentes a cada conjunto de dados na `matriz`. As categorias são:

   - 0 - Seu nível de Glicose está Normal
   - 1 - Seu nível de Glicose está Baixo
   - 2 - Diagnóstico de Diabetes Mellitus
   - 3 - Quadro de Hipoglicemia
   - 4 - Exame inválido

3. Classificador: Um objeto do tipo DecisionTreeClassifier é criado a partir da biblioteca sklearn e é treinado usando a `matriz` e `labels` com o método `fit()`. Isso resulta em um modelo que pode prever a categoria (label) de um novo conjunto de dados baseado nos que foram usados para treiná-lo.

4. Loop: O código entra em um loop que só terminará quando o usuário digitar 'N' para a pergunta "Deseja continuar [S/N]". 

   Dentro do loop, o programa solicita ao usuário os valores de três exames diferentes. Estes valores são usados para criar um novo conjunto de dados que é passado para o método `predict()` do classificador. O resultado, `x`, é uma previsão da categoria (label) baseada nos valores fornecidos.

   Dependendo do valor de `x`, o programa imprime uma mensagem diferente. 

   O bloco `try/except` é usado para lidar com possíveis erros que possam ocorrer durante a execução do código dentro do `try`. Se ocorrer um `ValueError`, provavelmente porque o usuário inseriu um valor não numérico para um dos exames, uma mensagem de erro é impressa.

<br>

## Conclusão

<br>

Em suma, este projeto serve como um exemplo de aplicação de algoritmos de aprendizado de máquina para previsão de condições de saúde com base em exames de glicose. No entanto, é crucial lembrar que as previsões feitas pelo programa são puramente indicativas e não devem ser usadas como substitutas de um diagnóstico profissional.

Esperamos que este código possa servir como um ponto de partida para quem esteja interessado em explorar mais a aplicação da ciência de dados na área da saúde. O código é simples e bastante comentado, tornando-o acessível mesmo para iniciantes em Python ou aprendizado de máquina.

Agradecemos pela sua atenção e esperamos que você encontre este projeto útil e informativo. Lembre-se, cuide bem da sua saúde e sempre consulte profissionais da saúde para aconselhamento e diagnóstico.

<br>

# Colaboradores:

<a href="https://github.com/Aykie"> Júlia Barboza Brunelli</a>, <a href="https://github.com/NCalegariS"> Nicholas Calegari</a> e <a href="https://github.com/WHrez1ns"> Renan Dias</a>
<br>
**RM: 98558, 93912 e 99258** <br>
**1TDCG**



 
