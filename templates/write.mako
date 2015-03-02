<%inherit file="base.mako"/>

<%block name="content">
<main class="flex-center">
  <div class="write">
    <input name="title" form="postForm" type="text"
           required="true" placeholder="Title"/>
    <br/>
    <textarea name="body" form="postForm" required="true" rows="30"
              cols="80" placeholder="Write something..."> </textarea>

    <br/>
    <form id="postForm" action="/post" method="post">
      <input type="hidden" name="author" value="William McDonald"/>
      <input type="submit" value="Post"/>
    </form>
  </div>

  <div class="preview">
    This will be the preview area!
  </div>
</main>
</%block>

<%block name="scripts">
<script src="/js/write.js"></script>
</%block>

<%block name="styles">
<link href="/css/write.css" rel="stylesheet"/>
</%block>
