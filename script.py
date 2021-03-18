import json
import sys

filesArray = sys.argv[1]
print(filesArray)
# sourcePath = sys.argv[2]
coverageFile = open('coverage.json')
coverageJson = json.load(coverageFile)

print(coverageJson["targets"][0]["files"])

for file in filesArray:
    print(file)

coverageFile.close()
