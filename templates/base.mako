<html>
<head>
<title>${title}</title>
<%block name="styles"/>
<link href="/css/base.css" rel="stylesheet"/>
</head>

<body>
<div id="canvasWrapper">
  <canvas id="graphCanvas">Please use a modern browser</canvas>
</div>

<main class="flex-center">
<div class="main-content">
<h1>William's Blog</h1>

<%block name="content"/>
</div>
</main>
</body>

<%block name="scripts"/>
<script data-main="/js/mainGraph.js" src="/js/require.js"></script>
</html>
