'''OpenGL extension EXT.pixel_transform

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_pixel_transform'
_DEPRECATED = False
GL_PIXEL_TRANSFORM_2D_EXT = constant.Constant( 'GL_PIXEL_TRANSFORM_2D_EXT', 0x8330 )
GL_PIXEL_MAG_FILTER_EXT = constant.Constant( 'GL_PIXEL_MAG_FILTER_EXT', 0x8331 )
GL_PIXEL_MIN_FILTER_EXT = constant.Constant( 'GL_PIXEL_MIN_FILTER_EXT', 0x8332 )
GL_PIXEL_CUBIC_WEIGHT_EXT = constant.Constant( 'GL_PIXEL_CUBIC_WEIGHT_EXT', 0x8333 )
GL_CUBIC_EXT = constant.Constant( 'GL_CUBIC_EXT', 0x8334 )
GL_AVERAGE_EXT = constant.Constant( 'GL_AVERAGE_EXT', 0x8335 )
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = constant.Constant( 'GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT', 0x8336 )
glget.addGLGetConstant( GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT, (1,) )
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = constant.Constant( 'GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT', 0x8337 )
glget.addGLGetConstant( GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT, (1,) )
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = constant.Constant( 'GL_PIXEL_TRANSFORM_2D_MATRIX_EXT', 0x8338 )
glPixelTransformParameteriEXT = platform.createExtensionFunction( 
'glPixelTransformParameteriEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,),
doc='glPixelTransformParameteriEXT(GLenum(target), GLenum(pname), GLint(param)) -> None',
argNames=('target','pname','param',),
deprecated=_DEPRECATED,
)

glPixelTransformParameterfEXT = platform.createExtensionFunction( 
'glPixelTransformParameterfEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLfloat,),
doc='glPixelTransformParameterfEXT(GLenum(target), GLenum(pname), GLfloat(param)) -> None',
argNames=('target','pname','param',),
deprecated=_DEPRECATED,
)

glPixelTransformParameterivEXT = platform.createExtensionFunction( 
'glPixelTransformParameterivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glPixelTransformParameterivEXT(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glPixelTransformParameterfvEXT = platform.createExtensionFunction( 
'glPixelTransformParameterfvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glPixelTransformParameterfvEXT(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)


def glInitPixelTransformEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )