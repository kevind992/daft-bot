#!/usr/bin/python

from dataclasses import dataclass


@dataclass
class House:
    date: str
    address: str
    price: str
    url: str
