# coding=utf-8 
__version__ = '1.0.19' 

# import zuper_json
import logging


logging.basicConfig()
logger = logging.getLogger('dt-world')
logger.setLevel(logging.DEBUG)

logger.info('duckietown-world %s' % __version__)
# _ = zuper_json.__version__

from .geo import *
from .seqs import *
from .svg_drawing import *
from .world_duckietown import *
