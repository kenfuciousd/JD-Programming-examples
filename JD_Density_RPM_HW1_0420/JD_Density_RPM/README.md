# Density On Prem Homework Assignment

## Goal
Your goal is to show how you would package and deliver the applications in this repo in a reproducible way.  

## Assignment
Your task is to accomplish the following:

- Package the applications in this repo into a format deliverable on RHEL 6/7/8 systems
- Your package should install all necessary dependencies
- Your package should include start / stop scripts for both applications

## Don't Let the Dog Eat Your Homework

For delivery of this assignment, we'd like to see:

- An rpm SPEC file for each application
- A Makefile automating the build process
- A Virtual Machine template for testing the built packages
- Documentation on how you would:
  * Deliver the final packages to a client
  * Document a strategy for building update packages (e.g., how would you specify code versions, especially across repos)
  * What tools or methods you would lean on for remote support of these applications once installed

Create a new repo using your Github account with a unique name and send us the final product!


## Notes

- Please do not fork or submit a PR to this repo
- Please document your thought-processes and use well-written git commit messages to show your progress
- Feel free to change the python application and its requirements in any way you see fit
- We are purposefully not being overly prescriptive in this assignment, as we want you to think creatively about the solution
- This assignment should take less than 5 hours to complete
- If you get stuck or need more information, please reach out for clarity
- Have fun!

## Getting Started in Local Development

Please create and source your virtualenv before beginning. 

Running the apps locally:
```
pip install -r requirements.txt
sqlite3 database.db < schema.sql
python app_a.py
python app_b.py
```

Making a request
```
curl -X POST -H 'Authorization: mytoken' http://127.0.0.1:5000/jobs
```
