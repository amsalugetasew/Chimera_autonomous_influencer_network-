# Chimera Agent Skills

## skill_fetch_trends
Input: { "platform": "string", "region": "string" }
Output: { "trends": [] }

## skill_generate_content
Input: { "trend": "string" }
Output: { "script": "string" }

## skill_publish_content
Input: { "content_id": "string" }
Output: { "status": "published" }

# Agent Skills

## Skill 1: skill_download_youtube
- Input: {"url": "string"}
- Output: {"file_path": "string"}

## Skill 2: skill_transcribe_audio
- Input: {"file_path": "string"}
- Output: {"text": "string"}

## Skill 3: skill_fetch_trends
- Input: {"platform": "string", "category": "string"}
- Output: {"trends": [{"title": "string", "url": "string", "score": "float"}]}
