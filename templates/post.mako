<%inherit file="base.mako"/>

<%block name="content">
<div class="post content">
<h1 class="mainTitle">${title}</h1>
<div class="subtitle">${timestamp}</div>
<hr>

<div class="post-body">
${body}
</div>

</div>
</%block>

<%block name="styles">
<link href="/css/post.css" rel="stylesheet"/>
</%block>
