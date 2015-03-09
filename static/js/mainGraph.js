(function() {
  requirejs.config({
    baseUrl : '/blog/js',
    paths : { 'require' : '.' }
  });

  var canvas = document.getElementById('graphCanvas');
  var wrapper = document.getElementById('canvasWrapper');
  canvas.height = wrapper.clientHeight;
  canvas.width = wrapper.clientWidth;


  requirejs(['graph/generate'], function(generateGraph) {
    var bgColour = window.getComputedStyle(document.body).backgroundColor;
    generateGraph({
      canvas: 'graphCanvas',
      graph: {
        node: {
          fillColour: bgColour,
          colour: '#bc74ff'
        }
      }
    });
  });
})();
