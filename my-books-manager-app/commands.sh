URL=192.168.99.100:31178

case "$1" in
	show)
		curl -X GET http://$URL/books/show-books
		echo
		;;
	add)
		curl -X POST http://$URL/books/add-book -d '{"authors": "'"$2"'", "title": "'"$3"'"}' -H 'Content-Type: application/json'
		echo
		;;
	update)
		curl -X PUT http://$URL/books/update-book -d '{"id": "'"$2"'", "status": "'"$3"'"}' -H 'Content-Type: application/json'
		echo
		;;
	status)
		curl -X GET http://$URL/books/book-status?id=$2
		echo
		;;
	delete)
		curl -X DELETE http://$URL/books/delete-book -d '{"id": "'"$2"'"}' -H 'Content-Type: application/json'
		echo
		;;
	search)
		curl -X GET http://$URL/books/search-book-online?title=$2
		echo
		;;
	*)
		echo "Usage: $0 {show|add|update|delete|status|search}"
		exit 1 
esac
