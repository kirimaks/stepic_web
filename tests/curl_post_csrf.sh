csrf_token="vdb7DGfUfacMLe2e4jQjp01UZKcoDkJa"
curl -vv -X POST\
	--data "title=bugaga&text=sometext&csrfmiddlewaretoken=${csrf_token}"\
	--cookie "csrftoken=${csrf_token}"\
	localhost/ask/
