import json
import sys
import requests

sourcePath = sys.argv[1]
threshold = sys.argv[2]
pullrequestId = sys.argv[3]
githubToken = sys.argv[4]

#baseUrl
baseURL = "https://cap-sdebbich:{0}@api.github.com/repos/cap-sdebbich/CI-Sample".format(githubToken)
# Get Pull request SHA
prUrl = "{0}/pulls/{1}".format(baseURL,pullrequestId)
prJson = None
with requests.get(prUrl, stream=True) as response:
    # print(response)
    for chunk in response.iter_content(chunk_size=5000):
        if chunk:  # filter out keep-alive new chunks
            prJson = chunk
head = json.loads(prJson)["head"]
sha =head["sha"]

# Get changed or added files in the Pull Request
filesUrl = "{0}/files".format(prUrl)
filesJson = requests.get(filesUrl).json()

# Get Coverage
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

percentage = -100
if count != 0:
    percentage = sum/count

# Update PullRequest
coverageStatus = "success"
coverageDescription = "No Coverage Required"
if percentage >= 0:
    if percentage >= threshold:
        coverageDescription = "Percentage: {0}%".format(percentage)
    else:
        coverageStatus = "error"
        coverageDescription = "Percentage: {0}%, should be at least {1}%".format(threshold,percentage)
status = {"state":coverageStatus, "description":coverageDescription, "context":"New Code Coverage"}
updateStatusUrl = "{0}/statuses/{1}".format(baseURL,sha)
print(updateStatusUrl)
resp = requests.post(updateStatusUrl, json=status)
coverageFile.close()
