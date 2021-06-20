from flask import Flask, request, jsonify

app = Flask(__name__)


def _get_every_n_letter(string_to_cut: str, n: int) -> str:
    return string_to_cut[n-1::n]


@app.route('/')
def hello():
    return 'Hi! My name is Isabella (Xiaoxiao) Wang. This is my code sample for my application to Lyft. Thanks!'


@app.route('/test', methods=['POST'])
def test():
    return_data = {
        'return_string': None
    }

    request_data = request.get_json()
    if request_data:
        if 'string_to_cut' in request_data:
            str_to_cut = request_data['string_to_cut']
            return_data['return_string'] = _get_every_n_letter(str_to_cut, n=3)

    resp = jsonify(return_data)
    resp.status_code = 200
    return resp


@app.route('/string-cut', methods=['GET', 'POST'])
def string_cut():
    # handle the POST request
    if request.method == 'POST':
        str_to_cut = request.form.get('string_to_cut')
        str_to_return = _get_every_n_letter(str_to_cut, n=3)
        return '''<h1>The return string containing every 3rd letter is: {}</h1>'''.format(str_to_return)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>String to Cut: <input type="text" name="string_to_cut"></label></div>
               <input type="submit" value="Submit">
           </form>
           '''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
