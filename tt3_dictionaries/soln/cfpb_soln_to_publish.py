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
    Compute a list of companies complained about.

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (list or set) of companies
    '''

    companies = set()
    for complaint in complaints:
        companies.add(complaint["Company"])
    return companies


# Task 2
def count_complaints_about(complaints, company_name):
    '''
    Count complaints about a specified company.

    Inputs:
        complaints (list) A list of complaints, where each complaint is a
            dictionary
        company_name (str): The company name to count complaints for

    Returns: count of complaints (int)
    '''

    count = 0
    for complaint in complaints:
        if complaint["Company"] == company_name:
            count += 1
    return count


# Task 3
def count_by_state(complaints):
    '''
    Compute counts by state of all complaints.

    Inputs:
         complaints (list) A list of complaints, where each complaint is a
            dictionary

    Returns: (dict) that maps states to number of complaints
    '''

    by_state = {}
    for complaint in complaints:
        by_state[complaint["State"]] = by_state.get(complaint["State"], 0) + 1
    return by_state


# Task 4
def state_with_most_complaints(cnt_by_state):
    '''
    Find the state with the most complaints. Can break ties arbitrarily.

    Inputs:
        cnt_by_state (dict) A dictionary relating each state to the
            count of complaints in that state

    Returns: (str) the state with the most complaints
    '''

    worst_cnt = None
    worst_state = ""
    for state, cnt in cnt_by_state.items():
        if worst_cnt is None or cnt > worst_cnt:
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

    by_company_by_state = {}
    for complaint in complaints:
        company = complaint["Company"]
        state = complaint["State"]
        if company not in by_company_by_state:
            by_company_by_state[company] = {}
        if state not in by_company_by_state[company]:
            by_company_by_state[company][state] = 0
        by_company_by_state[company][state] += 1

    return by_company_by_state


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

    by_company = {}
    for complaint in complaints:
        company = complaint["Company"]
        if company not in by_company:
            by_company[company] = []
        by_company[company].append(complaint)

    return by_company


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

    by_company = complaints_by_company(complaints)
    by_company_by_state = {company: count_by_state(company_complaints)
        for company, company_complaints in by_company.items()}
    return by_company_by_state