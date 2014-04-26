# -*- coding: utf-8 -*-



class Animal(object):

    def __init__(self, name):
        self.name = name

    def grawl(self):
        """
        animal crying function
	"""
	return '{name} grawl!'.format(name=self.name)

class Human(Animal):
    def __init__(self, name, age):
	super(Human, self).__init__(name)
	self.age = age

    def say(self, words):
        return '%s say : %s' % (self.name, words)

    def __repr__(self):
        return 'Human(%s)' % self.name
	
    def __str__(self):
        """
        __len__, __cmp__, __lt__, __rt__, __eq__, __getitem__, __setitem__,
        ___delitem__
	"""
        return 'str-human.%s' % self.name


def test_animal():
    ani_name = 'dog'
    ani = Animal(ani_name)
    assert ani_name == ani.name
    assert 'dog grawl!' == ani.grawl()


def test_human():
    name = 'gong'
    age = 22
    gong = Human(name, age)
    assert name == gong.name
    assert age == gong.age
    assert 'gong grawl!' == gong.grawl()
    assert 'gong say : hello' == gong.say('hello')
    assert 'Human(gong)' == repr(gong)
    assert 'str-human.gong' == str(gong)
    
