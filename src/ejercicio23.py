#!/usr/bin/python
a=float(raw_input('valor de a: '))
b=float(raw_input('valor de b: '))
if (a != 0):
  x= -b/a
  print 'la solucion es: ', x
if ((a==0)and(b!=0)):
  print 'no tiene solucion'
if ((a==0)and(b==0)):
 print 'ecuacion infinitas soluciones: '
