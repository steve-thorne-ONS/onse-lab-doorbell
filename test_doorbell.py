import doorbell


def test_ring_returns_a_string():
    assert type(doorbell.ring(1)) is str


def test_ring_returns_1_when_called_with_1():
    assert doorbell.ring(1) == '1'


def test_ring_returns_2_when_called_with_2():
    assert doorbell.ring(2) == '2'


def test_ring_returns_ding_when_called_with_3():
    assert doorbell.ring(3) == 'Ding'


def test_ring_returns_ding_when_called_with_6():
    assert doorbell.ring(6) == 'Ding'


def test_ring_returns_dang_when_called_with_5():
    assert doorbell.ring(5) == 'Dang'


def test_ring_returns_dang_when_called_with_10():
    assert doorbell.ring(10) == 'Dang'


def test_ring_returns_dong_when_called_with_7():
    assert doorbell.ring(7) == 'Dong'


def test_ring_returns_dong_when_called_with_14():
    assert doorbell.ring(14) == 'Dong'


def test_ring_returns_dingdang_when_called_with_15():
    assert doorbell.ring(15) == 'DingDang'


def test_ring_returns_dingdang_when_called_with_30():
    assert doorbell.ring(30) == 'DingDang'


def test_ring_returns_dingdong_when_called_with_21():
    assert doorbell.ring(21) == 'DingDong'


def test_ring_returns_dangdong_when_called_with_35():
    assert doorbell.ring(35) == 'DangDong'


def test_ring_returns_dingdangdong_when_called_with_105():
    assert doorbell.ring(105) == 'DingDangDong'
