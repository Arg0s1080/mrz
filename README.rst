MRZ Generator & MRZ Checker
===========================

Description:
------------

Machine Readable Zone generator and checker for official travel
documents sizes 1, 2, 3, MRVA and MRVB (Passports, Visas, national id
cards and other travel documents)

MRZ Generator and MRZ Checker are built according to International Civil
Aviation Organization specifications (ICAO 9303):

-  `Specifications Common to all Machine Readable Travel Documents
   (MRTDs) <https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf>`__
-  `Specifications for Machine Readable Passports
   (MRPs) <https://www.icao.int/publications/Documents/9303_p4_cons_en.pdf>`__
-  `Specifications for TD1 Size Machine Readable Official Travel
   Documents
   (MROTDs) <https://www.icao.int/publications/Documents/9303_p5_cons_en.pdf>`__
-  `Specifications for TD2 Size Machine Readable Official Travel
   Documents
   (MROTDs) <https://www.icao.int/publications/Documents/9303_p6_cons_en.pdf>`__
-  `Specifications for Machine Readable Visas
   (MRV) <https://www.icao.int/publications/Documents/9303_p7_cons_en.pdf>`__

See all 9303 ICAO docs (`البيت العربي <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/Arab/Files_ar.rst>`__, `中文 <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/Chinese/Files_zh.rst>`__, `English <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/English/Files_en.rst>`__, `Français <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/French/Files_fr.rst>`__, `Русский <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/Russian/Files_ru.rst>`__ and `Español <https://github.com/Arg0s1080/mrz/tree/master/docs/ICAO9303/Spanish/Files_es.rst>`__)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

Fields Distribution of Official Travel Documents:
-------------------------------------------------

.. figure:: https://raw.githubusercontent.com/Arg0s1080/mrz/master/docs/Fields_Distribution.png
   :alt: image

   image

Usage Generator:
----------------

TD1's (id cards):
^^^^^^^^^^^^^^^^^

