# HTTP & REST — Quick Reference

This document summarizes how clients talk to servers using HTTP and how RESTful APIs are commonly designed. It covers core HTTP concepts, common status codes, examples, REST principles, authentication, and best practices.

## What is HTTP vs REST
- **HTTP**: an application-layer protocol used to transfer resources over the web (requests and responses). It defines methods, headers, status codes, and message formats.
- **REST (Representational State Transfer)**: an architectural style for designing networked applications that uses HTTP semantics (methods, URIs, status codes) to operate on resources. REST is a set of conventions rather than a formal specification.

## Core HTTP Methods
- **GET** — Retrieve a representation of a resource (safe, idempotent).
- **POST** — Create a new resource or submit data (not idempotent by default).
- **PUT** — Replace a resource entirely (idempotent).
- **PATCH** — Partially modify a resource (not necessarily idempotent).
- **DELETE** — Remove a resource (idempotent when repeated deletes have same effect).
- **HEAD** — Like GET but returns only headers (no body).
- **OPTIONS** — Describe communication options for the target resource (CORS preflight uses this).

## Common HTTP Status Codes
- **200 OK** — Request succeeded; response contains representation.
- **201 Created** — Resource successfully created; include `Location` header with new URI.
- **204 No Content** — Success but no body to return (commonly for DELETE or successful PUT/PATCH with no response body).
- **400 Bad Request** — Malformed request or validation error.
- **401 Unauthorized** — Authentication required or invalid credentials.
- **403 Forbidden** — Authenticated but not allowed to perform action.
- **404 Not Found** — Resource or endpoint not found.
- **405 Method Not Allowed** — HTTP method not supported for this resource.
- **409 Conflict** — Resource conflict, e.g., duplicate unique key.
- **415 Unsupported Media Type** — Server refuses to accept the request because the payload format is unsupported.
- **429 Too Many Requests** — Rate limiting.
- **500 Internal Server Error** — Unexpected server-side error.

## Request and Response Structure
- Typical request:

  - Request line: `GET /v1/users?page=2 HTTP/1.1`
  - Headers: `Host`, `Authorization`, `Content-Type`, `Accept`, `User-Agent`, etc.
  - Body: for methods like `POST`, `PUT`, `PATCH` (often JSON).

- Typical response:
  - Status line: `HTTP/1.1 200 OK`
  - Headers: `Content-Type`, `Content-Length`, `Cache-Control`, etc.
  - Body: resource representation (JSON, XML, HTML, binary).

## Common Headers
- `Content-Type` — indicates the media type of the body (e.g., `application/json`).
- `Accept` — media types the client can accept.
- `Authorization` — credentials (e.g., `Bearer <token>`).
- `Cache-Control`, `ETag`, `If-None-Match` — caching.
- `Content-Length` / `Transfer-Encoding` — body size / streaming.

## Example: cURL JSON POST
Example sending JSON to a hypothetical API (uses `Authorization` header):

```bash
curl -X POST https://api.example.com/v1/items \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d '{"name":"sample","quantity":3}'
```

Example with the OpenAI-style snippet (replace model and API key appropriately):

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "input": "Write a short bedtime story about a unicorn."
  }'
```

## REST Design Principles & Conventions
- **Resources**: model your API around nouns (resources), not actions: `/users`, `/orders/123/items`.
- **Use HTTP verbs** to express actions (GET, POST, PUT, DELETE).
- **Stateless**: each request contains all information needed to process it (no server-side session state).
- **Use proper status codes** to indicate the outcome.
- **Hypermedia (HATEOAS)**: optionally include links in responses to related resources.
- **Versioning**: include API versions in the URI or headers, e.g., `/v1/...` or `Accept` header.

## Idempotency and Safe Methods
- **Safe methods** (GET, HEAD) should not change server state.
- **Idempotent methods** (GET, PUT, DELETE) can be repeated with the same effect; POST is generally non-idempotent.
- For non-idempotent operations, provide client support (idempotency keys) if retries are possible.

## Security & Authentication
- Prefer `Authorization: Bearer <token>` (OAuth2/JWT) for APIs.
- Use TLS (HTTPS) for all production traffic.
- Validate and sanitize all inputs; enforce rate limits and quotas.
- For sensitive data return minimal information in errors.

## Error Responses
- Return structured error objects (JSON) with at least `message` and an application `code` where useful. Example:

```json
{
  "error": {
    "code": "invalid_input",
    "message": "Field 'email' is required",
    "details": {
      "field": "email"
    }
  }
}
```

## Best Practices Checklist
- Use nouns for URIs and HTTP verbs for actions.
- Return appropriate status codes and helpful error messages.
- Support pagination, filtering, and sorting for collection endpoints.
- Use consistent date/time formats (ISO 8601).
- Document your API (OpenAPI/Swagger).

## Further Reading
- Roy Fielding's dissertation on REST: https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm
- HTTP/1.1 RFC: https://datatracker.ietf.org/doc/html/rfc7231
- OpenAPI Specification: https://www.openapis.org/

---
Last updated: 2025-12-15
