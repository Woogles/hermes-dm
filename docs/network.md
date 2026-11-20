Docker Network

Network Name:
hermes-net

Services:

- hermes-postgres
- hermes-qdrant
- hermes-api
- hermes-dashboard
- hermes-whisper
- hermes-kokoro

Rules:

- Services communicate using container names.
- Avoid hardcoded IP addresses.
- External access only through published ports.