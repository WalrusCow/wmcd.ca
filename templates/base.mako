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

<main class="flex-center">

<div class="main-content">
<div class="content nav-container">
<span class="nav-item">William McDonald</span>
<ul class="nav-menu">
<li class="nav-item"><a href="/blog">Blog</a></li>
<li class="nav-item"><a href="/code">Code</a></li>
<li class="nav-item"><a href="https://github.com/WalrusCow/">GitHub</a></li>
</ul>
</div>

<%block name="content"/>
</div>
</main>
</div>
</body>

<script src="/js/lib/requirejs/require.js"></script>
<script src="/js/graphMain.js"></script>
<%block name="scripts"/>
</html>
