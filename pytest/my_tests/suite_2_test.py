import  pytest
pytestmark = [pytest.mark.frontend, pytest.mark.slow]

@pytest.mark.regression
class TestCheckout:
    def test_checkout_as_guest(self):
        print('\nCheckout guest')
    def test_checkout_existing_user(self):
        print('\nCheckout existing user.')