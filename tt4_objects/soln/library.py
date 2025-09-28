'''
Team Tutorial #4: Library class
'''


class Library:

    def __init__(self, island, name, reference, book, microform):
        '''
        Constructor for the Library class

        Input:
            island: (string) Hawaiian island name
            name: (string) name of library branch
            reference: (int) number of references
            book: (int) number of books
            microform: (int) number of microform
        '''
        self.island = island
        self.name = name
        self.reference = reference
        self.book = book
        self.microform = microform

    def total_circulation(self):
        '''
        Calculate the total number of items in circulation

        Returns: total (int)

        '''
        total = self.reference + self.book + self.microform
        return total

    def has_microform_catalogue(self):
        '''
        Does a library has a microform catalogue?

        Returns: True if library has microform, False otherwise (boolean)

        '''
        return not self.microform == 0

    def __repr__(self):
        '''
        String representation of a library (for debugging)

        Returns: string representation (string)

        '''
        return "Library({}, {}, {}, {}, {})".format(self.island,
                                                    self.name, 
                                                    self.reference,
                                                    self.book, 
                                                    self.microform)

def branch_with_biggest_circulation(libraries):
    '''
    Find the library with the largest total number of
    items in circulation

    Input:
        libraries: (list of Library) libraries

    Returns: name of library (string)
    '''
    name = None
    biggest = -1

    for lib in libraries:
        total = lib.total_circulation()
        if total > biggest:
            biggest = total
            name = lib.name

    return name

def percentage_with_microform(libraries):
    '''
    Find the percentage of libraries that have
    microform catalogues

    Input:
        libraries: (list of Library) libraries

    Returns: percentage (float)
    '''
    has_microform = 0

    for lib in libraries:
        if lib.has_microform_catalogue():
            has_microform += 1

    return has_microform/len(libraries)*100

