# ---------------------------------------------------------------------------------------
# Feature: Geração do calendário Anbima
# Autor:   Claudio Alves Jr
# Changes:
#    01) Data:      2024-07-23
#        Descrição: Criação da classe e funções para o retorno dos feriados
# ---------------------------------------------------------------------------------------
# Imports
from datetime import date
from libyshire.extensions import obter_domingo_pascoa, obter_data_com_intervalo, formatar_feriados


# Functions
class Anbima:
    def __init__(self) -> None:
        pass

    def gerar_feriados(self, ano: int = date.today().year) -> list:
        """
        Faz a geração do calendário Anbima de feriados usando como referência: <https://www.anbima.com.br/feriados/feriados.asp>
        :return: lista de feriados Anbima do ano solicitado
        """
        if ((ano < 1980) or (ano > 2200)):
            raise Exception('O ano informado deve ser entre 1980 e 2199')

        feriados: list = []

        # base para os outros feriados, como carnaval e paixão de cristo
        domingo_pascoa = obter_domingo_pascoa(ano)

        feriados.append(formatar_feriados(date(year=ano, month=1, day=1)))                  # Confraternização Universal
        feriados.append(formatar_feriados(obter_data_com_intervalo(domingo_pascoa, -48)))   # segunda-feira de carnaval
        feriados.append(formatar_feriados(obter_data_com_intervalo(domingo_pascoa, -47)))   # terça-feira de carnaval
        feriados.append(formatar_feriados(obter_data_com_intervalo(domingo_pascoa, -2)))    # Paixão de Cristo
        feriados.append(formatar_feriados(date(year=ano, month=4, day=21)))                 # Tiradentes
        feriados.append(formatar_feriados(date(year=ano, month=5, day=1)))                  # Dia do Trabalho
        feriados.append(formatar_feriados(obter_data_com_intervalo(domingo_pascoa, 60)))    # Corpus Christi
        feriados.append(formatar_feriados(date(year=ano, month=9, day=7)))                  # Independência do Brasil
        feriados.append(formatar_feriados(date(year=ano, month=10, day=12)))                # Nossa Senhora Aparecida - Padroeira do Brasil
        feriados.append(formatar_feriados(date(year=ano, month=11, day=2)))                 # Dia de finados
        feriados.append(formatar_feriados(date(year=ano, month=11, day=15)))                # Proclamação da República
        if (ano >= 2024):
            feriados.append(formatar_feriados(date(year=ano, month=11, day=20)))            # Dia Nacional de Zumbi e da Consciência Negra
        feriados.append(formatar_feriados(date(year=ano, month=12, day=25)))                # Natal

        return feriados
