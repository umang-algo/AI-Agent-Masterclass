#!/bin/bash
# Instead of writing complex LangChain routing code, you just POST data payload to your n8n visual AI agent:

curl -X POST https://your-n8n-instance.com/webhook/support-ticket \
     -H "Content-Type: application/json" \
     -d '{
           "ticket_id": "TCK-9902",
           "customer_email": "angry_client@example.com",
           "message": "Your app crashed again during my presentation! Unacceptable."
         }'
