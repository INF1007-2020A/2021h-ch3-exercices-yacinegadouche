#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    return sum([a, b, c])/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degres = sum([angle_degs, angle_mins/60, angle_secs/3600])
    angle_rads = (angle_degres*math.pi)/180
    return angle_rads


def to_degrees(angle_rads: float) -> tuple:
    angle = (angle_rads*180)/math.pi
    partie_decimale_angle = angle - int(angle)
    minutes = partie_decimale_angle*60
    partie_decimal_minutes = minutes - int(minutes)
    secondes = partie_decimal_minutes*60


    return int(angle), int(minutes), secondes


def to_celsius(temperature: float) -> float:
    return (temperature - 32)/1.8


def to_farenheit(temperature: float) -> float:
    return temperature*1.8 + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
