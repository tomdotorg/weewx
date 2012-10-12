#!/usr/bin/env python
#
#    Copyright (c) 2009, 2010, 2011 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
#    $Revision$
#    $Author$
#    $Date$
#
"""Entry point to the weewx weather system."""
import sys
from optparse import OptionParser

# First import any user extensions:
import user.extensions       #@UnusedImport
# Now the engine
import weewx.wxengine

usagestr = """
  %prog config_path [--help] [--daemon] [--pidfile=PIDFILE] [--version] [--exit]

  Entry point to the weewx weather program. Can be run from the command
  line or, by specifying the '--daemon' option, as a daemon.

Arguments:
    config_path: Path to the weewx configuration file to be used.
"""

#===============================================================================
#                       function parseArgs()
#===============================================================================

def parseArgs():
    """Parse any command line options."""

    parser = OptionParser(usage=usagestr)
    parser.add_option("-d", "--daemon",  action="store_true", dest="daemon",  help="Run as a daemon")
    parser.add_option("-p", "--pidfile", type="string",       dest="pidfile", help="Path to process ID file", default="/var/run/weewx.pid")     
    parser.add_option("-v", "--version", action="store_true", dest="version", help="Give version number then exit")
    parser.add_option("-x", "--exit",    action="store_true", dest="exit"   , help="Exit on I/O error (rather than restart)")
    (options, args) = parser.parse_args()
    
    if options.version:
        print weewx.__version__
        sys.exit()
        
    if len(args) < 1:
        sys.stderr.write("Missing argument(s).\n")
        sys.stderr.write(parser.parse_args(["--help"]))
        sys.exit(weewx.CMD_ERROR)
    
    return (options, args)

if __name__ == "__main__":
    
    # Get the command line options and arguments:
    (options, args) = parseArgs()
    
    # Enter the main loop. This call will use the default
    # engine, StdEngine, but this can be overridden with
    # keyword EngineClass. E.g.,
    #
    # weewx.wxengine.main(options, args, EngineClass = MyEngine)
    #
    weewx.wxengine.main(options, args)
