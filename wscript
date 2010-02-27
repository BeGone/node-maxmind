import Options
from os import unlink, symlink, popen
from os.path import exists 

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

  conf.env.append_value("LIBPATH_GEO", ['/opt/local/lib','/usr/local/lib','/usr/lib'])
  conf.env.append_value("LIB_GEO", "GeoIP")
  conf.env.append_value("CPPPATH_GEO", ['/opt/local/include','/usr/local/include','/usr/include/'])


def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'maxmind'
  obj.source = "maxmind.cc"
  obj.uselib = "GEO"


def shutdown():
  # HACK to get binding.node out of build directory.
  # better way to do this?
  if Options.commands['clean']:
    if exists('maxmind.node'): unlink('maxmind.node')
  else:
    if exists('build/default/maxmind.node') and not exists('maxmind.node'):
      symlink('build/default/maxmind.node', 'maxmind.node')
