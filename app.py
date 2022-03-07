from bottle import Bottle, run,response, request

app = Bottle()

@app.route('/echo/<text>')
def echo(text):
    return {"Your Path Param":text}

@app.route('/queries')
def query():
    q = request.query_string
    if q:
        return {"You queried":q}
    else:
        response.status = 400
        return "Please supply a query string"


if __name__ == "__main__":
    app.run(host='localhost', port=8080)