import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    conn = None
    results = []

    try:
        # Connect to the DB
        conn = psycopg2.connect("dbname='task_manager'")
        # Define a cursor
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # Execute the SQL
        cur.execute(sql, values)
        # Commit
        conn.commit()
        # Fetch the results
        results = cur.fetchall()
        # Close the connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        # Print an error
        print(error)
    finally:
        # Close the connection
        if conn is not None:
            conn.close()
    # Return results
    return results