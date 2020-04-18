# Question history mockup

## Overview
This is a simple proof-of-concept web service that:
- Lets you create questions which can be answered by users
- Lets you edit existing questions
- Tracks question change history so you view changes across time

It may or may not have been created and published here as part of a job interview.

To avoid unneccesary re-invention of wheels, I used django with the [django-simple-history](https://django-simple-history.readthedocs.io/) package to handle the guts of the history tracking. 

The project took approximately 11 hours to complete (see "Challenges" below).

# Demo

1. Copy/paste the following into a shell running `bash` on a system with django and python3 installed:

    ```bash
    ( set -xe   # be verbose, stop if any command fails
    git clone https://github.com/usernamenumber/floaty_takehome
    cd floaty_takehome
    pip3 install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py loaddata fixtures/demo.json
    python3 manage.py runserver
    )
    ```
2. Point your browser at http://localhost:8000
3. You should see a pre-populated question. Click the `History` link to see its revisions.
4. (optional) Add your own questions and revisions
5. (optional) Go to http://localhost:8000/admin/chatbot/answer/add/ (login admin:admin) to add answers, albeit via an awkward auto-generated interface

# Notes
## Challenges
I haven't used django in many years, so probably 50% of the time spent on this project was (re-)reading documentation to get back up to speed (some big things have changed - they have migrations built-in now!!).

The part of the project that went through the most revision was probably the code that became `chatbot/templatetags/diff_filter.py`, not because of the code its self, which was easy enough to base on [the difflib `SequenceMatcher` docs](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.get_opcodes), but because I couldn't settle on where it made the most sense to put it. At first it was a method on the `HistoricalQuestion` model, but I didn't like having a model output HTML. I then moved it to a helper function in `chatbot.util` (which no longer exists), but that just obfustaced the problem rather than moving the HTML to the presentation layer. I settled on creating a custom filter, though I dislike that that solution required creating an awkward `previous_and_current_text` on the Model to get content for the filter.

## Succcesses
Despite the learning curve, I'm happy with the result. Thanks to `SequenceMatcher` I was able to make a much fanicer diff than I thought I would, and even had time to add some styling. I think I made the right call by not implementing the history tracking myself.  

## What I would have done with more time
Lots, but off the top of my head...
- _**Docstrings!**_
- _**Tests!**_
- Look for more opportunities to save work by using pre-existing django packages like [the django REST framework](https://www.django-rest-framework.org/)
- Consolidate views, i.e. add the `question_create` form to the bottom of the `question_list` view. 
- Add a non-admin interface for answering questions
- Add support for tagging questions, and maybe answers, with arbitrary metadata
