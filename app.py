from flask import Flask, make_response, request, render_template
from weather import Weather
import json


file = 'database'
app = Flask(__name__)

@app.route('/')
def list_page():
    return render_template('list_cities.html')

@app.route('/city/add')
def create_page():
	return render_template('create_city.html')

@app.route('/view/<city_id>')
def view_page(city_id):
	return render_template('view_city.html', city_id = city_id)
   
@app.route('/city/<int:city_id>')
def city(city_id):
	content_file = []
	with open(file) as json_file:
		content_file = json.load(json_file)

	for content in content_file:
		if content['key'] == city_id:
			""" get the list forecast in the external api"""
			external = Weather()
			forecast = external.getForcast(content['name'], content['country_code'])
			return output_json({"city_id": city_id, "name": content['name'], "country_code" : content['country_code'], "forecast": forecast}, 200)

	return output_json({"error" : "INVALID_KEY"}, 400)

@app.route('/create', methods=['POST'])
def create_city():
	try:
		city  = request.get_json()

		validate = validade_city(city['name'], city['country_code'])
		if validate == False:
			return output_json({"success" : "False"}, 400)

		content_file = []
		with open(file) as json_file:
			content_file = json.load(json_file)
		
		city_dict = {}
		city_dict['key'] = len(content_file) + 1
		city_dict['name'] = city['name']
		city_dict['country_code'] = city['country_code']
		content_file.append(city_dict)

		with open(file, 'w') as outfile:  
			json.dump(content_file, outfile)

		return output_json({"success" : "True"}, 200)
	except:
		return output_json({"success" : "False"}, 500)

@app.route("/cities")
def list_cities():
	content_file = []
	with open(file) as json_file:
		content_file = json.load(json_file)
		return output_json(content_file, 200)


def validade_city(city_name, country_code):
	external = Weather()
	response = external.validate_city(city_name, country_code)
	return response

def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)