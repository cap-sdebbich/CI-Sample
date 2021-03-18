import json
import sys

filePath = sys.argv[1]
sourcePath = sys.argv[2]
coverageFile = open('coverage.json')
coverageJson = json.load(coverageFile)

coveredFiles = coverageJson["targets"][0]["files"]
coverage = -100
if sourcePath in filePath:
    for covered in coveredFiles:
        path = covered["path"]
        if filePath in path:
            coverage = covered["lineCoverage"] * 100
            break

print(int(coverage))
coverageFile.close()
