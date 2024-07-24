# ---------------------------------------------------------------------------------------
# Feature: Coleção de funções para formar o calendário de feriados
# Autor:   Claudio Alves Jr
# Changes:
#    01) Data:      2024-07-23
#        Descrição: Criação de uma função de retorne a data do domingo de pascoa
#                   a partir de um ano informado.
# ---------------------------------------------------------------------------------------
# Imports
from datetime import date, timedelta


# Functions
def obter_domingo_pascoa(ano: int) -> date:
    """
    retorna o domingo de páscoa para o ano informado
    :param ano: ano para o qual deseja-se obter o domingo de pascoa
    :return: data do domingo de páscoa
    """
    step_1 = ano % 19
    step_2 = ano // 100
    step_3 = ano % 100
    step_4 = step_2 // 4
    step_5 = step_2 % 4
    step_6 = (step_2 + 8) // 25
    step_7 = (step_2 - step_6 + 1) // 3
    step_8 = (19 * step_1 + step_2 - step_4 - step_7 + 15) % 30
    step_9 = step_3 // 4
    step_10 = step_3 % 4
    step_11 = (32 + 2 * step_5 + 2 * step_9 - step_8 - step_10) % 7
    step_12 = (step_1 + 11 * step_8 + 22 * step_11) // 451

    mes = (step_8 + step_11 - 7 * step_12 + 114) // 31
    dia = ((step_8 + step_11 - 7 * step_12 + 114) % 31) + 1

    return date(year=ano, month=mes, day=dia)


def obter_data_com_intervalo(data: date, intervalo: int) -> date:
    return data + timedelta(days=intervalo)


def formatar_feriados(data: date) -> str:
    return data.strftime('%Y-%m-%d')
