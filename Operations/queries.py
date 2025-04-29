from typing import get_type_hints
from Database import connection
from Schema import schema
from contacts import Contact

def create_and_insert(table_type, **kwargs):
    """
    Create table (if not exists) and insert a record into it.

    Args:
    table_type: 'address_book' or 'contact'
    **kwargs: Data to insert
    """
    conn = connection.connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    try:
        create_query = schema.TableSchema.generate_create_query(table_type)
        cursor.execute(create_query)

        insert_query, insert_columns = schema.TableSchema.generate_insert_query(table_type)
        values = tuple(kwargs[col] for col in insert_columns)
        cursor.execute(insert_query,values)
        print(f"{table_type.capitalize()} record inserted.")
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

def get_all_address_books():
    """
    Funtion to get all address books that exist in database
    """
    conn = connection.connect_db()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = "SELECT name from AddressBooks"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in result]

def get_address_book_id(name):
    """
    Function to get the id of address book by name
    """
    conn = connection.connect_db()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = "SELECT id FROM AddressBooks WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0] 
    return None

def get_contacts(name):
    """
    Function to to get all contacts from a specific address book"""
    conn = connection.connect_db()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = schema.TableSchema.generate_select_query(table_key='contact')
    cursor.execute(query, (name,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    columns = list(get_type_hints(schema.ContactSchema).keys())
    return [Contact(**dict(zip(columns, row))) for row in result]

def get_contact_id(first_name,last_name):
    """
    Function to get id of contacts by name
    """
    conn = connection.connect_db()
    if conn is None:
        return False

    cursor = conn.cursor()
    query = "SELECT id FROM Contacts WHERE first_name = %s and last_name = %s"
    cursor.execute(query,(first_name,last_name))
    id = cursor.fetchone()
    cursor.close()
    conn.close()
    if id:
        return id[0]  
    return None
        
def delete_from_table(table_type,**kwargs):
    """
    Function to delete address book or contacts
    """
    conn = connection.connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    try:
        delete_query = schema.TableSchema.generate_delete_query(table_type)
        if table_type == 'contact':
            cursor.execute(delete_query,(kwargs['id'],))
        elif table_type == 'address_book':
            cursor.execute(delete_query,(kwargs['name'],))

        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

def edit_contacts(**kwargs):
    """
    Function to edit contacts
    """
    conn = connection.connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    id = get_contact_id(kwargs["first_name"],kwargs["last_name"])

    try:
        update_query = schema.TableSchema.generate_update_query(id = id,**kwargs)
        cursor.execute(update_query)
        conn.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()