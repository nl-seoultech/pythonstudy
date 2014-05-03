class Animal(object):

    def __init__(self, name):
       self.name=name


    def grawl(self):

	return '{0} grawl'.format(self.name)
 	#return '{name} grawl!'.format(name) = self.(name)

class Human(Animal):
    
    def __init__(self, name, age):
        self.name = name
        super(Human, self).__init__(name)
        self.age = age

    def say(self,words):
        return '%s say : %s' % (self.name, words)

    def __repr__(self):
        return 'Human(%s)' % self.name

    def __str__(self):
        return 'str-human.%s' % self.name


def test_animal():
   
    ani_name = 'dog'
    animal = Animal(ani_name)
    assert ani_name == ani.name
    assert 'dog grawl!' == ani.grawl()

def test_human():
    name = 'jinseok'
    age = 27
    jinseok = Human(name, age)
    assert name == jinseok.name
    assert 'jinseok grawl' == jinseok.grawl()
    assert 'jinseok say : Hello' == jinseok.say('Hello')
    assert 'Human(jinseok)' == repr(jinseok)
    assert 'str-human.jinseok' == str(jinseok)
