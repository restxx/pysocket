# coding=utf-8
# __author__ = 'doc007'

import os
import sys
from pygccxml import utils
from pygccxml import parser
from pyplusplus import module_builder

generator_path, generator_name = utils.find_xml_generator()
# (u'/usr/local/bin/gccxml', 'gccxml')

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name)


mb = module_builder.module_builder_t(
    files=['chg.h']
    , xml_generator_config=xml_generator_config)

mb.build_code_creator(module_name='libchg_py')

mb.code_creator.user_defined_directories.append(os.path.abspath('.'))

mb.write_module(os.path.join(os.path.abspath('.'), 'chg_py.cc'))
