# ----------------------------- Project Todo list ---------------------------- #
# TODO Project Todo list

'''
    # Models
    # Signals
'''











# -------------------------- Adding Multiple Workers ------------------------- #
# NOTE Adding multiple workers
'''
So you want a Procfile like so:

capture: node capture.js
process: node process.js
purge: node purge.js
api: node api.js
web: node web.js

You can then scale each process separately:

$ heroku ps:scale purge=4

'''
