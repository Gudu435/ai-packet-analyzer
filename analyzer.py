import subprocess
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_pcap(file_path):
    try:
        # Run tshark directly (stable)
        result = subprocess.run(
            ["tshark", "-r", file_path, "-c", "50"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if not output:
            return "No packet data extracted."

        prompt = f"""
You are a senior network engineer.

Analyze this packet capture output and identify issues.

DATA:
{output}

Give:
1. Summary
2. Issues
3. Root cause
4. Recommendations
"""

        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error: {str(e)}"
