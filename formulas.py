from math import sin, cos


def formula10(x):
    return round(sin(x)-cos(x**3)*sin(x**2-4.2)+4.27, 3)


def formula11(x):
    return round(abs(sin(12*x)*cos(abs(2*x))/3)+4.21, 3)


def formula12(x):
    return round(cos(x**3)/2.1+cos(x**2)/1.1-8.3*sin(3*x+1), 3)


def formula13(x):
    return round(sin(x**2)*cos(x**3)-sin(x)+5.2, 3)


def formula14(x):
    return round(2*sin(x)*sin(2*x-1.5)*cos(2*x+1.5)-6, 3)


def formula15(x):
    return round(abs(cos(x**2)-0.51)*sin(3*x-4)-4.44, 3)


def formula16(x):
    return round(cos(2.1*x)*sin(abs(x))/0.15-5.8, 3)


def formula17(x):
    return round(abs(cos(2*x**3)+2*sin(x))+10.51*cos(abs(3*x)), 3)


def formula18(x):
    return round(abs(sin(x**2/1.5-2))+11.73*cos(abs(x/7.5)), 3)
