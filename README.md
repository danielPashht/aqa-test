How to run the tests:

Option 1 (local):
1. Install Python 3.10
2. Install requirements (Command: pip3 install -r requirements.txt)
from the root directory
3. Navigate to /tests/ folder
4. Run "pytest test_suit.py" 
- Option 2 (Docker):
1. Run docker -> $ docker run -d -p 4444:4444 selenium/standalone-chrome
2. Navigate to /tests/ folder
3. Run "pytest test_suit.py --remote true" 
tests will run in Docker container (Chrome)