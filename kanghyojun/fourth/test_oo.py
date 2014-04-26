# -*- coding: utf-8 -*-

class Animal(object):
    """ 동물 클래스
    """

    def __init__(self, name):
        self.name = name

    def grawl(self):
        """ 동물을 울부짖게 만든다

        .. sourcecode: python

           >>> a = Animal()
           >>> a.grawl()
           'grawl'
        """
        #return '{0} grawl!'.format(self.name)
        return '{name} grawl!'.format(name=self.name)


class Human(Animal):

    def __init__(self, name, age):
        super(Human, self).__init__(name)
        self.age = age

    def say(self, words):
        return '%s say: %s' % (self.name, words)

    def __repr__(self):
        return 'Human(%s)' % self.name

    def __str__(self):
        """ __len__, __cmp__, __lt__, __rt__, __eq__,
            __getitem__, __setitem__, __delitem__
        """
        return 'str-human.%s' % self.name


def test_animal():
    ani_name = 'dog'
    ani = Animal(ani_name)
    assert ani_name == ani.name
    assert 'dog grawl!' == ani.grawl()


def test_human():
    # representation -> repr
    name = 'hyojun'
    age = 12
    hyojun = Human(name, age)
    assert name == hyojun.name
    assert age == hyojun.age
    assert 'hyojun grawl!' == hyojun.grawl()
    assert 'hyojun say: hello' == hyojun.say('hello')
    assert 'Human(hyojun)' == repr(hyojun)
    assert 'str-human.hyojun' == str(hyojun)
