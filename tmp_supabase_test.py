from urllib.parse import urlparse, urlunparse
raw = 'https://mcp.supabase.com/mcp?project_ref=cyhcrgumjmjzwmzyncha'
parsed = urlparse(raw)
print('raw=', raw)
print('scheme=', parsed.scheme)
print('netloc=', parsed.netloc)
print('path=', parsed.path)
print('query=', parsed.query)
print('candidate1=', raw)
print('candidate2=', urlunparse((parsed.scheme, parsed.netloc, '', '', '', '')))
print('candidate3=', urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', '')))
