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

#   NOTE:  Requires IMDbPY 5.0 or greater - imdbpy.sourceforge.net

#############################################################################

import sys
import imdb

#############################################################################

ia = imdb.IMDb()

#############################################################################
# SINGLE USE FUNCTIONS - EACH SHOULD ONLY RUN ONCE FOR EACH ATTEMPTED SOLUTION
#############################################################################
 
def __init__(self):
    self.kbd = {
                principle_a_cli_argument: None,
                principle_a_person_object: None,
                principle_b_cli_argument: None,
                principle_b_person_object: None,
        
                max_recursion_limit: 0,
                matching_films: 0,
                current_level: 0,
                current_actor: None,
                current_movie: None,

                principle_a_movie_list: [],
                principle_b_movie_list: [],
                current_actors_sorted_movie_list: [],
                matching_list: [],

                film_level1: None,
                film_level2: None,
                film_level3: None,
                film_level4: None,
                film_level5: None,
                film_level6: None,

                actor_level1: None,
                actor_level2: None,
                actor_level3: None,
                actor_level4: None,
                actor_level5: None,
                actor_level6: None
                }

def get_sys_argv():
    if len(sys.argv) != 4:
        print len(sys.argv)
        print 'Incorrect number of parameters specified - precisely 3 are ' \
              'required - Principle A, Principle B, and Max number of levels' \
              'to search.'
    kbd.principle_a_argument = sys.argv[1]
    kbd.principle_b_argument = sys.argv[2]
    kbd.max_limit = sys.argv[3] 
    
def intro():
    print ''
    print 'KEVIN BACON SOLVER - Morrolan 2013'
    print ''
    print kbd.principle_a_argument , '>>', kbd.principle_b_argument
    print 'Searching a maximum of', str(max_limit), 'films deep.'
    print ''
    
#############################################################################
# RE-USABLE GET FUNCTIONS TO RETURN BITS OF DATA
#############################################################################

def fetch_actor_object(actor_to_search):
    _actor_search_result = ia.search_person(actor_to_search)
    _actor_personid = _actor_search_result[0].personID
    person_object = ia.get_person(str(_actor_personid))
    return person_object

#############################################################################
# SINGLE-USE SCRIPTED BITS AND MAIN LOGIC FLOW
#############################################################################

def main():
    
    get_sys_argv()
    intro()
    #get_principles()
    #get_principle_filmography()
    #search_start()

#############################################################################

if __name__ == "__main__":
    main()