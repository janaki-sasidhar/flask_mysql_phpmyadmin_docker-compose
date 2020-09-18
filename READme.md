## If needed to use without docker compose , we need to create a network manually.

>sudo docker volume create mariadbtestvolume
>sudo docker network create mariadbnetwork

### This creates a network and volume. (here we are not dockerizing flask app, we are using docker mysql and phpmyadmin only)

## The below commands create a mariadb and phpmyadmin containers and runs them , they share the mariadbnetwork.

```sh
> sudo docker run -d \
 --name mariadbtest \
-e MYSQL_ROOT_PASSWORD=password \
-v mariadbtestvolume:/var/lib/mysql  \ 
-p 30021:3306  \ 
--network mariadbnetwork mariadb:latest
```

```sh
> sudo docker run -d \
--name mariadbadmin \ 
--network mariadbnetwork \
 -e MYSQL_ROOT_PASSWORD=password \ 
-e PMA_HOST=mariadbtest  \
-e  PMA_USER=root \
-e  PMA_PASSWORD=password \
 -p 8080:80 phpmyadmin:latest
```

## The only extra configuration is a config variable for mysql connect url  in flask app. 

> SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:password@localhost:30021/flask_blog'

> Remember  , we used port 30021:3306 while running docker mysql container

> Now you need to initiate a database table manually using flask.

```sh
	from flask_blog import db
	from flask_blog.models import Profile
	db.create_all()
	profile = Profile(name="testname" , email="testemail" , country = "yourcountry" , hobbies = "your hobbies")
	db.session.add(profile)
	db.session.commit()
```


# If you want to use docker-compose, look at the docker compose file. 
