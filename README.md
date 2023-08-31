<h1>Lily-Lang</h1>
<img src="pic.png" width="100" height="100">
<h3>This is the repository for my compiler, I am mostly using it to store my progress on learning about compiler engineering.</h3>

List of additions:
  - Added variables(value cant be changed after initialization, however in the near future I will fix that)
  - Added setmem, a function that lets you directly set an integer value to a memory address(with it, I added my first own argument parsing, MAKE SURE YOU KNOW THE MEM ADDR YOU ARE USING IS ACCESSIBLE OR YOU WILL GET A SEG FAULT AND YOUR PROGRAM WILL STOP)
  - Print is now working(kinda because the arguments aren't parsed yet, **treat them like C**)!
  - Now Keeping Track Of Lines(for future error handling)
  - Started working on the print keyword(only detecting it for now, hardest thing until now)!
  - Organized some small stuff for optimization
  - File Opening Error Handling(Small Addition).
  - Compilation Choices Involving GCC(Only works on linux yet)
  - Optimization, Organization, and added comments(pain in the ass)
  - Simple Binary Expressions
