from .magics import JSdiagrammerMagics

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(JSdiagrammerMagics)