from log_parser import parse_ssh_log, parse_http_log

# Test SSH
print("--- Analyse SSH ---")
ssh_data = parse_ssh_log('auth.log')
for entry in ssh_data:
    print(entry)

# Test HTTP
print("\n--- Analyse HTTP ---")
http_data = parse_http_log('access.log')
for entry in http_data:
    print(entry)
