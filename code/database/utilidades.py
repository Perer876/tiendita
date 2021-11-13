def get_column_names(description:tuple):
    return [description[i][0] for i in range(len(description))]

def column_names(column_list:list):
    if len(column_list) == 0:
        return "*"
    return ",".join(column_list)

def where_condition(condition:str, conditions:dict):
    boolean_expresion = ""
    if condition:
        boolean_expresion = f" WHERE {condition} "
    for column, value in conditions.items():
        if len(boolean_expresion) == 0:
            boolean_expresion += " WHERE "
        else:
            boolean_expresion += " AND "
        boolean_expresion += f"{column}='{value}'"
    return boolean_expresion

def assignment_list(relations:dict):
    return ",".join([f"{column}='{value}'" for column, value in relations.items()])
    