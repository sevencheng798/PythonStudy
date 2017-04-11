#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Inheritance and polymorphism

class Animal(object):
    def run(self):
        print("Animal is running...")
    def sleep(self):
        print('Animal is sleeping...')

class Dog(Animal):
    def run(self):
        print("Dog is running...")
    pass

class Cat(Animal):
    def run(self):
        print("Cat is running...")

    def sleep(self):
        print('Cat is sleeping...')

def test_animal():
    dog = Dog()
    dog.run()
    print("dog:", dir(dog))
    print("__class__:", dog.__class__)

def run_twice(animal):
    animal.run()
    animal.sleep()

if __name__ == '__main__':
    test_animal()
    run_twice(Dog())

