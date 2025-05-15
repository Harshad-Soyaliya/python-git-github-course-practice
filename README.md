# python-git-github-course-practice
this is about practice and learning beginer to advance python programming and git and gihub lernning...

# git commands :

<h1>Git & GitHub Cheat Sheet</h1>

<h2>🔧 Configuring Git</h2>
<p>Connect Git to your GitHub account:</p>
<pre><code>git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list</code></pre>

<hr>

<h2>📦 Clone & Status</h2>

<h3>Clone a Repository</h3>
<p>Clone a repository from GitHub to your local machine:</p>
<pre><code>git clone https://github.com/username/repo.git</code></pre>

<h3>Check Status</h3>
<p>Displays the state of the code:</p>
<ul>
  <li><b>Untracked</b> – New files that Git doesn't yet track</li>
  <li><b>Modified</b> – Changed files</li>
  <li><b>Unmodified</b> – Unchanged files</li>
  <li><b>Staged</b> – File is ready to be committed</li>
</ul>
<pre><code>git status</code></pre>

<hr>

<h2>➕ Add & Commit</h2>

<h3>Add Files</h3>
<pre><code># Add a single file
git add filename

# Add all files
git add .</code></pre>

<h3>Commit Changes</h3>
<pre><code>git commit -m "Your commit message"</code></pre>

<hr>

<h2>🚀 Push Command</h2>
<p>Upload local repo content to remote (GitHub) repository:</p>
<pre><code>git push origin main</code></pre>

<hr>

<h2>🆕 Init Command</h2>
<p>Used to create a new Git repository:</p>
<pre><code>git init
git remote add origin &lt;link&gt;
git remote -v
git branch
git branch -M main
git push -u origin main</code></pre>
<p>After that, next time you can use just:</p>
<pre><code>git push</code></pre>

<hr>

<h2>🔁 Git Workflow</h2>
<p><b>Flow:</b> GitHub repo create → Clone → Changes → Add → Commit → Push</p>

<hr>

<h2>🌿 Branch Commands</h2>
<pre><code>git branch            # Check current branch
git branch -M main    # Rename branch
git checkout branch_name         # Switch branch
git checkout -b new_branch_name  # Create and switch to new branch
git branch -d branch_name        # Delete a branch</code></pre>

<hr>

<h2>🔀 Merging Code</h2>

<h3>Way 1: Git Merge</h3>
<pre><code>git diff branch_name   # Compare
git merge branch_name  # Merge branches</code></pre>

<h3>Way 2: Pull Request (PR)</h3>
<p>Create a Pull Request on GitHub to merge changes between branches or forks.</p>

<hr>

<h2>⬇️ Pull Command</h2>
<pre><code>git pull origin main</code></pre>
<p>Fetch and download content from remote repo and update local repo.</p>

<hr>

<h2>⚔️ Resolving Merge Conflicts</h2>
<p>Occurs when Git cannot automatically resolve differences between commits.</p>

<hr>

<h2>↩️ Undoing Changes</h2>

<h3>Case 1: Staged Changes</h3>
<pre><code>git reset filename
git reset</code></pre>

<h3>Case 2: Undo Last Commit</h3>
<pre><code>git reset HEAD~1</code></pre>

<h3>Case 3: Undo Multiple Commits</h3>
<pre><code>git reset commit_hash
git reset --hard commit_hash</code></pre>

<hr>

<h2>🧾 Git Log</h2>
<pre><code>git log</code></pre>
<p>Show all previous commits (with hashes).</p>

<hr>

<h2>🍴 Fork</h2>
<p>
A fork is a new repository that shares code and visibility with the original "upstream" repository.  
A fork is essentially a rough copy that you can work on independently.
</p>
