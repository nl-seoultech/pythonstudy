# -*- coding: utf-8 -*-

class Robot(object):
    """ 로봇 클래스입니다
    """

    def __init__(self, name):
        self.name = name

    def transform(self):
        """  로봇을 변신시키는 함수입니다.

        .. sourcecode::python

           >>> r = Robot('a')
           >>> r.transform()
        """
        # '%s transform!!!' % self.name
        # '{0} transform!!!'.format(self.name)
        return '{n} transform!!!'.format(n=self.name)


class SuperRobot(Robot):

    def __init__(self, name, special_weapon):
        super(SuperRobot, self).__init__(name)
        self.special_weapon = special_weapon

    def transform(self):
        return u'%s 발싸!, %s 변신!' % (self.special_weapon, self.name)

    def __repr__(self):
        return 'SuperRobot(%s, %s)' % (self.name, self.special_weapon)

    def __str__(self):
        return 'SuperStr(%s, %s)' % (self.name, self.special_weapon)


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


def test_robot():
    # DRY - Don't Repeat Yourself
    a = 'gundam'
    robot = Robot(a)
    assert a == robot.name
    assert 'gundam transform!!!' == robot.transform()


def test_super_robot():
    # pythonic
    n = 'SuperGundam'
    weap = 'shining finger'
    super_robot = SuperRobot(n, weap)
    assert n == super_robot.name
    assert weap == super_robot.special_weapon
    assert 'SuperRobot(SuperGundam, shining finger)' == repr(super_robot)
    assert 'SuperStr(SuperGundam, shining finger)' == str(super_robot)
    assert u'shining finger 발싸!, SuperGundam 변신!' == super_robot.transform()
