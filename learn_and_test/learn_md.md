# 实现页内跳转
[参考链接](https://www.cnblogs.com/tocy/p/markdown-link-inner-page.html)

### 写在前面
- 本文档是 copy 别人学习 [廖雪峰Git教程](http://t.cn/zQ6LFwE) 后所做的笔记


### 目录
* [1 创建版本库](#1)
* 2 添加文件到版本库
* [3 时光机穿梭](#3)
* 4 远程仓库
* 5 分支管理
* 6 标签管理


<h4 id='1'>1 创建版本库</h4>

```
git init  #初始化所在目录为Git仓库
```
> 初始化的目录可以不为空


#### 2 添加文件到版本库

```
git add <file> ...  #添加文件到暂存区（stage）
        -f <file> ...  #强制添加到暂存区（可用于添加忽略文件）
git commit -m "提交说明"  #从暂存区提交到版本库
```
> git add 命令可多次执行，然后commit一次。

<h4 id="3">3 时光机穿梭</h4>

<!-- #### 3 时光机穿梭 -->
- 查看状态、差异

```
git status  #查看仓库当前状态
git diff [file]  #比较工作区和暂存区的差异
git diff --cached [file]  #比较暂存区和版本库的差异
git diff HEAD -- [file]  #比较工作区和版本库的差异
```
- 版本切换

```
git log  #查看提交历史
git log -1  #查看最后一次提交信息（-2 则是最后两次）
git log --pretty=oneline  #单行格式显示提交历史
        --graph  #显示分支合并图
        --abbrev-commit  #简写的commit_id
git reflog  #查看所有操作记录，包括删除的commit记录
git reset --hard HEAD^  #回退到上一版本
# HEAD 表当前版本， HEAD^ 表上一版本，HEAD^^ 表上两版本，HEAD~99 表上99版本。
git reset --hard commit_id  #切换到指定版本
```
> Git跟踪管理的是修改，而非文件

- 撤销修改

```
git checkout -- <file>  #撤销工作区的修改
git reset HEAD <file>  #撤销暂存区的修改
```
> 若已commit但没提交到远程库，可用版本回退进行撤销

- 删除文件
  - 方法一：工作区删除文件，然后正常提交
  
  ```
  rm <file> ...  #工作区删除
  git add <file> ...  #将修改提交至暂存区
  git commit -m "说明"  #提交到版本库
  ```
  - 方法二：直接命令删除工作区和暂存区，然后提交版本库
  
  ```
  git rm <file> ...  #删除工作区和暂存区文件
  git commit -m "说明"  #提交到版本库
  ```
> 删除、增加文件也都属于修改

##### 4 远程仓库
- 创建SSH Key

```
ssh-keygen -t rsa -C "youremail@example.com"  #生成的Key在家目录.ssh文件夹里面，pub后缀是公钥，另一个是私钥。
```

- 添加远程库

```
git remote add origin git@server-name:path/repo-name.git  #添加远程仓库
git remote  #查看远程库信息
           -v  #显示详细信息
git push -u origin <branch>  #推送并关联指定分支到远程库
```
> 除第一次关联，之后push不用加-u选项

- 从远程库克隆

```
git clone git@server-name:path/repo-name.git  #将远程仓库克隆到当前目录
git pull  #在clone后，可拉取远程仓库最新的提交内容

ps:多人协作时，clone到本地的仓库是看不到分支的，想显示并修改分支可以输入以下命令
   git checkout -b <branch> origin/<branch>
```

#### 5 分支管理
```
git branch <branch>  #创建分支
git checkout <branch>  #切换到指定分支
git checkout -b <branch>  #创建并切换到该分支
git branch  #查看现有分支
git branch -d <branch>  #删除指定分支
git branch --set-upstream <branch_local> <branch_remote>  #指定本地分支与远程分支的链接-> 多人合作pull失败时可用
git merge <branch>  #合并指定分支到当前分支
          --no-ff <branch>  #禁用快速合并
git merge --no-ff -m "提交说明" <branch>  #普通方式合并，并附提交说明
git stash  #保存当前工作环境（包括工作区和暂存区）
git stash list  #查看保存的工作列表
git stash apply [stash@{X}]  #恢复工作状态，但不删除stash内容
git stash pop [stash@{X}]  #恢复工作状态，并删除stash内容
git stash drop [stash@{X}]  #删除stash内容
git branch -D <branch>  #强制删除分支（常用于未合并的分支）
```
> HEAD不是直接指向提交点，而是指向分支，分支再指向提交点

- 多人协作

```
## 由于小伙伴先推送了提交，而你恰好和他修改了同一文件且发生冲突：
## error: failed to push some refs to ... 
## 解决方案如下：

1. git pull 远程库
2. 解决冲突（若有），再push
```

- 分支管理策略图

![image](http://www.liaoxuefeng.com/files/attachments/001384909239390d355eb07d9d64305b6322aaf4edac1e3000/0)

#### 6 标签管理
```
git tag  #查看现有标签
git tag <tag_name>  #给当前所在的commit打标签
git tag <tag_name> <commit_id>  #给指定commit打标签
git tag -a <tag_name> -m "标签说明" <commit_id>  #给指定commit打标签，并附说明
        -s <tag_name> -m "标签说明" <commit_id>  #用gpg私钥签名
        -d <tag_name>  #删除标签
git show <tag_name>  #显示标签信息
git push origin <tag_name>  #推送标签到远程库
git push origin --tags  #推送所有未推送的标签到远程库
git push origin :refs/tags/<tag_name>  #删除远程标签（先删除本地，再使用该命令删除）
```
