<%inherit file="base.mako"/>

<%block name="content">
<div class="post content">
<h1 class="mainTitle">${post['title']}</h1>
<div class="subtitle">${post['timestamp']}</div>
<hr>

<div class="post-body">
${post['body']}
</div>

<hr>

<div class="flex-sides post-footer">
<div class="prev-post">
% if prevPost is not None:
<a href="/blog/post/${prevPost['id']}">${prevPost['title']}</a>
<br/>
${prevPost['timestamp']}
% endif
</div>

% if nextPost is not None:
<div class="next-post">
<a href="/blog/post/${nextPost['id']}">${nextPost['title']}</a>
<br/>
${nextPost['timestamp']}
</div>
% endif
</div>

</div>
</%block>
