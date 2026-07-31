# Git Commands Reference

## Contents

1. Git Setup
2. Repository Initialization
3. Clone a Repository
4. Basic Workflow
5. Branching
6. Merging and Rebasing
7. Stashing
8. Remote Repositories
9. Undo and Fix Mistakes
10. Viewing History
11. Tags
12. Ignoring Files
13. Configuration
14. Git Status and Diff
15. Notes

---

## 1. Git Setup

Configure your user name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check configuration:

```bash
git config --list
```

Set default editor:

```bash
git config --global core.editor "code --wait"
```

---

## 2. Repository Initialization

Create a new repository:

```bash
git init
```

Initialize with a specific directory:

```bash
git init my-project
```

---

## 3. Clone a Repository

Clone remote repository:

```bash
git clone https://github.com/user/repo.git
```

Clone with SSH:

```bash
git clone git@github.com:user/repo.git
```

Clone into a custom folder:

```bash
git clone https://github.com/user/repo.git my-folder
```

---

## 4. Basic Workflow

Check current status:

```bash
git status
```

Add files to staging area:

```bash
git add file.txt
git add .
git add '*.md'
```

Commit changes:

```bash
git commit -m "Add feature description"
```

Commit with staged and unstaged changes:

```bash
git commit -a -m "Update all tracked files"
```

View commit log:

```bash
git log
```

---

## 5. Branching

List branches:

```bash
git branch
```

Create a branch:

```bash
git branch feature-branch
```

Switch branches:

```bash
git checkout feature-branch
```

Create and switch in one step:

```bash
git checkout -b feature-branch
```

Delete a branch:

```bash
git branch -d feature-branch
```

Force delete:

```bash
git branch -D feature-branch
```

---

## 6. Merging and Rebasing

Merge a branch into the current branch:

```bash
git merge feature-branch
```

Rebase current branch onto another branch:

```bash
git rebase main
```

Interactive rebase:

```bash
git rebase -i HEAD~3
```

Abort a rebase:

```bash
git rebase --abort
```

Continue after resolving conflicts:

```bash
git add resolved-file.txt
git rebase --continue
```

---

## 7. Stashing

Save local changes:

```bash
git stash
```

List stashes:

```bash
git stash list
```

Apply the latest stash:

```bash
git stash apply
```

Apply and drop stash:

```bash
git stash pop
```

Drop a stash:

```bash
git stash drop stash@{0}
```

---

## 8. Remote Repositories

Show remotes:

```bash
git remote -v
```

Add a remote:

```bash
git remote add origin https://github.com/user/repo.git
```

Fetch changes:

```bash
git fetch origin
```

Pull latest changes:

```bash
git pull origin main
```

Push your branch:

```bash
git push origin feature-branch
```

Set upstream branch:

```bash
git push -u origin feature-branch
```

Remove a remote:

```bash
git remote remove origin
```

---

## 9. Undo and Fix Mistakes

Unstage a file:

```bash
git reset HEAD file.txt
```

Discard changes in working directory:

```bash
git checkout -- file.txt
```

Reset to a previous commit (keep changes):

```bash
git reset --soft HEAD~1
```

Reset to a previous commit (discard changes):

```bash
git reset --hard HEAD~1
```

Revert a commit with a new commit:

```bash
git revert <commit-hash>
```

---

## 10. Viewing History

Show commit history:

```bash
git log
```

Show one-line history:

```bash
git log --oneline
```

Show history with graph:

```bash
git log --oneline --graph --decorate --all
```

Show file history:

```bash
git log -- file.txt
```

Show a commit diff:

```bash
git show <commit-hash>
```

---

## 11. Tags

List tags:

```bash
git tag
```

Create a lightweight tag:

```bash
git tag v1.0
```

Create an annotated tag:

```bash
git tag -a v1.0 -m "Release 1.0"
```

Push tags:

```bash
git push origin v1.0
```

Push all tags:

```bash
git push origin --tags
```

---

## 12. Ignoring Files

Create a `.gitignore` file and add patterns:

```text
# Ignore Python bytecode
__pycache__/
*.pyc

# Ignore OS files
.DS_Store
Thumbs.db

# Ignore local environment
.env
```

Apply `.gitignore` to tracked files:

```bash
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

---

## 13. Configuration

Set default branch name:

```bash
git config --global init.defaultBranch main
```

Enable helpful diff options:

```bash
git config --global color.ui auto
```

Set global excludes file:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

---

## 14. Git Status and Diff

Show working tree status:

```bash
git status
```

Show changes between working tree and index:

```bash
git diff
```

Show staged changes:

```bash
git diff --staged
```

Show changes for a specific file:

```bash
git diff -- file.txt
```

Show commit differences:

```bash
git diff HEAD~1 HEAD
```

---

## 15. Notes

- Always run `git status` before committing.
- Use branches to keep features isolated.
- Commit small, logical changes with clear messages.
- Use `git pull --rebase` to keep history linear when collaborating.
- Back up important branches with tags or remote pushes.
- Use `git log --oneline --graph --decorate --all` for a quick history overview.
