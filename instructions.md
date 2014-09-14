Efsharp Problem - Nathaniel
====================
...

Getting The Repo
----------
This solution uses Python, some common Python packages (within a _virtualenv_ and installed with _pip_), the Flask micro/web/framework, and PhantomJS. To get rolling, you'll need to clone/pull the repo into your directory of choice:

	git clone git@bitbucket.org:efsharp/interview-problem-nathaniel.git

If you've already done this, you'll just need to pull the most recent commits down, and I assume you know how to do this :-)

Virtualenv
----------
This instruction assumes you have the necessary sotware to use _Python_, _virtualenv_, etc. 

	cd /path/into/repo
	virtualenv .
	. bin/activate
	pip install -r requirements.txt
	

Running the Server
----------
To view the page locally, run from within the root directory of the project:
	
	python app.py

 You should see something like this in the console.:

	* Running on http://0.0.0.0:5005/

 Proceed to [http://0.0.0.0:5005/](http://0.0.0.0:5005/) and the page/form should load.
 
 