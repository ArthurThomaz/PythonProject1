# git commit - cria um novo git
# Ramos no git - Devido a não existir sobrecarga de armazenamento/
# memória associada à criação de ramos, é mais fácil dividir logicamente
# o seu trabalho do que ter ramos grandes e gordos.
#
# um ramo diz essencialmente "Quero incluir o trabalho deste commit e de todos os seus ancestrais".
#
# git commit = creates a new git down the main
# git branch [name] = creates a new branch
# git checkout -b [name] = create a new branch and select on the same time
# git checkout [name] = select the branch
# git merge [name] = merge the named branch to the already selected branch
# git rebase [name] = bring the selected branch under the nominated branch
# detach HEAD = just click on the branch and turn it to HEAD
# git checkout HEAD~4 = Go backwards on the tree and move the HEAD
# git branch -f main HEAD~3 = branch forcing - directly reassign 'main' to a commit 3 up of HEAD
# local commit reversing = git reset HEAD~1
# remote commit reversing = git revert HEAD
# git cherry-pick [C1 C2 C3] =  copy the commits to trasnfer them
# git rebase -i HEAD~4 = copy commits to transfer
# select the commit and drag to re arrenge, then selet the one you DONT want to copy
#
# rebase and copy = git rebase bugFix main = will copy the bugFix to the main and transfer the base with the nominated   
#
#
#
# ( Rebasing ) = While this sounds confusing, the advantage of rebasing is that it can be
#                used to make a nice linear sequence of commits. The commit log
#                / history of the repository will be a lot cleaner if only rebasing is allowed.
#
#
#
#
#
#