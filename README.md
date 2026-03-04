# \# Quick-Calc

# 

# Quick-Calc is a lightweight command-line calculator application built in Python. It supports the four fundamental arithmetic operations — addition, subtraction, multiplication, and division — along with a clear/reset function. The project demonstrates a professional software development workflow using Git version control and a multi-layered automated testing strategy with pytest.

# 

# ---

# 

# \## Setup Instructions

# 

# \*\*Prerequisites:\*\* Python 3.9 or higher must be installed.

# 

# 1\. Clone the repository:

# &nbsp;  ```bash

# &nbsp;  git clone https://github.com/Alex-Glitch-X/swe-testing-assignment.git

# &nbsp;  cd swe-testing-assignment

# &nbsp;  ```

# 

# 2\. Install dependencies:

# &nbsp;  ```bash

# &nbsp;  pip install -r requirements.txt

# &nbsp;  ```

# 

# ---

# 

# \## How to Run Tests

# 

# Execute the full test suite with a single command from the project root:

# 

# ```bash

# pytest

# ```

# 

# To view a verbose, per-test breakdown:

# 

# ```bash

# pytest -v

# ```

# 

# ---

# 

# \## Testing Framework Research: Pytest vs Unittest

# 

# Python's standard library includes `unittest`, a class-based testing framework modelled after Java's JUnit. It requires developers to subclass `unittest.TestCase` and use specific assertion methods like `assertEqual` and `assertRaises`. While this structured approach offers reliability and zero external dependencies, the verbosity of defining classes and methods for every test group makes it feel heavyweight for small, focused projects.

# 

# `pytest` is a third-party framework that treats each plain Python function prefixed with `test\_` as a test case. Its automatic test discovery, minimal boilerplate, and powerful `assert` introspection produce far more readable failure messages. When an assertion fails, pytest displays the actual vs. expected values directly inline, while unittest simply states that the test failed. Additionally, pytest's fixture system provides a clean, reusable mechanism for setting up shared state.

# 

# For this project, \*\*pytest\*\* was chosen because its readability and fixture support make tests easier to maintain and extend. It is the industry-standard choice for modern Python projects and integrates seamlessly with CI/CD pipelines. The only trade-off is the external dependency, which is trivially managed via `requirements.txt`.



