# zeotap-ast-rule-engine
Introduction:
The Rule Engine utilizes AST to represent and manipulate conditional rules, allowing for the dynamic creation, modification, and evaluation of rules for user eligibility determination. Rules are expressed in terms of logical conditions (e.g., AND, OR), and the engine evaluates user data against these rules.

Features:
Dynamic Rule Creation: Define rules based on attributes such as age, department, income, and experience.
AST Representation: Efficiently represent and modify rules using an Abstract Syntax Tree.
Rule Combination: Merge multiple rules for optimized evaluation.
Evaluation Engine: Check user data against rules to determine eligibility.
Error Handling: Graceful handling of invalid rule strings and unsupported operations.
Technologies Used:
Language: Python
Libraries: Standard Python libraries (e.g., json, operator)
Architecture: 3-tier architecture (UI, API, Backend)
Installation
To run the project locally, follow these steps:
1.	Clone the Repository
Bash:



2. Install Dependencies:
If there are any external dependencies, install them by running:
Bash:
pip install -r requirements.txt
3. Run the Application:
Run the Python script to interact with the Rule Engine:
Bash:
python rule_engine.py
Usage:
Example Rule Creation:
You can create a rule like this:
Python:
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)" ast_rule = create_rule(rule1)
Rule Combination:
You can combine multiple rules into a single AST:
Python:
combined_ast = combine_rules([rule1, rule2])
Rule Evaluation:
Evaluate the rule against user data:
Python:
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(ast_rule, data)
print(result)  # True or False based on eligibility
API Documentation:
The rule_engine.py provides three main API functions:
1.	create_rule(rule_string): Parses a rule string and returns its AST representation.
2.	combine_rules(rules_list): Combines multiple ASTs into a single AST.
3.	evaluate_rule(AST, data): Evaluates the AST against a dictionary of user data.
Example API Usage:
Python:
ast_rule = create_rule("age > 30 AND department = 'Sales'")
result = evaluate_rule(ast_rule, {"age": 32, "department": "Sales"})
Testing
1.	Test Rule Creation: Validate that rules are correctly converted into ASTs.
2.	Test Rule Combination: Verify that multiple rules are properly combined.
3.	Test Rule Evaluation: Check rule evaluation results against various user data scenarios.

Run tests using:
Bash:
python -m unittest test_rule_engine.py
Improvements and Bonus Features:
•	Input Validation: Ensures valid rule strings and proper data formats.
•	Error Handling: Graceful handling of edge cases and invalid inputs.
•	Security: Implemented basic input sanitization to prevent rule injection.
•	Performance: Optimized rule combination to reduce redundant checks.
Conclusion:
This project demonstrates the core concepts of Abstract Syntax Trees (AST) in a Rule Engine context, offering flexibility for dynamically creating, modifying, and evaluating user eligibility rules. The system is designed to be extendable and can be enhanced with additional features such as user-defined functions or integration with real-world applications.

# zeotap-real-time-weather-monitoring
Features:
•	Fetches real-time weather data for a specified city.
•	Displays the temperature in either Celsius or Kelvin.
•	Easy to use and modify.
Prerequisites:
•	Python 3.x
•	requests library (You can install it using pip install requests)
•	An API key from OpenWeatherMap (replace the placeholder in the script with your actual API key)
Installation:
1.	Clone this repository or download the script.
2.	Install the required dependencies using:
Bash:
pip install requests
Usage:
1.	Replace the API_KEY in the script with your actual OpenWeatherMap API key.
2.	Run the script in your terminal and provide the city name to get the current weather.
Bash:
python weather_monitor.py
Functions:
•	get_weather_data(city): Fetches weather data for the provided city.
•	kelvin_to_celsius(kelvin): Converts temperature from Kelvin to Celsius.
•	process_weather_data(data, temp_unit): Processes and formats the weather data, allowing the temperature to be displayed in Celsius or Kelvin based on the user's preference.
Example:
Python:
Replace with your OpenWeatherMap API key
 API_KEY = 'your_api_key' 
city = 'London' 
weather_data = get_weather_data(city)
 if weather_data: 
process_weather_data(weather_data, temp_unit='C') # Display in Celsius
Notes:
•	You can change the temperature unit by modifying the temp_unit parameter in the process_weather_data function to either 'C' for Celsius or 'K' for Kelvin.
•	Make sure to handle your API key securely and avoid hardcoding it in production environments.

