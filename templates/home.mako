<%inherit file="base.mako"/>

<%block name="content">
<div class="content">
<h1>Recent Posts</h1>

% for post in posts:
${makePost(post)}
% endfor

<hr>
<div class="flex-sides">
<div>
% if nextOffset is not None:
<a class="older-posts" href="/blog/?offset=${nextOffset}">Older posts</a>
% endif
</div>

% if prevOffset is not None:
<a class="newer-posts" href="/blog/?offset=${prevOffset}">Newer posts</a>
% endif
</div>
</%block>

<%def name="makePost(post)">
<div class="post-list">
<h2 class="post-title"><a href="/blog/post/${post['id']}">${post['title']}</a></h2>
<span>(${post['timestamp']})</span>
</div>
</%def>
