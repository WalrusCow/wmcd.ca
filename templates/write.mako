<%inherit file="base.mako"/>

<%block name="content">
<div class="flex-center">
  <div class="write content">
    <input id='titleInput' name="title" form="postForm" type="text"
           required="true" placeholder="New Post"/>
    <br/>
    <textarea name="body" form="postForm" required="true" rows="30"
              id="bodyInput" cols="80" placeholder="Write something..."></textarea>

    <br/>
    <form id="postForm" action="/blog/post" method="post">
      <input type="hidden" name="author" value="William McDonald"/>
      <input type="submit" value="Post"/>
    </form>
  </div>

  <div class="post content">
    <h1 class="mainTitle" id="titleOutput">New Post</h1>
    <div class="subtitle">March 15, 2015</div>
    <hr>
    <div class="post-body" id="bodyOutput">
      Write something...
    </div>
  </div>
</div>
</%block>

<%block name="scripts">
<script src="/js/lib/markdown/markdown.min.js"></script>
<script src="/js/write.js"></script>
</%block>
