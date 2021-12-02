import json

from getTwoCommitCompare import get_two_commit_compare


def get_all_commit_compare(release_info_path, owner, repo_name):
    resultList = []
    with open(release_info_path, 'r') as read:
        data = json.load(read)
        for i in range(len(data)):
            if i + 1 < len(data):
                start_tag = data[i + 1]['tag_name']
                end_tag = data[i]['tag_name']
                resItem = get_two_commit_compare(owner, repo_name, start_tag, end_tag)
                resultList.append(resItem)
    with open("./originData/" + owner + "_" + repo_name + "_compare_info" + ".json", "w") as f:
        json.dump(resultList, f)
        print("加载入文件完成...")
