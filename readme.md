# Homework6: Gettring Ready for Production:Logging , Environmental variables and Devops
- The purpose of this project is to enhance your program by introducing key practices that are essential for preparing software for a production environment.  
1. Create directory and use touch command create files.
2. Integrate these concepts with existing program to add four basic commands: add, subtract, multiply, and divide, making calculator interactive.
3. Make a menu command that, when the application launches and the user inputs "menu," shows the available commands from the command dictionary.
4. Plugin Architecture:
 - refactor program to enable plugins to load automatically, making it simple to add commands without requiring manual updates.
5. GitHub Actions:
- This feature involves setting up GitHub Actions to automatically run our program's tests whenever changes are pushed to the main branch. By doing this, yoweu can ensure that any new code additions or modifications don't break existing functionality.
6. Environment Variables:
- Using environment variables is important for managing sensitive data like passwords, API keys, and other configuration settings without hardcoding them in our program. By storing this information in environment variables, we can keep it secure and easily change it without modifying the code.
- create .env file 
 - ENVIRONMENT=DEVELOPMENT
 - DATABASE_USERNAME=root
 
- we learn to create a .env file to store these variables locally and ensure that this file is added to .gitignore to prevent it from being accidentally pushed to GitHub. This practice protects sensitive information and helps maintain security in our projects. 
7. Logging:
- Adding logging functionality to our program will allow us to track application behavior, monitor usage, and debug more effectively. Unlike simple print statements, logging can provide more structured and detailed output.
## Instructions:
1. create clone the repo.
2. First Deactivate the virtual environment with the command "deactivate" and then activate it again command.
  i. source venv/bin/activate
3. Install the required libraries.
  - Update the requirements file with pip freeze > requirements.txt.

Note When someone copies / clones my repository they will install the specfic library / dependency requirements for my project using the command:

-> pip install -r requirments.txt
-> Finally, Open VScode and test code.
   i. code .

## Testing

1. Run all tests with : pytest
2. Run Coverage : pytest --cov
3. Run application: python main.py
4. To test a specific file, use pytest tests/test_calculator.py

## Output:
1. ~/Webdeploy_projects2024/HW-6_Logging-environment$ python3 main.py
- 2024-10-17 10:22:40,006 - root - INFO - Logging configured.
- 2024-10-17 10:22:40,018 - root - INFO - Environment variables loaded.
- 2024-10-17 10:22:40,031 - root - INFO - Loading plugin 'add'..
- 2024-10-17 10:22:40,031 - root - INFO - Command 'add' has been registered.
- 2024-10-17 10:22:40,031 - root - INFO - Command 'add' from plugin 'add' registered.
- 2024-10-17 10:22:40,067 - root - INFO - Loading plugin 'divide'..
- 2024-10-17 10:22:40,068 - root - INFO - Command 'divide' has been registered.
- 2024-10-17 10:22:40,068 - root - INFO - Command 'divide' from plugin 'divide' registered.
- 2024-10-17 10:22:40,105 - root - INFO - Loading plugin 'exit'..
- 2024-10-17 10:22:40,105 - root - INFO - Command 'exit' has been registered.
- 2024-10-17 10:22:40,106 - root - INFO - Command 'exit' from plugin 'exit' registered.
- 2024-10-17 10:22:40,135 - root - INFO - Loading plugin 'menu'..
- 2024-10-17 10:22:40,135 - root - INFO - Command 'menu' has been registered.
- 2024-10-17 10:22:40,136 - root - INFO - Command 'menu' from plugin 'menu' registered.
- 2024-10-17 10:22:40,142 - root - INFO - Loading plugin 'multiply'..
- 2024-10-17 10:22:40,142 - root - INFO - Command 'multiply' has been registered.
- 2024-10-17 10:22:40,142 - root - INFO - Command 'multiply' from plugin 'multiply' registered.
- 2024-10-17 10:22:40,173 - root - INFO - Loading plugin 'subtract'..
- 2024-10-17 10:22:40,173 - root - INFO - Command 'subtract' has been registered.
- 2024-10-17 10:22:40,174 - root - INFO - Command 'subtract' from plugin 'subtract' registered.
- 2024-10-17 10:22:40,174 - root - INFO - Application started. Type 'exit' to exit.
- Type 'exit' to exit.
- 2024-10-17 10:22:40,174 - root - INFO - Type 'menu' to see all available commands.
- >>> menu
- 2024-10-17 10:22:54,858 - root - INFO - Available commands: ['add', 'divide', 'exit', 'menu', 'multiply', 'subtract']
- >>> add
- 2024-10-17 10:22:59,785 - root - ERROR - 'add' requires two numeric arguments.
- >>> add 1 3
- 2024-10-17 10:23:04,377 - root - INFO - 4.0
- >>> add 1 e
- 2024-10-17 10:23:09,048 - root - ERROR - Both arguments must be numbers.
- >>> subtract 5 8
- 2024-10-17 10:23:27,742 - root - INFO - -3.0
- >>> multiply e 5
- 2024-10-17 10:23:46,337 - root - ERROR - Both arguments must be numbers.
- >>> multiply 3
- 2024-10-17 10:24:06,667 - root - ERROR - 'multiply' requires two numeric arguments.
- >>> multiply 3 4
- 2024-10-17 10:24:14,264 - root - INFO - 12.0
- >>> divide 10 2
- 2024-10-17 10:24:25,937 - root - INFO - 5.0
- >>> divide 4 0
- 2024-10-17 10:24:34,323 - root - ERROR - Cannot divide by zero.
- >>> mod
- 2024-10-17 10:24:44,579 - root - ERROR - No such command: mod
- >>> exit
- 2024-10-17 10:24:56,474 - root - INFO - Application exit. Goodbye!
-  Exiting...


## Other commands used during project
 1. mv oldfile newfilename
 2. git remote remove origin
 3. rm -rf .pytest_cache
 4. To add multiple specific files: git add path/to/file1.py path/to/file2.py path/to/file3.py
 5. coverage report -m