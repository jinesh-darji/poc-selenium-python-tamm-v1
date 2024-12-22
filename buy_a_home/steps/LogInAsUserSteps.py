import random

from framework.browser.Browser import Browser
from framework.utils.EnvReader import EnvReader

FAKE_USER = "fake-login?userNumber={}".format(random.randint(40 ** 39, 40 ** 51 - 1))
DUBAI_USER_NOT_VERIFIED = "fake-login?userNumber=DubaiNotVerified"
DUBAI_USER_VERIFIED = "fake-login?userNumber=DubaiVerified"
ABU_DHABI_USER_NOT_VERIFIED = "fake-login?userNumber=ADNotVerified"
ABU_DHABI_USER_VERIFIED = "fake-login?userNumber=ADVerified"
ABU_DHABI_USER_PENDING_VERIFICATION = "fake-login?userNumber=ADPendingVerification"
EXPAT_USER_NOT_VERIFIED = "fake-login?userNumber=expatUserNotVerified"
EXPAT_USER_VERIFIED = "fake-login?userNumber=expatUserVerified"


class LogInAsUserSteps:
    """Log in as an User"""

    @staticmethod
    def login_as_user(user):
        """
        Login as a local and not verified user
        """
        Browser.set_url(EnvReader().get_env_config()['start_url'] + user)
