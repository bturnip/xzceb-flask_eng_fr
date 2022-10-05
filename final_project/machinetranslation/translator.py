''' Translator: uses IBM Watson translation service via API calls '''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
import pandas as pd

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#print(f'+++DEBUG: apikey:{apikey}')
#print(f'+++DEBUG: url:{url}')

# create Translator instance
try:
    auth = IAMAuthenticator(apikey)

    language_translator = LanguageTranslatorV3(
        version='2018-05-01'
        ,authenticator=auth
        )

    language_translator.set_service_url(url)

except Exception as e:
    print(f'+++ERROR: translator instance creation failed:\n{e}')


def englishToFrench(english_text):
    ''' input English text, receive French text'''
    if english_text:
        translation_dict = language_translator.translate(
            text=english_text
            ,model_id='en-fr').get_result()

        # extract the data we want from the dictionary
        lang_df = pd.DataFrame(translation_dict['translations'])
        french_text=lang_df.loc[0]['translation']
        return french_text

    #else
    return None

def frenchToEnglish(french_text):
    ''' input French text, receive English text'''
    if french_text:
        translation_dict = language_translator.translate(
            text=french_text
            ,model_id='fr-en').get_result()

        # extract the data we want from the dictionary
        lang_df = pd.DataFrame(translation_dict['translations'])
        english_text=lang_df.loc[0]['translation']
        return english_text

    # else (whatever, pylint)
    return None
