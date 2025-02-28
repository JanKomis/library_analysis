import pycountry
import pandas as pd

MACRO_LANGS = {
    "crp",  # Creoles and pidgins (general category)
    "zh",   # Chinese (macro language)
    "ar",   # Arabic (macro language)
    "sla",  # Slavic languages
    "bnt",  # Bantu languages
    "mis",  # Uncoded languages
    "cpe",  # Creoles and pidgins based on English
    "cpf",  # Creoles and pidgins based on French
    "cpp",  # Creoles and pidgins based on Portuguese
    "fiu",  # Finno-Ugric languages
    "ira",  # Iranian languages
    "apa",  # Apache languages
    "ypk",  # Yupik languages
    "sem",  # Semitic languages
    "pra",  # Prakrit languages (Middle Indic languages)
    "phi",  # Philippine languages
    "roa",  # Romance languages
    "art",  # Artificial languages (e.g., Esperanto)
    "tai",  # Tai-Kadai languages
    "aus"   #Australian Aboriginal languages
}

def contain_lang(pandas_series):
    if not isinstance(pandas_series, pd.Series):
        raise TypeError("Input must be a pandas Series")

    def is_valid_language(lang):
        if pd.isna(lang):
            return False
        return bool(
            pycountry.languages.get(alpha_2=lang) or 
            pycountry.languages.get(alpha_3=lang) or 
            lang in MACRO_LANGS
        )

    return pandas_series.apply(is_valid_language).astype(bool)

