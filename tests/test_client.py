from frogsay.client import Client


def test_empty_cache_fetches_more_tips():
    cache = {}
    client = Client(cache)

    assert client.should_refresh

    tip = client.frog_tip()

    assert tip is not None
    assert not client.should_refresh

def test_non_empty_cache_returns_existing_tips():
    expected_tip = "DO NOT HARDCORE FROG'S TEST DATA. THIS IS BAD PRACTICE AND WILL CONFUSE FROG."
    cache = {
        '1': expected_tip
    }
    client = Client(cache)

    tip = client.frog_tip()
    assert tip == expected_tip
    assert client.should_refresh
