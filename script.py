import json
import sys

filePath = sys.argv[1]
sourcePath = sys.argv[2]
coverageFile = open('coverage.json')
coverageJson = json.load(coverageFile)

coveredFiles = coverageJson["targets"][0]["files"]

for covered in coveredFiles:
    path = covered["path"]
    if path in filePath:
        coverage = covered["lineCoverage"] * 100
        print(coverage)
        break

coverageFile.close()
