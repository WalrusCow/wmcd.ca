<%inherit file="base.mako"/>

<%block name="content">
<main>

<h1>Recent Posts</h1>

% for post in posts:
${makePost(post)}
% endfor

</main>
</%block>

<%def name="makePost(post)">
<div class="post">
<h2><a href="/post/${post['id']}">${post['title']}</a></h2>
<p class="date">${post['timestamp']}</p>
</div>
</%def>
