<%inherit file="base.mako"/>

<%block name="content">
<div class="content">
<h2>Snake</h2>
<p>Most people have played snake before in some form or other.  If you don't
know how to play, it's very simple.  Using the arrow keys (or WSAD) to control
the "snake" (black thing), collect the food (red things) to grow longer.</p>
<p>You lose if the snake hits itself or any wall!</p>

<p>You can find <a href="https://github.com/WalrusCow/canvas">the source</a>
for the curious. You can find it under <code>scripts/snake.js</code>.</p>

<div class="game">
<canvas id="Snake-canvas" tabIndex="1" height="200" width="200">Please use a
modern browser to see it in action.</canvas>

<br/>
<button class="game-control" id="Snake-start">Play Snake</button>
</div>

</div>
</%block>

<%block name="scripts">
<script data-main="/js/snakeMain.js", src="/js/require.js"></script>
</%block>
