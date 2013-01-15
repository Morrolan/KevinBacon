#!/usr/bin/env python

#############################################################################
#    KevinBacon.py - an attempt to solve the kevin bacon game in Python
#    Copyright (C) 2012  Ian Havelock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

#   NOTE:  Requires IMDbPY - imdbpy.sourceforge.net

#############################################################################

import sys

#############################################################################


class KevinBaconData(object):
   def __init__(self):
        self.x = None
        self.principle_a_argument = None
        self.principle_a_person_object = None
        self.principle_b_argument = None
        self.principle_b_person_object = None
        
        self.max_limit = 0
        self.match = 0
        self.current_level = 0

        self.principle_a_movie_list = []
        self.principle_b_movie_list = []
        self.matching_list = []

        self.film_level1 = None
        self.film_level2 = None
        self.film_level3 = None
        self.film_level4 = None
        self.film_level5 = None
        self.film_level6 = None

        self.actor_level1 = None
        self.actor_level2 = None
        self.actor_level3 = None
        self.actor_level4 = None
        self.actor_level5 = None
        self.actor_level6 = None

kbd = KevinBaconData()