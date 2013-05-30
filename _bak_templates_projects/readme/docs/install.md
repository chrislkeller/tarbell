# Install
*Clone repository, install virtual environment, install requirements, configure your system for Amazon S3, and run a test server.*

Tarbell is a Python library based on Flask which powers static sites. Truth be 
told, it doesn't do much on its own except read a directory and render templates
in any subdirectory it finds a `config.py` file. To see Tarbell in action, you 
should probably start with the Tarbell template, which sets up an Amazon S3
publishing workflow and basic framework for building modern web apps using 
Tarbell.

<div class="row-fluid">

<div class="span7">
<p>Make sure you have <code>python</code> (2.6+), <code>git</code>, <code>pip</code>, <code>virtualenv</code>
and <code>virtualenv-wrapper</code> installed on your system.</p>

<pre>git clone https://github.com/newsapps/tarbell
cd tarbell
mkvirtualenv tarbell
pip install -r requirements.txt
python runserver.py
</pre>

<p>Now visit <a href="http://localhost:5000/readme">http://localhost:5000/readme</a> in your browser. 
You should see the latest version of this page.</p>

</div>

<div class="span4 offset1 aside">
    <h2><i class="icon icon-question-sign"></i> How do I install these tools on my system?</h2>
    <p>For a very basic guide, see the <a href="https://hackpad.com/Install-Chicago-Birthrates-6V2O2Un04Ow">Chicago Birthrates installation docs</a>.</p>
    <p>For more detailed, Mac-specific information, see Brian Boyer's <a href="https://gist.github.com/brianboyer/1696819">Lion dev environment notes</a>.</p>
</div>

</div>
