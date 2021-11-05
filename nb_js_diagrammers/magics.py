from IPython.core.magic import Magics, magics_class, cell_magic, line_cell_magic, needs_local_scope
from IPython.core import magic_arguments

import io
import uuid
from pathlib import Path
from IPython.display import IFrame

from .flowchartjs import TEMPLATE_FLOWCHARTJS
from .wavedrom import TEMPLATE_WAVEDROM
from .wavesurfer import TEMPLATE_WAVESURFERJS
from .mermaid import TEMPLATE_MERMAIDJS

from pyflowchart import Flowchart
 
def js_ui(data, template, out_fn = None, out_path='.',
          width="100%", height="", **kwargs):
    """Generate an IFrame containing a templated javascript package."""
    if not out_fn:
        out_fn = Path(f"{uuid.uuid4()}.html")
         
    # Generate the path to the output file
    out_path = Path(out_path)
    filepath = out_path / out_fn
    # Check the required directory path exists
    filepath.parent.mkdir(parents=True, exist_ok=True)
 
    # The open "wt" parameters are: write, text mode;
    with io.open(filepath, 'wt', encoding='utf8') as outfile:
        # The data is passed in as a dictionary so we can pass different
        # arguments to the template
        outfile.write(template.format(**data))
 
    return IFrame(src=filepath, width=width, height=height)

@magics_class
class JSdiagrammerMagics(Magics):
    """Magics for Javascript diagramming."""
    def __init__(self, shell):
        super(JSdiagrammerMagics, self).__init__(shell)
 
    @line_cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--outfile', '-o', default=None, help='Output file.')
    @magic_arguments.argument(
        "--file", "-f", help="Source for audio file."
    )
    def wavesurfer_magic(self, line, cell=None):
        "Send code to wavesurfer.js."
        args = magic_arguments.parse_argstring(self.wavesurfer_magic, line)
        if not args.file:
            return
        return js_ui({"src":args.file}, TEMPLATE_WAVESURFERJS,
                     height=200, out_fn=args.outfile)
 
    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--outfile', '-o', default=None, help='Output file.')
    @magic_arguments.argument(
        "--height", "-h", default="300", help="IFrame height."
    )
    def mermaid_magic(self, line, cell):
        "Send code to mermaid.js."
        args = magic_arguments.parse_argstring(self.mermaid_magic, line)
        return js_ui({"src":cell}, TEMPLATE_MERMAIDJS,
                     height=args.height, out_fn=args.outfile)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--outfile', '-o', default=None, help='Output file.')
    @magic_arguments.argument(
        "--height", "-h", default="300", help="IFrame height."
    )
    def flowchart_magic(self, line, cell):
        "Send code to flowchart.js."
        args = magic_arguments.parse_argstring(self.mermaid_magic, line)
        return js_ui({"src":cell}, TEMPLATE_FLOWCHARTJS,
                     height=args.height, out_fn=args.outfile)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--outfile', '-o', default=None, help='Output file.')
    @magic_arguments.argument(
        "--height", "-h", default="300", help="IFrame height."
    )
    @magic_arguments.argument(
        "--execute", "-x", action="store_true", help="Execute code in cell"
    )
    @needs_local_scope
    def pyflowchart_magic(self, line, cell, local_ns=None):
        "Render flowchart based on an analysis of Python code in code cell."
        args = magic_arguments.parse_argstring(self.pyflowchart_magic, line)
        if args.execute:
            exec(cell, self.shell.user_ns, local_ns)
        fc = Flowchart.from_code(cell)
        return js_ui({"src":str(fc.flowchart())}, TEMPLATE_FLOWCHARTJS,
                     height=args.height, out_fn=args.outfile)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--outfile', '-o', default=None, help='Output file.')
    @magic_arguments.argument(
        "--height", "-h", default="300", help="IFrame height."
    )
    def wavedrom_magic(self, line, cell):
        "Send code to flowchart.js."
        args = magic_arguments.parse_argstring(self.mermaid_magic, line)
        return js_ui({"src":cell}, TEMPLATE_WAVEDROM,
                     height=args.height, out_fn=args.outfile)
 