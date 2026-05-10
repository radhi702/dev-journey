# 📚 Complete Git Reference Guide
## From Beginner to Pro — Radhika's Git Bible

---

## 🔰 WHAT IS GIT?

**Git** = A tool on your computer that takes snapshots of your code
**GitHub** = A website that stores those snapshots online

- Git works offline (on your laptop)
- GitHub needs internet (stores code online)
- You can use Git without GitHub — but not GitHub without Git

---

## ⏰ DAILY WORKFLOW (Memorize These First)

```
git pull          → get latest from GitHub (do this FIRST every day)

// write your code...

git add .         → select all files for snapshot
git commit -m ""  → take the snapshot with a label
git push          → upload to GitHub
```

---

## 📗 BEGINNER COMMANDS

| Command | What It Does | When To Use |
|---------|-------------|-------------|
| `git init` | Start tracking a folder | Starting a new project |
| `git clone URL` | Download repo from GitHub | Getting an existing project |
| `git add .` | Stage ALL changed files | Before every commit |
| `git add filename` | Stage ONE specific file | When you want to commit selectively |
| `git commit -m "message"` | Take a snapshot with label | After finishing a feature or task |
| `git push` | Upload snapshots to GitHub | After committing |
| `git pull` | Download latest from GitHub | Before starting work every day |
| `git status` | See what changed | When confused about current state |
| `git log` | See full commit history | Reviewing past snapshots |
| `git log --oneline` | See history in clean one-line format | Quick history review |
| `git log --oneline -5` | See only last 5 commits | Quick recent history |
| `git diff` | See exactly what changed line by line | Before committing |
| `git diff filename` | See changes in one specific file | Checking specific file changes |
| `git remote add origin URL` | Connect folder to GitHub repo | One-time setup per project |
| `git remote -v` | See connected remote repositories | Checking connections |
| `git branch -M main` | Rename branch to main | One-time setup per project |
| `git push -u origin main` | Push AND remember connection | First push of new project |

---

## 📘 INTERMEDIATE COMMANDS

| Command | What It Does | When To Use |
|---------|-------------|-------------|
| `git branch` | List all branches | Seeing what branches exist |
| `git branch feature-name` | Create a new branch | Starting a new feature |
| `git branch -d branch-name` | Delete a branch | After merging a finished feature |
| `git branch -a` | List ALL branches including remote | Full overview |
| `git checkout branch-name` | Switch to a different branch | Moving between features |
| `git checkout -b new-branch` | Create AND switch to branch | Fastest way to start new feature |
| `git checkout -- filename` | Restore file to last committed version | Undoing unwanted changes in a file |
| `git merge branch-name` | Combine branch into current branch | After feature is ready |
| `git fetch origin` | Download latest but don't apply yet | When you want to review before applying |
| `git stash` | Hide unfinished work temporarily | When switching tasks urgently |
| `git stash pop` | Bring back hidden work | Coming back to stashed work |
| `git stash list` | See all stashed work | Checking what's stored |
| `git stash drop` | Delete stashed work permanently | Clearing old stashes |
| `git reset filename` | Unstage a file (undo git add) | Accidentally staged wrong file |
| `git reset HEAD~1` | Undo last commit but keep changes | Made wrong commit message |
| `git reset --hard HEAD~1` | Undo last commit AND delete changes ⚠️ | Very careful — permanent! |
| `git revert HEAD` | Safely undo last commit | When working in teams |
| `git revert abc123` | Undo a specific commit by ID | Fixing specific past mistake |
| `git cherry-pick abc123` | Copy one specific commit to current branch | Taking one change from another branch |
| `git tag v1.0` | Mark an important version | Releasing a version |
| `git tag` | List all tags | Seeing all versions |
| `git clean -fd` | Remove untracked files and folders | Cleaning up messy workspace |

---

## 📙 TEAM/PROFESSIONAL COMMANDS

| Command | What It Does | When To Use |
|---------|-------------|-------------|
| `git rebase main` | Rewrite commits on top of main (cleaner than merge) | Keeping clean history |
| `git rebase -i HEAD~3` | Interactive rebase — edit last 3 commits | Cleaning up messy commits |
| `git push --force` | Force push to GitHub ⚠️ | VERY careful — overwrites GitHub history |
| `git push --force-with-lease` | Safer force push | Better alternative to --force |
| `git blame filename` | See who wrote each line of code | Finding who made a change |
| `git bisect start` | Start finding which commit introduced a bug | Debugging — binary search through history |
| `git bisect good` | Mark current commit as working | During bisect session |
| `git bisect bad` | Mark current commit as broken | During bisect session |
| `git reflog` | See EVERY action ever taken | Recovery tool when things go wrong |
| `git shortlog` | Summarize commits by author | Team contribution overview |
| `git describe` | Describe commit relative to tags | Versioning |
| `git submodule add URL` | Use one repo inside another | Complex projects with dependencies |
| `git worktree add` | Work on multiple branches simultaneously | Advanced multi-tasking |
| `git archive` | Export project as zip file | Sharing without git history |
| `git config --list` | See all git configurations | Checking setup |
| `git config --global` | Set global git settings | One-time setup |

