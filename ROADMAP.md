# 🗺️ Radhika's 6-Month Automation Engineer Roadmap

**Start date:** April 26, 2026  
**Target:** October 2026 — ready for remote automation engineer jobs + Upwork gigs  
**Current status:** Day 19 complete (May 15, 2026)

---

## How to Use This Document

- This is your master plan. Come back to it every week.
- Each phase has **learning goals** (what you'll understand) and **build projects** (what you'll create).
- Every project goes into your `dev-journey` repo on GitHub — your living portfolio (collection of work that shows employers what you can do).
- You don't need to follow this perfectly. Some days you'll go fast, some days slow. That's normal.
- **Rule:** Never skip a phase. Each one builds on the last.

---

## How to Use Claude Code (Me!) Safely

Before we go further, here are rules for working with me:

### Things I Will NEVER Do Without Asking You First
- Create new files or folders
- Delete anything
- Push code to GitHub
- Install packages (new tools/libraries)
- Change your existing files

### How to Talk to Me
- **Ask me to explain:** "What does this mean?" or "Why do we need this?"
- **Ask me to plan:** "What should I do next?" — I'll explain before doing anything
- **Ask me to build with you:** "Let's build X together" — I'll go step by step, asking your permission before each action
- **Ask me to review:** "Check my code" or "Did I do this right?"
- **Stop me:** If I'm doing something you don't understand, say "Stop" or "Wait, explain this first"

### Useful Commands You Can Type
- `/help` — shows what I can do
- `! command` — runs a terminal command (the `!` tells me to run it for you). Example: `! git status`
- You can also just type normally and ask questions

### How to Find Files on Mac
- **Finder** (the smiley face icon in your dock) — this is like "My Computer" on Windows
- Your project is at: `/Users/radhikasharma/dev-journey/`
- In Finder, press `Cmd + Shift + G` and paste that path to go there directly
- **Terminal** — where you type commands. You're using it right now with Claude Code!

---

## ✅ PHASE 1: Foundations (Weeks 1-3) — COMPLETED

*You already did this! Here's what you learned:*

- JavaScript basics (variables, functions, loops, conditionals)
- Python basics (same concepts, different language)
- Git & GitHub (commits, push, pull, .gitignore)
- API calls (REST APIs, GET requests, authentication)
- n8n basics (nodes, connections, triggers, webhooks)
- Built 3 workflows: Daily Briefing, Onboarding, Error Alert
- OAuth (a secure way for apps to connect without sharing passwords)
- Security: credential management, no hardcoded keys
- Error handling (try/catch — code that catches mistakes gracefully)

**Portfolio items:** 3 production n8n workflows, practice code files

---

## 📘 PHASE 2: JavaScript Deep Dive (Weeks 4-5) — Days 20-33

*Why this matters:* JavaScript is the #1 language for automation. n8n uses it, APIs use it, web apps use it. You need to be comfortable writing it, not just copying it.

### Week 4 (Days 20-26): JavaScript Core Skills

**Learn:**
- Arrays in depth — `.map()`, `.filter()`, `.reduce()`, `.forEach()` (ways to loop through lists of data)
- Objects in depth — nested objects (objects inside objects), destructuring (pulling values out quickly)
- Promises & async/await (how JavaScript handles things that take time, like API calls)
- Template literals (the backtick strings you already use in n8n: `` `Hello ${name}` ``)
- JSON — parsing (reading) and stringifying (converting to text). You already work with JSON in n8n!
- String methods — `.split()`, `.trim()`, `.includes()`, `.replace()`

**Build:**
- **Project: Data Transformer Tool** — a script that takes messy API data (like raw weather JSON) and cleans it into a nice format. Practice with real data from your existing APIs.

**Risks to know:**
- `async/await` is confusing for everyone at first. That's normal. We'll practice with simple examples before complex ones.

### Week 5 (Days 27-33): JavaScript for Automation

