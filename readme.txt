The coding files in "VSscripts" contains Python scripts (for study and test) writen by VSCODE, which could be tracked by git and pushed to github. Below are some commonly used git commands (in terminal):

%install the git and set global configuration. 
git config --global user.name "Your Name"
git config --global user.email email@example.com

cd ~ (your current working directory)
git init (get .git)
%After set and change a file in ~ 
git add filename (add the new edition in working memory, aka stage)
git commit -m "instruction of this change and edition" (commit the change and save in long-term memory, aka master)

%Check current repository
git status
git diff filename
%Check history
git log (--pretty=oneline)

%Get back to the last edition
git reset --hard HEAD^
%Get back to any edition
git reset --hard commit id.
%Check commit id
git reflog
%Give up your changes in work directory, go back to the version in stage or master 
git checkout -- filename
%unstage (delete the edition in stage)
git reset HEAD filename

%remove the file in wd and repository
rm filename
git rm filename
git commit -m "instruction"

%Connect local repository to github repository
git remote add origin git@github.com:HaijiangYan/VSscripts.git
git push -u origin master (firstly)
git push origin master
%Clone a remote repository to local wd
git clone git@github.com:HaijiangYan/gitskills.git
%Disconnect
git remote -v
git remote rm origin