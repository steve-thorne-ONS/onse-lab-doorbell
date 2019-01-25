import doorbell


def test_ring_returns_a_string():
    assert type(doorbell.ring(1)) is str


def test_ring_returns_1_when_called_with_1():
    assert doorbell.ring(1) == '1'


def test_ring_returns_2_when_called_with_2():
    assert doorbell.ring(2) == '2'


def test_ring_returns_7_when_called_with_7():
    assert doorbell.ring(7) == '7'


def test_ring_returns_ding_when_called_with_3():
    assert doorbell.ring(3) == 'Ding'


def test_ring_returns_ding_when_called_with_6():
    assert doorbell.ring(6) == 'Ding'


def test_ring_returns_dong_when_called_with_5():
    assert doorbell.ring(5) == 'Dong'


def test_ring_returns_dong_when_called_with_10():
    assert doorbell.ring(10) == 'Dong'


def test_ring_returns_dingdong_when_called_with_15():
    assert doorbell.ring(15) == 'DingDong'


def test_ring_returns_dingdong_when_called_with_30():
    assert doorbell.ring(30) == 'DingDong'