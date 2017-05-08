'''OpenGL extension NV.texture_shader

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_texture_shader'
_DEPRECATED = False
GL_OFFSET_TEXTURE_RECTANGLE_NV = constant.Constant( 'GL_OFFSET_TEXTURE_RECTANGLE_NV', 0x864C )
GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV = constant.Constant( 'GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV', 0x864D )
GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV = constant.Constant( 'GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV', 0x864E )
GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = constant.Constant( 'GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV', 0x86D9 )
GL_UNSIGNED_INT_S8_S8_8_8_NV = constant.Constant( 'GL_UNSIGNED_INT_S8_S8_8_8_NV', 0x86DA )
GL_UNSIGNED_INT_8_8_S8_S8_REV_NV = constant.Constant( 'GL_UNSIGNED_INT_8_8_S8_S8_REV_NV', 0x86DB )
GL_DSDT_MAG_INTENSITY_NV = constant.Constant( 'GL_DSDT_MAG_INTENSITY_NV', 0x86DC )
GL_SHADER_CONSISTENT_NV = constant.Constant( 'GL_SHADER_CONSISTENT_NV', 0x86DD )
GL_TEXTURE_SHADER_NV = constant.Constant( 'GL_TEXTURE_SHADER_NV', 0x86DE )
glget.addGLGetConstant( GL_TEXTURE_SHADER_NV, (1,) )
GL_SHADER_OPERATION_NV = constant.Constant( 'GL_SHADER_OPERATION_NV', 0x86DF )
GL_CULL_MODES_NV = constant.Constant( 'GL_CULL_MODES_NV', 0x86E0 )
GL_OFFSET_TEXTURE_MATRIX_NV = constant.Constant( 'GL_OFFSET_TEXTURE_MATRIX_NV', 0x86E1 )
GL_OFFSET_TEXTURE_SCALE_NV = constant.Constant( 'GL_OFFSET_TEXTURE_SCALE_NV', 0x86E2 )
GL_OFFSET_TEXTURE_BIAS_NV = constant.Constant( 'GL_OFFSET_TEXTURE_BIAS_NV', 0x86E3 )
GL_PREVIOUS_TEXTURE_INPUT_NV = constant.Constant( 'GL_PREVIOUS_TEXTURE_INPUT_NV', 0x86E4 )
GL_CONST_EYE_NV = constant.Constant( 'GL_CONST_EYE_NV', 0x86E5 )
GL_PASS_THROUGH_NV = constant.Constant( 'GL_PASS_THROUGH_NV', 0x86E6 )
GL_CULL_FRAGMENT_NV = constant.Constant( 'GL_CULL_FRAGMENT_NV', 0x86E7 )
GL_OFFSET_TEXTURE_2D_NV = constant.Constant( 'GL_OFFSET_TEXTURE_2D_NV', 0x86E8 )
GL_DEPENDENT_AR_TEXTURE_2D_NV = constant.Constant( 'GL_DEPENDENT_AR_TEXTURE_2D_NV', 0x86E9 )
GL_DEPENDENT_GB_TEXTURE_2D_NV = constant.Constant( 'GL_DEPENDENT_GB_TEXTURE_2D_NV', 0x86EA )
GL_DOT_PRODUCT_NV = constant.Constant( 'GL_DOT_PRODUCT_NV', 0x86EC )
GL_DOT_PRODUCT_DEPTH_REPLACE_NV = constant.Constant( 'GL_DOT_PRODUCT_DEPTH_REPLACE_NV', 0x86ED )
GL_DOT_PRODUCT_TEXTURE_2D_NV = constant.Constant( 'GL_DOT_PRODUCT_TEXTURE_2D_NV', 0x86EE )
GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = constant.Constant( 'GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV', 0x86F0 )
GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = constant.Constant( 'GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV', 0x86F1 )
GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = constant.Constant( 'GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV', 0x86F2 )
GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = constant.Constant( 'GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV', 0x86F3 )
GL_HILO_NV = constant.Constant( 'GL_HILO_NV', 0x86F4 )
GL_DSDT_NV = constant.Constant( 'GL_DSDT_NV', 0x86F5 )
GL_DSDT_MAG_NV = constant.Constant( 'GL_DSDT_MAG_NV', 0x86F6 )
GL_DSDT_MAG_VIB_NV = constant.Constant( 'GL_DSDT_MAG_VIB_NV', 0x86F7 )
GL_HILO16_NV = constant.Constant( 'GL_HILO16_NV', 0x86F8 )
GL_SIGNED_HILO_NV = constant.Constant( 'GL_SIGNED_HILO_NV', 0x86F9 )
GL_SIGNED_HILO16_NV = constant.Constant( 'GL_SIGNED_HILO16_NV', 0x86FA )
GL_SIGNED_RGBA_NV = constant.Constant( 'GL_SIGNED_RGBA_NV', 0x86FB )
GL_SIGNED_RGBA8_NV = constant.Constant( 'GL_SIGNED_RGBA8_NV', 0x86FC )
GL_SIGNED_RGB_NV = constant.Constant( 'GL_SIGNED_RGB_NV', 0x86FE )
GL_SIGNED_RGB8_NV = constant.Constant( 'GL_SIGNED_RGB8_NV', 0x86FF )
GL_SIGNED_LUMINANCE_NV = constant.Constant( 'GL_SIGNED_LUMINANCE_NV', 0x8701 )
GL_SIGNED_LUMINANCE8_NV = constant.Constant( 'GL_SIGNED_LUMINANCE8_NV', 0x8702 )
GL_SIGNED_LUMINANCE_ALPHA_NV = constant.Constant( 'GL_SIGNED_LUMINANCE_ALPHA_NV', 0x8703 )
GL_SIGNED_LUMINANCE8_ALPHA8_NV = constant.Constant( 'GL_SIGNED_LUMINANCE8_ALPHA8_NV', 0x8704 )
GL_SIGNED_ALPHA_NV = constant.Constant( 'GL_SIGNED_ALPHA_NV', 0x8705 )
GL_SIGNED_ALPHA8_NV = constant.Constant( 'GL_SIGNED_ALPHA8_NV', 0x8706 )
GL_SIGNED_INTENSITY_NV = constant.Constant( 'GL_SIGNED_INTENSITY_NV', 0x8707 )
GL_SIGNED_INTENSITY8_NV = constant.Constant( 'GL_SIGNED_INTENSITY8_NV', 0x8708 )
GL_DSDT8_NV = constant.Constant( 'GL_DSDT8_NV', 0x8709 )
GL_DSDT8_MAG8_NV = constant.Constant( 'GL_DSDT8_MAG8_NV', 0x870A )
GL_DSDT8_MAG8_INTENSITY8_NV = constant.Constant( 'GL_DSDT8_MAG8_INTENSITY8_NV', 0x870B )
GL_SIGNED_RGB_UNSIGNED_ALPHA_NV = constant.Constant( 'GL_SIGNED_RGB_UNSIGNED_ALPHA_NV', 0x870C )
GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = constant.Constant( 'GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV', 0x870D )
GL_HI_SCALE_NV = constant.Constant( 'GL_HI_SCALE_NV', 0x870E )
glget.addGLGetConstant( GL_HI_SCALE_NV, (1,) )
GL_LO_SCALE_NV = constant.Constant( 'GL_LO_SCALE_NV', 0x870F )
glget.addGLGetConstant( GL_LO_SCALE_NV, (1,) )
GL_DS_SCALE_NV = constant.Constant( 'GL_DS_SCALE_NV', 0x8710 )
glget.addGLGetConstant( GL_DS_SCALE_NV, (1,) )
GL_DT_SCALE_NV = constant.Constant( 'GL_DT_SCALE_NV', 0x8711 )
glget.addGLGetConstant( GL_DT_SCALE_NV, (1,) )
GL_MAGNITUDE_SCALE_NV = constant.Constant( 'GL_MAGNITUDE_SCALE_NV', 0x8712 )
glget.addGLGetConstant( GL_MAGNITUDE_SCALE_NV, (1,) )
GL_VIBRANCE_SCALE_NV = constant.Constant( 'GL_VIBRANCE_SCALE_NV', 0x8713 )
glget.addGLGetConstant( GL_VIBRANCE_SCALE_NV, (1,) )
GL_HI_BIAS_NV = constant.Constant( 'GL_HI_BIAS_NV', 0x8714 )
glget.addGLGetConstant( GL_HI_BIAS_NV, (1,) )
GL_LO_BIAS_NV = constant.Constant( 'GL_LO_BIAS_NV', 0x8715 )
glget.addGLGetConstant( GL_LO_BIAS_NV, (1,) )
GL_DS_BIAS_NV = constant.Constant( 'GL_DS_BIAS_NV', 0x8716 )
glget.addGLGetConstant( GL_DS_BIAS_NV, (1,) )
GL_DT_BIAS_NV = constant.Constant( 'GL_DT_BIAS_NV', 0x8717 )
glget.addGLGetConstant( GL_DT_BIAS_NV, (1,) )
GL_MAGNITUDE_BIAS_NV = constant.Constant( 'GL_MAGNITUDE_BIAS_NV', 0x8718 )
glget.addGLGetConstant( GL_MAGNITUDE_BIAS_NV, (1,) )
GL_VIBRANCE_BIAS_NV = constant.Constant( 'GL_VIBRANCE_BIAS_NV', 0x8719 )
glget.addGLGetConstant( GL_VIBRANCE_BIAS_NV, (1,) )
GL_TEXTURE_BORDER_VALUES_NV = constant.Constant( 'GL_TEXTURE_BORDER_VALUES_NV', 0x871A )
GL_TEXTURE_HI_SIZE_NV = constant.Constant( 'GL_TEXTURE_HI_SIZE_NV', 0x871B )
GL_TEXTURE_LO_SIZE_NV = constant.Constant( 'GL_TEXTURE_LO_SIZE_NV', 0x871C )
GL_TEXTURE_DS_SIZE_NV = constant.Constant( 'GL_TEXTURE_DS_SIZE_NV', 0x871D )
GL_TEXTURE_DT_SIZE_NV = constant.Constant( 'GL_TEXTURE_DT_SIZE_NV', 0x871E )
GL_TEXTURE_MAG_SIZE_NV = constant.Constant( 'GL_TEXTURE_MAG_SIZE_NV', 0x871F )


def glInitTextureShaderNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )