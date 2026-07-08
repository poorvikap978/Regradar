# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Scripted (rule-based, no live LLM calls) demo data. RegRadar's agent
# "reasoning" steps and the final impact report are pre-written here so the
# demo is fast, reliable, and fully reproducible on stage. The README
# explains what's simulated vs. what a production build would connect to.

CIRCULARS = {
    "esg": {
        "title": "SEBI Circular No. SEBI/HO/CFD/2026/071",
        "subject": "Mandatory Quarterly ESG Disclosure & Scope 3 Emissions Reporting for Top 1000 Listed Companies",
        "summary": "Effective next quarter, top 1000 listed companies by market cap must move from annual to quarterly ESG disclosure, and must additionally report Scope 3 (value chain) emissions alongside existing Scope 1 and Scope 2 reporting.",
        "reasoning_steps": [
            "Parsing circular text and extracting obligations...",
            "Identified 2 key obligations: disclosure frequency change, expanded emissions scope.",
            "Retrieving company policy documents from database...",
            "Found: 'Sustainability Reporting Policy v2.1' (last updated 14 months ago).",
            "Comparing circular obligations against policy clauses...",
        ],
        "company_doc": "Sustainability Reporting Policy v2.1",
        "flags": [
            {
                "clause": "Clause 4.2 \u2014 Disclosure Frequency",
                "current": "\"The Company shall publish its ESG performance report on an annual basis, in line with the Business Responsibility Report.\"",
                "issue": "Circular now mandates quarterly disclosure. This clause is out of date and must be revised before the next reporting cycle.",
                "severity": "High",
            },
            {
                "clause": "Clause 6.1 \u2014 Emissions Scope",
                "current": "\"Reported emissions shall cover Scope 1 (direct) and Scope 2 (indirect energy) sources.\"",
                "issue": "Circular requires Scope 3 (value chain) emissions in addition to Scope 1 & 2. Policy has no provision for Scope 3 data collection.",
                "severity": "High",
            },
            {
                "clause": "Clause 8.4 \u2014 External Assurance",
                "current": "\"External assurance of ESG data is recommended but not mandatory.\"",
                "issue": "No direct conflict, but circular's emphasis on data quality suggests assurance may become mandatory in a future amendment. Flagged for monitoring only.",
                "severity": "Low",
            },
        ],
    },
    "kyc": {
        "title": "SEBI Circular No. SEBI/HO/MIRSD/2026/044",
        "subject": "Enhanced Periodic KYC Refresh Norms for Trading & Demat Accounts",
        "summary": "Brokers and depository participants must now refresh KYC records for high-risk category clients every 12 months (down from 24 months), with mandatory video-based in-person verification for refreshes.",
        "reasoning_steps": [
            "Parsing circular text and extracting obligations...",
            "Identified 2 key obligations: refresh frequency change, new verification method requirement.",
            "Retrieving company policy documents from database...",
            "Found: 'Client Onboarding & KYC Policy v3.0' (last updated 20 months ago).",
            "Comparing circular obligations against policy clauses...",
        ],
        "company_doc": "Client Onboarding & KYC Policy v3.0",
        "flags": [
            {
                "clause": "Clause 3.5 \u2014 KYC Refresh Cycle",
                "current": "\"High-risk category clients shall undergo KYC refresh once every 24 months.\"",
                "issue": "Circular reduces this to 12 months for high-risk clients. Policy timeline is now non-compliant and must be halved.",
                "severity": "High",
            },
            {
                "clause": "Clause 5.2 \u2014 Verification Method",
                "current": "\"Refresh verification may be conducted via physical document submission or digital upload.\"",
                "issue": "Circular mandates video-based in-person verification (V-IPV) for refreshes. Current policy does not reference V-IPV at all.",
                "severity": "High",
            },
        ],
    },
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/circulars")
def list_circulars():
    return jsonify([
        {"id": key, "title": val["title"], "subject": val["subject"]}
        for key, val in CIRCULARS.items()
    ])


@app.route("/api/analyze/<circular_id>")
def analyze(circular_id):
    data = CIRCULARS.get(circular_id)
    if not data:
        return jsonify({"error": "not found"}), 404
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
