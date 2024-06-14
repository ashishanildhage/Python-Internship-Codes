""" System Design"""

# System design is an iterative process, and the design may change as new information is gathered and requirements evolve. 
# it’s important to communicate the design effectively to all stakeholders, including developers, users, and stakeholders, to ensure that 
#   the system meets their needs and expectations.

# defining the system’s architecture, components, modules, and interfaces, and identifying the technologies and tools that will be used to implement the system.
# three-tier architecture: presentation layer (front-end), business logic layer (back-end), and data storage layer (database).

def components_modules_interfaces():
    # User Component
    # user.py (Module)

    class User:
        def __init__(self, user_id, name):
            self.user_id = user_id
            self.name = name

        def __str__(self):
            return f"User[ID={self.user_id}, Name={self.name}]"

    # user_management.py (Module)

    class UserManager:
        def __init__(self):
            self.users = {}

        def add_user(self, user_id, name):
            if user_id in self.users:
                print(f"User with ID {user_id} already exists.")
            else:
                self.users[user_id] = User(user_id, name)
                print(f"Added {self.users[user_id]}")

        def get_user(self, user_id):
            return self.users.get(user_id, None)


    # Book Component
    # book.py (Module)

    class Book:
        def __init__(self, book_id, title):
            self.book_id = book_id
            self.title = title

        def __str__(self):
            return f"Book[ID={self.book_id}, Title={self.title}]"

    # book_management.py (Module)

    class BookManager:
        def __init__(self):
            self.books = {}

        def add_book(self, book_id, title):
            if book_id in self.books:
                print(f"Book with ID {book_id} already exists.")
            else:
                self.books[book_id] = Book(book_id, title)
                print(f"Added {self.books[book_id]}")

        def get_book(self, book_id):
            return self.books.get(book_id, None)


    # Interfaces
    # interface.py (Module)

    class LibraryInterface:
        def __init__(self, user_manager, book_manager):
            self.user_manager = user_manager
            self.book_manager = book_manager

        def add_user(self, user_id, name):
            self.user_manager.add_user(user_id, name)

        def get_user(self, user_id):
            user = self.user_manager.get_user(user_id)
            if user:
                print(user)
            else:
                print(f"User with ID {user_id} not found.")

        def add_book(self, book_id, title):
            self.book_manager.add_book(book_id, title)

        def get_book(self, book_id):
            book = self.book_manager.get_book(book_id)
            if book:
                print(book)
            else:
                print(f"Book with ID {book_id} not found.")


    # Main Application (Presentation Layer)
    # main.py (Entry Point)

    def main():
        # Create managers
        user_manager = UserManager()
        book_manager = BookManager()

        # Create library interface
        library = LibraryInterface(user_manager, book_manager)

        # Add and retrieve users
        library.add_user(1, "Alice")
        library.add_user(2, "Bob")
        library.get_user(1)
        library.get_user(3)

        # Add and retrieve books
        library.add_book(101, "The Great Gatsby")
        library.add_book(102, "1984")
        library.get_book(101)
        library.get_book(103)


    if __name__ == "__main__":
        main()

# COMPONENTS - 
#       self-contained units that encapsulate a set of related functions or data. Each component has a specific responsibility within the system.
# Encapsulation: Components encapsulate data and behavior.
# Reusability: Designed to be reusable in different parts of the system.
# Replaceability: Can be replaced with another component that provides similar functionality.
# Eg - user authentication component, a database access component, and a payment processing component.

# MODULES - 
#       organize code within a component. They are smaller units of functionality that make up a component and can be reused within the component.
# Organization: Modules help in logically organizing code.
# Scope: Typically, a module is a single file or a collection of related files in Python.
# Namespace: Modules define a namespace for the functions, classes, and variables they contain. 
#       (Namespace is a container that holds a set of identifiers (names) and ensures that all names within it are unique. 
#       It helps organize and manage the scope of variables, functions, classes, and other objects to avoid naming conflicts.
#       Local Namespace: Created when a function is called and destroyed when the function returns. It contains names defined within the function.
#       Global Namespace: Created when a module is loaded and lasts until the interpreter exits. It contains names defined at the module level.
#       Built-in Namespace: Always available and contains built-in functions and exceptions.)
        def namespace():
            # Global namespace
            x = 10

            def outer_function():
                # Enclosing namespace (in case of nested functions)
                x = 20

                def inner_function():
                    # Local namespace
                    x = 30
                    print("Inner:", x)

                inner_function()
                print("Outer:", x)

            outer_function()
            print("Global:", x)

