# python-git-github-course-practice
this is about practice and learning beginer to advance python programming and git and gihub lernning...

# git commands :


  <h1>Git Commands Guide</h1>

  <div class="section">
    <h2>Configuring Git</h2>
    <div class="command">
      <pre>git config --global user.name "my name"</pre>
    </div>
    <div class="command">
      <pre>git config --global user.email "someone@email.com"</pre>
    </div>
    <div class="command">
      <pre>git config --list</pre>
    </div>
  </div>

  <div class="section">
    <h2>Clone & Status</h2>
    <p><strong>Clone:</strong> Clone a repository to your local machine.</p>
    <div class="command">
      <pre>git clone https://github.com/your/repo.git</pre>
      
    </div>
    <p><strong>Status:</strong> Show the working tree status.</p>
    <div class="command">
      <pre>git status</pre>
     
    </div>
  </div>

  <div class="section">
    <h2>Add & Commit</h2>
    <p><strong>Add:</strong> Add files to staging area.</p>
    <div class="command">
      <pre>git add filename</pre>
    
    </div>
    <div class="command">
      <pre>git add .</pre>
      
    </div>
    <p><strong>Commit:</strong> Record changes to the repository.</p>
    <div class="command">
      <pre>git commit -m "some msg"</pre>
   
    </div>
  </div>

  <div class="section">
    <h2>Push Command</h2>
    <p>Push local repository changes to remote.</p>
    <div class="command">
      <pre>git push origin main</pre>

    </div>
  </div>

  <div class="section">
    <h2>Init Command</h2>
    <div class="command">
      <pre>git init</pre>
    
    </div>
    <div class="command">
      <pre>git remote add origin https://github.com/your/repo.git</pre>
     
    </div>
    <div class="command">
      <pre>git remote -v</pre>
    
    </div>
    <div class="command">
      <pre>git branch</pre>
     
    </div>
    <div class="command">
      <pre>git branch -M main</pre>
    
    </div>
    <div class="command">
      <pre>git push -u origin main</pre>
     
    </div>
  </div>

  <div class="section">
    <h2>Workflow</h2>
    <p>GitHub repo create → Clone → Changes → Add → Commit → Push</p>
  </div>

  <div class="section">
    <h2>Branch Commands</h2>
    <div class="command">
      <pre>git branch</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git branch -M main</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git checkout branch-name</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git checkout -b new-branch-name</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git branch -d branch-name</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
  </div>

  <div class="section">
    <h2>Merging Code</h2>
    <p><strong>Way 1:</strong></p>
    <div class="command">
      <pre>git diff branch-name</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git merge branch-name</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <p><strong>Way 2:</strong> Create PR (Pull Request)</p>
  </div>

  <div class="section">
    <h2>Pull Request</h2>
    <p>Pull request lets you tell others about changes you've pushed to a branch in a repository on GitHub.</p>
  </div>

  <div class="section">
    <h2>Pull Command</h2>
    <div class="command">
      <pre>git pull origin main</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
  </div>

  <div class="section">
    <h2>Resolving Merge Conflicts</h2>
    <p>An event takes place when Git is unable to automatically resolve differences in code between two commits.</p>
  </div>

  <div class="section">
    <h2>Undoing Changes</h2>
    <p><strong>Staged Changes:</strong></p>
    <div class="command">
      <pre>git reset filename</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git reset</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <p><strong>Committed Changes (1 commit):</strong></p>
    <div class="command">
      <pre>git reset HEAD~1</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <p><strong>Committed Changes (Multiple):</strong></p>
    <div class="command">
      <pre>git reset commit-hash</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
    <div class="command">
      <pre>git reset --hard commit-hash</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
  </div>

  <div class="section">
    <h2>Git Log</h2>
    <div class="command">
      <pre>git log</pre>
      <button class="copy-btn" onclick="copyText(this)">Copy</button>
    </div>
  </div>

  <div class="section">
    <h2>Fork</h2>
    <p>A fork is a new repository that shares code and visibility settings with the original "upstream" repository.</p>
  </div>



