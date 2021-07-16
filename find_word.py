if __name__=="__main__":
	import argparse
	import os
	import re
	import shutil
	import time



	parser = argparse.ArgumentParser()
		
	parser.add_argument('-w','--word', default='Latitude', 
						help='word to find', 
						type = str)

	parser.add_argument('-p','--path', default='/home/xavier/Documents', 
						help='path to parse', 
						type = str)

	args = parser.parse_args()




	word = args.word
	path = args.path

	print('\n-----------------------------------------')
	print('Searching: {}\nIn: {}'.format(word, path))
	print('-----------------------------------------\n')


	genobj = os.walk(path)#gives you a generator function with all directorys

	for root, dirs, files in genobj:
		for name in files:
			if name.endswith(".R") or name.endswith(".txt") or name.endswith(".py"):
				with open(os.path.join(root,name), errors='ignore') as f:
					count = 0
					for lines in f.readlines():			
						count += 1

						if word in lines:
							print("{} detected in line {} of:\n{} ".format(word, count, os.path.join(root,name)) )
							print("line : ", lines)
							print("\n")
					
