# hello.py

def handler(request, response):
    response.status_code = 200
    response.headers['Content-Type'] = 'text/plain'
    response.set_body('Hello from Vercel Python!')
