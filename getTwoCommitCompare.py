import json

from baseRequest import base_request


def get_two_commit_compare(owner, repo_name, tag_one, tag_two):
    resultList = []
    over = False
    page = 1
    while not over:
        res = base_request("repos/" + owner + "/" + repo_name + "/compare/" + tag_one + "..." + tag_two,
                           {"per_page": 100, "page": page})
        page += 1
        if 'commits' in res.keys():
            resultList += res['commits']
        if not ('commits' in res.keys()) or len(res['commits']) < 100:
            over = True

    commitList = []
    for item in resultList:
        commitList.append(item['commit']['message'])
    print(commitList)
    result = {'tag_start': tag_one, 'tag_end': tag_two, 'commits': commitList}
    return result
