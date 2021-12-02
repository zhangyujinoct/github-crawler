import datetime
import json

from baseRequest import base_request


def get_all_release_by_repo(owner, repo_name):
    resultList = []
    over = False
    page = 1
    while not over:
        res = base_request("repos/"+owner+"/"+repo_name+"/releases", {"per_page": 100, "page": page})
        page += 1
        print(len(res))
        resultList += res
        if len(res) < 100:
            over = True
    with open("./originData/"+owner+"_"+repo_name+"_releaseInfo"+".json", "w") as f:
        json.dump(resultList, f)
        print("加载入文件完成...")
