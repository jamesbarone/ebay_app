'''The get UPC module contains the get_UPC function, which gets input from the user in the form of a
UPC. '''


def get_UPC():
    '''Gets a UPC from the user, which will be used to guide the product search.
    '''
    user_UPC = input( 
            'Please enter the keyword of the product you would like to search for and press \'enter\' when finished! \n'
            'Note that the more specifc the product, the better the search results')
    
    return user_UPC
