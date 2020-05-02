import os

def findCommit():
    countLine=0
    html=""
    with open ('htmldata/jenkins-test', 'rt') as myfile:
        for myline in myfile:
            countLine+=1
            if countLine>600 and countLine<700:
                html+=myline

    res = html.find("span class=\"num text-emphasized\"")
    commit=0
    while html[res]!='<':
        if html[res].isdigit():
            commit=commit*10+int(html[res])
        res+=1
    return commit

def askRepo():
    repo = input('Enter the repository ')
    return repo

def downloadHtml(repo):
    os.system('rm -d htmldata/*')
    os.system('wget '+repo+' -P htmldata/')

def cloneRepo(repo):
    os.system("rm -f /var/www/html/*")    
    os.system("rm -rf /var/www/html/.git/")
    os.system("git clone "+repo+".git  /var/www/html/.  ")

def checkCommit(repo, totalCommit):
    downloadHtml(repo)
    totalNewCommit = findCommit()
    if totalNewCommit>totalCommit :
        cloneRepo(repo)

    return totalNewCommit

repo = askRepo()
totalCommit = 0
while True:
    totalCommit = checkCommit(repo, totalCommit)
    print(totalCommit)








