import pyshark
from openai import OpenAI

client = OpenAI()

def analyze_pcap(file_path):
    capture = pyshark.FileCapture(file_path, only_summaries=True)

    packets = []
    count = 0

    for packet in capture:
        packets.append(f"{packet.source} → {packet.destination} | {packet.protocol} | {packet.info}")
        count += 1

        if count >= 50:
            break

    capture.close()

    summary = "\n".join(packets)

    prompt = f"""
You are a senior network engineer performing packet-level troubleshooting.

Your task is to analyze packet capture data and produce a precise, evidence-based diagnosis.

=====================
ANALYSIS OBJECTIVES
=====================
1. Identify anomalies in traffic patterns
2. Detect protocol-level issues (TCP, DNS, HTTP, etc.)
3. Infer possible root causes
4. Provide actionable recommendations

=====================
STRICT INSTRUCTIONS
=====================
- Do NOT give generic answers
- Base every conclusion on observable evidence
- If unsure, state "insufficient data"
- Prefer deterministic reasoning over speculation

=====================
DATA SAMPLE
=====================
{summary}

=====================
OUTPUT FORMAT (MANDATORY)
=====================

1. EXECUTIVE SUMMARY
- 2–3 lines describing the main issue

2. DETECTED ANOMALIES
- Bullet list
- Include evidence (e.g., repeated SYN, DNS retries, etc.)

3. PROTOCOL-LEVEL ANALYSIS
- TCP:
- DNS:
- Other protocols:

4. ROOT CAUSE HYPOTHESIS
- Most likely cause
- Why (based on evidence)

5. CONFIDENCE LEVEL
- High / Medium / Low
- Justify briefly

6. RECOMMENDED ACTIONS
- конкрет steps (e.g., check firewall, MTU, routing)

7. ADDITIONAL DATA NEEDED
- What would improve accuracy (if needed)
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
