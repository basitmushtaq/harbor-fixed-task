Parse the Apache-style access log at `/app/access.log` and write a JSON
summary to `/app/report.json`.

Success criteria:
1. `/app/report.json` exists and is valid JSON.
2. `total_requests` is the total number of log lines.
3. `unique_ips` is the count of distinct client IP addresses.
4. `top_path` is the path string with the most requests.