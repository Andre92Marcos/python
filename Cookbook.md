**List files from path**

	from os.path import isfile, join 
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	Print like C
		print("Filename %s:\t%s" % (fileFound[0],line))


**Semaphore**

	screenLock = Semaphore(value=1)

	screenLock.acqure()

	[do stuff]

	screenLock.release()


**Iterate Through directory tree**

	for subdir, dirs, files in os.walk(PATH_TO_PN_FOLDER):
		for file in files:
			print("Test %s" %  os.path.join(subdir, file))



**Read JSON file**

	def getConfig(configKey):
		configsFile = open('configs/config.json')
		json1_str = configsFile.read()
			json_data = json.loads(json1_str)
		if not (configKey in json_data):
			return None
		return json_data[configKey]

**Write To File**

	indexHtml = indexHtml.format(chartsHTML)
	with open(self.CHARTS_DIRECTORY+"index.html" ,"w") as file:
		file.write(str(indexHtml))

**Sort A List**

	#modifies the original list
	mylist = ["b", "C", "A"]
	mylist.sort()

	#returns a copy of the original list sorted
	for x in sorted(mylist):
	print x

	ticksSortedByQuoteVolume = sorted(ticks, key=lambda x: Decimal(x.quoteVolume))

**Start a server**

	python -m http.server <server_port>

	allows to then run things like wget to download files from the directory where the server was started