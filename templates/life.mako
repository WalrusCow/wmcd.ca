<%inherit file="base.mako"/>

<%block name="content">
<div class="content">
<h2>Conway's Game of Life</h2>
<p>If you haven't heard of Conway's Game of Life before, you should read
<a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">the Wikipedia
article</a>, which does a good job at describing what it is.</p>
<p>Alternatively, you can just start clicking on the canvas below. Press
play once you have some squares and see what happens!</p>
<p>And a <a href="https://github.com/WalrusCow/canvas">link to the source</a>
for the curious. You can find it under <code>scripts/life.js</code>.</p>

<div class="game">
<canvas id="Life-canvas" height="300" width="200">Please use a
modern browser to see it in action.</canvas>

<br/>
<button class="game-control" id="Life-start">Play</button>
<button class="game-control" id="Life-stop">Pause</button>
<button class="game-control" id="Life-clear">Reset</button>
<br/>
<input type="range" id="Life-speed" value="4" min="1" max="10"/>
</div>

</div>
</%block>

<%block name="scripts">
<script data-main="/js/lifeMain.js", src="/js/require.js"></script>
</%block>
