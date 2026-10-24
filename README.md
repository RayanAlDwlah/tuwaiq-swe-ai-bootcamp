# Tuwaiq Academy: Modern Software Engineering and AI Systems

My exercise log from the Tuwaiq Academy bootcamp *Modern Software Engineering and AI Systems* (8 weeks, July to September 2026).

The first weeks covered the working basics every engineer uses daily: the terminal, Git and GitHub, Python, and calling an API. Each exercise began as its own small repository. They are collected here so the profile stays focused. Every folder was imported with `git subtree`, so its original commit history is kept.

The later weeks moved on to AI systems and automation. Those projects have their own repositories (see [Projects from the same bootcamp](#projects-from-the-same-bootcamp)).

## Contents

| Folder | Topic | What the exercise practises |
|---|---|---|
| [`01-terminal/terminal-log`](01-terminal/terminal-log) | Terminal | Redirecting command output into a log file (`uname`, `whoami`, `pwd`, `git --version`) |
| [`01-terminal/cli-tree`](01-terminal/cli-tree) | Terminal | Building a folder structure with `mkdir`, `mv`, `tree` |
| [`01-terminal/read-files`](01-terminal/read-files) | Terminal | Locating and reading files inside a folder tree |
| [`02-git/hello-github`](02-git/hello-github) | GitHub | First repository and edits on github.com |
| [`02-git/git-commit`](02-git/git-commit) | Git | The snapshot model, staging area vs commit, notes in [`git-notes.md`](02-git/git-commit/git-notes.md) |
| [`02-git/git-branch`](02-git/git-branch) | Git | Feature branch, then merge back into `main` |
| [`02-git/git-merge`](02-git/git-merge) | Git | Resolving a merge conflict, then `git revert` of a bad commit ([`revert-log.txt`](02-git/git-merge/revert-log.txt)) |
| [`02-git/git-push`](02-git/git-push) | Git | Syncing local and remote: pull a web edit, resolve, push |
| [`02-git/alula-trip-group-4`](02-git/alula-trip-group-4) | GitHub | Shared repository for a group exercise (group 4) |
| [`03-python/python-setup`](03-python/python-setup) | Python | Environment setup and a first script |
| [`03-python/python-basics`](03-python/python-basics) | Python | Variables, conditionals, `for` and `while` loops |
| [`03-python/python-functions`](03-python/python-functions) | Python | Functions, docstrings, refactoring repeated code |
| [`03-python/python-data`](03-python/python-data) | Python | Lists, dictionaries, lists of records, JSON parsing |
| [`04-apis/todo-api`](04-apis/todo-api) | APIs | A Postman collection for a to-do REST API on Supabase: login, then create, read, update and delete |

## Running the API exercise

1. Create a Supabase project with a `todos` table (`id`, `task`, `is_compleated`).
2. Import [`todo-api.postman_collection.json`](04-apis/todo-api/todo-api.postman_collection.json) into Postman.
3. Fill the collection variables: `SUPABASE_URL`, `SUPABASE_KEY` (the project's publishable key), `EMAIL` and `PASSWORD` for a test user.
4. Run `login` first. It stores `ACCESS_TOKEN`, which the other requests send as a bearer token.

The collection ships with empty credentials on purpose.

## Projects from the same bootcamp

| Repository | What it is |
|---|---|
| [n8n-expenses-mcp-server](https://github.com/RayanAlDwlah/n8n-expenses-mcp-server) | An MCP server in n8n that gives any MCP client persistent memory over Saudi bank-SMS expenses |
| [n8n-idea-validation-agents](https://github.com/RayanAlDwlah/n8n-idea-validation-agents) | A five-agent idea-validation workflow in which two agents exist only to reject |
| [n8n-saudi-jobs-digest](https://github.com/RayanAlDwlah/n8n-saudi-jobs-digest) | A daily Arabic digest of fresh-graduate tech jobs filtered from Saudi Telegram channels |

The final project, **Manat**, was an Arabic voice and text assistant built by a team of three. It answers questions only from nine Saudi fatwa books, cites the book, and declines when no source supports an answer. Its repository is private.

---

Rayan Saleh Al-Dwlah · [LinkedIn](https://www.linkedin.com/in/rayanaldwlah)
