import pytest
from .inscritos_repository import InscritosRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "meuNome",
        "email": "email@dominio.com",
        "evento_id": 2
    }
    subs_repo = InscritosRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "email@dominio.com"
    evento_id = 2

    subs_repo = InscritosRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)

@pytest.mark.skip("Select in DB")
def test_ranking():
    evento_id = 2
    subs_repo = InscritosRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()
    
    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")