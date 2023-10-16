# RESTful API with Flask and MongoDB

## Installation
1. Clone the repo:
```bash
git clone https://github.com/codingoleg/RESTful_API_Flask_MongoDB.git
```
2. Change directory:
```bash
cd .\RESTful_API_Flask_MongoDB\
```
+ Edit Dockerfile and docker-compose.yml if needed.
+ Run docker-compose.
```bash
docker-compose up
```

## Usage
Available routes:
1. http://127.0.0.1:5000/create [POST]\
Creates one document (saves both body и headers). Returns document hash and MongoDB id value. 
Key order doesn't matter - the hash will be the same. 
2. http://127.0.0.1:5000/read [GET]. Arguments: ["h", "id"]\
Reads one or multiple documents by hash ("h") or one document by id ("id").
3. http://127.0.0.1:5000/update [PUT]. Arguments: ["h", "id"]\
Updates one or multiple documents by hash ("h") or one document by id ("id").
4. http://127.0.0.1:5000/delete [DELETE]. Arguments: ["h", "id"]\
Deletes one or multiple documents by hash ("h") or one document by id ("id").

## License
GNU GPLv3 