<html>
<head>
<title>${title}</title>
<%block name="styles"/>
<link href="/css/main.css" rel="stylesheet"/>
</head>

<body>
<div id="canvasWrapper">
  <canvas id="graphCanvas">Please use a modern browser</canvas>
</div>

<div class="wrapper">

<div class="flex-center">
<div class="content">
<span class="nav-item">William McDonald</span>
<ul class="nav-menu">
<li class="nav-item"><a href="/">Blog</a></li>
<li class="nav-item"><a href="/">Code</a></li>
<li class="nav-item"><a href="/">GitHub</a></li>
</ul>
</div>
</div>

<main class="flex-center">

<div class="main-content">
<%block name="content"/>
</div>
</main>
</div>
</body>

<%block name="scripts"/>
<script data-main="/js/mainGraph.js" src="/js/require.js"></script>
</html>
