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

#   NOTE:  Requires IMDbPY - imdbpy.sourceforge.net

#############################################################################

import imdb
import sys
from kevinbacon_data import kbd

#############################################################################

ia = imdb.IMDb()

#############################################################################
# RE-USABLE GET FUNCTIONS TO RETURN BITS OF DATA
#############################################################################


def get_sys_argv():
    if len(sys.argv) != 4:
        print len(sys.argv)
        print 'Incorrect number of parameters specified - precisely 3 are required - Principle A, Principle B, and Max number of levels to drill down.'
    kbd.principle_a_argument = sys.argv[1]
    kbd.principle_b_argument = sys.argv[2]
    kbd.max_limit = sys.argv[3]


def get_actor(actor_search):
    _actor_search_res = ia.search_person(actor_search)
    _actor_personid = _actor_search_res[0].personID
    person_object = ia.get_person(str(_actor_personid))
    return person_object
 

def get_principles():
    kbd.principle_a_person_object = get_actor(kbd.principle_a_argument)
    kbd.principle_b_person_object = get_actor(kbd.principle_b_argument)

    
def get_filmography(person_object):
        try:
            if len(person_object['actor']) != 0:
                person_filmography = person_object['actor']
        except KeyError:
            if len(person_object['actress']) != 0:
                person_filmography = person_object['actress']
        return person_filmography
    
#############################################################################
# END OF RE-USABLE GET FUNCTIONS TO RETURN BITS OF DATA
#############################################################################




#############################################################################
# SINGLE-USE SCRIPTED BITS AND MAIN LOGIC FLOW
#############################################################################

def intro():
    print ''
    print 'KEVIN BACON SOLVER - Morrolan 2013'
    print ''
    print kbd.principle_a_argument , '>>', kbd.principle_b_argument
    #print 'Going a maximum of', str(max_limit), 'films deep.'
    print ''
    pass


def principle_filmography():
   
    _principle_a_filmography = get_filmography(kbd.principle_a_person_object)
    _principle_b_filmography = get_filmography(kbd.principle_b_person_object)
        
    print ''
    if len(_principle_a_filmography) == 1:
        print kbd.principle_a_argument, 'has starred in', len(_principle_a_filmography), 'film.'
    elif len(_principle_a_filmography) > 1:
        print kbd.principle_a_argument, 'has starred in', len(_principle_a_filmography), 'films.'
    print '---------------------------------------'
    
    for item in _principle_a_filmography:
        ia.update(item)
        cast_num = len(item['cast'])
        tuple_a = (item['long imdb canonical title'], item.movieID, cast_num)
        kbd.principle_a_movie_list.append(tuple_a)
        
        print item['long imdb canonical title'], '\t IMDb MovieID:', item.movieID, '\t Cast:', cast_num
    
    
    print ''
    if len(_principle_b_filmography) == 1:
        print kbd.principle_b_argument, 'has starred in', len(_principle_b_filmography), 'film.'
    elif len(_principle_b_filmography) > 1:
        print kbd.principle_b_argument, 'has starred in', len(_principle_a_filmography), 'films.'
    print '---------------------------------------'
    
    for item in _principle_b_filmography:
        ia.update(item)
        cast_num = len(item['cast'])
        tuple_b = (item['long imdb canonical title'], item.movieID, cast_num)
        kbd.principle_b_movie_list.append(tuple_b)
                
        print item['long imdb canonical title'], '\t IMDb MovieID:', item.movieID, '\t Cast:', cast_num


def check_for_matches(list_to_match):
    if len(list_to_match) > 0:
        kbd.match = kbd.match + 1
    #elif len(list_to_match) <= 0:
    #    print '---------------------------------------'
    #    print '{!s} and {!s} have never appeared in a film together.'.format(kbd.principle_a_argument, kbd.principle_b_argument)
    #    print ''
    
    if kbd.match > 0:
        found_match(list_to_match)
    else:
        return

    
