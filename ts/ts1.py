# coding=utf-8
# __author__ = 'doc007'


import os
import sys
from pyplusplus import module_builder

mb = module_builder.module_builder_t(
    files=['chg.h'],
    xml_generator_path='D:\\GCC_XML\\bin\\gccxml.exe'
)

mb.build_code_creator(module_name='libchg_py')  # 要生成的python模块的名称

mb.code_creator.user_defined_directories.append(os.path.abspath('.'))

mb.write_module(os.path.join(os.path.abspath('.'), 'chg_py.cc'))  # 要生成的boost.python封装好的代码文件的名称