**Learn:**
- Reading and writing files with Node.js (`fs` module — the built-in tool for file operations)
- Environment variables (`.env` files — the safe way to store secrets in code projects)
- `npm` packages (how to use other people's code safely — and what to watch out for)
- `axios` or `node-fetch` (libraries that make API calls easier than raw `fetch`)
- Basic date/time handling with `dayjs` (dates are surprisingly tricky in programming)
- Scheduling with `node-cron` (running code at specific times — like n8n's Schedule Trigger, but in pure code)

**Build:**
- **Project: GitHub Activity Tracker** — a Node.js script that checks your GitHub activity daily, saves it to a file, and optionally sends a Telegram summary. This practices file I/O, APIs, scheduling, and `.env` for secrets.

**Risks to know:**
- When installing npm packages: always check if the package is popular and maintained. Fake/malicious (harmful) packages exist. We'll check together before installing anything.
- `.env` files must ALWAYS be in `.gitignore`. We'll set this up first before putting any secrets in them.

---

## 🔧 PHASE 3: Advanced n8n + Real Automation (Weeks 6-8) — Days 34-54

*Why this matters:* You already know n8n basics. Now you become an n8n expert — the skill companies actually pay for.

### Week 6 (Days 34-40): n8n Power User

**Learn:**
- Sub-workflows (workflows that call other workflows — like functions in code)
- Error handling patterns in n8n (retry on failure, fallback paths)
- Merge node (combining data from multiple sources into one stream)
- Switch node (more advanced routing than IF — like multiple if/else)
- Item Lists node (working with arrays/lists inside n8n)
- HTTP Request node advanced: pagination (when APIs send data in pages), headers, query params
- Expressions deep dive (the `{{ }}` syntax inside n8n nodes)

**Build:**
- **Project: Multi-Source Content Aggregator** — a workflow that pulls content from 3+ sources (Reddit, Hacker News, Dev.to), filters by keywords you care about, removes duplicates (items that appear twice), and sends a daily digest to Telegram.

### Week 7 (Days 41-47): Database Basics

**Learn:**
- What is a database and why you need one (storing data that survives restarts)
- Google Sheets as a simple database (you already know this a bit!)
- Airtable basics (a more powerful spreadsheet-database, free tier available)
- Basic SQL concepts (the language databases understand — SELECT, INSERT, WHERE)
- Supabase intro (a free database service that's very beginner-friendly)

**Build:**
- **Project: Lead Tracker Automation** — when a Google Form is submitted (Google Forms is completely free), save the lead to a database, check for duplicates, send a welcome email, and log everything. This is a real automation that businesses pay for.

**Risks to know:**
- Supabase free tier: limited to 2 projects, 500MB storage. Enough for learning but don't create lots of test projects.
- Airtable free tier: 1,000 records per base. Fine for learning.
- NEVER put real customer data in free-tier services. We'll use fake/test data.

### Week 8 (Days 48-54): Webhooks & Real-Time Automation

**Learn:**
- Webhooks deep dive (your n8n workflow becoming an API that other services can call)
- Webhook security (how to verify that the caller is legitimate, not a hacker)
- Respond to Webhook node (sending data back to the caller)
- Chatbot basics with n8n (receiving messages, processing them, replying)
- Integrating with Slack (many companies use Slack — this is a very marketable skill)

**Build:**
- **Project: Slack Command Bot** — a Slack bot that responds to commands like `/weather` or `/crypto` by calling your existing APIs and returning formatted data. Reuses your existing API integrations!

**Risks to know:**
- Webhook URLs are like door keys — anyone with the URL can trigger your workflow. We'll add authentication (verification) to prevent this.
- Slack apps need workspace admin approval in companies. For learning, create your own free Slack workspace.

---

## 🐍 PHASE 4: Python for Automation (Weeks 9-11) — Days 55-75

*Why this matters:* Python is the #2 automation language. Many jobs want both JS and Python. You already know Python basics — now we make it useful.

### Week 9 (Days 55-61): Python Practical Skills

**Learn:**
- Python virtual environments (`venv` — isolated spaces so packages don't conflict)
- `pip` package manager (Python's version of npm)
- `requests` library (the most popular Python HTTP library — for API calls)
- Working with JSON in Python
- File reading/writing in Python
- Error handling patterns (`try/except` — Python's version of try/catch)
- f-strings (Python's version of template literals: `f"Hello {name}"`)

**Build:**
- **Project: API Health Checker** — a Python script that checks if a list of APIs are working, logs the results, and alerts you if something is down. Practices APIs, file I/O, error handling.

### Week 10 (Days 62-68): Python Web Scraping

**Learn:**
- What is web scraping (extracting data from websites automatically)
- `BeautifulSoup` library (a tool for reading HTML pages)
- Legal and ethical rules of scraping — **very important!** (check robots.txt, respect rate limits, don't scrape private data)
- CSS selectors (how to tell your scraper which part of the page to read)
- Handling pagination in scraping (reading multiple pages)
- Saving scraped data to CSV/JSON files

**Build:**
- **Project: Job Listing Scraper** — scrapes remote automation engineer job postings from job boards, saves them to a file, and optionally sends new ones to Telegram. You'll actually use this to find jobs later!

**Risks to know:**
- Some websites block scrapers. Never scrape a site that says "no scraping" in their terms of service.
- Don't make too many requests too fast — this is called "rate limiting abuse" and can get your IP address blocked. We'll add delays between requests.
- Web scraping can break when websites change their design. This is normal — you just update your selectors.

### Week 11 (Days 69-75): Python + n8n Integration

**Learn:**
- Running Python scripts from n8n (Execute Command node)
- Building Python Flask/FastAPI microservices (small web servers) that n8n can call
- When to use Python vs JavaScript vs n8n for a task
- Data processing with Python `pandas` basics (a powerful library for working with tables of data)

**Build:**
- **Project: Data Pipeline** — n8n collects raw data from APIs → sends it to a Python service for processing/analysis → results go back to n8n → delivered via Telegram. This shows you can combine tools, which is what real automation engineers do.

---

## ☁️ PHASE 5: Cloud & Deployment (Weeks 12-14) — Days 76-96

*Why this matters:* Everything you've built runs on your laptop. Real automation runs in the cloud (on servers on the internet). Employers need to see you can deploy things.

### Week 12 (Days 76-82): Cloud Fundamentals

**Learn:**
- What is "the cloud"? (Someone else's computer that's always on)
- Linux command line basics (most servers use Linux, similar to Mac terminal but some differences)
- SSH (Secure Shell — a way to connect to a remote server from your terminal)
- VPS (Virtual Private Server) basics — Oracle Cloud Always Free tier (truly free forever, no credit card charges)
- Docker basics (a way to package your app so it runs the same everywhere — like a shipping container for code)
- NGINX basics (a web server that sits in front of your app — like a receptionist)

**Build:**
- **Project: Deploy n8n to the Cloud** — get your n8n instance running on a cloud server so it works 24/7, not just when your laptop is open.

**Risks to know:**
- We use ONLY truly free services — no credit card, no trial that expires.
- Oracle Cloud Always Free: gives you a small server forever for free. No charges ever if you stay on the free tier.
- Docker Hub: free for public images. Never put secrets in Docker images.
- **SECURITY:** When you deploy to the cloud, your app is on the internet. We'll set up firewalls (rules about who can connect) and passwords before exposing anything.

### Week 13 (Days 83-89): Self-Hosted n8n + Persistence

**Learn:**
- Docker Compose (running multiple containers together — n8n + database)
- PostgreSQL basics (a professional database — free, powerful)
- Backing up your workflows and data
- Environment variables on servers (`.env` but for the cloud)
- Free subdomains and HTTPS (the padlock in the browser address bar — means the connection is encrypted/secure). We'll use free subdomains like `.duckdns.org` instead of buying a domain name.
- Let's Encrypt (free HTTPS certificates)

**Build:**
- **Project: Production n8n Setup** — n8n + PostgreSQL in Docker, with HTTPS, auto-backups, and proper security. This is resume-worthy.

### Week 14 (Days 90-96): CI/CD Basics

**Learn:**
- What is CI/CD? (Continuous Integration / Continuous Deployment — automatic testing and deploying of your code)
- GitHub Actions basics (GitHub's built-in automation — like n8n but for your code)
- Automatic testing: when you push code, GitHub runs checks automatically
- Automatic deployment: when checks pass, code goes live automatically
- Secrets in GitHub Actions (how to safely use API keys in automation)

**Build:**
- **Project: Auto-Deploy Pipeline** — push code to GitHub → GitHub Actions runs tests → if tests pass, deploys automatically. GitHub Actions is free for public repos (which yours already is).

---

## 💼 PHASE 6: Professional Skills + Portfolio (Weeks 15-18) — Days 97-124

*Why this matters:* Technical skills get you interviews. Professional skills get you hired.

### Week 15 (Days 97-103): Make.com (Integromat)

**Learn:**
- Make.com basics (another popular automation platform, like n8n but cloud-hosted)
- Differences between n8n and Make.com
- Why knowing both makes you more hireable (some companies use n8n, some use Make.com)
- Scenarios (Make.com's name for workflows)
- Modules, routers, filters in Make.com

**Build:**
- **Project: Rebuild one of your n8n workflows in Make.com** — pick the Daily Briefing or Lead Tracker and recreate it. Shows employers you're platform-flexible (can use different tools).

**Risks to know:**
- Make.com free tier: 1,000 operations per month. Enough for learning but be careful with loops that run many times.

### Week 16 (Days 104-110): Zapier Basics

**Learn:**
- Zapier basics (the most popular automation platform — many job listings mention it)
- Zaps, triggers, actions
- Multi-step Zaps (note: Zapier free tier only allows 2-step Zaps — we'll learn the concepts and build what we can for free)
- Zapier vs n8n vs Make.com: strengths and weaknesses of each

**Build:**
- **Project: Zapier Workflow** — build a simple 2-step automation in Zapier's free tier to add it to your skills list. The goal is to understand the platform, not build everything there.

### Week 17-18 (Days 111-124): Portfolio Building

**Learn:**
- Writing a professional README for your GitHub repo
- Documenting your projects (so others can understand what you built)
- Recording short demo videos (Mac has built-in screen recording: `Cmd + Shift + 5`, or use OBS Studio which is free)
- Building a simple portfolio website (GitHub Pages — completely free, hosted on your GitHub account)
- Writing case studies (stories about your projects: the problem, your solution, the result)

**Build:**
- **Project: Portfolio Website on GitHub Pages** — a simple site showcasing your 6-8 best projects with descriptions, screenshots, and links. Hosted free on GitHub Pages (yourname.github.io)
- **Project: 3 Case Studies** — detailed write-ups of your best projects
- Clean up `dev-journey` repo with professional README, screenshots, and documentation

---

## 🚀 PHASE 7: Advanced Automation + AI (Weeks 19-21) — Days 125-145

*Why this matters:* AI-powered automation is the hottest skill in 2026. This is your competitive edge (what makes you stand out).

### Week 19 (Days 125-131): AI Integration Deep Dive

**Learn:**
- Free AI APIs — Groq (you already use this!), Google Gemini free tier, Hugging Face free models
- Prompt engineering (writing instructions that make AI give good results)
- AI agents concept (AI that can take actions, not just answer questions)
- Comparing free AI options (Groq vs Gemini vs Hugging Face — which is best for what)

**Build:**
- **Project: AI Email Responder** — automatically categorize incoming emails and draft responses using AI. Human reviews before sending. (Never let AI send emails without human approval!)

**Risks to know:**
- We only use free AI APIs. Groq, Google Gemini, and Hugging Face all have free tiers.
- Free tiers have rate limits (limits on how many requests you can make). We'll design around these limits.
- **NEVER** let AI take irreversible (cannot be undone) actions without human approval. Always have a human-in-the-loop (a person checking before the final step).

### Week 20 (Days 132-138): Advanced Integrations

**Learn:**
- CRM integrations (HubSpot free tier — CRM means Customer Relationship Management, software for managing business contacts. HubSpot free tier is truly free, no card needed)
- E-commerce concepts (WooCommerce is free and open-source — we'll learn the patterns without needing a live store)
- Telegram Bot API advanced (you already know Telegram — we'll build more complex bots as a free alternative to paid SMS services like Twilio)
- Google Workspace integrations (Gmail, Sheets, Calendar — all free with your Google account)

**Build:**
- **Project: Business Order Automation** — simulate (pretend/practice) an order system: Google Form as order input → n8n processes it → updates Google Sheets inventory → sends confirmation email via Gmail → notifies team on Slack/Telegram. Same skills as real e-commerce, zero cost.

### Week 21 (Days 139-145): Complex Workflow Patterns

**Learn:**
- Queue-based processing (handling tasks one at a time instead of all at once)
- Retry strategies (what to do when things fail — exponential backoff means waiting longer between each retry)
- Idempotency (making sure running the same automation twice doesn't create duplicate results)
- Rate limiting (controlling how fast you call APIs so you don't get blocked)
- Monitoring and alerting (knowing when your automations break — you already started this with your Error Alert System!)

**Build:**
- **Project: Batch Data Processor** — a workflow that processes thousands of items reliably, with retries, rate limiting, error logging, and progress tracking.

---

## 💰 PHASE 8: Job Preparation (Weeks 22-25) — Days 146-173

*Why this matters:* This is where your learning turns into money.

### Week 22-23 (Days 146-159): Freelance Preparation

**Learn:**
- Creating an Upwork profile (we'll write it together)
- How to write proposals that win (the message you send when applying to jobs)
- Pricing your services (hourly vs. project-based)
- Client communication skills (how to talk to people who hire you)
- Scope management (agreeing on exactly what you'll build, so there's no confusion)
- Contracts basics (protecting yourself legally)

**Build:**
- **Project: 3 Upwork Proposals** — we'll find real job postings and draft proposals
- **Project: Service Packages** — define 3 clear packages you can offer (basic, standard, premium)
- **Project: Client Onboarding Template** — a professional document you send to new clients explaining how you work

### Week 24-25 (Days 160-173): Interview Preparation

**Learn:**
- Common automation engineer interview questions
- How to explain your projects in 2 minutes (elevator pitch)
- Technical assessment practice (live coding / workflow building)
- Behavioral questions ("Tell me about a time you solved a difficult problem")
- Salary negotiation basics (for India-based remote roles: ₹4-8 LPA entry level, $15-30/hr USD for international remote)
- How to evaluate if a job/client is good or bad (red flags to watch for)

**Build:**
- **Project: Interview Prep Document** — your answers to the 20 most common questions
- Practice building a workflow from scratch in 30 minutes (timed practice)

---

## 🏁 PHASE 9: Launch (Week 26) — Days 174-180

### The Final Week

- [ ] Upwork profile is live with portfolio links
- [ ] LinkedIn profile updated with automation engineer title
- [ ] Portfolio website is live
- [ ] `dev-journey` repo has clean README with project showcase
- [ ] Applied to at least 10 Upwork jobs
- [ ] Applied to at least 5 full-time remote positions
- [ ] Have at least 3 case study write-ups
- [ ] Can build a multi-service automation from scratch in under 1 hour
- [ ] Know n8n, Make.com, and Zapier basics
- [ ] Can deploy to cloud
- [ ] Can explain your work confidently in English

---

## 📅 Weekly Schedule Template

Here is a pattern for each day (adjust to your life):

| Time | Activity |
|------|----------|
| 30-45 min | **Learn** — read/watch tutorial, I explain concepts |
| 45-60 min | **Build** — hands-on project work with me |
| 15-20 min | **Document** — commit to GitHub, update learning log |
| 15 min | **Review** — what you learned, what confused you |

**Total: ~2-2.5 hours per day**

Some days you'll do more, some days less. That's fine. Consistency (doing it regularly) matters more than intensity (doing a lot at once).

---

## 🛡️ Safety Rules (Follow These Always)

1. **Never push API keys to GitHub.** Always use `.env` files + `.gitignore`. I will remind you every time.
2. **Never spend money. Period.** Every tool and service in this roadmap is 100% free. If something asks for payment or a credit card, we find a free alternative.
3. **Never let AI take actions without your approval.** Always keep a human-in-the-loop.
4. **Never scrape websites without checking their rules.** We check robots.txt and terms of service first.
5. **Never deploy without security.** No public servers without passwords and firewalls.
6. **Always commit your work to Git.** Small, frequent commits. If your laptop breaks, your work survives on GitHub.
7. **Never share your `.env` file, credentials, or API keys** with anyone or any service you don't trust.
8. **Back up your n8n workflows** by exporting them regularly (you already do this with JSON files — good!).

---

## 📊 Skills You'll Have by Month 6

| Skill | Level |
|-------|-------|
| JavaScript | Intermediate (comfortable writing automation code) |
| Python | Intermediate (can build scripts, scrapers, APIs) |
| n8n | Advanced (your main tool) |
| Make.com | Beginner-Intermediate |
| Zapier | Beginner |
| Git/GitHub | Intermediate |
| APIs/Webhooks | Intermediate-Advanced |
| Databases (SQL) | Beginner-Intermediate |
| Docker/Cloud | Beginner-Intermediate |
| AI Integration | Beginner-Intermediate |
| CI/CD | Beginner |

---

## 🎯 Job Targets

### Upwork (Freelance)
- "n8n automation" gigs — $20-50/hr
- "Zapier/Make automation" gigs — $15-40/hr
- "API integration" projects — $200-1000 per project
- "Workflow automation" consulting — $25-50/hr

### Full-Time Remote
- Junior Automation Engineer — ₹4-8 LPA (India) or $30-50K USD (international remote)
- Junior Integration Specialist
- n8n Developer / Workflow Developer
- Junior DevOps/Automation role

### Where to Find Jobs
- **Upwork** — freelance, start here for first income
- **LinkedIn** — search "automation engineer remote"
- **RemoteOK** — remote jobs board
- **We Work Remotely** — another remote jobs board
- **n8n Community** — people hire n8n specialists there
- **AngelList/Wellfound** — startup jobs
- **Naukri.com** — Indian job board, search "automation"

---

## 💬 English Improvement (Ongoing)

Your English will improve naturally as you:
- Read documentation (docs/manuals for tools)
- Write commit messages and project descriptions
- Communicate with me daily (I'll use simple English and explain hard words)
- Write case studies and proposals

**Tips:**
- Keep a "new words" list — when you see a word you don't know, ask me
- Watch tech YouTube videos with English subtitles (captions at the bottom of the video)
- Practice writing: your learning log is great for this!
- Don't worry about being perfect. Clear communication > perfect grammar (grammar = rules of a language)

---

## 🔥 Remember This

You went from "what's a variable?" to building a 6-API production automation pipeline in 19 days. 

The people who succeed aren't the ones who know the most on Day 1. They're the ones who keep showing up on Day 50, Day 100, Day 150.

You're already showing up. Keep going.

---

*Last updated: May 15, 2026 — Day 19*
*Next review: Day 33 (end of Phase 2)*
