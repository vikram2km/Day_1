Day-4:
    Date: 27/FEB/2026
    Phase:0

    Concepts Covered- 
        ✅ Abstraction
                __init__ vs class body
                Instance variables vs class variables
                self (what it actually is)
                Object lifecycle
        ✅ Dependency Injection
        ✅ ABC, abstractmethod
        ✅ Composition

       
    Problems Solved:
        ✅ Problem 1 — Extensible ETL Framework (Improved Version)
            1️⃣ Create abstract base classes:
                    BaseExtractor
                    BaseTransformer
                    BaseLoader
            2️⃣ Concrete implementations:
                    ListExtractor (returns mock list)
                    RemoveDuplicatesTransformer
                    ConsoleLoader (prints rows)
            3️⃣ Pipeline class:
                    Accept base types
                    Run extract → transform → load
            4️⃣ Add new transformer:
                    MultiplyByTwoTransformer
       