# Eg - In a user authentication component, you might have modules like user_registration.py, user_login.py, and user_profile.py.


# INTERFACES - points of interaction between different components or modules. They specify how different parts of the system communicate with each other.
# APIs: define how different parts of a system interact programmatically.
# Contracts: Interfaces act as contracts, ensuring that components or modules adhere to specified methods and data formats.
# Abstraction: Interfaces provide an abstraction layer, hiding the implementation details of a component or module.
# Eg - An interface for a payment processing component might define methods like process_payment(), refund_payment(), and get_payment_status().


''' Example of SD'''

def sd_webapp():
    '''System Architecture
        Architecture: The system follows a microservices architecture. Each service is responsible for a specific business domain.
        Technologies: Django for the main web application, Celery for background tasks, PostgreSQL for database, and REST APIs for communication between services.
    
    Components
        Authentication Service: Manages user login, registration, and authentication.
        Payment Service: Handles payment processing, refunds, and payment status.
        Notification Service: Manages sending emails and push notifications.
    
    Modules
        Authentication Service:
            user_registration.py: Handles user registration.
            user_login.py: Manages user login.
            token_management.py: Manages JWT tokens.
        Payment Service:
            payment_gateway.py: Integrates with external payment gateways.
            transaction_management.py: Manages payment transactions.
            refund_processing.py: Handles refunds.
            
    Interfaces
        Authentication Service API:
            POST /register: Registers a new user.
            POST /login: Logs in a user and returns a token.
            GET /user: Returns authenticated user details.
        Payment Service API:
            POST /process: Processes a payment.
            POST /refund: Initiates a refund.
            GET /status: Gets the status of a payment.'''

# Understand the requirements: Gather requirements by consulting stakeholders, reviewing documentation, and analyzing business processes.
# Define the system architecture: Identify major components and their interfaces based on the requirements.
# Choose the technology stack: Select programming languages, databases, frameworks, and libraries aligned with the requirements and architecture.
# Design the modules: Define the functions and data for each module within the system.
# Plan for scalability: Identify bottlenecks and design for handling increased loads.
# Consider security and privacy: Address potential security threats and ensure privacy in the system design.
# Test and validate: Develop test cases and scenarios to ensure the system meets the requirements.


'''Approach to a system design problem'''

# CONFUSION TO START
# When you are given a System Design Problem, you should approach it in a planned manner.
# Initially, the Problem may look huge, and one can easily get confused about how to start solving it.
# And moreover, there is no fixed solution while you are designing a system.
# There is more than one way to reach the Solution.

# 1. Breakdown the Problem
# break into small components. These components can be Services or Features which you need to implement in the System.
# Initially, a System can have many features,
#        and you are not expected to design everything if it’s an Interview.
# Ask your interviewer about the Features you are planning to put in your system. 
#        Is there anything else you should be putting there? Any Feature? Any Service? … Ask!

# 2. Communicating your Ideas
# While designing the system keep interviewer/client in the loop.
# Discuss your process out loud.
# Try to demonstrate your design clearly on the whiteboard with flowcharts and diagrams.
# Describe how you have planned to tackle the problem of scalability, 
#          how you will be designing your database, and many others.

# 3. Assumptions that make sense
# To assume the number of requests the system will be processed per day, the number of database calls made in a month, or the efficiency rate of your Caching System. 
# These are some of the numbers you need to assume while designing. Try to keep these numbers as reasonable as possible. 
# Back up your assumption with some solid facts and figures. (Research competitors in a prototype level as per features)


# Reliability in System Design
#     meets end-user requirements and delivers planned features without degradation.
#     Fault Tolerance: A system remains reliable even when faults come/are there in components.
#         Fault: Errors in components.
#         Failure: The system can't perform as expected.