---

## 📕 ADVANCED / CI-CD COMMANDS

| Command | What It Does | When To Use |
|---------|-------------|-------------|
| `git hooks` | Run scripts automatically on git events | Automating checks before commit/push |
| `git gc` | Cleanup and optimize repository | Maintaining large repos |
| `git fsck` | Verify integrity of repository | Checking for corruption |
| `git bundle` | Package repo into single file | Transferring without internet |
| `git notes` | Add extra notes to commits | Adding context without changing history |
| `git filter-branch` | Rewrite entire history ⚠️ | Removing sensitive data from history |

---

## 🎯 WORD-BY-WORD MEANING OF KEY COMMANDS

### `git add .`
- `git` = hey Git
- `add` = select/stage files for next snapshot
- `.` = **dot = everything in this folder** (like Command+A)

### `git commit -m "message"`
- `git` = hey Git
- `commit` = take the snapshot now
- `-m` = m stands for message
- `"message"` = label for this snapshot

### `git push -u origin main`
- `git` = hey Git
- `push` = upload to GitHub
- `-u` = remember this connection for next time
- `origin` = nickname for GitHub repo address
- `main` = the branch being pushed

### `git remote add origin URL`
- `git` = hey Git
- `remote` = I'm talking about an online location
- `add` = add a new one
- `origin` = give it nickname "origin"
- `URL` = here's the actual address

### `git clone URL`
- `git` = hey Git
- `clone` = make an exact copy
- `URL` = from this address

### `git pull origin main`
- `git` = hey Git
- `pull` = download and apply
- `origin` = from GitHub
- `main` = the main branch

---

## 🌿 BRANCHING WORKFLOW (How Teams Work)

```
1. git pull                          → get latest code
2. git checkout -b feature-login     → create new branch
3. // write your code...
4. git add .
5. git commit -m "added login page"
6. git push origin feature-login     → push YOUR branch
7. // create Pull Request on GitHub
8. // teammate reviews your code
9. // merge approved → code goes to main
10. git checkout main                → go back to main
11. git pull                         → get the merged changes
12. git branch -d feature-login      → delete old branch
```

---

## 🚦 GIT STATUS MEANINGS

When you run `git status`:

```
Changes not staged for commit    → files changed but not added yet
Changes to be committed          → files added, ready to commit
Untracked files                  → new files Git doesn't know about yet
nothing to commit                → everything is clean and pushed
```

---

## ⚡ SHORTCUTS YOUR FRIEND SET UP

Your Mac has aliases (shortcuts) for Git:

| Shortcut | Full Command |
|----------|-------------|
| `g` | `git` |
| `gra` | `git remote add` |
| `gp` | `git push` |

So you can type `gp` instead of `git push`!

---

## 🔴 DANGER COMMANDS — USE CAREFULLY

| Command | Why Dangerous |
|---------|--------------|
| `git reset --hard` | Permanently deletes your changes |
| `git push --force` | Overwrites GitHub history |
| `git clean -fd` | Permanently deletes untracked files |
| `git filter-branch` | Rewrites entire history |
| `git rebase` (on shared branches) | Can cause conflicts for teammates |

---

## ✅ DAILY HABIT CHECKLIST

Every day before starting work:
- [ ] `git pull` → get latest code
- [ ] `git status` → check current state

Every day after finishing work:
- [ ] `git add .` → stage changes
- [ ] `git commit -m "what I did today"` → snapshot
- [ ] `git push` → upload to GitHub
- [ ] Check github.com → confirm green square added

---

## 💡 REMEMBER

- **Git** = camera on your laptop
- **GitHub** = Google Photos online
- **Commit** = one snapshot
- **Branch** = parallel timeline
- **Push** = upload
- **Pull** = download
- **Merge** = combine two timelines
- **Clone** = download entire project

The only commands you MUST know by heart:
```
git pull
git add .
git commit -m ""
git push
git status
```

Everything else → Google when you need it!
