import pytest
from django.utils import timezone
from gastos.models import Despesa

@pytest.mark.django_db
def test_criar_despesa():
    despesa = Despesa.objects.create(
        descricao="Aluguel",
        valor=1500.00,
        categoria="Moradia",
        data=timezone.now().date()
    )

    assert despesa.id is not None
    assert despesa.descricao == "Aluguel"
    assert despesa.valor == 1500.00
    assert despesa.categoria == "Moradia"
    assert despesa.data is not None

@pytest.mark.django_db
def test_str_despesa():
    despesa = Despesa.objects.create(
        descricao="Supermercado",
        valor=250.75,
        categoria="Alimentação",
        data=timezone.now().date()
    )

    assert str(despesa) == "Supermercado — R$ 250.75"

@pytest.mark.django_db
def test_listagem_despesa():
    Despesa.objects.create(
        descricao="Transporte",
        valor=100.00,
        categoria="Transporte",
        data=timezone.now().date()
    )
    Despesa.objects.create(
        descricao="Cinema",
        valor=50.00,
        categoria="Lazer",
        data=timezone.now().date()
    )

    despesas = Despesa.objects.all()
    assert despesas.count() == 2
    assert despesas[0].descricao == "Cinema"
    assert despesas[1].descricao == "Transporte"
