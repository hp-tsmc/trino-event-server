# Trino Event Listener Implementation

### How to run

```
# Dev Test
python server.py

# Production
# gunicorn --workers=<整數> --threads=<整數> <wsgi檔名>:<app名稱> 
gunicorn --workers=4 --threads=4 wsgi:app
```# trino-event-server
