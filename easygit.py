import os

gits = \
[
    "git@github.com:alibaba/async_simple.git",
    "git@github.com:yomorun/yomo.git"
]

temp = \
"if exist project_name (\n"\
"\tcd project_name\n"\
"\tgit pull\n"\
"\tcd ..\n"\
") else (\n"\
"\tgit clone --recurse-submodules=true project_git\n"\
")\n"\
"\n"

if __name__=='__main__':
    print("start...")

    lines = []

    for git in gits:
        project_name = git.split('/')[1].removesuffix(".git")
        project_git = git

        temp1 = temp
        result = temp1.replace("project_name", project_name).replace("project_git", project_git)
        lines.append(result)

    with open("easygit.bat", "w+") as fd:
        fd.writelines(lines)

    print("finish...")
    os.system("pause")
