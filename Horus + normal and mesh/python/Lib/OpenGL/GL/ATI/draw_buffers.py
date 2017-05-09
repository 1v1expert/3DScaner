'''OpenGL extension ATI.draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.draw_buffers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends ARB_fragment_program to allow multiple output 
	colors, and provides a mechanism for directing those outputs to 
	multiple color buffers.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/draw_buffers.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ATI.draw_buffers import *
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy
@lazy( glDrawBuffersATI )
def glDrawBuffersATI( baseOperation, n=None, bufs=None ):
    """glDrawBuffersATI( bufs ) -> bufs 
    
    Wrapper will calculate n from dims of bufs if only 
    one argument is provided...
    """
    if bufs is None:
        bufs = n
        n = None
    bufs = arrays.GLenumArray.asArray( bufs )
    if n is None:
        n = arrays.GLenumArray.arraySize( bufs )
    return baseOperation( n,bufs )