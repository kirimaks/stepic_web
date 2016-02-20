def app(env, make_response):

    #qs = env['QUERY_STRING']
	
    #results = str(type(qs.split("&")))

    results = ""

    for arg in env['QUERY_STRING'].split("&"):
	results += arg + "\n"

    headers = (
        ( "Content-type", "text/plain" ),
    )
    make_response("200 OK", headers)
    return (results)
