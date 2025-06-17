# Sistema de Atendimento Médico
---

## Descrição do Desafio: Sistema de Atendimento Médico

Uma clínica médica deseja automatizar seu sistema de atendimento ao paciente. Para isso, é necessário criar uma função que organize os pacientes em uma fila de prioridade, considerando a idade e a urgência do caso.

### 📌 Critérios de Prioridade:

* **Prioridade Máxima:** Pacientes que apresentam a palavra `"urgente"` na ficha.
* **Prioridade Intermediária:** Pacientes com idade acima de 60 anos (que não sejam "urgentes").
* **Ordem de Chegada:** Os demais pacientes são atendidos por ordem de chegada.

### Entrada

Você receberá os seguintes dados:

1.  Um número inteiro `n`, representando a quantidade de pacientes.
2.  `n` linhas subsequentes, cada uma contendo os dados de um paciente no formato: `nome, idade, status`.
    * `nome`: Uma `string` representando o nome do paciente.
    * `idade`: Um número inteiro representando a idade do paciente.
    * `status`: Uma `string` que pode ser `"urgente"` ou `"normal"`.

### Saída

A saída esperada deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato:
`Ordem de Atendimento: nome1, nome2, nome3, ...`

### Exemplos

A tabela abaixo apresenta exemplos de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                         | Saída Esperada                                      |
| :---------------------------------------------- | :-------------------------------------------------- |
| 3<br>Carlos, 40, normal<br>Ana, 70, normal<br>Bruno, 30, urgente | Ordem de Atendimento: Bruno, Ana, Carlos            |
| 4<br>Paula, 30, normal<br>Ricardo, 60, normal<br>Tiago, 60, urgente<br>Amanda, 50, urgente | Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula |
| 5<br>João, 65, normal<br>Maria, 80, urgente<br>Lucas, 50, normal<br>Fernanda, 25, normal<br>Pedro, 90, urgente | Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda |

---
**Atenção:** É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
