import os


class CredentialUtilites():

    @staticmethod
    def get_wc_api_keys():

        WC_KEY = os.environ.get('WC_KEY')
        WC_SECRET = os.environ.get('WC_SECRET')

        if not WC_KEY or not WC_SECRET:
            raise Exception ('API credentials are not set as environment variable')

        else:
            return {'wc_key':WC_KEY, 'wc_secret' : WC_SECRET}

    @staticmethod
    def get_db_credentials():

        DB_USER = os.environ.get('DB_USER')
        DB_PASSWORD = os.environ.get('DB_PASSWORD')

        if not DB_USER or not DB_PASSWORD:
            raise Exception ('DB credentials are not set as environment variable')

        else:
            return {'db_user':DB_USER, 'db_password' : DB_PASSWORD}
