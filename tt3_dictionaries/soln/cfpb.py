'''
Team Tutorial #4: Dictionaries
CMSC 121 / CAPP 30121
Autumn 2021
'''

import json

CFPB_16 = json.load(open("cfpb16_1000.json"))

# Task 1
def find_companies(complaints):
    '''
    Compute a list of companies complained about

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (list or set) of companies
    '''

    # Your code goes here
    # replace [] with a suitable return value
    return list(set([x["Company"] for x in complaints]))


# Task 2
def count_complaints_about(complaints, company_name):
    '''
    Count complaints about a specified company

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary
        company_name (str): The company name to count complaints for

    Returns: count of complaints (int)
    '''

    # Your code goes here
    # replace 0 with a suitable return value
    return len([c for c in complaints if c["Company"] == company])


# Task 3
def count_by_state(complaints):
    '''
    Compute counts by state of all complaints

    Inputs:
         complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) that relates states to complaint number
    '''

    # Your code goes here
    # replace {} with a suitable return value
    d = {}
    for c in complaints:
        d[c["State"]] = d.get(c["State"], 0) + 1
    return d


# Task 4
def state_with_most_complaints(cnt_by_state):
    '''
    Find the state with the most complaints. Can break ties arbitrarily.

    Inputs:
        cnt_by_state (dict) A dictionary relating each state to the
            count of complaints in that state

    Returns: (str) the state with the most complaints
    '''

    # Your code goes here
    # replace "" with a suitable return value
    worst_cnt = 0
    worst_state = ""
    for state, cnt in sorted(by_state.items()):
        if cnt > worst_cnt:
            worst_cnt = cnt
            worst_state = state

    return worst_state


# Task 5
def count_by_company_by_state(complaints):
    '''
    Computes a dict of {company: {state: count, state: count}} for all states
        and companies

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) with count per company per state
    '''

    # Your code goes here
    # replace {} with a suitable return value
    d = {}
    for complaint in complaints:
        c = complaint["Company"]
        st = complaint["State"]
        if c not in d:
            d[c] = {}
        d[c][st] = d[c].get(st, 0) + 1

    return d


# Task 6
def complaints_by_company(complaints):
    '''
    Create a dictionary that maps the name of a company to a list of the
    complaint dictionaries that concern that company.

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) mapping the name of the company to a list of complaints
    '''

    # Your code goes here
    # replace {} with a suitable return value
    d = {}
    for complaint in complaints:
        c = complaint["Company"]
        if c not in d:
            d[c] = []
        d[c].append(complaint)

    return d


# Task 7
def count_by_company_by_state_2(complaints):
    '''
    Computes a dict of {company: {state: count, state: count}} for all states
        and companies

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) with count per company per state

    This implementation involves composing complaints_by_company with 
        count_by_state
    '''

    # Your code goes here
    # replace {} with a suitable return value
    by_company = complaints_by_company(complaints)
    by_company_by_state = {company: count_by_state(company_complaints)
        for company, company_complaints in by_company.items()}
    return by_company_by_state



#################### Code from previous version of assignment


# Writeup code

def count_complaints_by_company_0(complaints):
    # used in writeup, not a task
    rv = {}
    for company in find_companies(complaints):
        rv[company] = 0

    for d in complaints:
        c = d["Company"]
        rv[c] = rv[c] + 1

    return rv


def count_complaints_by_company_1(complaints):
    # used in writeup, not a task
    rv = {}
    for d in complaints:
        c = d["Company"]
        if c in rv:
            rv[c] = rv[c] + 1
        else:
            rv[c] = 1
    return rv


def count_complaints_by_company_2(complaints):
    # used in writeup, not a task
    rv = {}
    for d in complaints:
        c = d["Company"]
        if c not in rv:
            rv[c] = 0
        rv[c] = rv[c] + 1

    return rv


def count_complaints_by_company_3(complaints):
    # used in writeup, not a task
    rv = {}
    for d in complaints:
        c = d["Company"]
        rv[c] = rv.get(c, 0) + 1

    return rv


def print_state_counts(complaints):
    state_cnts = count_by_state(complaints)
    for key in state_cnts.keys():
        print(key, state_cnts[key])
    print()

    for key in state_cnts:
        print(key, state_cnts[key])
    print()

    for key in sorted(state_cnts):
        print(key, state_cnts[key])
    print()

    for key, cnt in sorted(state_cnts.items()):
        print(key, cnt)
    print()


# Unused

def find_company_with_most_complaints(complaints):
    max_complaint_company = None
    max_complaint_count = 0

    counts = count_complaints(complaints)
    for (c, cnt) in counts.items():
        if cnt > max_complaint_count:
            max_complaint_count = cnt
            max_complaint_company = c

    return max_complaint_company


def find_companies_with_at_least_n_complaints(complaints, n):
    rv = []
    counts = count_complaints(complaints)
    for (c, cnt) in counts.items():
        if cnt >= n:
            rv.append((c, cnt))

    return rv


def find_complaints_about(complaints, company):
    return [c for c in complaints if c["Company"] == company]


def complaint_as_list(c):
    rv = []
    for k in sorted(c):
        rv.append(c[k])

    return rv


def count_complaints_0(complaints):
    by_company = {}
    for c in find_companies(complaints):
        by_company[c] = 0
    
    for complaint in complaints:
        c = complaint["Company"]
        by_company[c] = by_company[c] + 1

    return by_company


def find_worst_state_by_company(by_company_by_state):
    d = {}
    for company, by_state in by_company_by_state.items():
        worst_cnt = 0
        worst_state = ""
        for state, cnt in by_state.items():
            if cnt > worst_cnt:
                worst_cnt = cnt
                worst_state = state
        d[company] = worst_state
    return d      


import csv
def write_as_csv(filename):
     data = json.load(open("cfpb16_1000.json"))
     f = open(filename, "w")
     k = ['Complaint ID', 'Company', 'State', 'Product', 'Issue']
     dw = csv.DictWriter(f, fieldnames = k, extrasaction="ignore") 
     dw.writeheader()
     for d in data:
         dw.writerow(d)
     f.close()


import pandas as pd
def top_state_per_company(filename, min_count):
    df = pd.read_csv("cfpb16_1000.csv")
    for name,g in sorted(df.groupby("Company")):
        if (len(g) > min_count) and (len(g["State"].mode()) > 0):
            print(name, g["State"].mode().iloc[0])


def find_bad_companies(filename, threshold_count):
    df = pd.read_csv("cfpb16_1000.csv")
    for name,g in sorted(df.groupby("Company")):
        s = g["State"].value_counts()
        s = s[s >= threshold_count]
        for label, cnt in s.items():
            print(name, label, cnt)




        
    
    




    
