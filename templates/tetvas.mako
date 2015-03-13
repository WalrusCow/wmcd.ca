## -*- coding: utf-8 -*-
<%inherit file="base.mako"/>

<%block name="content">
<div class="content">
<h2>Tetvas</h2>
<p>It's just a Tetris clone. I created it with my favourite keybindings - sorry
if they don't match your expectations!</p>
<p>Use ↑ and Z to rotate, shift to hold and ctrl to drop. Press P to pause the
game.</p>

<p>Check out the source <a href="https://github.com/WalrusCow/tetvas">on
GitHub</a>.</p>

<div class="game">
<canvas id="tetvas" tabIndex="1" height="354" width="330">Please use a
modern browser to see it in action.</canvas>

<br/>
<button class="game-control" id="tetvas-start">Play</button>
</div>

<%include file="code-footer.mako"/>
</div>
</%block>

<%block name="scripts">
<script src="/js/tetvasMain.js"></script>
</%block>
