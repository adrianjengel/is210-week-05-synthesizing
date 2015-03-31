#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 WK5 sythesiszing - Converting fahrenheit to celsius and kelvin."""

import decimal
ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """A function to convert fahrenheit to celsius.

    The input will be converted from fahrenheit to celcious and returned
    as a decimal.

    Args:
        degrees (int): A value in fahrenheit.
    Returns:
        Returns the temperature in celsius as a decimal.

    Example:

    >>> fahrenheit_to_celsius(212)
    Decimal('100')

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
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


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
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
