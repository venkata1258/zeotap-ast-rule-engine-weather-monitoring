class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child (another node)
        self.right = right  # Right child (another node)
        self.value = value  # Operand value (for conditions)

def create_rule(rule_string):
    if 'AND' in rule_string:
        left_rule, right_rule = rule_string.split(' AND ', 1)
        return Node("operator", left=create_rule(left_rule), right=create_rule(right_rule), value="AND")
    elif 'OR' in rule_string:
        left_rule, right_rule = rule_string.split(' OR ', 1)
        return Node("operator", left=create_rule(left_rule), right=create_rule(right_rule), value="OR")
    else:
        return Node("operand", value=rule_string)

def combine_rules(rules):
    combined_ast = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if combined_ast is None:
            combined_ast = rule_ast
        else:
            combined_ast = Node("operator", left=combined_ast, right=rule_ast, value="AND")
    return combined_ast

def evaluate_rule(ast, data):
    if ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.type == "operand":
        condition = ast.value.split()
        attribute, operator, value = condition[0], condition[1], condition[2]

        if operator == ">":
            return data[attribute] > int(value)
        elif operator == "<":
            return data[attribute] < int(value)
        elif operator == "=":
            return data[attribute] == value.strip("'")
    return False

# Test the system
if __name__ == "__main__":
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "age < 25 AND department = 'Marketing'"

    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)

    combined_ast = combine_rules([rule1, rule2])

    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

    print(evaluate_rule(ast1, data))  # Expected True (for rule1)
    print(evaluate_rule(combined_ast, data))  # Evaluate combined rule AST
