import os
from typing import Optional
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR,
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def translate(text: str, model_id: str) -> Optional[str]:
    """
    Translates the given text using the specified model ID.

    Args:
        text: The text to translate.
        model_id: The model ID to use for translation.

    Returns:
        The translation of the input text, or None if an error occurred.
    """
    if not isinstance(text, str):
        return None
    try:
        response = LANGUAGE_TRANSLATOR.translate(
            text=text,
            model_id=model_id
        ).get_result()
        return response["translations"][0]["translation"]
    except Exception:
        return None

def english_to_french(english_text: str) -> Optional[str]:
    """
    Translates English text to French.

    Args:
        english_text: The English text to translate.

    Returns:
        The French translation of the input text, or None if an error occurred.
    """
    return translate(english_text, 'en-fr')

def french_to_english(french_text: str) -> Optional[str]:
    """
    Translates French text to English.

    Args:
        french_text: The French text to translate.

    Returns:
        The English translation of the input text, or None if an error occurred.
    """
    return translate(french_text, 'fr-en')

if __name__ == "__main__":
    english_text = "Hello"
    french_text = "Bonjour"
    print(english_to_french(english_text))
    print(french_to_english(french_text))
