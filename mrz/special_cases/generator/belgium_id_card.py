from mrz.generator.td1 import *
from mrz.base.string_checkers import field
from mrz.base.functions import hash_string


class TD1BELCodeGenerator(TD1CodeGenerator):

    @property
    def document_number(self) -> str:
        return self._document_number

    @document_number.setter
    def document_number(self, value: str, set_hash=True):
        sc = ("<", " ")
        for c in sc:
            if c in value:
                if c == value[9]:
                    value = value.replace(c, "")
                else:
                    # TODO: Raise error
                    print("special char is not in correct position")
                break
            else:
                # special char not detected
                pass
        first = value[:9]
        second = "%s%s" % (value[9:], hash_string("%s<%s" % (first, value[9:]))) if set_hash else value[9:]
        self._document_number = field(first, 9, "document number")
        self._optional_data1 = field(second, 15, "optional data 1")

    @property
    def document_number_hash(self) -> str:
        """Return hash digit of document number

        """
        return "<"

    @property
    def optional_data1(self) -> str:
        return self._optional_data1

    @optional_data1.setter
    def optional_data1(self, value: str):
        # TODO: raise an error
        pass





