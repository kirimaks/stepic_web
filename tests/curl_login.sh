csrf_token="vdb7DGfUfacMLe2e4jQjp01UZKcoDkJa"
curl -vv -X POST\
	--data "username=kirimaks&password=1234&csrfmiddlewaretoken=${csrf_token}"\
	--cookie "csrftoken=${csrf_token}"\
	localhost/login/
