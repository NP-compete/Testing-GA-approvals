---
title: Deployment Approval Required for {{ env.ENVIRONMENT }}
labels: deployment-requested
---

Deployment Approval requested from {{ payload.sender.login }}.

Comment "Approved" to kick the deployment off.

```json target_payload
{
    "runNumber":  {{ env.RUN_NUMBER }},
    "environment": "{{ env.ENVIRONMENT }}"
}
```
