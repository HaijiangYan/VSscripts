The coding files in "VSscripts" contains Python scripts (for study and test) writen by VSCODE, which could be tracked by git and pushed to github. Below are some commonly used git commands (in terminal):

%install the git and set global configuration. 
git config --global user.name "Your Name"
git config --global user.email email@example.com

cd ~ (your current working directory)
git init (get .git)
%After set and change a file in ~ 
git add filename (add the new version in working memory, aka stage)
git commit -m "instruction of this change and version" (commit the change and save in long-term memory, aka master)

%Check current repository
git status
git diff filename
%Check history
git log (--pretty=oneline)

%Get back to the last version
git reset --hard HEAD^
%Get back to any version
git reset --hard commit id.
%Check commit id
git reflog
%Give up your changes in work directory, go back to the version in stage or master 
git checkout -- filename
%unstage (delete the version in stage)
git reset HEAD filename

%remove the file in wd and repository
rm filename
git rm filename
git commit -m "instruction"

%Connect local repository to github repository
git remote add origin git@github.com:HaijiangYan/VSscripts.git
git push -u origin master (firstly, please keep SSH key correct)
git push origin master
%Clone a remote repository to local wd
git clone git@github.com:HaijiangYan/gitskills.git
%Disconnect
git remote -v
git remote rm origin


%create a new branch "dev"
git branch dev
git checkout dev
(git checkout -b dev)

%submit as before
git add readme.txt
git commit -m "branch test"

%switch back (could also replace the 'checkout' with 'switch', the latter is more specific)
git checkout master
%merge the branches
git merge dev
%delete the branch dev
git branch -d dev


