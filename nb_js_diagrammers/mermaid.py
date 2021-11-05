TEMPLATE_MERMAIDJS = """<html>
    <body>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
 
        <div class="mermaid">
            {src}
        </div>
 
    </body>
</html>
"""