def found_match(list_to_match):
    
    print ''
    print ''
    print 'MATCH FOUND:'
    
    for entry in list_to_match:
        kbd.matching_list.append(entry)
    
    
    # THIS NEXT LINE NEEDS TO BE REMOVED AND CHANGED WHEN WE MOVE TO MULTIPLE LEVELS    
    film = kbd.matching_list[0]
    
    if kbd.current_level ==1:
        kbd.film_level1 = film[0]
    elif kbd.current_level ==2:
        kbd.film_level2 = film[0]
    elif kbd.current_level ==3:
        kbd.film_level3 = film[0]
    elif kbd.current_level ==4:
        kbd.film_level4 = film[0]  
    elif kbd.current_level ==5:
        kbd.film_level5 = film[0]  
    elif kbd.current_level ==6:
        kbd.film_level6 = film[0]
    
        
    if len(list_to_match) > 0:
        
        if kbd.current_level == 1:
            print_degree(kbd.principle_a_person_object, kbd.principle_b_person_object, kbd.film_level1)
        elif kbd.current_level == 2:
            print_degree(kbd.principle_a_person_object, kbd.actor_level1, kbd.film_level1)
            print_degree(kbd.actor_level1, kbd.principle_b_person_object, kbd.film_level2)
        elif kbd.current_level == 3:
            print_degree(kbd.principle_a_person_object, kbd.actor_level1, kbd.film_level1)
            print_degree(kbd.actor_level1, kbd.actor_level2, kbd.film_level2)
            print_degree(kbd.actor_level2, kbd.principle_b_person_object, kbd.film_level3)
        elif kbd.current_level == 4:
            print_degree(kbd.principle_a_person_object, kbd.actor_level1, kbd.film_level1)
            print_degree(kbd.actor_level1, kbd.actor_level2, kbd.film_level2)
            print_degree(kbd.actor_level2, kbd.actor_level3, kbd.film_level3)
            print_degree(kbd.actor_level3, kbd.principle_b_person_object, kbd.film_level4)
        elif kbd.current_level == 5:
            print_degree(kbd.principle_a_person_object, kbd.actor_level1, kbd.film_level1)
            print_degree(kbd.actor_level1, kbd.actor_level2, kbd.film_level2)
            print_degree(kbd.actor_level2, kbd.actor_level3, kbd.film_level3)
            print_degree(kbd.actor_level3, kbd.actor_level4, kbd.film_level4)
            print_degree(kbd.actor_level4, kbd.principle_b_person_object, kbd.film_level5)
        elif kbd.current_level == 6:
            print_degree(kbd.principle_a_person_object, kbd.actor_level1, kbd.film_level1)
            print_degree(kbd.actor_level1, kbd.actor_level2, kbd.film_level2)
            print_degree(kbd.actor_level2, kbd.actor_level3, kbd.film_level3)
            print_degree(kbd.actor_level3, kbd.actor_level4, kbd.film_level4)
            print_degree(kbd.actor_level4, kbd.actor_level5, kbd.film_level5)
            print_degree(kbd.actor_level5, kbd.principle_b_person_object, kbd.film_level6)
    print ''    
 

def print_degree(actor_1, actor_2, film):  
    print actor_1, '&', actor_2, '-', film
    
#############################################################################
#############################################################################
#############################################################################  
    
    
def debug():
    print '********************* DEBUG *********************'
    print ''
    tuple_test = sorted(kbd.principle_a_movie_list, key=lambda noofcast: noofcast[2], reverse=True) 
    for ele in tuple_test:
        print ele
    
    
#############################################################################
#############################################################################
#############################################################################

def search_start():
    
    # LEVEL 1
    kbd.current_level = 1
    set_a = set(kbd.principle_a_movie_list)
    kbd.matching = set_a.intersection(kbd.principle_b_movie_list)
    check_for_matches(kbd.matching)
    
    # LEVEL 2
    kbd.current_level = 2
    set_a = set(kbd.principle_a_movie_list)
    
    
#############################################################################
#############################################################################
#############################################################################    





def main():
    
    get_sys_argv()
    intro()
    get_principles()
    principle_filmography()
    search_start()
    #debug()


#############################################################################

if __name__ == "__main__":
    main()