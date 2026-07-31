# 🧪 Python-Projects

A **collection of Python projects** focused on **physics simulations, mathematical tools, and algorithmic experiments**. Built to explore theoretical concepts through code!

---

## 📌 **Projects Included**


| Project                          | Description                                                        | Run Command                                 | Screenshot        |
| -------------------------------- | ------------------------------------------------------------------ | ------------------------------------------- | ----------------- |
| **Weather API**                  | Fetches real-time weather data using the World Weather Online API  | `python Weather_API.py --location "London"` | Weather API       |
| **Projectile Motion Calculator** | Simulates and calculates projectile motion trajectories            | `python Projectile_Motion_Calculator.py`    | Projectile Motion |
| **Physics Unit Converter**       | Converts between different units (e.g., meters to feet, kg to lbs) | `python Physics_Unit_Converter.py`          | Unit Converter    |
| **11D Manifold Solver**          | Explores theoretical physics concepts in 11 dimensions             | `python 11D_Manifold_Solver.py`             | 11D Manifold      |
| **Vector Resultant Calculator**  | Calculates the resultant of multiple vectors                       | `python Vector_Resultant_Calculator.py`     | Vector Calculator |
| **Kinematics Solver**            | Solves kinematic equations for physics problems                    | `python Kinematics_solver.py`               | Kinematics Solver |
| **Escape Velocity Calculator**   | Calculates the escape velocity for celestial bodies                | `python Escape_velocity.py`                 | Escape Velocity   |
| **Trigonometry Tool**            | Solves trigonometric problems and visualizes functions             | `python Trigonometry.py`                    | Trigonometry      |


---

## 📦 **Requirements**

