from django.db import connection

def a():
    cursor = connection.cursor()
    cursor.execute('DROP TABLE "blogs_post_new"')
    
def b():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE "blogs_post_new" ( \
                      "id"          integer NOT NULL PRIMARY KEY, \
                      "title"       varchar(50) NOT NULL, \
                      "image_url"   varchar(100) NOT NULL, \
                      "keywords"    varchar(50) NOT NULL, \
                      "category_id" integer NOT NULL REFERENCES "blogs_category" ("id"), \
                      "short_desc"  varchar(100) NOT NULL, \
                      "long_desc"   varchar(400) NOT NULL, \
                      "author"      varchar(50) NOT NULL, \
                      "pub_date"    datetime NOT NULL, \
                      "post"        text NOT NULL)')    
def c():
    cursor = connection.cursor()    
    cursor.execute('INSERT INTO "blogs_post_new" \
                      ( "title", \
                        "image_url", \
                        "keywords",  \
                        "category_id", \
                        "short_desc", \
                        "long_desc", \
                        "author",  \
                        "pub_date",  \
                        "post") \
                      SELECT  NULL, \
                              "p.title", \
                              "p.image_url", \
                              "p.keywords", \
                              "c.id", \
                              "p.short_desc", \
                              "p.long_desc", \
                              "p.author", \
                              "p.pub_date", \
                              "p.post" \
                        FROM "blogs_post" p, \
                             "blogs_category" c \
                       WHERE "c.category_type" = "p.category_type"')

def d():
    cursor = connection.cursor()
    cursor.execute('DROP TABLE "blogs_post"')
    
def e():
    cursor = connection.cursor()
    cursor.execute('ALTER TABLE "blogs_post_new" RENAME TO "blogs_post"')

