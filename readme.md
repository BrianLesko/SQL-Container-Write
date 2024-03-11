
# SQL Server Container

Hosts a mySQL server within a container, which can be spun up and shut down quickly, avoiding polluting the host machine. The container starts automatically when the python script is run, but it does not shut down automatically. 

Written for learning purposes. By Brian Lesko.

&nbsp;

## Dependencies

You must install docker either through the docker desktop app on Mac and Windows or through the Docker Engine which is built for Linux environments

Next, you must retreive or create the image for the SQL server, Docker has a good image retreivable with 
```
docker pull mysql 
```

or you can create a dockerfile and modify the mysql image. 

## Run the image Manually

The, the image can be run with 
```
docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql
```
where the tags, or the modifiers to the run command are as follows:
--name mysql-server gives your container a name.
-e MYSQL_ROOT_PASSWORD=my-secret-pw sets the root password (replace my-secret-pw with your desired password).
-p 3306:3306 maps port 3306 on your host to port 3306 in the container.
-d runs the container in detached mode. # meaning the terminal is not blocked, its a background container
mysql is the image you're using.

the Server can then be accessed using: mysql -h 127.0.0.1 -P 3306 -u root -p

To stop the MySQL container, use: docker stop mysql-server.
To start it again, use: docker start mysql-server.

## Run the image and client with this repository web client

1. install the python dependencies, use a virtual env

This code uses the following libraries:
- `streamlit`: for building the user interface and HTML web app 
- `pymysql`: for interacting with the DB
- `cryptography`: needed for SQL authentication

2. Install Docker and the docker engine

3. Create the docker image from the dockerfile or with docker pull according to the manual instructions above

4. run the streamlit app
```
streamlit run app.py
```

5. Use a web browser to open the client at 
```
localhost:8501
```

&nbsp;

<hr>

&nbsp;

<div align="center">



╭━━╮╭━━━┳━━┳━━━┳━╮╱╭╮        ╭╮╱╱╭━━━┳━━━┳╮╭━┳━━━╮
┃╭╮┃┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃        ┃┃╱╱┃╭━━┫╭━╮┃┃┃╭┫╭━╮┃
┃╰╯╰┫╰━╯┃┃┃┃┃╱┃┃╭╮╰╯┃        ┃┃╱╱┃╰━━┫╰━━┫╰╯╯┃┃╱┃┃
┃╭━╮┃╭╮╭╯┃┃┃╰━╯┃┃╰╮┃┃        ┃┃╱╭┫╭━━┻━━╮┃╭╮┃┃┃╱┃┃
┃╰━╯┃┃┃╰┳┫┣┫╭━╮┃┃╱┃┃┃        ┃╰━╯┃╰━━┫╰━╯┃┃┃╰┫╰━╯┃
╰━━━┻╯╰━┻━━┻╯╱╰┻╯╱╰━╯        ╰━━━┻━━━┻━━━┻╯╰━┻━━━╯
  


&nbsp;


<a href="https://twitter.com/BrianJosephLeko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/x-logo-white.svg" width="30" alt="X Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://github.com/BrianLesko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/github-mark-white.svg" width="30" alt="GitHub"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://www.linkedin.com/in/brianlesko/"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/linkedin-icon-white.svg" width="30" alt="LinkedIn"></a>

follow all of these for pizza :)

</div>


&nbsp;


