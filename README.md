# resume-parser

## Questions
1. **What is your domain?**
   The domain that we chose was application filter. It takes resumes, which can number in the tens of thousands, and widdles them down to only those who have the required skills for the position.

2. **What is the task you are performing?**
   Each task consists of parsing a resume from a directory and then looking for some keywords in it. Currently, it’s only looking for the following keywords: Java, Python.

3. **Why does it take long?**
   It takes a long time because processing files when the number of said files is only capped by how much disk space you have on your machine.

4. **How do you split work among the various threads?**
   We used queues in that as soon as a thread becomes free it takes another resume from the queue and processes it.

5. **How do you deal with individual threads finishing their original tasks?**
   We use the Executors framework to handle threads. This internally uses a Blocking Queue. All the resumes are pushed into the queue while each thread is reading a file from the queue. Once a thread finishes reading a file from the queue, it automatically starts picking another file from the queue, this goes on until all the resumes in the queue are read completely.

6. **How much faster is the task performed with 10 threads vs 1? (If you cannot perform the task with 1 thread due to it taking too long, this is ok)**
   We could see a difference of 3X. The time taken by 10 threads was hovering around 300 milliseconds, whereas the time taken by 1 thread was around 1000 milliseconds.

7. **How long does it take the task to complete?**
   With 10 threads and 1000 resumes, it takes 300 milliseconds. But if you put a different upper bound for the script that generates the resumes, it will take longer.

## Parts
### App.java
   Responsible for setup and driving of the system. A FileProcessor object is generated for each file in the generated resume directory. 10 threads are made and set to pull from a queue containing all the FileProcessor objects. The threads are then invoked and set to scraping the resumes.

### FileProcessor.java
   Represents a resume to be scraped as well as the logic to do it. FileProcessor objects know the path to the file that they are responsible for as well as the keywords they are looking for. When it gets passed to a thread to be run, the file is opened, then the keywords are searched. If found, then a copy of the resume will be placed in the valid resume directory.

### createResumes.py
   Responsible for generating the resumes. This is not run every time but if increasing the number of generated resumes is needed, running this script will do so. This might be desirable because the benefits of using multiple threads become more apparent when more files are used.

## Requirements
- Gradle (Install Gradle extension for Java in VSCode)
- Python
- Java

## How to Run
### Resume generation Python
 .\createResumes.py 10000 (optional there are 9999 pre-generated) 
### Resume scraping 
Use IDE (Visual Studio Code is recommended) to run App.java

