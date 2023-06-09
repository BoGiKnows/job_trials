import psycopg2

from config import config


def first_task():
    conn = None
    query = """
        SELECT
        article.id,
        article.title,
        article.text
    FROM article
    LEFT JOIN comment
        ON article.id = comment.article_id
    WHERE comment.article_id IS NULL
    """
    res = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            conn.close()

    return res


if __name__ == '__main__':
    result = first_task()
    print(result)