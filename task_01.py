#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 WK5 sythesiszing - Converting Fahrenheit to Celcius and Kelvin."""

import decimal
ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """A function to convert fahrenheit to celcius.

    The input will be converted from fahrenheit to celcious and returned
    as a decimal.

    Args:
        degrees (int): A value in fahrenheit.
    Returns:
        Returns the temperature in celcius as a decimal.

    Example:

    >>> fahrenheit_to_celsius(212)
    Decimal('100')

    >>> fahrenheit_to_kelvin(212)
    Decimal('373.15')

    """
    return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """A function to convert celsius to kelvin.

    The input will be converted from celsius to kelvin and returned
    as a decimal.

    Args:
        degrees (int): A value in celsius.
    Returns:
        Returns the temperature in kelvin as a decimal.

    Example:

    >>> celsius_to_kelvin(100)
    Decimal('373.15')

    """
    return decimal.Decimal(degrees) + decimal.Decimal(ABSOLUTE_DIFFERENCE)


def fahrenheit_to_kelvin(degrees):
    """A function to convert fahrenheit to kelvin.

    The input will be converted from fahrenheit to kelvin and returned
    as a decimal.

    Args:
        degrees (int): A value in fahrenheit.
    Returns:
        Returns the temperature in kelvin as a decimal.

    Example:

    >>> fahrenheit_to_kelvin(212)
    Decimal('373.15')

    """
    return fahrenheit_to_celsius(degrees) + decimal.Decimal(ABSOLUTE_DIFFERENCE)