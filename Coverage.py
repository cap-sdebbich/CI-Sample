import json
import sys

file = open('files.json')
filesJson = json.load(file)
sourcePath = sys.argv[1]
threshold = sys.argv[2]
coverageFile = open('coverage.json')
coverageJson = json.load(coverageFile)

filesArray=[]
for fileJson in filesJson:
    status = fileJson["status"]
    if status == "modified" or status == "added":
        filename = fileJson["filename"]
        if sourcePath in filename:
            filesArray.append(filename)

count = 0
sum = 0
for filePath in filesArray:
  coveredFiles = coverageJson["targets"][0]["files"]
  for covered in coveredFiles:
      path = covered["path"]
      if filePath in path:
          count = count + 1
          sum = sum + (covered["lineCoverage"] * 100)

percentage = 100
if count != 0:
    percentage = sum/count

print("{:.2f}".format(percentage))

file.close()
coverageFile.close()
