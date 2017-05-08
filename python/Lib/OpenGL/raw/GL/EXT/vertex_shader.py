'''OpenGL extension EXT.vertex_shader

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_vertex_shader'
_DEPRECATED = False
GL_VERTEX_SHADER_EXT = constant.Constant( 'GL_VERTEX_SHADER_EXT', 0x8780 )
glget.addGLGetConstant( GL_VERTEX_SHADER_EXT, (1,) )
GL_VERTEX_SHADER_BINDING_EXT = constant.Constant( 'GL_VERTEX_SHADER_BINDING_EXT', 0x8781 )
glget.addGLGetConstant( GL_VERTEX_SHADER_BINDING_EXT, (1,) )
GL_OP_INDEX_EXT = constant.Constant( 'GL_OP_INDEX_EXT', 0x8782 )
GL_OP_NEGATE_EXT = constant.Constant( 'GL_OP_NEGATE_EXT', 0x8783 )
GL_OP_DOT3_EXT = constant.Constant( 'GL_OP_DOT3_EXT', 0x8784 )
GL_OP_DOT4_EXT = constant.Constant( 'GL_OP_DOT4_EXT', 0x8785 )
GL_OP_MUL_EXT = constant.Constant( 'GL_OP_MUL_EXT', 0x8786 )
GL_OP_ADD_EXT = constant.Constant( 'GL_OP_ADD_EXT', 0x8787 )
GL_OP_MADD_EXT = constant.Constant( 'GL_OP_MADD_EXT', 0x8788 )
GL_OP_FRAC_EXT = constant.Constant( 'GL_OP_FRAC_EXT', 0x8789 )
GL_OP_MAX_EXT = constant.Constant( 'GL_OP_MAX_EXT', 0x878A )
GL_OP_MIN_EXT = constant.Constant( 'GL_OP_MIN_EXT', 0x878B )
GL_OP_SET_GE_EXT = constant.Constant( 'GL_OP_SET_GE_EXT', 0x878C )
GL_OP_SET_LT_EXT = constant.Constant( 'GL_OP_SET_LT_EXT', 0x878D )
GL_OP_CLAMP_EXT = constant.Constant( 'GL_OP_CLAMP_EXT', 0x878E )
GL_OP_FLOOR_EXT = constant.Constant( 'GL_OP_FLOOR_EXT', 0x878F )
GL_OP_ROUND_EXT = constant.Constant( 'GL_OP_ROUND_EXT', 0x8790 )
GL_OP_EXP_BASE_2_EXT = constant.Constant( 'GL_OP_EXP_BASE_2_EXT', 0x8791 )
GL_OP_LOG_BASE_2_EXT = constant.Constant( 'GL_OP_LOG_BASE_2_EXT', 0x8792 )
GL_OP_POWER_EXT = constant.Constant( 'GL_OP_POWER_EXT', 0x8793 )
GL_OP_RECIP_EXT = constant.Constant( 'GL_OP_RECIP_EXT', 0x8794 )
GL_OP_RECIP_SQRT_EXT = constant.Constant( 'GL_OP_RECIP_SQRT_EXT', 0x8795 )
GL_OP_SUB_EXT = constant.Constant( 'GL_OP_SUB_EXT', 0x8796 )
GL_OP_CROSS_PRODUCT_EXT = constant.Constant( 'GL_OP_CROSS_PRODUCT_EXT', 0x8797 )
GL_OP_MULTIPLY_MATRIX_EXT = constant.Constant( 'GL_OP_MULTIPLY_MATRIX_EXT', 0x8798 )
GL_OP_MOV_EXT = constant.Constant( 'GL_OP_MOV_EXT', 0x8799 )
GL_OUTPUT_VERTEX_EXT = constant.Constant( 'GL_OUTPUT_VERTEX_EXT', 0x879A )
GL_OUTPUT_COLOR0_EXT = constant.Constant( 'GL_OUTPUT_COLOR0_EXT', 0x879B )
GL_OUTPUT_COLOR1_EXT = constant.Constant( 'GL_OUTPUT_COLOR1_EXT', 0x879C )
GL_OUTPUT_TEXTURE_COORD0_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD0_EXT', 0x879D )
GL_OUTPUT_TEXTURE_COORD1_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD1_EXT', 0x879E )
GL_OUTPUT_TEXTURE_COORD2_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD2_EXT', 0x879F )
GL_OUTPUT_TEXTURE_COORD3_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD3_EXT', 0x87A0 )
GL_OUTPUT_TEXTURE_COORD4_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD4_EXT', 0x87A1 )
GL_OUTPUT_TEXTURE_COORD5_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD5_EXT', 0x87A2 )
GL_OUTPUT_TEXTURE_COORD6_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD6_EXT', 0x87A3 )
GL_OUTPUT_TEXTURE_COORD7_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD7_EXT', 0x87A4 )
GL_OUTPUT_TEXTURE_COORD8_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD8_EXT', 0x87A5 )
GL_OUTPUT_TEXTURE_COORD9_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD9_EXT', 0x87A6 )
GL_OUTPUT_TEXTURE_COORD10_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD10_EXT', 0x87A7 )
GL_OUTPUT_TEXTURE_COORD11_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD11_EXT', 0x87A8 )
GL_OUTPUT_TEXTURE_COORD12_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD12_EXT', 0x87A9 )
GL_OUTPUT_TEXTURE_COORD13_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD13_EXT', 0x87AA )
GL_OUTPUT_TEXTURE_COORD14_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD14_EXT', 0x87AB )
GL_OUTPUT_TEXTURE_COORD15_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD15_EXT', 0x87AC )
GL_OUTPUT_TEXTURE_COORD16_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD16_EXT', 0x87AD )
GL_OUTPUT_TEXTURE_COORD17_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD17_EXT', 0x87AE )
GL_OUTPUT_TEXTURE_COORD18_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD18_EXT', 0x87AF )
GL_OUTPUT_TEXTURE_COORD19_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD19_EXT', 0x87B0 )
GL_OUTPUT_TEXTURE_COORD20_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD20_EXT', 0x87B1 )
GL_OUTPUT_TEXTURE_COORD21_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD21_EXT', 0x87B2 )
GL_OUTPUT_TEXTURE_COORD22_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD22_EXT', 0x87B3 )
GL_OUTPUT_TEXTURE_COORD23_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD23_EXT', 0x87B4 )
GL_OUTPUT_TEXTURE_COORD24_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD24_EXT', 0x87B5 )
GL_OUTPUT_TEXTURE_COORD25_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD25_EXT', 0x87B6 )
GL_OUTPUT_TEXTURE_COORD26_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD26_EXT', 0x87B7 )
GL_OUTPUT_TEXTURE_COORD27_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD27_EXT', 0x87B8 )
GL_OUTPUT_TEXTURE_COORD28_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD28_EXT', 0x87B9 )
GL_OUTPUT_TEXTURE_COORD29_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD29_EXT', 0x87BA )
GL_OUTPUT_TEXTURE_COORD30_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD30_EXT', 0x87BB )
GL_OUTPUT_TEXTURE_COORD31_EXT = constant.Constant( 'GL_OUTPUT_TEXTURE_COORD31_EXT', 0x87BC )
GL_OUTPUT_FOG_EXT = constant.Constant( 'GL_OUTPUT_FOG_EXT', 0x87BD )
GL_SCALAR_EXT = constant.Constant( 'GL_SCALAR_EXT', 0x87BE )
GL_VECTOR_EXT = constant.Constant( 'GL_VECTOR_EXT', 0x87BF )
GL_MATRIX_EXT = constant.Constant( 'GL_MATRIX_EXT', 0x87C0 )
GL_VARIANT_EXT = constant.Constant( 'GL_VARIANT_EXT', 0x87C1 )
GL_INVARIANT_EXT = constant.Constant( 'GL_INVARIANT_EXT', 0x87C2 )
GL_LOCAL_CONSTANT_EXT = constant.Constant( 'GL_LOCAL_CONSTANT_EXT', 0x87C3 )
GL_LOCAL_EXT = constant.Constant( 'GL_LOCAL_EXT', 0x87C4 )
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = constant.Constant( 'GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT', 0x87C5 )
glget.addGLGetConstant( GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT, (1,) )
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = constant.Constant( 'GL_MAX_VERTEX_SHADER_VARIANTS_EXT', 0x87C6 )
glget.addGLGetConstant( GL_MAX_VERTEX_SHADER_VARIANTS_EXT, (1,) )
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = constant.Constant( 'GL_MAX_VERTEX_SHADER_INVARIANTS_EXT', 0x87C7 )
glget.addGLGetConstant( GL_MAX_VERTEX_SHADER_INVARIANTS_EXT, (1,) )
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = constant.Constant( 'GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT', 0x87C8 )
glget.addGLGetConstant( GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT, (1,) )
GL_MAX_VERTEX_SHADER_LOCALS_EXT = constant.Constant( 'GL_MAX_VERTEX_SHADER_LOCALS_EXT', 0x87C9 )
glget.addGLGetConstant( GL_MAX_VERTEX_SHADER_LOCALS_EXT, (1,) )
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = constant.Constant( 'GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT', 0x87CA )
glget.addGLGetConstant( GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT, (1,) )
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = constant.Constant( 'GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT', 0x87CB )
glget.addGLGetConstant( GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT, (1,) )
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = constant.Constant( 'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT', 0x87CC )
glget.addGLGetConstant( GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT, (1,) )
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = constant.Constant( 'GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT', 0x87CD )
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = constant.Constant( 'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT', 0x87CE )
glget.addGLGetConstant( GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT, (1,) )
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = constant.Constant( 'GL_VERTEX_SHADER_INSTRUCTIONS_EXT', 0x87CF )
GL_VERTEX_SHADER_VARIANTS_EXT = constant.Constant( 'GL_VERTEX_SHADER_VARIANTS_EXT', 0x87D0 )
GL_VERTEX_SHADER_INVARIANTS_EXT = constant.Constant( 'GL_VERTEX_SHADER_INVARIANTS_EXT', 0x87D1 )
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = constant.Constant( 'GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT', 0x87D2 )
GL_VERTEX_SHADER_LOCALS_EXT = constant.Constant( 'GL_VERTEX_SHADER_LOCALS_EXT', 0x87D3 )
GL_VERTEX_SHADER_OPTIMIZED_EXT = constant.Constant( 'GL_VERTEX_SHADER_OPTIMIZED_EXT', 0x87D4 )
glget.addGLGetConstant( GL_VERTEX_SHADER_OPTIMIZED_EXT, (1,) )
GL_X_EXT = constant.Constant( 'GL_X_EXT', 0x87D5 )
GL_Y_EXT = constant.Constant( 'GL_Y_EXT', 0x87D6 )
GL_Z_EXT = constant.Constant( 'GL_Z_EXT', 0x87D7 )
GL_W_EXT = constant.Constant( 'GL_W_EXT', 0x87D8 )
GL_NEGATIVE_X_EXT = constant.Constant( 'GL_NEGATIVE_X_EXT', 0x87D9 )
GL_NEGATIVE_Y_EXT = constant.Constant( 'GL_NEGATIVE_Y_EXT', 0x87DA )
GL_NEGATIVE_Z_EXT = constant.Constant( 'GL_NEGATIVE_Z_EXT', 0x87DB )
GL_NEGATIVE_W_EXT = constant.Constant( 'GL_NEGATIVE_W_EXT', 0x87DC )
GL_ZERO_EXT = constant.Constant( 'GL_ZERO_EXT', 0x87DD )
GL_ONE_EXT = constant.Constant( 'GL_ONE_EXT', 0x87DE )
GL_NEGATIVE_ONE_EXT = constant.Constant( 'GL_NEGATIVE_ONE_EXT', 0x87DF )
GL_NORMALIZED_RANGE_EXT = constant.Constant( 'GL_NORMALIZED_RANGE_EXT', 0x87E0 )
GL_FULL_RANGE_EXT = constant.Constant( 'GL_FULL_RANGE_EXT', 0x87E1 )
GL_CURRENT_VERTEX_EXT = constant.Constant( 'GL_CURRENT_VERTEX_EXT', 0x87E2 )
GL_MVP_MATRIX_EXT = constant.Constant( 'GL_MVP_MATRIX_EXT', 0x87E3 )
GL_VARIANT_VALUE_EXT = constant.Constant( 'GL_VARIANT_VALUE_EXT', 0x87E4 )
GL_VARIANT_DATATYPE_EXT = constant.Constant( 'GL_VARIANT_DATATYPE_EXT', 0x87E5 )
GL_VARIANT_ARRAY_STRIDE_EXT = constant.Constant( 'GL_VARIANT_ARRAY_STRIDE_EXT', 0x87E6 )
GL_VARIANT_ARRAY_TYPE_EXT = constant.Constant( 'GL_VARIANT_ARRAY_TYPE_EXT', 0x87E7 )
GL_VARIANT_ARRAY_EXT = constant.Constant( 'GL_VARIANT_ARRAY_EXT', 0x87E8 )
GL_VARIANT_ARRAY_POINTER_EXT = constant.Constant( 'GL_VARIANT_ARRAY_POINTER_EXT', 0x87E9 )
GL_INVARIANT_VALUE_EXT = constant.Constant( 'GL_INVARIANT_VALUE_EXT', 0x87EA )
GL_INVARIANT_DATATYPE_EXT = constant.Constant( 'GL_INVARIANT_DATATYPE_EXT', 0x87EB )
GL_LOCAL_CONSTANT_VALUE_EXT = constant.Constant( 'GL_LOCAL_CONSTANT_VALUE_EXT', 0x87EC )
GL_LOCAL_CONSTANT_DATATYPE_EXT = constant.Constant( 'GL_LOCAL_CONSTANT_DATATYPE_EXT', 0x87ED )
glBeginVertexShaderEXT = platform.createExtensionFunction( 
'glBeginVertexShaderEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glBeginVertexShaderEXT() -> None',
argNames=(),
deprecated=_DEPRECATED,
)

glEndVertexShaderEXT = platform.createExtensionFunction( 
'glEndVertexShaderEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glEndVertexShaderEXT() -> None',
argNames=(),
deprecated=_DEPRECATED,
)

glBindVertexShaderEXT = platform.createExtensionFunction( 
'glBindVertexShaderEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glBindVertexShaderEXT(GLuint(id)) -> None',
argNames=('id',),
deprecated=_DEPRECATED,
)

glGenVertexShadersEXT = platform.createExtensionFunction( 
'glGenVertexShadersEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLuint,),
doc='glGenVertexShadersEXT(GLuint(range)) -> constants.GLuint',
argNames=('range',),
deprecated=_DEPRECATED,
)

glDeleteVertexShaderEXT = platform.createExtensionFunction( 
'glDeleteVertexShaderEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glDeleteVertexShaderEXT(GLuint(id)) -> None',
argNames=('id',),
deprecated=_DEPRECATED,
)

glShaderOp1EXT = platform.createExtensionFunction( 
'glShaderOp1EXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,),
doc='glShaderOp1EXT(GLenum(op), GLuint(res), GLuint(arg1)) -> None',
argNames=('op','res','arg1',),
deprecated=_DEPRECATED,
)

glShaderOp2EXT = platform.createExtensionFunction( 
'glShaderOp2EXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glShaderOp2EXT(GLenum(op), GLuint(res), GLuint(arg1), GLuint(arg2)) -> None',
argNames=('op','res','arg1','arg2',),
deprecated=_DEPRECATED,
)

glShaderOp3EXT = platform.createExtensionFunction( 
'glShaderOp3EXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glShaderOp3EXT(GLenum(op), GLuint(res), GLuint(arg1), GLuint(arg2), GLuint(arg3)) -> None',
argNames=('op','res','arg1','arg2','arg3',),
deprecated=_DEPRECATED,
)

glSwizzleEXT = platform.createExtensionFunction( 
'glSwizzleEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLenum,constants.GLenum,constants.GLenum,constants.GLenum,),
doc='glSwizzleEXT(GLuint(res), GLuint(in), GLenum(outX), GLenum(outY), GLenum(outZ), GLenum(outW)) -> None',
argNames=('res','in','outX','outY','outZ','outW',),
deprecated=_DEPRECATED,
)

glWriteMaskEXT = platform.createExtensionFunction( 
'glWriteMaskEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLenum,constants.GLenum,constants.GLenum,constants.GLenum,),
doc='glWriteMaskEXT(GLuint(res), GLuint(in), GLenum(outX), GLenum(outY), GLenum(outZ), GLenum(outW)) -> None',
argNames=('res','in','outX','outY','outZ','outW',),
deprecated=_DEPRECATED,
)

glInsertComponentEXT = platform.createExtensionFunction( 
'glInsertComponentEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glInsertComponentEXT(GLuint(res), GLuint(src), GLuint(num)) -> None',
argNames=('res','src','num',),
deprecated=_DEPRECATED,
)

glExtractComponentEXT = platform.createExtensionFunction( 
'glExtractComponentEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glExtractComponentEXT(GLuint(res), GLuint(src), GLuint(num)) -> None',
argNames=('res','src','num',),
deprecated=_DEPRECATED,
)

glGenSymbolsEXT = platform.createExtensionFunction( 
'glGenSymbolsEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLuint,),
doc='glGenSymbolsEXT(GLenum(datatype), GLenum(storagetype), GLenum(range), GLuint(components)) -> constants.GLuint',
argNames=('datatype','storagetype','range','components',),
deprecated=_DEPRECATED,
)

glSetInvariantEXT = platform.createExtensionFunction( 
'glSetInvariantEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,ctypes.c_void_p,),
doc='glSetInvariantEXT(GLuint(id), GLenum(type), c_void_p(addr)) -> None',
argNames=('id','type','addr',),
deprecated=_DEPRECATED,
)

glSetLocalConstantEXT = platform.createExtensionFunction( 
'glSetLocalConstantEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,ctypes.c_void_p,),
doc='glSetLocalConstantEXT(GLuint(id), GLenum(type), c_void_p(addr)) -> None',
argNames=('id','type','addr',),
deprecated=_DEPRECATED,
)

glVariantbvEXT = platform.createExtensionFunction( 
'glVariantbvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLbyteArray,),
doc='glVariantbvEXT(GLuint(id), GLbyteArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantsvEXT = platform.createExtensionFunction( 
'glVariantsvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLshortArray,),
doc='glVariantsvEXT(GLuint(id), GLshortArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantivEXT = platform.createExtensionFunction( 
'glVariantivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,),
doc='glVariantivEXT(GLuint(id), GLintArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantfvEXT = platform.createExtensionFunction( 
'glVariantfvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLfloatArray,),
doc='glVariantfvEXT(GLuint(id), GLfloatArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantdvEXT = platform.createExtensionFunction( 
'glVariantdvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLdoubleArray,),
doc='glVariantdvEXT(GLuint(id), GLdoubleArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantubvEXT = platform.createExtensionFunction( 
'glVariantubvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLubyteArray,),
doc='glVariantubvEXT(GLuint(id), GLubyteArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantusvEXT = platform.createExtensionFunction( 
'glVariantusvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLushortArray,),
doc='glVariantusvEXT(GLuint(id), GLushortArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantuivEXT = platform.createExtensionFunction( 
'glVariantuivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLuintArray,),
doc='glVariantuivEXT(GLuint(id), GLuintArray(addr)) -> None',
argNames=('id','addr',),
deprecated=_DEPRECATED,
)

glVariantPointerEXT = platform.createExtensionFunction( 
'glVariantPointerEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLuint,ctypes.c_void_p,),
doc='glVariantPointerEXT(GLuint(id), GLenum(type), GLuint(stride), c_void_p(addr)) -> None',
argNames=('id','type','stride','addr',),
deprecated=_DEPRECATED,
)

glEnableVariantClientStateEXT = platform.createExtensionFunction( 
'glEnableVariantClientStateEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glEnableVariantClientStateEXT(GLuint(id)) -> None',
argNames=('id',),
deprecated=_DEPRECATED,
)

glDisableVariantClientStateEXT = platform.createExtensionFunction( 
'glDisableVariantClientStateEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glDisableVariantClientStateEXT(GLuint(id)) -> None',
argNames=('id',),
deprecated=_DEPRECATED,
)

glBindLightParameterEXT = platform.createExtensionFunction( 
'glBindLightParameterEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glBindLightParameterEXT(GLenum(light), GLenum(value)) -> constants.GLuint',
argNames=('light','value',),
deprecated=_DEPRECATED,
)

glBindMaterialParameterEXT = platform.createExtensionFunction( 
'glBindMaterialParameterEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glBindMaterialParameterEXT(GLenum(face), GLenum(value)) -> constants.GLuint',
argNames=('face','value',),
deprecated=_DEPRECATED,
)

glBindTexGenParameterEXT = platform.createExtensionFunction( 
'glBindTexGenParameterEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,),
doc='glBindTexGenParameterEXT(GLenum(unit), GLenum(coord), GLenum(value)) -> constants.GLuint',
argNames=('unit','coord','value',),
deprecated=_DEPRECATED,
)

glBindTextureUnitParameterEXT = platform.createExtensionFunction( 
'glBindTextureUnitParameterEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glBindTextureUnitParameterEXT(GLenum(unit), GLenum(value)) -> constants.GLuint',
argNames=('unit','value',),
deprecated=_DEPRECATED,
)

glBindParameterEXT = platform.createExtensionFunction( 
'glBindParameterEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLuint, 
argTypes=(constants.GLenum,),
doc='glBindParameterEXT(GLenum(value)) -> constants.GLuint',
argNames=('value',),
deprecated=_DEPRECATED,
)

glIsVariantEnabledEXT = platform.createExtensionFunction( 
'glIsVariantEnabledEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glIsVariantEnabledEXT(GLuint(id), GLenum(cap)) -> constants.GLboolean',
argNames=('id','cap',),
deprecated=_DEPRECATED,
)

glGetVariantBooleanvEXT = platform.createExtensionFunction( 
'glGetVariantBooleanvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLbooleanArray,),
doc='glGetVariantBooleanvEXT(GLuint(id), GLenum(value), GLbooleanArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetVariantIntegervEXT = platform.createExtensionFunction( 
'glGetVariantIntegervEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetVariantIntegervEXT(GLuint(id), GLenum(value), GLintArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetVariantFloatvEXT = platform.createExtensionFunction( 
'glGetVariantFloatvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glGetVariantFloatvEXT(GLuint(id), GLenum(value), GLfloatArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetVariantPointervEXT = platform.createExtensionFunction( 
'glGetVariantPointervEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glGetVariantPointervEXT(GLuint(id), GLenum(value), POINTER(ctypes.c_void_p)(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetInvariantBooleanvEXT = platform.createExtensionFunction( 
'glGetInvariantBooleanvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLbooleanArray,),
doc='glGetInvariantBooleanvEXT(GLuint(id), GLenum(value), GLbooleanArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetInvariantIntegervEXT = platform.createExtensionFunction( 
'glGetInvariantIntegervEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetInvariantIntegervEXT(GLuint(id), GLenum(value), GLintArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetInvariantFloatvEXT = platform.createExtensionFunction( 
'glGetInvariantFloatvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glGetInvariantFloatvEXT(GLuint(id), GLenum(value), GLfloatArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetLocalConstantBooleanvEXT = platform.createExtensionFunction( 
'glGetLocalConstantBooleanvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLbooleanArray,),
doc='glGetLocalConstantBooleanvEXT(GLuint(id), GLenum(value), GLbooleanArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetLocalConstantIntegervEXT = platform.createExtensionFunction( 
'glGetLocalConstantIntegervEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetLocalConstantIntegervEXT(GLuint(id), GLenum(value), GLintArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)

glGetLocalConstantFloatvEXT = platform.createExtensionFunction( 
'glGetLocalConstantFloatvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glGetLocalConstantFloatvEXT(GLuint(id), GLenum(value), GLfloatArray(data)) -> None',
argNames=('id','value','data',),
deprecated=_DEPRECATED,
)


def glInitVertexShaderEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
