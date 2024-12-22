from framework.browser.Browser import Browser
from framework.utils.EnvReader import EnvReader

REFRESH_LEAD_ETISALAT = "api/etisalat/deleteAllLeads"


class EtisalatLeadSteps:
    """Refresh Etisalat lead"""

    @staticmethod
    def refresh_lead_etisalat(url):
        """
        Refresh a Lead for Etisalat
        """
        Browser.set_url(EnvReader().get_env_config()['start_url'] + url)
