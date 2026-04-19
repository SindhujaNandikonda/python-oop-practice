class TestCase:
    def __init__(self,test_id, title, status, priority):
        self.test_id = test_id
        self.title = title
        self.status = status
        self.priority = priority
    
    def mark_passed(self):
        return "Passed"
        
    
    def mark_failed(self):
        return "Failed"
    
    def __str__(self):
        return f"TestCase({self.test_id}, {self.title}, {self.status}, {self.priority})"
        
    
test_case1 = TestCase(1, "Verify login functionality", "Executed", "High")
test_case2 = TestCase(2, "Verify registration functionality", "Not Executed", "Medium")
print(test_case1.title)  # Output: Verify login functionality
print(test_case2.status)  # Output: Not Executed
print(test_case1.mark_passed())  # Output: Passed
print(test_case2.mark_failed())  # Output: Failed

print(TestCase.mark_passed(test_case1))  # This should print: Failed
test_case3 = TestCase(3, "Verify password reset functionality", test_case2.mark_failed(), "Low")
print(test_case3.status)  # Output: Failed

print(test_case2.__str__())# prints string representation of test_case2 object