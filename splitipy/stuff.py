# -*- coding: utf-8 -*-

"""splitipy.stuff: stuff module within the splitipy package."""
from __future__ import division
from math import ceil
import os

class Stuff():

	@staticmethod
	def split(sfile, splitsize):

		if os.path.isfile(sfile):
			filesize = os.stat(sfile).st_size
		else:
			print "Hey, the file named "+sfile+" doesn't exists."
			return 1

		splitsize = int(splitsize) * 1024 * 1024 #converting into MBs
		bsize=1024 * 1024
		if bsize > splitsize:
			bsize = splitsize

		times = int(ceil(splitsize/bsize))
		parts = int(ceil(filesize/splitsize))

		print "Splitting file "+ str(sfile) + " into "+ str(parts) + " parts";
		try:
			i=1
			block=True
			fcombine  = open(sfile,"rb")
			while block!="" and i<=parts:
				fw = open(sfile+"."+str(i),"wb")
				j=1
				while block!="" and j<=times:
					block = fcombine.read(bsize)
					fw.write(block)
					j+=1
				fw.close()
				i+=1
		finally:
			fcombine.close()


	@staticmethod
	def combine(jfile, options):
		print( "joining " + jfile)
