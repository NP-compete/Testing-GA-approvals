---
title: Deployment Approval Required for {{ env.ENVIRONMENT }}
labels: deployment-requested
---

```json target_payload
{
    "requested_by": "{{ payload.sender.login }}",
    "runNumber":  {{ env.RUN_NUMBER }},
    "environment": "{{ env.ENVIRONMENT }}"
}
```
