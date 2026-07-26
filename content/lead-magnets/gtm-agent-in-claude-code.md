# How to Build a GTM Agent in Claude Code (for your own LinkedIn)

Hey, thanks for commenting on the post. Here is the actual build, the same setup I run for myself. Nothing held back. If you have Claude Code and an API key, you can have this working in an afternoon.

Quick promise before we start. This is not "AI writes your posts." It is a small team of agents that researches, writes, and scores a post before you approve it. The difference is the research, the memory, and the quality gate. That is what makes it a GTM agent instead of a prompt.

Here is the whole thing, in the same five parts from the post.

## What you need first
- Claude Code installed.
- An API key. This runs for about the cost of a coffee habit, not a 2,000 dollar content tool.
- One folder on your computer for the project. Everything lives there.

## Step 1: The inputs (connect your MCP tools)
MCP is how Claude Code plugs into outside tools. You need two.

1. Apify, so the agent can read your own LinkedIn. It scrapes your profile and your recent posts, which tells the agent what is actually landing and what is flopping. You add it as an MCP server in Claude Code and give it your Apify token.
2. A web research tool (web search or a browser tool), so the agent can pull the current LinkedIn algorithm rules and this week's trending angles instead of guessing from old training data.

That is the agent's eyes. Now it can see your account and the outside world.

## Step 2: The brain (build a small knowledge base)
Make a folder called knowledge-base and put a few plain markdown files in it. This is what the agents read before they write a single word.

- your-voice.md: how you actually talk. Paste three to five of your best messages or posts so it copies your rhythm, not a robot's.
- your-offer.md: who you help, the problem you solve, and how people work with you.
- algorithm.md: the current rules that matter, what the platform rewards and what it punishes right now.
- angles.md: a running list of post ideas you can pull from.

Keep these short and honest. The agents are only as good as this folder.

## Step 3: The team (five sub-agents, one job each)
In Claude Code you can create sub-agents. Make five, and give each one a single job. One job per agent is the whole trick. It keeps them sharp.

1. Strategist: picks the angle for today and the keywords that tell the algorithm what the post is about.
2. Hook writer: writes three opening lines and keeps the strongest one.
3. Post writer: turns the hook into the full post, in your voice, using a real story or a real number.
4. CTA writer: writes the close and the first comment.
5. QA scorer: grades the draft out of 100 against your algorithm.md, blocks anything weak, and tells you how to fix it.

Every agent reads the knowledge base from Step 2, so they all stay on brand.

## Step 4: The one command
Create a slash command that runs the five agents in order. You type one thing, for example /post with your topic, and it goes strategist, then hook, then post, then CTA, then QA. Out the other end comes a finished draft with a score. No more staring at a blank page.

## Step 5: The guardrail (this part stays human)
The agent drafts. You approve. Always. I never let it hit publish on its own, and I tell every client the same thing about their sales agents. An agent that is confident and wrong is worse than no agent. You reading the draft before it goes out is the guardrail, and the guardrail is the product.

## That is the whole thing
Inputs, a brain, a team of five, one command, and a human at the end. Build it once and posting stops being the hard part.

If you get stuck on any step, reply to me and I will point you at the fix. And if you would rather I build a GTM agent for your business instead of your feed, the kind that answers leads and books calls, that is the day job. Just say the word.
