(function() {
  requirejs.config({
    baseUrl : '/js',
    paths : { 'require' : '.' }
  });

  var canvas = document.getElementById('graphCanvas');
  var wrapper = document.getElementById('canvasWrapper');
  canvas.height = wrapper.clientHeight;
  canvas.width = wrapper.clientWidth;

  requirejs(['graph/generate'], function(generateGraph) {
    generateGraph({ canvas: 'graphCanvas' });
  });
})();
