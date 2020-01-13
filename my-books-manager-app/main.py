'''
Add new book: curl -X POST http://127.0.0.1:6666/books/add-book -d '{"authors": "J K", "title": "Harry"}' -H 'Content-Type: application/json
Show added books: curl -X GET http://0.0.0.0:6666/books/show-books
Check an added book status: curl -X GET http://0.0.0.0:6666/books/book-status?id=5
Update added book progress: curl -X PUT http://0.0.0.0:6666/books/update-book -d '{"id": "5", "status": "In Progress"}' -H 'Content-Type: application/json'
Delete added book by id: curl -X DELETE http://0.0.0.0:6666/books/delete-book -d '{"id": "1"}' -H 'Content-Type: application/json'
Search book online: curl -X GET http://0.0.0.0:6666/books/search-book-online?title=Harry
'''

from flask import Flask, request, Response
import json
import sqlite3
import db_queries
import requests

DB_PATH = './data.db'
URL = "http://0.0.0.0:5035"

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, BD proj! Wanna read some books?'

@app.route('/books/add-book', methods = ['POST'])
def add_book():
   #Get item from the POST body
   req_data = request.get_json()
   authors = req_data['authors']
   title = req_data['title']

   #Add item to the list
   res_data = db_queries.add_book_to_list(authors, title)

   #Return error if item not added
   if res_data is None:
      response = Response("{'error': 'Book not added'}", status=400 , mimetype='application/json')
      return response

   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')

   return response

@app.route('/books/show-books')
def get_all_books():
   # Get items from the helper
   res_data = db_queries.get_all_books()
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')

   return response

@app.route('/books/book-status', methods=['GET'])
def get_book_status():
   #Get parameter from the URL
   book_id = request.args.get('id')

   # Get items from the helper
   status = db_queries.get_book_status_by_id(book_id)

   #Return 404 if item not found
   if status is None:
      response = Response("{'error': 'Book not found'}", status=404 , mimetype='application/json')
      return response

   #Return status
   res_data = {
      'status': status
   }

   response = Response(json.dumps(res_data), status=200, mimetype='application/json')
   return response

@app.route('/books/update-book', methods = ['PUT'])
def update_book_status():
   #Get item from the POST body
   req_data = request.get_json()
   book_id = req_data['id']
   status = req_data['status']

   #Update item in the list
   res_data = db_queries.update_book_status(book_id, status)
   if res_data is None:
      response = Response("{'error': 'Error updating book'}", status=400 , mimetype='application/json')
      return response

   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')

   return response

@app.route('/books/delete-book', methods = ['DELETE'])
def delete_book():
   #Get item from the POST body
   req_data = request.get_json()
   book_id = req_data['id']

   #Delete item from the list
   res_data = db_queries.delete_book(book_id)
   if res_data is None:
      response = Response("{'error': 'Error deleting book'}", status=400 , mimetype='application/json')
      return response

   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')

   return response

@app.route('/books/search-book-online', methods=['GET'])
def get_search_book_online():
   #Get parameter from the URL
   book_title = request.args.get('title')

   r = requests.get(URL + "/books/" + book_title)
   data = r.text

   print(data)

   return data

if __name__ == "__main__":
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER, authors TEXT NOT NULL, title TEXT NOT NULL, status TEXT NOT NULL, PRIMARY KEY(id));')
        app.run(debug=True, port=6666, host="0.0.0.0")
    except Exception as e:
        print('Error: ', e)
