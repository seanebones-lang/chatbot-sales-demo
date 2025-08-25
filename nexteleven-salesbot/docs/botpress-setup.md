## Botpress setup (free options)

### Option A: Botpress Cloud (free tier) — recommended
1) Create account and workspace
   - Go to `https://botpress.com` and sign up.
   - Create a workspace and click "+ New bot" (name it "SevenTwelve SalesBot").

2) Build in Studio
   - Open the bot in Studio. Add a Knowledge Base and upload the files from `knowledge/`.
   - Create Workflows: import or build flows mirroring `flows/` files (Main, Pricing, Capabilities, Lead Capture).

3) Test
   - Use the Emulator inside Studio to test greetings, pricing Q&A, and lead capture.

4) Deploy and embed
   - Open the Deploy tab, enable the Web Chat channel, and copy the embed snippet.
   - Follow `embed/instructions.md` to add it to your website.

Notes
- Cloud free tier typically includes generous limits suitable for demos and early pilots.
- No local install required; versioning is managed by Botpress Cloud.

### Option B: Self-hosted / Community (advanced)
Prereqs: Docker or Node.js LTS, and a Postgres database for production.

1) Run with Docker (example)
```bash
docker run -p 3000:3000 -e BP_PRODUCTION=true botpress/server:latest
```
Then open `http://localhost:3000` and create a workspace/bot.

2) Local development tips
- Keep content in `knowledge/` and replicate flows from `flows/`.
- Use environment variables from `config/env.sample`.

### Connecting knowledge
- Upload documents: `knowledge/company.md`, `services.md`, `pricing.md`, `industries.md`, `offers.md`, `faqs.md`.
- Use chunking defaults, enable citations, and restrict to "Use Knowledge Only" for accurate pricing answers.

### Initial guardrails
- Add a System Instruction: "You are SevenTwelve SalesBot. Be concise and helpful."
- Add a list of disallowed topics (unrelated or medical/legal advice) and redirect to contact.

