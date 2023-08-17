#!/usr/bin/python3
"""Defines object attribute called lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
