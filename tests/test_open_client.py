import tempfile

from frogsay.client import open_client


def test_empty_cache_fetches_more_tips():
    with tempfile.NamedTemporaryFile() as file:
        with open_client(file.name) as client:
            # Exhaust all tips
            tries = 0
            max_tips = 49
            client.frog_tip()

            while not client.should_refresh:
                tries += 1
                client.frog_tip()

            assert tries == max_tips

        # Ensure the cache is empty
        contents = file.read()
        assert contents == b''
