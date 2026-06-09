 require('dotenv').config();
  const fs = require('fs');

  const USERNAME = process.env.GITHUB_USERNAME;
  const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN;
  const CHAT_ID = process.env.TELEGRAM_CHAT_ID;

  // Fetch recent GitHub activity
  async function getGitHubActivity() {
    const response = await fetch(`https://api.github.com/users/${USERNAME}/events/public`);
    const events = await response.json();

    // Filter only push events (commits) from last 24 hours
    const oneDayAgo = new Date(Date.now() - 24 * 60 * 60 * 1000);
    const recentPushes = events.filter(event =>
      event.type === 'PushEvent' && new Date(event.created_at) > oneDayAgo
    );

    return recentPushes;
  }

  // Create a summary from the activity
  function createSummary(pushes) {
    if (pushes.length === 0) {
      return 'No GitHub activity in the last 24 hours.';
    }

    let totalCommits = 0;
    const repos = new Set();

    pushes.forEach(push => {
      totalCommits += push.payload.commits.length;
      repos.add(push.repo.name);
    });

    const repoList = Array.from(repos).join(', ');
    return `GitHub Activity Summary:\nTotal commits: ${totalCommits}\nRepos: ${repoList}`;
  }

  // Save summary to a file
  function saveToFile(summary) {
    const date = new Date().toLocaleDateString();
    const entry = `\n--- ${date} ---\n${summary}\n`;
    fs.appendFileSync('github-activity-log.txt', entry);
  }

  // Send summary to Telegram
  async function sendTelegram(summary) {
    const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;
    await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: CHAT_ID, text: summary })
    });
  }

  // Run everything
  async function run() {
    console.log('Checking GitHub activity...');
    const pushes = await getGitHubActivity();
    const summary = createSummary(pushes);
    saveToFile(summary);
    console.log('Saved to file!');
    await sendTelegram(summary);
    console.log('Sent to Telegram!');
    console.log(summary);
  }

  run();