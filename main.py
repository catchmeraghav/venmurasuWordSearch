
import os
import time
import sys
sys.path.insert(0, '../venmurasu code/')
from makeCollections import makeWordSearch

from app import app
from forms import SearchForm
from flask import flash, render_template, request, redirect

@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search, results='')


@app.route('/results', methods=['POST'])
def search_results(search):
    start = time.time()
    search = SearchForm(request.form)
    search_string = search.data['search'].encode('utf-8')
    results = makeWordSearch( search_string )
    stop = time.time()
    
    results += "\n\n ... it took "+ str(stop - start) + " seconds"
    if not isinstance( results, str):
        results = ''
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        return render_template( 'index.html', form = search, results = results )

if __name__ == '__main__':
    import os
    app.run(port=5001)
