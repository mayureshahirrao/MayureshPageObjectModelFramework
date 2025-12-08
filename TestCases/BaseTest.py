import pytest

@pytest.mark.usefixtures("on_log_failure", "browser_setup")
class BaseTest:
    pass