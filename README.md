# Regradar
RegRadar — Agentic AI compliance system that monitors SEBI circulars and flags exactly which internal policy clauses are now non-compliant. Built for SEBI Securities Market TechSprint (HackCulture) | Agentic Compliance from Regulatory
# RegRadar — Demo Prototype

A scripted (rule-based, no live LLM calls) demo of the RegRadar agentic AI
compliance system, built for the SEBI Securities Market TechSprint
(HackCulture) — Agentic Compliance from Regulatory problem statement.

This demo simulates the core interaction pattern: pick a sample SEBI
circular, watch the agent "reason" through parsing it and retrieving the
company's policy documents, then see a generated compliance impact report
that flags exactly which internal clauses are now non-compliant.

## Setup (2 minutes)

1. Make sure Python 3.9+ is installed.
2. Open a terminal in this folder and install Flask:
   ```
   pip install flask
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser to: **http://127.0.0.1:5001**

(Note: this runs on port 5001, not 5000, so it won't clash if DigiSakhi is
also running on your machine.)

## How to demo it

1. Pick one of the two sample circulars (ESG Disclosure or KYC Refresh).
2. Click **"Run RegRadar Agent"**.
3. Watch the reasoning steps appear one by one (parsing → retrieving
   policies → comparing clauses).
4. The compliance impact report appears below, showing exactly which
   policy clauses are flagged, why, and how severe the gap is.
5. Use **"↻ Restart Demo"** to reset and record again.

## Recording your demo video

- Use screen recording (Mac: `Cmd+Shift+5`, Windows: `Win+G`).
- Keep it to 60–90 seconds: pick a circular → run the agent → let the
  reasoning steps play out → scroll through the impact report.
- Optionally add a voiceover explaining what's scripted vs. what a full
  build would connect to.

## What's real vs. simulated

| Part | This demo | Full production version |
|---|---|---|
| Circular parsing | Pre-written sample data | LLM + RAG parsing live SEBI circulars |
| Policy comparison | Scripted flag list | Real clause-by-clause LLM comparison |
| Regulatory monitoring | Manual selection from 2 samples | Continuous automated circular ingestion |
| Data storage | None | PostgreSQL for regulations, policies & history |
| Audit trail | Not included | Timestamped compliance action log |

This is intentional — a "Wizard of Oz" prototype that demonstrates the
interaction pattern and UX clearly within hackathon time constraints, while
the pitch deck carries the full technical vision.

## Project structure

```
regradar/
├── app.py              # Flask backend (routes + scripted circular/report data)
├── templates/
│   └── index.html      # Dashboard UI markup
├── static/
│   ├── style.css        # Styling (matches pitch deck slate/amber palette)
│   └── app.js           # Demo flow logic
└── README.md
```
