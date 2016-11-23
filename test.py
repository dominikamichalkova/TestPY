import numpy;

array1 = numpy.array([1, 2, 3]);
print(array1[1] ** 3);

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
      "and your favorite color is %s." % (name, quest, color)

bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False

print bool_one;
print bool_two;
print bool_five;