# Availability in System Design
#     ensures agreed level of operational performance (uptime).
#     Importance:
#         High: Critical for hospitals, data centers, and banking where delays can cause significant losses.
#         Moderate: Acceptable delays in non-critical systems like social media.
#     Principles:
#         Avoid single points of failure - not be dependent on a single service in order to process all of its requests. 
#               Because when that service fails then your entire system will end up becoming unavailable.
#         Detect and resolve failures at that point.

# Scalability in System Design
#     system’s ability to handle increasing loads. 
#     If told to desin for X, then Design for 10X expected load, test for 100X.
#           can expect a spike in the load during a Flash Sale or when a new Product is Launched for sale.
#     To ensure scalability you should be able to compute the load that your system will experience.
#     Factors Affecting Load: Daily request volume, Number of database calls, Cache hit/miss requests ratio, Number of currently active users.....

# Points to consider - 
# Scalability: handle increased loads and scale horizontally or vertically as needed.
# Performance: perform efficiently and effectively, with minimal latency and response time.
# Reliability: reliable and available, with minimal downtime or system failures.
# Security: designed with security in mind, including measures to prevent unauthorized access and protect sensitive data.
# Maintainability: easy to maintain and update, with clear documentation and well-organized code.
# Interoperability: work seamlessly with other systems and components, with clear and well-defined interfaces.
# Usability: user-friendly and intuitive, with a clear and consistent user interface.
# Cost-effectiveness: cost-effective, minimizing development and operational costs while still meeting the requirements.

# Advantages of designing a software system - 
# Improved Efficiency: automating repetitive tasks, reducing errors, and increasing productivity.
# Scalability: scale up or down as needed to accommodate changes in business requirements or user demand.
# Improved User Experience: easier for users to accomplish their goals and increasing user satisfaction.
# Better Security: implementing best practices for security and data protection.
# Better Integration: easily integrate with other systems or applications, improving interoperability and reducing complexity.

# Disadvantages - 
# Increased Complexity: more difficult to design, develop, and maintain.
# Increased Cost: requiring significant resources and expertise.
# Longer Development Time: longer to develop than a simpler system, potentially delaying the delivery of the system.
# Higher Risk of Failure: more prone to failure, requiring additional resources to diagnose and fix issues.
# Difficulty in Adapting to Change: difficult to modify or adapt to changing business requirements or technology trends.


'''Availability'''

# readiness and accessibility of a system or service to users at any given time.
# measures the percentage of time a system remains operational and usable.
# achieved through redundancy, fault tolerance, and efficient recovery mechanisms.
# measured as a percentage and is often expressed in terms of “uptime” versus “downtime” over a given period.

# UX: Systems that are frequently unavailable or experience downtime frustrate users and may lead to dissatisfaction,
# Business continuity: maintaining business continuity and ensuring uninterrupted operations. 
#       to deliver services or conduct transactions, even brief periods of downtime can result in significant financial losses, damage to reputation, and legal liabilities.

# Service Level Agreements (SLAs): commit to specific availability targets through SLAs. Failure to meet SLAs can result in financial penalties or contractual obligations.
# Competitive Advantage: differentiate in uptime critical businesses. Better availability attracts and retains customers, providing a market edge.
# Disaster Recovery: High availability includes redundancy, failover mechanisms, and disaster recovery plans to withstand and recover from unexpected events 
#     like hardware failures, network outages, natural disasters, or cyberattacks.
# Regulatory Compliance: regulations mandating minimum system availability. Non-compliance can lead to legal consequences, fines, or sanctions.


# How to Achieve High Availability
# Redundancy: Employing redundant components or servers ensures that if one fails, another can take over seamlessly.
#     implemented at various levels, including hardware, networking, and data centers.
# Load Balancing: Distributing incoming requests across multiple servers or resources prevents overload on any single component.
# Failover Mechanisms: Implementing automated processes to detect failures and switch to redundant systems without manual intervention.
# Disaster Recovery (DR): Having a comprehensive plan to recover the system in case of a catastrophic event affecting the primary infrastructure.
# Monitoring and Alerting: Implementing robust monitoring systems to detect issues in real-time. Notifying administrators promptly to take appropriate action.
# Performance Optimization: Ensuring the system designed and tuned to handle expected loads efficiently.
# Scalability: to scale easily by adding more resources as needed. Accommodates increased demand.











