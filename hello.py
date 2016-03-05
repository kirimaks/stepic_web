def app(env, make_response):

    results = ""

    for arg in env['QUERY_STRING'].split("&"):
	results += arg + "\n"

    headers = (
        ( "Content-type", "text/plain" ),
    )
    make_response("200 OK", headers)
    return (results)
