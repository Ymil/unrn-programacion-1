from operaciones import sumar
import pytest

def test_sumar_dos_positivos():
    """
    Caso normal
    """
    assert sumar(2, 3) == 5

def test_sumar_invalido():
    """
    Tratando de hacer fallar la función sumar

    Caso invalido
    """
    with pytest.raises(ValueError):
        sumar(-1, 1)