Efsharp/Nathaniel : Solution Overview
====================
...

General Thinking
----------
This was an interesting problem, mostly because I couldn't shake the thought that there's some simple solution that exists for some cool, if arcane, javascript-family framework. But after a bit of research, I didn't uncover anything clever, and I took to heart the section of the instructions that said:

> This should be implemented in a language with which you are familiar

So, having used a lot of Javascript, and Python- and having written some automated tests with PhantomJS, I tried to make a minimal yet functional schema that solved for the requirements.

The Components
---------
The basic components are:

* **Flask**: Provides the minimal server. Flask is a micro-webdev framework written in Python, and has minimal, sensible architecture. This should be run locally within a `virtualenv` directory.
*  **Bootstrap Template**: I had recently purchased a couple of _Bootstrap_-based templates from [http://wrapbootstrap.com](http://wrapbootstrap.com) and grabbed the HTML, CSS, and some javascript animations from one, just to provide a nicer "skin" to the solution.
*  **Form**: While the instructions directed me towards an AJAX solution, I did make the form functional without javascript with an "action" parameter. Otherwise the submit is, as usual, captured by a small jQuery function which does some minimal checking before submitting, via AJAX POST, to the processing page, subsequently processing the result.
*  **PhantomJS**: Using Python's `subprocess.Popen()` function, the Flask server page kicks off an os/console command to the included `phantomjs` binary and waits for the result (piped in from stdout).
*  **Testing**: there's a minimal suite of tests, based off Flask's framework and Python's `unittest` library... which simply checks some known pages and confirms the return values.
*  **Error Checking**: There's some error checking/catching along the way, though this is an area that could do with some testing/improvement. Things like _empty urls_, _invalid urls_, _stderr output_ are accounted for, but there may be a wider variety of responses from the `phantomjs` execution than I experienced. 


The Future
----------
* It would have been nice to add some sort of animation while checking- something beyond the typical spinner.
* As mentioned before, reviewing more sites and examining the output might uncover some edge cases we can account for when processing the return from `phantomjs`
* From my early research, it seems there's exists a better relationship between `Node.js` and `phantomjs` (though they explicitly state that `phantomjs` is not available as an `npm` package, it seems there's a way to do it easily); given more time, I'd experiment with that configuration to see if I can avoid the somewhat awkward `subprocess.Popen()` path.

Thanks!
----------
In any case, it was fun and interesting. Let me know if you have any questions or would like to go over this in any more detail.

~~ _Nathaniel_


