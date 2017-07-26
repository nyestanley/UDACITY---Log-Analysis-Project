# UDACITY--Log-Analysis-Project"

This a reporting tool that prints out reports based on the data in the 'news' database.


The 'news' database has three tables:
Author table contains author's name, author's unique id (that can be referned in the articles table) and bio info.

Articles table contains author id, article's title, article's lead paragraph, article's slugline (referenced in the the log table), content of the article, time article was created and article unique id.

Log table contains path that was entered at time of request, ip address of article, method of request, status code of request, time article was selected and unique id of request

The Pythogn program will report:
1. The most popular three articles of all time
2. The most popular authors of all time listed in descending order by sum of total views of all author's articles
3. Days where 1% of all requests lead to error

To start on this project, you'll need to:
1. Install vagrant
2. Download virtual configuration for vagrant at: https://github.com/udacity/fullstack-nanodegree-vm
3. Start virtual machine and log in: vagrant up, vagrant ssh
4. To run the database use 'psql' command in terminal
5. Download database data at: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5. Import newdata.sql by using command: psql -d news -f newsdata.sql
 
To run program use command: python3 loganalysis.py

This program use views. To create run command in postgres database:
create view v_author_articles as select authors.name, articles.title, articles.slug from authors left join articles on articles.author=authors.id ordy authors.name asc;