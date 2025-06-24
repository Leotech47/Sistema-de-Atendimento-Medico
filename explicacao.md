# Explicação do Código: Sistema de Triagem de Pacientes 🏥

Este código implementa um sistema de triagem para definir a ordem de atendimento de pacientes com base em um conjunto de regras de prioridade. A lógica é construída em torno de uma função de ordenação sofisticada.

## Como Funciona

1.  **Captura de Dados e Índice de Chegada**:

      * O programa primeiro lê o número de pacientes a serem cadastrados.
      * Em um loop, ele solicita o `nome`, `idade` e `status` de cada um.
      * Crucialmente, ao adicionar o paciente à lista, ele também armazena o **índice original (`i`)**. Esse índice representa a **ordem de chegada**, que será usada como critério de desempate. Cada paciente é armazenado como uma tupla: `(nome, idade, status, indice_original)`.

2.  **A Função de Prioridade (`get_prioridade`)**:

      * Esta é a parte central do código. Ela serve como a "chave" para a função `sort`, dizendo a ela como comparar dois pacientes.
      * Para cada paciente, a função retorna uma **tupla de três valores**: `(nível, idade, -índice_original)`. A ordenação acontece com base nesses valores, em ordem.

3.  **A Lógica da Ordenação**:

      * O comando `pacientes.sort(key=get_prioridade, reverse=True)` ordena a lista de pacientes em **ordem decrescente** com base nas tuplas geradas pela chave.
      * A comparação funciona assim:
          * **1º Nível de Prioridade (Status)**: O primeiro item da tupla é o nível de urgência (`3` para urgente, `2` para idoso, `1` para normal). Como a ordenação é decrescente, pacientes com `status="urgente"` (nível 3) sempre vêm primeiro.
          * **2º Idade (Desempate)**: Se dois pacientes têm o mesmo nível de prioridade (ex: dois idosos), o Python olha para o segundo item da tupla: a `idade`. Como a ordenação é decrescente, o paciente **mais velho** é atendido primeiro.
          * **3º Ordem de Chegada (Desempate final)**: Se o nível e a idade são idênticos, o critério final é o `-indice_original`. Usar o índice negativo com a ordenação decrescente é um truque inteligente: um número negativo "maior" (ex: -2) vem antes de um "menor" (ex: -3). Isso faz com que o paciente com o menor índice original (que chegou antes) seja priorizado.

4.  **Exibição do Resultado**:

      * Após a ordenação, o código extrai apenas os nomes da lista já ordenada e os exibe em uma única linha, formatada conforme o solicitado.

-----

## Testes do Código 🧪

Abaixo estão três testes que cobrem diferentes cenários para garantir que a lógica de priorização está correta.

| Teste | Entrada | Saída Esperada |
| :--- | :--- | :--- |
| **1. Mix de Prioridades**\<br\ >\<sub\>(Urgente \> Idoso \> Normal)\</sub\> | `3`\<br\>`Carlos, 55, normal`\<br\ >`Beatriz, 80, urgente`\<br\ >`Ana, 70, normal` | `Ordem de Atendimento: Beatriz, Ana, Carlos` |
| **2. Desempate por Idade**\<br\>\<sub\>(Dois idosos com idades diferentes)\</sub\> | `4`\<br\>`Lucas, 25, normal`\<br\>`Mariana, 80, normal`\<br\>`Gustavo, 22, urgente`\<br\>`Helena, 75, normal` | `Ordem de Atendimento: Gustavo, Mariana, Helena, Lucas` |
| **3. Desempate por Chegada**\<br\>\<sub\>(Dois urgentes com a mesma idade)\</sub\> | `4`\<br\>`Joao, 65, urgente`\<br\>`Maria, 40, normal`\<br\>`Pedro, 65, urgente`\<br\>`Sofia, 30, normal` | `Ordem de Atendimento: Joao, Pedro, Maria, Sofia` |
