sudo nginx -c nginx.conf -p nginx || exit 1
mongod 2>&1 > mongo.log &
cd python && gunicorn -w 4 server:server --log-file ../server.log &
echo "Started!"
