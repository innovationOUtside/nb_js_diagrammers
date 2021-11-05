TEMPLATE_WAVEDROM = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>wavedrom.js</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/skins/default.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/wavedrom.min.js" type="text/javascript"></script>
</head>
        <body onload="WaveDrom.ProcessAll()">
<script type="WaveDrom">
{src}
</script>
        </body>
</html>
"""