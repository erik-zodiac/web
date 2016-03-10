def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [str(i)+"\n" for i in environ['QUERY_STRING'].split("&")]


 
