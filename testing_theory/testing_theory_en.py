"""
1. Software Testing 🔗
    — checking the conformity between actual and expected behavior.
    — is one of the quality control techniques, including activities on:
        Test Management (work planning)
        Test Design (test design)
        Test Execution (test execution)
        Test Analysis (test results analysis)

   Software Quality
    — is a set of software characteristics related to its ability to satisfy stated and expected needs.

2. Validation vs Verification 🔗
    Verification
    — assessment of product compliance with requirements (specifications).
    Answers the question: “Does the system work in accordance with the requirements?”

    Validation
    — assessment of product compliance with user expectations and requirements.
    Answers the question: “Do the requirements meet user expectations?”

3. Purpose of testing 🔗
    — To increase the probability that the application under test will work correctly under all conditions.
    — Increase the probability that the application intended for testing will meet all the described requirements.
    — Providing up-to-date information about the current state of the product.

4. Stages of testing 🔗
    — Product analysis
    — Working with requirements
    — Test plan development
    — Creation of test documentation
    — Testing
    — Test report
    — Stabilization
    — Operation

5. Test plan 🔗
    Test Plan is a document describing the entire scope of testing work
    Answers the questions:
        What?
        When?
        Testing start/end criteria.
        Environment dev/staging/production?
        Testing approaches/techniques/tools/types?
        Browsers/versions/OS/screen resolutions?
        Who? Responsibilities? Resources? Training?
        Deadlines?
        Schedule?
        Testing strategy.
        Links to documentation.
        Links to requirements.

6. Test design 🔗
    Test design is a stage of the software testing process where test cases are designed and created, in accordance
    with the quality criteria and testing objectives.
        — Test analyst - defines "WHAT to test?"
        — Test designer - defines "HOW to test?"
        — Reality - 1 person does everything :)

7. Test design techniques 🔗
    1. Equivalence Partitioning
        As an example, you have a range of acceptable values from $1.00 to $10.00, you should choose any one correct
        value inside the interval, say 5.00, and any incorrect values outside the interval, such as 0.99 and 11.00.

    2. Boundary Value Analysis
        As an example, you have a range of acceptable values from $1.00 to $10.00.
        Two value (two-digit) BVA: valid boundary values are 1.00, 10.00, and invalid values are 0.99 and 10.01.
        Three/Full value (three-digit) BVA: valid boundary values are 1.00, 1.01, 10.00, 9.99,
        and invalid values are 0.99 and 10.01.

    3. Cause / Effect
        Enter combinations of conditions (causes) to get a response from the system (effect).
        For example, you are checking the ability to add a client:
        Cause: you must fill in the fields "Name", "Address", "Phone Number" and click the "Add" button.
        Effect: After clicking the "Add" button, the system adds the client to the database and displays his number
        on the screen.

    4. Error Guessing
        Using system knowledge and the ability to interpret the specification (requirements) to "guess" under what
        input conditions the system may return an error.
        For example, the specification says: "the user must enter a code."
        The tester will think: "What if I do not enter the code?", "What if I enter the wrong code?"...

    5. Pairwise Testing
        Formation of such sets of test data in which each tested value of each of the tested parameters is combined
        at least once with each tested value of all other tested parameters. Sounds complicated, but in practice,
        using this technique is very simple and logical.The essence of the technique is that we do not check all
        combinations of all values, but we check ALL PAIRS of values.

    6. Decision table
        Decision tables present a set of conditions, the simultaneous fulfillment of which should lead to a certain
        action/decision.

    7. State Transition diagram
        A diagram for describing the behavior of a system.
        The system has a finite number of states and transitions between states.
        The diagram can be translated into a State Transition Table (or a decision table).

    8. Use case (user scenario)
        This is a scenario of user interaction with the system to achieve a specific goal.
        Use case contains:
        - who uses the system (for example, the role of admin/buyer/seller).
        - what the user wants to do.
        - user goals.
        - steps that the user takes.
        - description of how the system reacts to user actions.

8. Exploratory vs Ad-hoc testing_theory 🔗
    Exploratory testing (exploratory testing_theory)
        This is the simultaneous study of the system, test design and testing itself.
        This technique is based on the tester's experience (experience based).
        Example: a tester comes to a new project and begins to simultaneously study the site,
        write a checklist and go through this checklist (test).

    Ad-hoc testing
        Translation from the author of the article - "testing off the cuff".
        A type of testing that is performed without preparing for tests, without defining expected results,
        without designing test scenarios.
        Informal, improvisational testing.

9. Test Case (test case) 🔗
    is a test artifact/document describing a set of steps, specific conditions and parameters
    necessary to test the function being tested.
    is a description of the system operation test that can be performed by any person from the team.
    is a description of the system test for compliance with requirements.
    A test case consists of:
        ID
        Title
        Type
        Priority
        Preconditions
        Steps
        Expected Result
        Post conditions - for example, clearing data or returning the system to its original state.

    Test cases are divided into positive and negative:
        A positive test case uses only correct data and checks that the application has correctly
        executed the called function.

        A negative test case operates with both correct and incorrect data (at least 1 incorrect parameter)
        and aims to check for exceptional situations (validator triggering), and also checks that the function
        called by the system is not executed when the validator is triggered.

10. Checklist 🔗
    — This is a document describing what should be tested.
        A checklist can be of absolutely different levels of detail.
        As a rule, a checklist contains only actions (steps) without the expected result.
        A checklist is less formalized than a test case.
        A checklist is much easier to maintain than test cases.
        Checklist items answer the question “what to test?”, and specific steps and details “how to test?”
        are described in test cases.

11. Bug report 🔗
    — This is a document describing the sequence of actions that led to incorrect operation of the system,
    indicating the reasons and the expected result.
    The main components of a Bug report are:
        ID
        Title
        Summary
        Project
        Component
        Version
        Severity
        Priority
        Status
        Author
        Assignee
        Environment: dev/test/staging/prod/etc.
        App/build version
        Steps to Reproduce
        Actual Result
        Expected Result

    Additional components of a Bug report are:
        Screenshots
        Video
        Credentials (login + password)
        Browser console errors
        Mobile (app logs)
        Server )logs server)
        API Requests (API requests)
        Analytics events (events from analytics)
        Database data (data from the database)

        Database queries (queries to the database)
        Date and time (date and time)
        Comments/Notes (comments/notes)

        Link tasks/bugs (linking other tasks/bugs to the current one)
        HAR archive - an archive with all requests in the Network

12. Severity vs Priority 🔗
    Severity
        - This is an attribute that characterizes the impact of a defect on the performance of the application.
        In theory, Severity is set by the tester.
            Severity gradation:
            S1 Blocker
            S2 Critical
            S3 Major
            S4 Minor
            S5 Trivial

    Priority
        - This is an attribute that indicates the order of task execution or defect elimination.
        The higher the priority, the faster the defect needs to be fixed.
        In theory, Priority is set by the manager, team leader or customer.
        Priority gradation:
            P1 High
            P2 Medium
            P3 Low

    Reality: on all the projects where I worked, there was only priority :)
    Reality: different projects have different gradations.

13. Traceability matrix (Requirements compliance matrix) 🔗
    - This is a two-dimensional table containing the compliance of functional requirements and test cases.
    The table column headers contain requirements, and the row headers contain test case IDs.
    At the intersection, there is a mark indicating that the requirement of the current column is covered by the
    test scenario of the current row.

14. Defect / Error / Bug / Failure 🔗
    Bug (defect)
        is a discrepancy between the actual result and the expected result described in the requirements.
        - a programmer's (or other team member's) error, that is, when something in the program does not go as planned
        and the program gets out of control.

        For example, when user input is not controlled in any way, as a result, incorrect data causes crashes
        or other "jokes" in the program's operation. Or the program is built in such a way that it initially does
        not correspond to what is expected of it.

    Error (error)
        — an action that led to an incorrect result.
        Example 1 — entering letters in fields that require numbers (age, quantity of goods, etc.).
        Error: “the field must contain only numbers.”
        Example 2 — registering with an email that already exists in the system. Error: “this email is already in use.”

    Failure
        — a failure (not necessarily hardware-related) in the operation of a component, the entire program,
        or the system.

    That is, there are defects that lead to failures.
    And there are those that do not. UI defects, for example. But a hardware failure that is not related
    o software is also a failure.

15. Levels of testing_theory 🔗
    1. Unit Testing         the code of classes, functions, modules in the code. Usually performed by programmers.

    2. Integration Testing
        Testing the interaction between several classes, functions, modules.
        For example, testing API via Postman.

    3. System Testing
        Checking both functional and non-functional requirements for the system.

    4. Acceptance Testing
        Checking the system's compliance with the requirements and is carried out with the purpose of:
        - determining whether the system meets the acceptance criteria;
        - making a decision by the customer/manager whether to accept the application or not.

16. Testing types 🔗
    1. Functional testing types
        Functional testing_theory
        GUI testing
        Security and Access Control Testing
        Interoperability testing

    2. Non-functional testing types
        All types of performance testing:
        - Load testing - many users.
        - Stress Testing - lots of data and/or users (peak values).
        - Volume Testing - lots of data.
        - Stability / Reliability Testing
        Installation testing_theory
        Usability Testing
        Fail-over and Recovery Testing
        Configuration Testing

    3. Change-related testing
        Smoke Testing
        Regression Testing
        Re-testing_theory
        Build Verification Test
        Sanity Testing

17. Principles of testing_theory 🔗
    1. Testing shows presence of defects
        Testing can show that defects are present in the system, but it cannot prove that they are not.

    2. Exhaustive testing_theory is impossible
        Complete testing using all combinations of inputs and preconditions is physically impossible,
        except in trivial cases.

    3. Early testing_theory
        To find defects as early as possible, testing activities should be started as early as possible
        in the development life cycle.

    4. Defects clustering
        Typically, most of the defects found during testing are contained in a small number of modules.

    5. Pesticide paradox
        If the same tests are run many times, eventually that set of test cases will no longer find new defects.

    6. Testing is context dependent
        Testing is performed differently depending on the context.

    7. Absence-of-errors fallacy
        Detecting and fixing defects will not help if the created system does not suit the user and does
        not meet his expectations and needs.

18. Static and dynamic testing 🔗
    Static testing
        Is performed WITHOUT running the program code.
        Examples: requirements/documentation testing, code review, static code analyzers.

    Dynamic testing
        Is performed WITH running the program code.

19. Requirements 🔗
    Requirements are a specification (description) of what needs to be implemented.
    Requirements describe what needs to be implemented, without detailing the technical side of the solution. “What”, not “how”.
    Requirements for requirements:
        - correctness
        - unambiguity
        - completeness
        - consistency
        - ordering by importance and stability
        - testability
        - modifiability
        - traceability
        - understandability

20. Software Development Life Cycle 🔗
    Software Development Life Cycle (SDLC):
        - Idea
        - Planning and Requirement Analysis
        - Defining Requirements
        - Design Architecture
        - Developing
        - Testing
        - Deployment
        - Maintenance
        - Death

21. Development Methodologies 🔗
    - Waterfall
    - V-model
    - Spiral
    - Kanban
    - Scrum
    - Scrum-ban


The Agile principle is a set of practices for prompt response to changes during the work process.
Such approaches help to quickly respond to feedback from clients and representatives who are steadily improving
the product. Principles of the manifesto: https://agilemanifesto.org/iso/uk/principles.html
    Values of Agile
        1. People are important for processes and tools
        2. Products are important for the resulting documentation
        3. Management is important sha for agreeing on a contract
        4. Preparedness before changes is important for following the plan.
    The essence of the Agile Manifesto
        1. All work on the project is divided into short cycles (iterations) and is carried out in stages;
        2. At the end of the skin iteration, the assistant removes the finished minimally working product and its part,
           which can already be processed;
        3. Throughout the entire work process, the team works with the assistant;
        4. Any changes in the project are implemented and quickly integrated into the work.


The SCRUM approach communicates with each other to the development team, Product Owner and Scrum Master at every
stage of software development.
The essence of this framework:
    - Work is divided into sprints of stages 1-4
    - Before the start of the sprint, the team itself forms a list of tasks for iteration
    - During the sprint, a product and service are created that can be demonstrated to the client
    - Meetings that help in cesi robots: Generous stand-up , Planning, Retrospective and Sprint Review.
    - Basic roles:
        Scrum-master (helps to identify blockers, monitors the progress of Scrum)
        Product Owner (sets priorities and goals for the sprint)


KANBAN
Kanban is a way of properly adjusting the process to minimize the risk of skin inflammation as effectively
as possible. The approach allows you to optimize the work of the team through the separation of volumetric
stages around the operation.
The Kanban system is based on the principles:
    - Visualization.
        The basis of Kanban is a visual board, which represents the stages of composing a flow task:
        “planned” / “committed” / “detailed”.
    - I disintegrated the estate.
        Having a clear understanding of your goals will make the process easier.
    - Focus on robots.
        If the process takes longer, it is necessary to connect additional satellites and redistribute resources.

Main features:
    - There may be no sprints in Kanban. Assignments and priorities can be changed during the course of work,
      just as in Scrum - only until the start of the upcoming sprint.
    - There are no such roles in Kanban as in Scrum. Maybe only the team and Tech Lead.
    - In Scrum, meetings are obligatory, but in Kanban they are not.
"""