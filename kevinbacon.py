#!/usr/bin/env python

################################################################################
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
################################################################################

#   NOTE:  Requires IMDbPY 5.0 or greater - imdbpy.sourceforge.net

################################################################################

# Standard Modules
import sys
import argparse

# Third-Party Modules
import imdb
import logging

# Particular imports
from datetime import datetime

################################################################################
# CONSTANTS
################################################################################

################################################################################
# GLOBAL VARIABLES
################################################################################

ia = imdb.IMDb()

kbdata = {
        'principle_a_cli_param': None,
        'principle_a_actor': None,
        'principle_b_cli_param' : None,
        'principle_b_actor' : None,
        
        'max_recursion_limit' : None,
        'matching_films' : None,
        'current_level' : None,
        'current_actor' : None,
        'current_movie' : None,
        'omit_cast' : None,
        'omit_year' : None,

        'principle_a_movie_list' : [],
        'principle_b_movie_list' : [],
        'current_actor_movie_list' : [],
        'matching_list' : [],

        'film_lvl1' : None,
        'film_lvl2' : None,
        'film_lvl3' : None,
        'film_lvl4' : None,
        'film_lvl5' : None,
        'film_lvl6' : None,

        'actor_lvl1' : None,
        'actor_lvl2' : None,
        'actor_lvl3' : None,
        'actor_lvl4' : None,
        'actor_lvl5' : None,
        'actor_lvl6' : None
        }

################################################################################
# SINGLE USE FUNCTIONS - EACH SHOULD ONLY RUN ONCE FOR EACH ATTEMPTED SOLUTION
################################################################################

def get_sys_argv():
    global kbdata
    
    parser = argparse.ArgumentParser()
    parser.add_argument("actor1", help="type the name of the 1st actor or actress here, in single quotes.")
    parser.add_argument("actor2", help="type the name of the 2nd actor or actress here, in single quotes.")
    parser.add_argument("depth", help="enter the maximum number of levels you wish to dive down.", type=int)
    parser.add_argument("-c", "--cast", help="Optional parameter to remove number of cast \(dramatically improves speed\)", action="store_true")
    parser.add_argument("-y", "--year", help="Optional parameter to remove the year from the visibloe movie title.", action="store_true")
    argo = parser.parse_args()
    print argo.actor1, ':', argo.actor2, ':', argo.depth, ':', argo.cast
    
    kbdata['principle_a_cli_param'] = argo.actor1
    kbdata['principle_b_cli_param'] = argo.actor2
    kbdata['max_limit'] = argo.depth
    kbdata['omit_cast'] = argo.cast
    kbdata['omit_year'] = argo.year
    
    
    
def print_intro():
    print ''
    print 'KEVIN BACON SOLVER - Morrolan 2013'
    print ''
    print kbdata['principle_a_cli_param'] , '>>', kbdata['principle_b_cli_param']
    print 'Searching to a maximum depth of', str(kbdata['max_limit']), 'levels.'
    print ''
    
################################################################################
# RE-USABLE GET FUNCTIONS TO RETURN BITS OF DATA
################################################################################

# Here we fetch the objects for our principle actors that we need to link
def get_principles():
    global kbdata
    kbdata['principle_a_actor'] = get_actor_from_string(kbdata['principle_a_cli_param'])
    kbdata['principle_b_actor'] = get_actor_from_string(kbdata['principle_b_cli_param'])
    
# Pass in a STRING and return an OBJECT for the actor
def get_actor_from_string(actor_to_find):
    _result = ia.search_person(actor_to_find)
    _actor_id = _result[0].personID
    actor = ia.get_person(str(_actor_id))
    return actor
    
# Here we pass in the actor OBJECT, to return their filmography
def get_filmography(films_for_actor):
        try:
            if len(films_for_actor['actor']) != 0:
                actor_filmography = films_for_actor['actor']
        except KeyError:
            if len(films_for_actor['actress']) != 0:
                actor_filmography = films_for_actor['actress']
        return actor_filmography

# pass in an actor OBJECT
def print_filmography(actor):
    global kbdata
    _filmography = get_filmography(actor)
    
    if len(_filmography) == 1:
        print actor, 'has starred in', len(_filmography), 'film.'
    elif len(_filmography) > 1:
        print actor, 'has starred in', len(_filmography), 'films.'
    elif len(_filmography) == 0:
        print actor, 'hasn\'t starred in any films!'
    elif len(_filmography) is None:
        print actor, 'wasn\'t found.'
    print '---------------------------------------'
    
    if kbdata['omit_cast'] == True:
        for item in _filmography:  
            tuple_a = (item['long imdb canonical title'], item.movieID, -1)
            kbdata['principle_a_movie_list'].append(tuple_a)
            
            if kbdata['omit_year'] == True:
                print item['long imdb canonical title'][:-7]
            else:
                print item['long imdb canonical title']
    else:   
        for item in _filmography:  
            # NEED TO THINK OF BREAKING THIS DOWN SO THAT YOU CAN TURN OFF CAST!
            ia.update(item)
            cast_num = len(item['cast'])
            tuple_a = (item['long imdb canonical title'], item.movieID, cast_num)
            kbdata['principle_a_movie_list'].append(tuple_a) 
            
            if kbdata['omit_year'] == True:
                if len(item['long imdb canonical title']) < 30:
                    print item['long imdb canonical title'][:-7], '\t\t Cast:', cast_num
                elif len(item['long imdb canonical title']) > 30:
                    print item['long imdb canonical title'][:-7], '\t Cast:', cast_num
            else:
                if len(item['long imdb canonical title']) < 30:
                    print item['long imdb canonical title'], '\t\t Cast:', cast_num
                elif len(item['long imdb canonical title']) > 30:
                    print item['long imdb canonical title'], '\t Cast:', cast_num

    
# WORK IN PROGRESS
def dive_1_level(_x):
    global kbdata
#Given a single actor (X):
#
#    Order actors movie list by number of cast, highest first.
#	
#		for each movie in X's list:
#		
#			for each actor (Y) in this movie:
#			
#				Compare list of Y actors movies with B. (EXT FUNC)





def debug():
    global kbdata
    
    #print kbdata['hide_cast']
    
    #if kbdata['hide_cast'] == True:
    #    print 'YEAH MAN!'
    #else:
    #    print ''
    
    print_filmography(kbdata['principle_a_actor'])
    print ''
    print ''
    print_filmography(kbdata['principle_b_actor'])
    print ''
    print ''

################################################################################
# SINGLE-USE SCRIPTED BITS AND MAIN LOGIC FLOW
################################################################################

def main():
    
    get_sys_argv()
    print_intro()
    get_principles()
    #get_principle_filmography()
    #search_start()
    debug()

################################################################################

if __name__ == "__main__":
    main()