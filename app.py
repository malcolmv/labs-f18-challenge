from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>')
def queryPokemon(query):
	print("https://pokeapi.co/api/v2/pokemon/"+query+"/")
	r = requests.get("https://pokeapi.co/api/v2/pokemon/"+query.lower()+"/")
	if (r.status_code!=200):
		return "PokeAPI request returned status code "+r.status_code
	try:
		float(query)
		return "<h1>The pokemon with id "+query+" is "+r.json()['name'].capitalize()
	except ValueError:
		return "<h1>"+str(query).capitalize()+" has id "+str(r.json()['id'])

if __name__ == '__main__':
    app.run()
