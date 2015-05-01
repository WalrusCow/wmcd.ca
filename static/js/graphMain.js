require(['/js/config.js'], function() {
  var canvas = document.getElementById('graphCanvas');
  var wrapper = document.getElementById('canvasWrapper');
  canvas.height = wrapper.clientHeight;
  canvas.width = wrapper.clientWidth;

  requirejs.config({
  urlArgs: 'v=2',
    paths : {
      'graph': 'lib/graph'
    }
  });

  requirejs(['graph/generate'], function(generateGraph) {
    var bgColour = window.getComputedStyle(document.body).backgroundColor;
    var graph = generateGraph({
      canvas: 'graphCanvas',
      graph: {
        node: {
          fillColour: bgColour,
          colour: '#bc74ff'
        }
      }
    });

    var ctx = canvas.getContext('2d');
    window.addEventListener('resize', function() {
      ctx.clearRect(0,0,canvas.height, canvas.width);
      canvas.height = wrapper.clientHeight;
      canvas.width = wrapper.clientWidth;
      graph.draw(ctx);
    });
  });
});
