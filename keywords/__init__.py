from os.path import dirname, basename, isfile
import glob

#it's necessary for the dynamic bulk module import - see https://stackoverflow.com/a/1057534
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')] 