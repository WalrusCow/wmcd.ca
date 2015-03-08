<%inherit file="base.mako"/>

<%block name="content">
<div class="flex-center">
  <div class="write content">
    <input name="title" form="postForm" type="text"
           required="true" placeholder="Title"/>
    <br/>
    <textarea name="body" form="postForm" required="true" rows="30"
              id="input" cols="80" placeholder="Write something..."> </textarea>

    <br/>
    <form id="postForm" action="/blog/post" method="post">
      <input type="hidden" name="author" value="William McDonald"/>
      <input type="submit" value="Post"/>
    </form>
  </div>

  <div class="post content" id="output">
    Write something...
  </div>
</div>
</%block>

<%block name="scripts">
<script src="/blog/js/lib/markdown.min.js"></script>
<script src="/blog/js/write.js"></script>
</%block>