::

    Params:                      Case insensitive

        document_type    (str):  The first letter shall be 'I', 'A' or 'C'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        document_number  (str):  Document number
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        nationality      (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Holder primary identifier(s). This field will be transliterated
        given_names      (str):  Holder secondary identifier(s). This field will be transliterated
        optional_data1   (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default
        optional_data2   (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.
                                 

TD2
^^^

::

    Params:                      Case insensitive

        document_type    (str):  The first letter shall be 'I', 'A' or 'C'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Holder primary identifier(s). This field will be transliterated.
        given_names      (str):  Holder secondary identifier(s). This field will be transliterated.
        document_number  (str):  Document number.
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional_data    (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.
                                 

TD3 (Passports)
^^^^^^^^^^^^^^^

::

    Params:                      Case insensitive

        document_type    (str):  Normally 'P' for passport
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        document_number  (str):  Document number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional data    (str):  Personal number. In some countries non-mandatory field. Empty string by default
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.
                                 

MRVA (Visas type A)
^^^^^^^^^^^^^^^^^^^

::

    Params:                      Case insensitive

        document_type    (str):  The First letter must be 'V'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        document_number  (str):  Document number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional_data    (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default.
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.
                          

MRVB (Visas type B)
^^^^^^^^^^^^^^^^^^^

::

    Params:                      Case insensitive

        document_type    (str):  The First letter must be 'V'
        country_code     (str):  3 letters code (ISO 3166-1) or country name (in English)
        surname          (str):  Primary identifier(s)
        given_names      (str):  Secondary identifier(s)
        document_number  (str):  Document number
        nationality      (str):  3 letters code (ISO 3166-1) or country name
        birth_date       (str):  YYMMDD
        sex              (str):  Genre. Male: 'M', Female: 'F' or Undefined: 'X', "<" or ""
        expiry_date      (str):  YYMMDD
        optional_data    (str):  Optional personal data at the discretion of the issuing State.
                                 Non-mandatory field. Empty string by default.
        transliteration (dict):  Transliteration dictionary for non-ascii chars. Latin based by default
        force           (bool):  Disables checks for country, nationality and document_type fields.
                                 Allows to use 3-letter-codes not included in the countries dictionary
                                 and to use document_type codes without restrictions.
                                 

Passport generator example (ICAO9303 Specimen):
'''''''''''''''''''''''''''''''''''''''''''''''

.. figure:: https://raw.githubusercontent.com/Arg0s1080/mrz/master/docs/images/passports/ICAO_Example.png
   :alt: image

   image

TD3CodeGenerator -> str:
''''''''''''''''''''''''

.. code:: python

    from mrz.generator.td3 import TD3CodeGenerator

    code = TD3CodeGenerator("P", "UTO", "Eriksson", "Anna María", "L898902C3", "UTO", "740812", "F", "120415","ZE184226B")

    print(code)

Output:
'''''''

::

    P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<
    L898902C36UTO7408122F1204159ZE184226B<<<<<10

Note: See other uses in `mrz.generator examples folder <https://github.com/Arg0s1080/mrz/tree/master/examples/mrz_generator_samples>`__
                                                                                                                                       

Usage Checker:
--------------

TD1's (id cards):
^^^^^^^^^^^^^^^^^

::

    Params:

        mrz_string        (str):  MRZ string of TD1. Must be 90 uppercase characters long (3 lines)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False

TD2:
^^^^

::

    Params:

        mrz_string        (str):  MRZ string of TD2. Must be 72 characters long (uppercase) (2 lines)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False
        

TD3 (Passports):
^^^^^^^^^^^^^^^^

::

    Params:

        mrz_string        (str):  MRZ string of TD3. Must be 88 characters long (uppercase) (2 lines)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False
        

MRVA:
^^^^^

::

    Params:

        mrz_string        (str):  MRZ string of Visas type A. Must be 88 characters long (uppercase) (2 lines)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False
        

MRVB:
^^^^^

::

    Params:

        mrz_string        (str):  MRZ string of Visas type B. Must be 72 characters long (uppercase) (2 lines)
        check_expiry     (bool):  If it's set to True, it is verified and reported as warning that the
                                  document is not expired and that expiry_date is not greater than 10 years
        compute_warnings (bool):  If it's set True, warnings compute as False
        

Id Card Checker example
'''''''''''''''''''''''

.. figure:: https://raw.githubusercontent.com/Arg0s1080/mrz/master/docs/images/id_cards/Sweden.png
   :alt: image

   image

TD1CodeChecker -> bool
''''''''''''''''''''''

.. code:: python

    from mrz.checker.td1 import TD1CodeChecker
        
    check = TD1CodeChecker("I<SWE59000002<8198703142391<<<\n"
                           "8703145M1701027SWE<<<<<<<<<<<8\n"
                           "SPECIMEN<<SVEN<<<<<<<<<<<<<<<<")
    result = bool(check)
    print(result)

Output
''''''

::

    True

Note: See other uses in `mrz.checker examples folder <https://github.com/Arg0s1080/mrz/tree/master/examples/mrz_checker_samples>`__
                                                                                                                                   

Fields extraction example (valid for td1, td2, td3 and visas)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    from mrz.checker.td1 import TD1CodeChecker, get_country

    td1_check = TD1CodeChecker("IDLIEID98754015<<<<<<<<<<<<<<<\n"
                               "8205122M1906224LIE<<<<<<<<<<<6\n"
                               "OSPELT<BECK<<MARISA<<<<<<<<<<<")

    fields = td1_check.fields()

    print(fields.name, fields.surname)
    print(get_country(fields.country))

Output
''''''

::

    MARISA OSPELT BECK
    Liechtenstein

Note: See other uses in `mrz.checker examples folder <https://github.com/Arg0s1080/mrz/tree/master/examples/mrz_checker_samples>`__ and `this issue <https://github.com/Arg0s1080/mrz/issues/6>`__
                                                                                                                                                                                                  

Installation:
-------------

From `Pypi repo <https://pypi.org/project/mrz/>`__ (It may not be the latest version):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    pip install mrz 

Cloning this repo (It may not work fine):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    git clone https://github.com/Arg0s1080/mrz.git
    cd mrz
    sudo python3 setup.py install

Features:
---------

-  [x] Transliteration of special Latin characters (acutes, tildes,
   diaeresis, graves, circumflex, etc)
-  [x] Arabic chars transliteration
-  [x] Several variations of Cyrillic added: Serbian, Macedonian,
   Belarusian, Ukrainian and Bulgarian
-  [x] Transliteration of modern Greek (experimental)
-  [x] Transliteration of modern Hebrew (without vowels) (experimental)
-  [x] Generation of the country code from its name in English (Ex.:
   "Netherlands" -> "NLD")
-  [x] Name truncation detection
-  [x] Error report, warnings report and full report in Checker.
-  [x] Possibility that warnings compute as errors using
   compute\_warnings keyword in Checker.
-  [x] Possibility of disabling checks for country code, nationality and
   type of document, allowing to use 3-letter-codes not included in the
   countries dictionary and to use document\_type codes without
   restrictions in Generator.
-  [x] Added new checks for periods of time in Checker.
-  [x] Visas support
-  [x] Fields extraction in checker (name, surname, country, sex, etc)
   (version 0.5.0)

TODO:
     

-  [ ] Automatic name truncation in Generator
-  [ ] Possibility of disabling checks for country code, nationality,
   type of document and the others fields in Checker.
-  [ ] Add logging
