from customer_pipeline.ingestion import get_customer


def test_get_customer():
    result = get_customer(101)

    assert result["customer_id"] == 101
    assert result["name"] == "jhon"