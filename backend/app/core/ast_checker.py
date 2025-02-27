import ast

class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = []  # Store detected issues

    def visit_Call(self, node):
        """Detects dangerous function calls like eval(), exec(), etc."""
        if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec", "open", "os.system"]:
            self.issues.append(f"⚠️ Security Risk: Usage of '{node.func.id}' on line {node.lineno}")
        self.generic_visit(node)  # Continue visiting other nodes

    def visit_Import(self, node):
        """Detects potentially unsafe imports like os, subprocess."""
        for alias in node.names:
            if alias.name in ["os", "subprocess"]:
                self.issues.append(f"⚠️ Security Risk: Importing '{alias.name}' on line {node.lineno}")
        self.generic_visit(node)

    def visit_While(self, node):
        """Detects potentially infinite loops."""
        if not isinstance(node.test, ast.Constant):  # Skip static while True
            self.issues.append(f"⚠️ Possible Infinite Loop detected on line {node.lineno}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """Detects deep function nesting."""
        depth = self._get_function_depth(node)
        if depth > 3:
            self.issues.append(f"⚠️ Function '{node.name}' is deeply nested ({depth} levels) on line {node.lineno}")
        self.generic_visit(node)

    def _get_function_depth(self, node, depth=1):
        """Helper function to calculate function nesting depth."""
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                return self._get_function_depth(child, depth + 1)
        return depth

def analyze_code_with_ast(code):
    """Runs AST analysis on Python code."""
    try:
        tree = ast.parse(code)  # Convert code into AST
        analyzer = ASTAnalyzer()
        analyzer.visit(tree)  # Walk through the AST
        return analyzer.issues if analyzer.issues else ["✅ No issues detected."]
    except SyntaxError as e:
        return [f"Syntax Error: {e}"]
