import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))


""" try:
    # Invoke a method
except ApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message


def englishToFrench(englishText):
    #write the code here
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    return englishText
 """