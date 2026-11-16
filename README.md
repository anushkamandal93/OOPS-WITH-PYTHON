[README.md](https://github.com/user-attachments/files/34915833/README.md)
# 🐍 Python OOPs: Concepts & Assignments

A single repository for learning Python Object-Oriented Programming (OOP). It has two parts:

- **`CONCEPTS/`**: theory notes with small examples, covering classes, constructors, inheritance, polymorphism, encapsulation and abstraction.
- **`OOPS ASSIGNMENTS/`**: Jupyter / Google Colab notebooks that put those concepts into practice. Each has the problem statement, the expected output and a working solution.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter%20%2F%20Colab-orange?logo=jupyter&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-OOP-green)

---

## 📚 Table of Contents

- [Concepts Covered](#-concepts-covered)
- [Repository Structure](#-repository-structure)
- [Concept Notes](#-concept-notes-concepts)
- [Assignment Notebooks](#-assignment-notebooks-oops-assignments)
- [Quick Concept Examples](#-quick-concept-examples)
- [Getting Started](#-getting-started)
- [Learning Path](#-suggested-learning-path)

---

## 🎯 Concepts Covered

| Concept | Description |
|---|---|
| **Class & Object** | Blueprint for data and behaviour, and its instances |
| **Constructor (`__init__`)** | Initialising instance variables when an object is created |
| **`self` keyword** | Referring to the current instance inside methods |
| **Methods** | Functions defined inside a class |
| **Single Inheritance** | One child class derived from one parent class |
| **Multilevel Inheritance** | A chain of inheritance (Grandparent → Parent → Child) |
| **Multiple Inheritance** | A child class derived from more than one parent |
| **Hierarchical Inheritance** | Several child classes derived from one parent |
| **`super()`** | Accessing the parent class constructor and methods |
| **Abstraction** | Abstract classes and abstract methods using `abc` |
| **Encapsulation** | Private variables accessed via getter/setter methods |
| **Polymorphism** | Same method name (`area()`) behaving differently across classes |
| **Hybrid Inheritance** | A combination of two or more inheritance types |
| **Method Overriding** | A child class redefining a method of its parent |
| **Method Overloading** | Same method name with different parameters (not natively supported in Python) |
| **Access Modifiers** | Public (`name`), protected (`_age`) and private (`__height`) members |
| **`@classmethod` / `@staticmethod`** | Methods bound to the class, or to neither class nor instance |
| **Dunder (magic) methods** | `__init__`, `__str__`, `__add__`, `__eq__` and other methods Python calls automatically |

---

## 🗂 Repository Structure

```
.
├── CONCEPTS/                               # Theory notes with commented examples
│   ├── class&object.py
│   ├── constructor.py
│   ├── inheritance.py
│   ├── polymorphism.py
│   ├── encapsulation.py
│   └── abstraction.py
├── OOPS ASSIGNMENTS/                       # Practice notebooks with solutions
│   ├── oops_class_functions_1.ipynb        # Class, Object, Method, self (Basic)
│   ├── OOPS_Assingment.ipynb               # Student, Employee, Bank, Mobile, ATM systems
│   ├── oops_Assignment_2.ipynb             # Constructors, methods, multiple objects
│   ├── inheritance_assignment_1.ipynb      # Inheritance basics
│   ├── Inheritance_assignment_2.ipynb      # Single, multilevel, multiple, hierarchical
│   ├── Inheritance_assignment_3.ipynb      # Inheritance practice (Intermediate)
│   ├── oops_abstraction_assignment.ipynb   # Abstract classes and methods (Basic)
│   └── Full_OOPS_.ipynb                    # Mixed: super(), encapsulation, polymorphism
└── README.md
```

---

## 📝 Concept Notes (`CONCEPTS/`)

Short `.py` files with explanations as comments and small commented-out examples. Uncomment an example to run it.

| File | What it covers |
|---|---|
| `class&object.py` | Class as a blueprint, attributes, methods, creating objects, multiple objects per class |
| `constructor.py` | `__init__`, instance attributes, `@classmethod` and `@staticmethod` |
| `inheritance.py` | Single, multiple, multilevel, hierarchical (and hybrid) inheritance, with `super()` |
| `polymorphism.py` | Polymorphism, method overriding, and why method overloading has no real use in Python |
| `encapsulation.py` | Public, protected and private attributes and methods |
| `abstraction.py` | Abstract classes with `abc`, plus dunder methods (`__str__`, `__add__`, `__eq__`) |

> **Note:** `encapsulation.py` calls `obj1.__sleep()` on purpose. It raises an `AttributeError`, which shows that private members cannot be accessed from outside the class.

---

## 📓 Assignment Notebooks (`OOPS ASSIGNMENTS/`)

### 1. `oops_class_functions_1.ipynb` — Class, Object, Method & `self`
*Level: Basic · 10 questions*

Student, Car, Employee, Mobile, Laptop, Book, Teacher, Animal (multiple objects) and Bank classes. Focus is on creating objects, storing attributes and understanding `self`.

### 2. `OOPS_Assingment.ipynb` — Management Systems
*5 questions*

| # | Problem |
|---|---|
| Q1 | Student Information System |
| Q2 | Employee Management System |
| Q3 | Bank Account System (`deposit`, `withdraw`, `check_balance`) |
| Q4 | Mobile Information System |
| Q5 | ATM System (deposit, withdraw, balance check) |

### 3. `oops_Assignment_2.ipynb` — Constructors & Methods
*10 questions*

Player, Movie, Employee Bonus Calculator (10%), Circle (area and circumference), Bus (multiple objects), Product, BankAccount (deposit), University, Train and FoodItem (total bill).

### 4. `inheritance_assignment_1.ipynb` — Inheritance Basics
*10 questions*

Parent–child pairs using `super()`: Animal → Dog, Vehicle → Bike, Person → Teacher, Employee → Developer, Mobile → AndroidMobile, Shape → Square, University → Student, Book → Ebook, Hospital → Patient, Bank → SavingsAccount.

### 5. `Inheritance_assignment_2.ipynb` — Inheritance Types
*10 questions*

| Type | Examples |
|---|---|
| Single | Animal → Cat, Person → Employee |
| Multilevel | Grandfather → Father → Son, School → Teacher → Student, Device → Mobile → Smartphone |
| Multiple | Father + Mother → Child, Sports + Studies → Student, Camera + MusicPlayer → SmartPhone |
| Hierarchical | Vehicle → Car / Bike, Employee → Developer / Designer |

### 6. `Inheritance_assignment_3.ipynb` — Inheritance Practice
*Level: Intermediate · 10 questions*

Electronics → Laptop, Human → Doctor, Country → State → City, OnlineCourse → PythonCourse, Father + Mother → Son, Appliance → WashingMachine / Refrigerator, Account → CurrentAccount, Animal → Bird → Parrot, MusicSystem → Bluetooth, Teacher → MathsTeacher / ScienceTeacher.

### 7. `oops_abstraction_assignment.ipynb` — Abstraction
*Level: Basic · 10 questions*

Abstract base classes using Python's `abc` module (`ABC`, `@abstractmethod`):

`Animal → Dog` · `Vehicle → Car` · `Shape → Square` · `Payment → UPI` · `Employee → Developer` · `Notification → Email` · `Bank → SBI` · `Food → Pizza` · `Device → SmartTV` · `Student → SchoolStudent`

### 8. `Full_OOPS_.ipynb` — Mixed OOP Concepts
*6 problems*

| Problem | Concept |
|---|---|
| Employee Hierarchy (Person → Employee → Manager) | Multilevel inheritance |
| Vehicle → Car | Using `super()` |
| Bank Account with private balance | Encapsulation |
| Hospital Management (Person, Doctor, Patient) | Inheritance |
| Shape Area (Rectangle, Circle) | Polymorphism |
| Online Shopping (Product → ElectronicsProduct) | Discount calculation |

---

## 💡 Quick Concept Examples

**Class and constructor**

```python
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_details(self):
        print(f"Student Name : {self.name}")
        print(f"Roll Number  : {self.roll_number}")
        print(f"Course       : {self.course}")

Student("Rahul", 101, "Python").display_details()
```

**Inheritance with `super()`**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
```

**Abstraction**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

**Encapsulation**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private variable

    def get_balance(self):
        return self.__balance
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook / JupyterLab, or a Google account for Google Colab

### Run locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. (Optional) Install Jupyter
pip install notebook

# 3. Launch Jupyter and open any .ipynb file
jupyter notebook
```

### Run on Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Choose **File → Upload notebook** and select any `.ipynb` file
3. Run the cells with **Runtime → Run all**

No external libraries are needed. Everything uses the Python standard library.

---

## 🧭 Suggested Learning Path

0. Read the matching file in `CONCEPTS/` before each topic, then solve the notebooks in `OOPS ASSIGNMENTS/`
1. `oops_class_functions_1.ipynb` — classes, objects, `self`
2. `OOPS_Assingment.ipynb` and `oops_Assignment_2.ipynb` — constructors and methods
3. `inheritance_assignment_1.ipynb` — inheritance basics
4. `Inheritance_assignment_2.ipynb` and `Inheritance_assignment_3.ipynb` — all inheritance types
5. `oops_abstraction_assignment.ipynb` — abstract classes
6. `Full_OOPS_.ipynb` — revision across all concepts

---

## 🤝 Contributing

Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is for educational purposes. Add a license of your choice (for example MIT) if you plan to share it publicly.

---

⭐ If you found this helpful, consider giving the repository a star!
