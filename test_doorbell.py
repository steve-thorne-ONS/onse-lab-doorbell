import doorbell


def test_ring_returns_a_string():
    assert type(doorbell.ring(1)) is str
