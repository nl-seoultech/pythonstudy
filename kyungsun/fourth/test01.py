# -*- coding: utf-8 -*-

class Animal(object):
    
    """ 동물 클래스
    """
    
    def __init__(self, name):
        self.name = name


    def grawl(self):
        """ 동물을 울부짖게 만든다
        """
       # return '{0} grawl!'.format(self.name) 
        return '{name} grawl!'.format(name=self.name)

class Human(Animal):

    def __init__(self, name, age):
        super(Human, self).__init__(name)
        self.age = age

    def say(self , word):
        return '%s say : %s' % (self.name, word)

    def __repr__(self):
        return 'Human(%s)' % self.name

    def __str__(self):
        return 'str-human.%s' % self.name


def test_Animal():
    ani_name ='dog'
    ani = Animal(ani_name)

    assert ani_name == ani.name
    assert 'dog grawl!' == ani.grawl()


def test_Human():
    name = 'kyungsun'
    age = '22'
    human = Human(name, age)
    assert name == human.name
    assert age == human.age
    assert 'kyungsun grawl!' == human.grawl()
    assert 'kyungsun say : hello' == human.say('hello')
    assert 'Human(kyungsun)' == repr(human)
    assert 'str-human.kyungsun' == str(human)
