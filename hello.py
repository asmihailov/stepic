def app(environ, start_response):
	body = [str(i + '\n') for i in environ['QUERY_STRING'].split('&')]
#	body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]	
#	body = ''
#	begin = environ['QUERY_STRING'].find('?')
#	for i in environ['QUERY_STRING'][begin:].split('&'):
#		body += str(i) + '\n'
	status = '200 OK'
	headers = [('Content-Type','text/plain')]
	
	start_response(status, headers)

	return [body]

