<h1>Lily-Lang</h1>
<img src="pic.png" width="100" height="100">
<h3>This is the repository for my compiler, I am mostly using it to store my progress on learning about compiler engineering.</h3>

List of additions:
  - Symbol Table(Currently only works for variables since the compiler doesnt support other stuff yet)
  - Added check(if) Statements(when there is one inside another it raises a bug I still have to fix)!
  - Organized Folders
  - Finished Variables, Fully Working Assignements Now :)
  - Added Variables(value cant be changed after initialization, however in the near future I will fix that)
  - Added setmem, a Function That Lets You Directly Set An Integer Value To a Memory Address(with it, I added my first own argument parsing, MAKE SURE YOU KNOW THE MEM ADDR YOU ARE USING IS ACCESSIBLE OR YOU WILL GET A SEG FAULT AND YOUR PROGRAM WILL STOP)
  - Print Is Now Working(kinda because the arguments aren't parsed yet, **treat them like C**)!
  - Now Keeping Track Of Lines(for future error handling)
  - Started working on the print keyword(only detecting it for now, hardest thing until now)!
  - Organized some small stuff for optimization
  - File Opening Error Handling(Small Addition).
  - Compilation Choices Involving GCC(Only works on linux yet)
  - Optimization, Organization, and added comments(pain in the ass)
  - Simple Binary Expressions

TODO:
  - Add Support For The Compilation Choices In Windows
  - Work On The Documentation
  - Fix The Check Statement
  - Add The Else Statement
  - Add The While Loop
  - Functions And Function Calls(Add Type Inference to the data types of the functions)
  - Error Management 💀
  - Hand Written Code Optimizer(Optimizes the C Code, not Assembly)
