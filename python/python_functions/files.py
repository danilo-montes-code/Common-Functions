"""
files.py

Collection of methods in Python that I commonly use to handle files.
"""


def fn_creator(*terms: str, 
                 prefix: str=None,
                 given_delimiter: str=' ',
                 term_delimiter: str='_',
                 word_delimiter: str='-',
                 file_extension: str = '.txt') -> str:
    """
    Creates a filename with separated terms.
    

    Parameters
    ----------
    terms : tuple(str)
        the terms to be used in the filename, listed in order

    prefix : str, default = None
        the prefix of the filename

    given_delimiter : str, default = ' '
        the delimiter that separates words in the given terms

    term_delimiter : str, default = '_'
        the delimiter to use for separating terms in the filename

    word_delimiter : str, default = '-'
        the delimiter to use for separating 
        words in terms in the filename
    
    file_extension : str, default = '.txt'
        the desired extention of the file

    Returns
    -------
    str
        the created filename
    """

    filename = prefix or ''
    for i, term in enumerate(terms):
        filename += (f'{term_delimiter}'
                     f'{word_delimiter.join(
                         term.split(given_delimiter)
                     )}')
        
        # avoid unnecessary delimiter in the beginning 
        # if there is no prefix
        if i == 0 and not prefix:
            filename = filename[len(term_delimiter):]

    return (filename + file_extension)