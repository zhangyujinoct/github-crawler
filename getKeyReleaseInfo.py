import json


def get_key_release_info(owner, repo_name, file_path):
    resultList = []
    with open(file_path, 'r') as read:
        data = json.load(read)
        print(type(data))
        for item in data:
            resItem = {'tag_name': item['tag_name'], 'body': item['body']}
            resultList.append(resItem)

    print(len(resultList))
    with open("./resolvedData/" + owner + "_" + repo_name + "_releaseInfo_resolved" + ".json", "w") as f:
        json.dump(resultList, f)
        print("加载入文件完成...")
