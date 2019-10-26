#!/bin/python3

"""
This presentation is powered by *remark.js* in-browser presenation from markdown
see more <https://github.com/gnab/remark>
this python script just save you from copy and paste from markdown doc to html file
double-click the resulted html file to view the presentation
or server the html pages by "using_http_server = True" if you link to local files in this folder
"""

import sys, datetime
from string import Template  #

input = "Cpp for Scientists and Engineers.md"  # path to markdown file
output = "index.html"  # this may be served as http server
title = "C++ for Scientists and Engineers (draft)\n for Software Carpentry Training"
using_http_server = False
PORT = 8000

date = datetime.date.today()
author = "Qingfeng Xia"
more_info = """ Senior Research Software Engineer<br/>
Culham Centre for Fusion Energy, UKAEA<br/>
github: https://github.com/qingfengxia<br/>
"""

title_section=f"""
#{title}
<br/>
**{author}**
<br/>
<br/>
{more_info}
<br/>
{date}
---
"""

preample=Template("""
<!DOCTYPE html>
<html>
  <head>
    <title>$title</title>
    <meta charset="utf-8">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
      @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
      @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

      h1, h2, h3 {
        font-family: 'Yanone Kaffeesatz';
        font-weight: normal;
        margin-top: 5px;
        margin-bottom: 5px;
        text-decoration: underline;
        text-decoration-color: blue;
      }
      body {
        font-family: 'Droid Serif';
        line-height: 1.6;
      background-image: url('https://software-carpentry.org/assets/img/logo-white.svg');
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: right top;
      }
      .remark-slide-content {font-size: 25px; }
      .remark-code {overflow: scroll}
      .remark-inline-code { font-family: 'Ubuntu Mono'; }
    </style>
  </head>
  <body>
    <textarea id="source">
class: center, middle
""").substitute(title=title)

closing="""
    </textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js">
    </script>
    <script>
        var slideshow = remark.create({
          // Set the slideshow display ratio,  Default: '4:3' ,
          ratio: '16:9',  // Alternatives: '16:9', ...
          navigation: {
            // Enable or disable navigating using scroll , Default: true
            scroll: true,

            // Enable or disable navigation using touch,  Default: true
            touch: true,

            // Enable or disable navigation using click.  Default: false
            click: false,
          },

          // Customize slide number label, either using a format string..
          slideNumberFormat: 'Slide %current% of %total%',
          // .. or by using a format function
          slideNumberFormat: function (current, total) {
            return 'Slide ' + current + ' of ' + total;
          },

          // Enable or disable counting of incremental slides in the slide counting
          countIncrementalSlides: true,

          // Read source markdown for slides from URL (local or external) instead
          // of the textarea with id="source"
          // Default: undefined
          // Alternatives: 'some_file.md', 'https://example.host.com/file.md', ...
          sourceUrl: undefined
        });
    </script>
  </body>
</html>
"""

with open(output, "w") as outf:
    outf.write(preample)
    outf.write(title_section)
    with open(input, "r") as f:
        outf.write(f.read())
    outf.write(closing)

if using_http_server:
    if sys.version_info[0]<3:
        print("python -m SimpleHTTPServer")
    else:
        #print("server this folder by command")
        #print("python3 -m http.server 8000")
        import http.server
        import socketserver

        print("visit the page at: http://127.0.0.1:8000/")
        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()




