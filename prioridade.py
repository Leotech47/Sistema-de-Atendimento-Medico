# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes, agora com o índice original
pacientes = []

# Loop para entrada de dados
for i in range(n): # Adicione 'i' para o índice original
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status, i)) # Adiciona o índice 'i'

def get_prioridade(paciente):
    nome, idade, status, indice_original = paciente

    if status == "urgente":
        # Entre urgentes, priorize por idade (decrescente), depois por ordem de chegada (crescente)
        return (3, idade, -indice_original) # Prioridade máxima: (nível, idade, -indice_original)
    elif idade >= 60: # Inclui 60 anos aqui se não for urgente, como idoso prioritário
        # Pacientes >= 60 anos (mas não urgentes)
        # Priorize por idade (decrescente), depois por ordem de chegada (crescente)
        return (2, idade, -indice_original) # Prioridade intermediária: (nível, idade, -indice_original)
    else:
        # Demais pacientes (normais e menores de 60)
        # Ordem de chegada (crescente)
        return (1, idade, -indice_original) # Prioridade baixa: (nível, idade, -indice_original)

# A ordenação será feita por tuplas: (prioridade_numerica, idade_do_paciente, -indice_original).
# A primeira chave (prioridade_numerica) é decrescente (por causa do reverse=True no sort).
# A segunda chave (idade_do_paciente) é decrescente (porque é importante para "urgente" e "idoso").
# A terceira chave (-indice_original) é decrescente, o que faz com que o menor indice_original (primeiro a chegar) venha antes.
pacientes.sort(key=get_prioridade, reverse=True)


# TODO: Exiba a ordem de atendimento com título e vírgulas:
nomes_ordenados = [paciente[0] for paciente in pacientes]
print("Ordem de Atendimento: " + ", ".join(nomes_ordenados))
