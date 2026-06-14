import pytest
from django.test import Client
from django.utils import timezone
from gastos.models import Despesa


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def despesa(db):
    return Despesa.objects.create(
        descricao="Aluguel",
        valor="1500.00",
        categoria="moradia",
        data=timezone.now().date(),
    )


@pytest.mark.django_db
def test_index_lista_despesas(client, despesa):
    response = client.get("/")
    assert response.status_code == 200
    assert "Aluguel" in response.content.decode()


@pytest.mark.django_db
def test_adicionar_despesa_via_post(client):
    response = client.post(
        "/adicionar/",
        {
            "descricao": "Mercado",
            "valor": "200.00",
            "categoria": "alimentacao",
            "data": timezone.now().date().isoformat(),
        },
    )
    assert response.status_code == 302
    assert Despesa.objects.filter(descricao="Mercado").exists()


@pytest.mark.django_db
def test_editar_despesa(client, despesa):
    response = client.post(
        f"/editar/{despesa.pk}/",
        {
            "descricao": "Aluguel Atualizado",
            "valor": "1600.00",
            "categoria": "moradia",
            "data": timezone.now().date().isoformat(),
        },
    )
    assert response.status_code == 302
    despesa.refresh_from_db()
    assert despesa.descricao == "Aluguel Atualizado"


@pytest.mark.django_db
def test_excluir_despesa(client, despesa):
    pk = despesa.pk
    response = client.post(f"/excluir/{pk}/")
    assert response.status_code == 302
    assert not Despesa.objects.filter(pk=pk).exists()


@pytest.mark.django_db
def test_filtro_por_categoria(client):
    Despesa.objects.create(
        descricao="Uber", valor="30.00", categoria="transporte", data=timezone.now().date()
    )
    Despesa.objects.create(
        descricao="Pizza", valor="50.00", categoria="alimentacao", data=timezone.now().date()
    )
    response = client.get("/?categoria=transporte")
    content = response.content.decode()
    assert "Uber" in content
    assert "Pizza" not in content
