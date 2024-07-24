# ---------------------------------------------------------------------------------------
# Objetivo: testes de unidade da classe Anbima
# ---------------------------------------------------------------------------------------
from libyshire.anbima import Anbima


def test_validacao_feriados_ano_2023():
    # Arrange
    anbima = Anbima()

    # Act
    feriados = anbima.gerar_feriados(2023)

    # Assert
    assert 12 == len(feriados)
    assert '2023-01-01' == feriados[0]


def test_validacao_feriados_ano_2024():
    # Arrange
    anbima = Anbima()

    # Act
    feriados = anbima.gerar_feriados(2024)

    # Assert
    assert 13 == len(feriados)
    assert '2024-01-01' == feriados[0]
