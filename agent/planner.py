import json
import os
from groq import Groq

client = Groq(api_key="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")


def plan_step(observation, failures):
    prompt = f"""
You are a DevOps agent.

Goal: resolve system issue.

Available tools:
- get_logs
- restart_service
- install_dependency
- fix_env
- fix_config

Rules:
- Avoid repeating failed actions unless context changed
- Base decisions only on logs

Failures:
{failures}

Context:
{json.dumps(observation)[:2000]}

Return JSON:
{{"action": "...", "reason": "..."}}
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_completion_tokens=512,
    )

    out = completion.choices[0].message.content

    try:
        return json.loads(out)
    except:
        return {"action": "get_logs", "reason": "fallback"}
