import time

class TestExample:

    def test_a(self):
        assert True
        time.sleep(2)

    def test_b(self):
        assert 2 == 3
        time.sleep(2)

    def test_c(self):
        assert 2 == 2
        time.sleep(2)

    def test_d(self):
        assert False == 2
        time.sleep(2)

    def test_e(self):
        assert True is False
        time.sleep(2)

    def test_f(self):
        assert True
        time.sleep(2)

    def test_g(self):
        assert True
        time.sleep(2)

    def test_h(self):
        assert True
        time.sleep(2)

    def test_i(self):
        assert True
        time.sleep(2)

