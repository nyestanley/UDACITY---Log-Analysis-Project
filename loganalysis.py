##!/usr/bin/env python3
import psycopg2
import datetime

# Database Connection
databaseName = "news"

print("Niesha Stanley - LOGS ANALYSIS PROJECT")
print("--------------------------------------\n")

db = psycopg2.connect(database=databaseName)

# Print three most popular articles of all time
c = db.cursor()
c.execute("select articles.title, count(log.time) as hits from articles,log" +
          " where log.path =  ('/article/' || articles.slug) and " +
          " log.path!='/' group by articles.title order by hits desc limit 3;")

print("Most popular three articles of all time:")
for title, hits in c.fetchall():
    print(title + " - " + str(hits) + " views")


# most populart article authors of all time
# Make sure view v_author_articles has been created
c.execute("select AA.name, count(log.time) from log, v_author_articles as AA" +
          " where log.path = ('/article/' || AA.slug) group by AA.name " +
          "order by count desc;")
print("\nMost popular article authors of all time:")

for authorName, views in c.fetchall():
    print(authorName + " - " + str(views) + " views")

# On which days did more than 1% of requests lead to errors
c.execute("select to_char(views.date, 'FMMonth, DD YYYY'), " +
          "trunc((round(numOfErrors,1)/round(viewsPerDay,1))*100,2) " +
          "as percentageOfErrors from " +
          "(select errors.date, errors.numOfErrors, count(time) " +
          "as viewsPerDay from " +
          "(select date_trunc('day', time) as date, count(status) " +
          "as numOfErrors from log where status like '4%' " +
          "group by date order by date asc) " +
          "as errors left join log on errors.date=date_trunc('day', time) " +
          "group by errors.date, errors.numOfErrors) as views where " +
          "trunc((round(numOfErrors,1)/round(viewsPerDay,1))*100,2) > 1.0 " +
          "order by percentageOfErrors desc;")
print("\nOn which days did more than 1% of requests lead to errors?")

for date, successfulStatus in c.fetchall():
    print(str(date) + " - " + str(successfulStatus) + "% errors\n")

db.close()
