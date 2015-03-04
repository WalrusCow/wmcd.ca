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
<h2 class="inline"><a href="/post/${post['id']}">${post['title']}</a></h2>
<span>(${post['timestamp']})</span>
</div>
</%def>
