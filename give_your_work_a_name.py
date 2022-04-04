#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:14:39 2022

@author: Yihang Zhou

Contact: yihangjoe@foxmail.com
         https://github.com/Y-H-Joe/

####============================ description ==============================####
given the list of words
given the dictionary
return top abbreivated names by used frequency
for your work
=================================== input =====================================

=================================== output ====================================

================================= parameters ==================================

=================================== example ===================================

=================================== warning ===================================

####=======================================================================####
"""
import random

dp = r'20k.txt'
words_list = ['metagnome','whole','genome','sequencing','downstream','pipeline']
top = 10

with open(dp,'r') as r:
    dict_ = [x.strip() for x in r.readlines()]

def list_match_list(list1,list2):
    """
    whether characters in list1 match words in list2 pair-wisely
    """
    assert len(list1) == len(list2)
    return all([x1 in x2 for x1,x2 in zip(list1,list2)])


# =============================================================================
# def split_str_to_list(string,bins):
#     """
#     split a string to a list given bins.
#     e.g.
#     string: 'thisisastring'
#     bins: [2,2,2,5,2]
#     output: ['th','is','is','astri','ng']
#     """
#     assert sum(bins) == len(string)
#     indices = [int(sum(bins[:x])) for x in range(len(bins))]
#     return [string[indices[i]:indices[i+1]] for i in range(len(indices)-1)] + [string[indices[-1]:]]
#
# =============================================================================

def split_str_to_list(string,indices):
    """
    split a string to a list given bins.
    e.g.
    string: 'thisisastring'
    indices: [0, 2, 4, 6, 11]
    output: ['th','is','is','astri','ng']
    """
    assert len(string) > indices[-1]
    return [string[indices[i]:indices[i+1]] for i in range(len(indices)-1)] + [string[indices[-1]:]]

def random_indices_of_string(string,num_indices,count):
    """
    return `count` number of indices_list
    """
    assert len(string) >= num_indices
    indices = list(range(1,len(string)))
    picked_indices = []
    for i in range(count):
        tmp = random.sample(indices,k = num_indices-1)
        tmp.sort()
        if tmp not in picked_indices:
            picked_indices.append([0] + tmp)
        else:
            tmp = random.sample(indices,k = num_indices-1)
            tmp.sort()
            if tmp not in picked_indices:
                picked_indices.append([0] + tmp)
            else:
                tmp = random.sample(indices,k = num_indices-1)
                tmp.sort()
                picked_indices.append([0] + tmp)
    return picked_indices

def give_your_work_a_name(dict_,words_list,top,count = 100):
    """
    dict_ : dictionary of candidates
    words_list: key words of your work
    top: how many candidates you want to return
    count: higher count will increase your chance to find one good candidate
    """
    candidates = []
    for candidate in dict_:
        if len(candidate) >= len(words_list):
            indices_list = random_indices_of_string(candidate, len(words_list), count)
            for indices in indices_list:
                splited_candidate = split_str_to_list(candidate, indices)
                #print('--',candidate)
                #print('---',splited_candidate)
                #print('----',indices)
                if list_match_list(splited_candidate, words_list):
                    candidates.append(splited_candidate)
                    break
        if len(candidates) == top:
            return candidates
    return candidates

if __name__ == '__main__':
    candidates = give_your_work_a_name(dict_,words_list,top)
    print(candidates)

