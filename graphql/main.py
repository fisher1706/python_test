import requests


query_company_ceo_coo_name = """
{
    company {
        ceo
        coo
        name
    }
}
"""


def test_retrieve_graphql_data_should_yield_ceo_elon_musk():
    response = requests.post(
        "https://api.spacex.land/graphql/", json={"query": query_company_ceo_coo_name}
    )
    print(response)
    response_body = response.json()
    print(f"response: {response_body}")
    assert response_body["data"]["company"]["ceo"] == "Elon Musk"
