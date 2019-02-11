import doorbell


def test_ring_returns_an_int():
    print(doorbell.ring(106))
    assert type(doorbell.ring(106)) is int


def test_ring_returns_ding():
    print(doorbell.ring(6))
    assert doorbell.ring(6) == "Ding"


def test_ring_returns_dong():
    print(doorbell.ring(5))
    assert doorbell.ring(5) == "Dang"


def test_ring_returns_dingdang():
    print(doorbell.ring(15))
    assert doorbell.ring(15) == "DingDang"


def test_ring_returns_dang():
    print(doorbell.ring(7))
    assert doorbell.ring(7) == "Dong"


def test_ring_returns_dingdangdong():
    print(doorbell.ring(105))
    assert doorbell.ring(105) == "DingDangDong"


def test_ring_returns_dangdong():
    print(doorbell.ring(35))
    assert doorbell.ring(35) == "DangDong"


def test_ring_returns_dingdong():
    print(doorbell.ring(21))
    assert doorbell.ring(21) == "DingDong"
