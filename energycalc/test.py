'''
>>> from energycalc import *
>>> import coverage
>>> cov=coverage.Coverage()
>>> cov.start()
>>> line(5)
'*****'
>>> line(5,"&")
'&&&&&'
>>> convert(400)
'400.0 wh'
>>> convert(145400)
'145.4 Kwh'
>>> check_constraint(2)
2
>>> check_constraint(400)
24
>>> check_constraint(400,mode=2)
365
>>> handle_input("34")
34
>>> handle_input('asdasd')
0
>>> seperator("2,3,4,5,6")
['2', 3, 4, 5, 6]
>>> seperator("2;3;4;5;6",char=";")
['2', 3, 4, 5, 6]
>>> find_ref()
'NOFILE'
>>> cov.stop()
>>> cov.save()

'''