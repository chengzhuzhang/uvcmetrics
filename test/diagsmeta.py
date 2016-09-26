#!/usr/bin/env python
"""" This is a test of metadiags"""
import sys, os, shutil, tempfile, subprocess, filecmp
import argparse, pdb
import diags_test

#to run this app use
#uvcmetrics/test/diagsmeta.py --datadir $HOME//uvcmetrics_test_data/ --baseline $HOME/uvcmetrics/test/baselines/

#get commmand line args
p = argparse.ArgumentParser(description="Basic gm testing code for vcs")
p.add_argument("--datadir", dest="datadir", help="root directory for model and obs data")
p.add_argument("--baseline", dest="baseline", help="directory with baseline files for comparing results")

args = p.parse_args(sys.argv[1:])
datadir = args.datadir
print 'datadir = ', datadir
baselinepath = args.baseline + '/diagsmeta/'
print "baselinepath = ", baselinepath
#outpath = tempfile.mkdtemp() + "/"
#print "outpath=", outpath

test_str = 'metadiags\n'
#run this from command line to get the files required
command = "metadiags.py  --package AMWG --set 5  --model path=%s/cam35_data_smaller/,climos=yes  --obs path=%sobs_data_5.6/,climos=yes --dryrun "%(datadir, datadir)
print command
#+ "--outputdir " + outpath 

#run the command
proc = subprocess.Popen([command], shell=True)
proc_status = proc.wait()
if proc_status!=0: 
    raise "metadiags test failed"

new = open(os.path.join("/tmp","metadiags_commands.sh")).readlines()
old = open(os.path.join(baselinepath,"metadiags_commands.sh")).readlines()

diff = False
for i,l in enumerate(new):
    new_content = l.replace(datadir,"/Users/mcenerney1/uvcmetrics/test/data/")
    l2 = old[i]
    sp = new_content.split("--log")[:-1]
    sp2 = l2.split("--log")[:-1]
    if sp!=sp2:
        diff = True
if diff:
    raise Exception("metadiags.sh generated different files")
