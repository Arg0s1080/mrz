# GNU General Public License v3.0

default = "String was not recognized as a valid "


class FieldError(ValueError):
    def __init__(self, msg="", cause=""):
        self.cause = cause
        self.msg = msg if msg else "String contains invalid characters"
        self.args = (self.msg, self.cause)
        super(FieldError, self).__init__(self.msg, self.cause)

    def __str__(self):
        return str(self.args)


class DateError(FieldError):
    def __init__(self, msg="", cause=""):
        self.msg = msg if msg else default + "date. It should be 'YYMMDD'"
        self.cause = cause
        super(DateError, self).__init__(self.msg, self.cause)


class SexError(FieldError):
    def __init__(self, msg="", cause=""):
        self.msg = msg if msg else default + "genre. Sex code should be 'M', 'F' or 'X'"
        self.cause = cause
        super(SexError, self).__init__(self.msg, self.cause)


class CountryError(FieldError):
    def __init__(self, msg="", cause=""):
        self.msg = msg if msg else default + ("country code or country or country name. It should be a valid "
                                              "country code (3 letters) or a valid country name (english)")
        self.cause = cause
        super(CountryError, self).__init__(self.msg, self.cause)


class DocumentTypeError(FieldError):
    def __init__(self, msg="", cause=""):
        self.msg = msg if msg else default + "type of document."
        self.cause = cause
        super(DocumentTypeError, self).__init__(self.msg, self.cause)


class LengthError(FieldError):
    def __init__(self, msg="", cause=0, document="", length=0, amx=False):
        self.document = document
        self.cause = str(cause)
        extra = " as maximum" if amx else ""
        self.msg = msg if msg else default + "%s. It should have %d characters%s" % (self.document, length, extra)
        super(LengthError, self).__init__(self.msg, self.cause)