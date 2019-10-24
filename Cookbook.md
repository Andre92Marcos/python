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