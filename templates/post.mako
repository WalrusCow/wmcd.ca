<%inherit file="base.mako"/>

<%block name="content">
<main class="flex-center">
<div class="post content">
<h1 class="mainTitle">${title}</h1>

<div class="subtitle">
<p class="author">${author}</p>
<p class="date">${timestamp}</p>
</div>

<div class="post-body">
${body}
</div>

</div>
</main>
</%block>

<%block name="styles">
<link href="/css/post.css" rel="stylesheet"/>
</%block>
