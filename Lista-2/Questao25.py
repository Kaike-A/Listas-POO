#Durante o monitoramento de um servidor, um sistema registra os tempos de resposta das requisições, em milissegundos, armazenando-os em uma lista ordenada de forma crescente.
#Desenvolva uma função em Python que receba:

#uma lista contendo os tempos de resposta;
#um limite inferior;
#um limite superior.

#A função deverá identificar e exibir uma sublista contendo apenas os tempos de resposta
#maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

#tempos = [15, 22, 35, 48, 60, 75, 90, 120]
#limite inferior = 35
#limite superior = 75

#Saídas [35, 48, 60, 75]


def filtrar_tempo(tempos, limite_inferior, limite_superior):
    resultado = []

    for tempo in tempos:
        if tempo >= limite_inferior and tempo <= limite_superior:
            resultado.append(tempo)
    return resultado

tempos = [15, 22, 35, 48, 60, 75, 90, 120]
saida = filtrar_tempo(tempos, 35, 75)
print(saida)