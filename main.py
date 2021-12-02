from getAllCommitCompare import get_all_commit_compare
from getAllReleaseByRepo import get_all_release_by_repo
from getKeyReleaseInfo import get_key_release_info
from getTwoCommitCompare import get_two_commit_compare

if __name__ == '__main__':
    owner = "nextcloud"
    repo_name = "android"
    # 获取项目的所有release信息 params(owner, repo_name)
    # get_all_release_by_repo(owner, repo_name)

    # 处理获取到的release源数据文件
    # get_key_release_info(owner, repo_name, "./originData/"+owner+"_"+repo_name+"_releaseInfo.json")

    # 通过处理后的release源数据文件获取所有tag区间的commits
    get_all_commit_compare("./resolvedData/"+owner+"_"+repo_name+"_releaseInfo_resolved.json", owner, repo_name)
