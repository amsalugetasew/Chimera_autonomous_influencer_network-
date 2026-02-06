# OpenClaw & Moltbook Integration Specification

## Purpose
Define how Project Chimera agents participate in an Agent Social Network.

---

## 1. Supported Social Protocols

### 1.1 Agent Discovery
- Agents must query a skill registry.
- Discovery responses include:
  - Agent ID
  - Skill list
  - Reputation score

### 1.2 Messaging & Streams
- Agents publish async updates to topic streams.
- Streams are append-only and timestamped.

### 1.3 Task Delegation
- Planner agents assign tasks to Workers.
- Tasks include:
  - Objective
  - Required skills
  - Deadline

### 1.4 Validation & Feedback
- Workers submit outputs to Judges.
- Judges may:
  - Approve
  - Reject
  - Request revision

### 1.5 Reputation & Trust
- Reputation scores update based on:
  - Completion rate
  - Validation success
  - Security violations

### 1.6 Security & Authentication
- All agent messages must be signed.
- ACLs control access to streams and skills.

---

## 2. Human-in-the-Loop Enforcement

- Mandatory HITL for:
  - Publishing content
  - Financial actions
  - External communications

---

## 3. Non-Goals

- Real-time chat
- Self-modifying agents without review
