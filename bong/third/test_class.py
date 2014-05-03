# -*- coding: utf-8 -*-

class Robot(object):
    """로봇을 클래스입니다.
    """

    def __init__(self, name):
        self.name = name

    
    def transform(self):
        """로봇을 변신시키는 함수입니다
        """
        return "{0} transform!!".format(self.name)
    

class SuperRobot(Robot):
    def __init__(self, name, weap):
        super(SuperRobot, self).__init__(name)
        self.weap = weap


    def __repr__(self):
        return "SuperRobot(%s, %s)" % (self.name, self.weap)
    

    def __str__(self):
        return "SuperStr(%s, %s)" % (self.name, self.weap)
    

    def transform(self):
        return u'%s 발싸!, %s 변신!' % (self.weap, self.name)


def test_robot():
    a = "dagan"
    robot = Robot(a)
    assert a == robot.name
    assert "dagan transform!!" == robot.transform()
    

def test_super_robot():
    weap = "gun"
    n = "superdagan"
    super_robot = SuperRobot(n, weap)
    assert n == super_robot.name
    assert weap == super_robot.weap
    assert "SuperRobot(superdagan, gun)" == repr(super_robot)
    assert "SuperStr(superdagan, gun)" == str(super_robot)
    assert u'gun 발싸!, superdagan 변신!' == super_robot.transform()
