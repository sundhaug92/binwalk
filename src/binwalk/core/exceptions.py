class ParserException(Exception):

    '''
    Exception thrown specifically for signature file parsing errors.
    '''


class ModuleException(Exception):

    '''
    Module exception class.
    Nothing special here except the name.
    '''


class IgnoreFileException(Exception):

    '''
    Special exception class used by the load_file plugin method
    to indicate that the file that we are attempting to load
    should be ignored.
    '''
