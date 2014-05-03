# -*- coding: utf-8 -*-


def type_discriminate(data):
    """ method to discriminate the input data type """

    if isinstance(data, bool):
        return "bool"
    
    elif isinstance(data, int):
        return "int"

    elif isinstance(data, float):
        return "float"

    elif isinstance(data, str):
        return "str"

    elif isinstance(data, unicode):
        return "unicode"

    elif isinstance(data, type):
        return "type"

    elif isinstance(data, NoneType):
        return "NoneType"

    else:
        return "none of data"



def test_type_discriminate():
    assert "bool" == type_discriminate(False)
    assert "int"  == type_discriminate(1)
    assert "float" == type_discriminate(1.1)
    assert "str"  == type_discriminate("abc")
    assert "unicode" == type_discriminate(u"tiffany")
    assert "type" == type_discriminate(str)

    """
    assert "NoneType"	== type_discriminate(None)

    ##in repple, "type(None)" print "NoneType", but this type is undefined.
    """
