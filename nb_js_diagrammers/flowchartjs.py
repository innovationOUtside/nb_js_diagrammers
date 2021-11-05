TEMPLATE_FLOWCHARTJS = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Flowchart.js</title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.14.1/flowchart.js"></script>
        </head>
        <body>
         
        <div id="diagram"></div>
<script>
  var diagram = flowchart.parse(`{src}`);
  diagram.drawSVG('diagram');
</script>
 
        </body>
</html>
"""