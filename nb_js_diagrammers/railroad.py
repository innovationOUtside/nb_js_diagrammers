TEMPLATE_RAILROADJS = """
<!doctype html>
<html>
<head>
<script src="https://tabatkins.github.io/railroad-diagrams/railroad-diagrams.js">
<link href="https://tabatkins.github.io/railroad-diagrams/railroad-diagrams.css" rel=stylesheet>


<script type=module>
//import rr, * as rrClass from "./railroad.js";
//Object.assign(window, rr);
//window.rrOptions = rrClass.Options;

function process(input) {
	if(!input) input = find('.input').value;
	const standalone = True;
	try {
		var result = eval(input).format();
		location.hash = "#" + encodeURIComponent(input);
	} catch (e) {
		find('.output-text').textContent = "Invalid input.\n" + e
		throw e;
	}
	find('.output-image').innerHTML = '';
	result.addTo(find('.output-image'));
}

process(`{src}`)
</script>

<style>
@media all and (min-width: 400px) {
	html, body { margin: 0; padding: 0; height: 100%; }
	body {
		display: grid;
		grid-template:
			"input  code" 1fr
			"output info" 1fr
			/ 1fr   1fr;
	}
}
.input {
	grid-area: input;
}
.output-text {
	grid-area: code;
}
.output-image {
	grid-area: output;
}
.info {
	grid-area: info;
}
</style>
</head
<body>
<div class='output-image'></div>
</body></html>
"""