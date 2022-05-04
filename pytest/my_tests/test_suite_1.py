import  pytest
pytestmark = [pytest.mark.frontend, pytest.mark.slow]

@pytest.mark.smoke
def test_login_page_valid_user():
    print('\nLogin with valid user')

@pytest.mark.regression
@pytest.mark.smoke
def test_loging_wrong_password():
    print('\nLogin with wrong valid user')
    # assert 1==2, 'failed'
