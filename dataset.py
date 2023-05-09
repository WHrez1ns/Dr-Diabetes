dados_1 = []
dados_2 = []
dados_3 = []

# dados 1
with open('data/Diabetes-Data/data-01', 'r') as arquivo:
    for linha in arquivo:
        valor = linha.split()
        if valor[2] == '58':
            dados_1.insert(0, int(valor[3]))   
            print(valor[2], valor[3])

print('-------------------------------------------------------------------')
print('Medição de glicemia pré-café da manhã (em jejum)')
print('-------------------------------------------------------------------')
print(dados_1)
print('-------------------------------------------------------------------')

with open('dados_em_jejum.txt', 'w') as arquivo:
    for linha in dados_1:
        arquivo.write(str(linha) + '\n')


# dados 2
with open('data/Diabetes-Data/data-03', 'r') as arquivo:
    for linha in arquivo:
        valor = linha.split()
        if valor[2] == '61':
            dados_2.insert(0, int(valor[3]))   
            print(valor[2], valor[3])

print('-------------------------------------------------------------------')
print('Medição da glicemia pós-almoço (pós-sobrecarga))')
print('-------------------------------------------------------------------')
print(dados_2)
print('-------------------------------------------------------------------')

with open('dados_pos_sobrecarga.txt', 'w') as arquivo:
    for linha in dados_2:
        arquivo.write(str(linha) + '\n')


# dados 3
with open('data/Diabetes-Data/data-01', 'r') as arquivo:
    for linha in arquivo:
        valor = linha.split()
        if valor[2] == '48':
            dados_3.insert(0, int(valor[3]))   
            print(valor[2], valor[3])

print('-------------------------------------------------------------------')
print('Medição da glicemia não especificada (glicemia casual))')
print('-------------------------------------------------------------------')
print(dados_3)
print('-------------------------------------------------------------------')

with open('dados_glicemia_casual.txt', 'w') as arquivo:
    for linha in dados_3:
        arquivo.write(str(linha) + '\n')
             
# 48 = Medição de glicemia não especificada
# 57 = Medição de glicemia não especificada
# 58 = Medição de glicemia pré-café da manhã
# 59 = Glicemia pós-café da manhã medição
# 60 = Medição da glicemia antes do almoço
# 61 = Medição da glicemia pós-almoço
# 62 = Medição da glicemia antes do jantar 
# 63 = Medição da glicemia após o jantar
# 64 = Medição da glicemia antes do lanche