Install the required packages using:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install requests numpy matplotlib
```

---

## 🚀 **How to Run**

1. Clone the repository:
  ```bash
   git clone https://github.com/your-username/Python-Projects.git
   cd Python-Projects
  ```
2. Install dependencies (see above).
3. Run any project:
  ```bash
   python Weather_API.py --location "Coimbatore"
  ```

---

## 🔧 **Features**

- **Physics Simulations**: Visualize and calculate real-world physics problems.
- **Mathematical Tools**: Solve equations, convert units, and explore theoretical concepts.
- **API Integrations**: Fetch real-time data (e.g., weather) using external APIs.
- **User-Friendly**: Simple command-line interfaces for easy interaction.

---

## 🛠️ **Built With**

- [Python 3.8+](https://www.python.org/)
- [Requests](https://docs.python-requests.org/) (for API calls)
- [NumPy](https://numpy.org/) (for mathematical computations)
- [Matplotlib](https://matplotlib.org/) (for visualizations)

---

## 📂 **File Structure**

```
Python-Projects/
│
├── Weather_API.py
├── Projectile_Motion_Calculator.py
├── Physics_Unit_Converter.py
├── 11D_Manifold_Solver.py
├── Vector_Resultant_Calculator.py
├── Kinematics_solver.py
├── Escape_velocity.py
├── Trigonometry.py
├── requirements.txt
└── README.md
```

---

import sys

# --- 1. TOKEN TYPES ---
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_STRING = 'STRING'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_EQ = 'EQ'
TT_EE = 'EE'
TT_NE = 'NE'
TT_LT = 'LT'
TT_GT = 'GT'
TT_LTE = 'LTE'
TT_GTE = 'GTE'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_LBRACE = 'LBRACE'
TT_RBRACE = 'RBRACE'
TT_EOF = 'EOF'

KEYWORDS = ['let', 'print', 'if', 'while']

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"

# --- 2. LEXER ---
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t\n\r':
                self.advance()
            elif self.current_char in '0123456789':
                tokens.append(self.make_number())
            elif self.current_char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
                tokens.append(self.make_identifier())
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(TT_EE))
                    self.advance()
                else:
                    tokens.append(Token(TT_EQ))
            elif self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(TT_NE))
                    self.advance()
                else:
                    raise SyntaxError("Expected '=' after '!'")
            elif self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(TT_LTE))
                    self.advance()
                else:
                    tokens.append(Token(TT_LT))
            elif self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    tokens.append(Token(TT_GTE))
                    self.advance()
                else:
                    tokens.append(Token(TT_GT))
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LBRACE))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RBRACE))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                raise SyntaxError(f"Illegal Character '{char}'")
        tokens.append(Token(TT_EOF))
        return tokens

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char is not None and self.current_char in '0123456789.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        return Token(TT_INT, int(num_str)) if dot_count == 0 else Token(TT_FLOAT, float(num_str))

    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and self.current_char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789':
            id_str += self.current_char
            self.advance()
        return Token(TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER, id_str)

    def make_string(self):
        str_val = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            str_val += self.current_char
            self.advance()
        self.advance()
        return Token(TT_STRING, str_val)

# --- 3. AST NODES ---
class NumberNode:
    def __init__(self, tok): self.tok = tok
class StringNode:
    def __init__(self, tok): self.tok = tok
class VarAccessNode:
    def __init__(self, var_name_tok): self.var_name_tok = var_name_tok
class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node
class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
class PrintNode:
    def __init__(self, expr_node): self.expr_node = expr_node
class IfNode:
    def __init__(self, cases): self.cases = cases
class WhileNode:
    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node

# --- 4. PARSER ---
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        statements = []
        while self.current_tok.type != TT_EOF:
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.current_tok.type == TT_KEYWORD and self.current_tok.value == 'let':
            self.advance()
            if self.current_tok.type != TT_IDENTIFIER: raise SyntaxError("Expected identifier after 'let'")
            var_name = self.current_tok
            self.advance()
            if self.current_tok.type != TT_EQ: raise SyntaxError("Expected '='")
            self.advance()
            return VarAssignNode(var_name, self.expr())
        
        elif self.current_tok.type == TT_KEYWORD and self.current_tok.value == 'print':
            self.advance()
            return PrintNode(self.expr())
        
        elif self.current_tok.type == TT_KEYWORD and self.current_tok.value == 'if':
            self.advance()
            condition = self.expr()
            if self.current_tok.type != TT_LBRACE: raise SyntaxError("Expected '{'")
            self.advance()
            body = self.parse_block()
            return IfNode([(condition, body)])

        elif self.current_tok.type == TT_KEYWORD and self.current_tok.value == 'while':
            self.advance()
            condition = self.expr()
            if self.current_tok.type != TT_LBRACE: raise SyntaxError("Expected '{'")
            self.advance()
            body = self.parse_block()
            return WhileNode(condition, body)

        return self.expr()

    def parse_block(self):
        body = []
        while self.current_tok.type != TT_RBRACE and self.current_tok.type != TT_EOF:
            body.append(self.statement())
        if self.current_tok.type != TT_RBRACE: raise SyntaxError("Expected '}'")
        self.advance()
        return body

    def expr(self):
        return self.binary_op(self.comp_expr, (TT_PLUS, TT_MINUS))

    def comp_expr(self):
        return self.binary_op(self.term, (TT_EE, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE))

    def term(self):
        return self.binary_op(self.factor, (TT_MUL, TT_DIV))

    def factor(self):
        tok = self.current_tok
        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)
        elif tok.type == TT_STRING:
            self.advance()
            return StringNode(tok)
        elif tok.type == TT_IDENTIFIER:
            self.advance()
            return VarAccessNode(tok)
        elif tok.type == TT_LPAREN:
            self.advance()
            node = self.expr()
            if self.current_tok.type == TT_RPAREN:
                self.advance()
                return node
            raise SyntaxError("Expected ')'")
        raise SyntaxError(f"Unexpected token {tok.type}")

    def binary_op(self, func, ops):
        left = func()
        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)
        return left

# --- 5. INTERPRETER ---
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        val = self.symbols.get(name)
        if val is None and self.parent: return self.parent.get(name)
        return val

    def set(self, name, value):
        self.symbols[name] = value

class Interpreter:
    def visit(self, node, env):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.no_visit_method)
        return visitor(node, env)

    def no_visit_method(self, node, env):
        raise NotImplementedError(f'No visit_{type(node).__name__} method defined')

    def visit_NumberNode(self, node, env): return node.tok.value
    def visit_StringNode(self, node, env): return node.tok.value

    def visit_VarAccessNode(self, node, env):
        val = env.get(node.var_name_tok.value)
        if val is None: raise RuntimeError(f"'{node.var_name_tok.value}' is not defined")
        return val

    def visit_VarAssignNode(self, node, env):
        val = self.visit(node.value_node, env)
        env.set(node.var_name_tok.value, val)
        return val

    def visit_BinOpNode(self, node, env):
        left = self.visit(node.left_node, env)
        right = self.visit(node.right_node, env)
        op = node.op_tok.type
        
        if op == TT_PLUS: return left + right
        if op == TT_MINUS: return left - right
        if op == TT_MUL: return left * right
        if op == TT_DIV:
            if right == 0: raise RuntimeError("Division by zero")
            return left / right
        if op == TT_EE: return 1 if left == right else 0
        if op == TT_NE: return 1 if left != right else 0
        if op == TT_LT: return 1 if left < right else 0
        if op == TT_GT: return 1 if left > right else 0
        if op == TT_LTE: return 1 if left <= right else 0
        if op == TT_GTE: return 1 if left >= right else 0

    def visit_PrintNode(self, node, env):
        print(self.visit(node.expr_node, env))
        return None

    def visit_IfNode(self, node, env):
        for condition, body in node.cases:
            if self.visit(condition, env) != 0:
                for stmt in body: self.visit(stmt, env)
                break
        return None

    def visit_WhileNode(self, node, env):
        while self.visit(node.condition_node, env) != 0:
            for stmt in node.body_node: self.visit(stmt, env)
        return None

# --- 6. REPL EXECUTION LOOP ---
global_symbol_table = SymbolTable()

def run(text):
    try:
        lexer = Lexer(text)
        tokens = lexer.make_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        for node in ast:
            interpreter.visit(node, global_symbol_table)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("--- Custom Mini-Language REPL (Fixed) ---")
    while True:
        try:
            text = input("lang> ")
            if text.strip() == "exit": break
            if not text.strip(): continue
            run(text)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

## 🤝 **Contributing**

Want to add a new project or improve an existing one? Here’s how:

1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add projectile motion visualization"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a **Pull Request**.

---

## 📜 **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📫 **Connect with Me**

- **GitHub**: [@dhrruvanand-del](https://github.com/dhrruvanand-del)

---

**Developed with ❤️ by Dhrruv Anand(Zioles).**
