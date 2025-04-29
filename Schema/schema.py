from pydantic.dataclasses import dataclass
from typing import get_type_hints

@dataclass
class ContactSchema:  # schema for contact class
    first_name : str
    last_name : str
    email : str 
    phone_number : str
    address : str
    city : str
    state : str
    zip : str

def get_contact_details(schema_cls):
    """
    Function to get input from user
    """
    field_names = get_type_hints(schema_cls).keys()
    input_data = {field : input(f"{field.replace('_', ' ').title()}: ").strip() for field in field_names}

    return schema_cls(**input_data)


class TableSchema:
    table_schema = {
        "address_book": 
        {
            "table_name": "AddressBooks",
            "column_schema" : [
                {"name":"id","type":"INT","constraint":["AUTO_INCREMENT", "PRIMARY KEY"]},
                {"name":"name","type":"VARCHAR(100)","constraint":["UNIQUE", "NOT NULL"]},
            ],
        },
        "contact": {
            "table_name": "Contacts",
             "column_schema" : [
                {"name":"id","type":"INT","constraint":["AUTO_INCREMENT", "PRIMARY KEY"]},
                {"name":"first_name","type":"VARCHAR(50)","constraint":[]},
                {"name":"last_name","type":"VARCHAR(50)","constraint":[]},
                {"name":"email","type":"VARCHAR(100)","constraint":[]},
                {"name":"phone_number","type":"VARCHAR(15)","constraint":[]},
                {"name":"address","type":"VARCHAR(255)","constraint":[]},
                {"name":"city","type":"VARCHAR(50)","constraint":[]},
                {"name":"state","type":"VARCHAR(50)","constraint":[]},
                {"name":"zip","type":"VARCHAR(6)","constraint":[]},
                {"name":"address_book_id", "type": "INT", "constraint": []},
             ],
             "foreign_keys" :
                    {
                        "column": "address_book_id",
                        "references": {
                            "table": "AddressBooks",
                            "column": "id"
                        },
                        "on_delete": "CASCADE"
                    }
                }
            }

    
    @classmethod
    def generate_create_query(cls, table_key):
        """
        Funtion to generate query to create address book
        """
        table_info = cls.table_schema[table_key]
        table_name = table_info["table_name"]
    
        column_definitions = []
        for column in table_info["column_schema"]:
            column_definition = f"{column['name']} {column['type']}"
            if column["constraint"]:
                column_definition += " " + " ".join(column["constraint"])
            column_definitions.append(column_definition)
        
        fk_defs = []
        if "foreign_keys" in table_info:
            fks = table_info["foreign_keys"]
            if isinstance(fks, dict):
                fks = [fks]
            for fk in fks:
                fk_clause = (
                    f"FOREIGN KEY ({fk['column']}) "
                    f"REFERENCES {fk['references']['table']}({fk['references']['column']}) "
                    f"ON DELETE {fk.get('on_delete', 'NO ACTION')}"
                )
                fk_defs.append(fk_clause)

        all_definitions = column_definitions + fk_defs
        column_definitions_str = ", ".join(all_definitions)
                
        return f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions_str});"

    @classmethod
    def generate_insert_query(cls, table_key):
        """
        Funtion to generate query to insert address book or contact
        """
        table_info = cls.table_schema[table_key]
        table_name = table_info["table_name"]
        columns = [column["name"] for column in table_info["column_schema"]]
        
        insert_columns = [col for col in columns if col != "id"]
        placeholders = ", ".join(["%s"] * len(insert_columns))
        columns_str = ", ".join(insert_columns)

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
        return query, insert_columns

    @classmethod
    def generate_delete_query(cls,table_key):
        """
        Funtion to generate query to delete address book or contact
        """
        table_info = cls.table_schema[table_key]
        table_name = table_info["table_name"]
        if table_key == "address_book":
            query = f"DELETE FROM {table_name} WHERE name = %s"
        elif table_key == "contact":
            query = f"DELETE FROM {table_name} WHERE id = %s"
        else:
            raise ValueError(f"Unknown table name: {table_name}. Cannot generate delete query.")
        return query

    @classmethod
    def generate_select_query(cls,table_key):
        table_info = cls.table_schema[table_key]
        table_name = table_info["table_name"]
        columns = [column["name"] for column in table_info["column_schema"]]
        
        select_columns = [col for col in columns if col != "id"]
        columns_str = ", ".join(select_columns)
        query = f"SELECT {columns_str} from {table_name} WHERE address_book_id = (SELECT id from Addressbooks where name = %s)"
        return query
    
    @classmethod
    def generate_update_query(cls,**kwargs):
        table_info = cls.table_schema['contact']
        table_name = table_info["table_name"]
        query = f"UPDATE {table_name} SET {kwargs['field']} = '{kwargs['new_value']}' WHERE id = {kwargs['id']};"
        print(query)  
        return query      