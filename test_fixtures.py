import pytest

@pytest.fixture
def empty_list():
    return []

def test_len_of_empty_list(empty_list):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0


@pytest.fixture
def one_item(empty_list):
    empty_list.append("item")
    return empty_list

def test_len_of_unary_list(one_item):
    assert isinstance(one_item, list)
    assert len(one_item) == 1
    assert one_item[0] == "item"


# def test_get_all_planets_with_no_records(client):
#     response = client.get("/planet")
#     response_body = response.get_json()

#     assert response.status_code == 200
#     assert response_body == []

