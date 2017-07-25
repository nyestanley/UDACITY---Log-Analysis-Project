# UDACITY--Log-Analysis-Project"

To run: python3 loganalysis.py

This program use views. To create run command in postgres database:
create view v_author_articles as select authors.name, articles.title from authors left join articles on articles.author=authors.id order by authors.name asc;