from flask import Flask
import networkx as nx
import random

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return "Hello, World from flask server!"

@app.route('/wiki/randomNodes', methods=['GET'])
def get_randomNodes():
    g = nx.read_edgelist("D:\Python\docker_notebooks\notebooks\afleveringer\Week9/Wiki-Vote.txt")
    def randomNumber(n):
        return random.choice(list(g.nodes()))
    g[randomNumber(g)]
    return "Node: " + str(randomNumber(g)) + " neighbors: " + str(g[randomNumber(g)])

if __name__ == '__main__':
    app.run(debug=True)