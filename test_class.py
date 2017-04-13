#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score, age):
            self.__score = score
            self.age = age
            self.__name = name

    def print_info(self):
        print("name:%s, age:%d, score:%d" % (self.__name, self.age, self.__score))

    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_grade(self):
        if self.__score > 90:
            print("A")
        elif self.__score >= 60:
            print('B')
        else:
            print('C')

def test_class():
    bart = Student('Seven', 90, 12)
    jeff = Student('John', 80, 15)
    bart.print_info()
    jeff.print_info()
    bart.print_grade()
    jeff.print_grade()

    bart.set_score(10)
    bart.print_info()

    bartname=bart.get_name()
    print("bart.name:", bartname)

if __name__ == '__main__':
    test_class()

