# ---------------------------------------------------------------------------------------
# Objetivo: testes de unidade da classe Anbima
# ---------------------------------------------------------------------------------------
import os
import sys

try:
    libyshire = os.path.abspath(
        os.path.join(os.path.abspath(__file__),
                     os.path.abspath('./../../src/')))

    root = os.path.abspath(
        os.path.join(os.path.abspath(__file__),
                     os.path.abspath('./src/')))

    sys.path.append(libyshire)
    sys.path.append(root)

except:
    print('erro ao tentar importar modulo')


def test_validacao_feriados_ano_2023():
    # Arrange
    from libyshire.anbima import Anbima
    anbima = Anbima()

    # Act
    feriados = anbima.gerar_feriados(2023)

    # Assert
    assert 12 == len(feriados)
    assert '2023-01-01' == feriados[0]


def test_validacao_feriados_ano_2024():
    # Arrange
    from libyshire.anbima import Anbima
    anbima = Anbima()

    # Act
    feriados = anbima.gerar_feriados(2024)

    # Assert
    assert 13 == len(feriados)
    assert '2024-01-01' == feriados[0]
