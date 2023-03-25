import allure
import time

class TestExample:

    @allure.title("Test 1")
    def test_a(self):
        assert True
        time.sleep(2)

    @allure.title("Test 2")
    def test_b(self):
        assert 2 == 3
        time.sleep(2)

    @allure.title("Test 3")
    def test_c(self):
        assert 2 == 2
        time.sleep(2)

    @allure.title("Test 4")
    def test_d(self):
        assert False == 2
        time.sleep(2)

    @allure.title("Test 5")
    def test_e(self):
        assert True is False
        time.sleep(2)

    @allure.title("Test 6")
    def test_f(self):
        assert True
        time.sleep(2)

    @allure.title("Test 7")
    def test_g(self):
        assert True
        time.sleep(2)

    @allure.title("Test 8")
    def test_h(self):
        assert True
        time.sleep(2)

    @allure.title("Test 9")
    def test_i(self):
        assert True
        time.sleep(2)

