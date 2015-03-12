require(['/js/config.js'], function() {
  var canvas = document.getElementById('graphCanvas');
  var wrapper = document.getElementById('canvasWrapper');
  canvas.height = wrapper.clientHeight;
  canvas.width = wrapper.clientWidth;

  requirejs.config({
    paths : {
      'graph': 'lib/graph'
    }
  });

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
});
