require(['/js/config.js'], function() {
  var canvas = document.getElementById('graphCanvas');
  var wrapper = document.getElementsByClassName('page-header-wrapper')[0];
  canvas.height = wrapper.clientHeight;
  canvas.width = wrapper.clientWidth;

  requirejs.config({
  urlArgs: 'v=3'+new Date(),
    paths : {
      'graph': 'lib/graph'
    }
  });

  requirejs(['graph/generate'], function(generateGraph) {
    var graph = generateGraph({
      canvas: 'graphCanvas',
      graph: {
        node: {
          colour: '#eee'
        },
        edge: {
          colour: '#eee'
        }
      }
    });

    var ctx = canvas.getContext('2d');
    ctx.lineWidth=2;
    window.addEventListener('resize', function() {
      ctx.clearRect(0,0,canvas.height, canvas.width);
      canvas.height = wrapper.clientHeight;
      canvas.width = wrapper.clientWidth;
      graph.draw(ctx);
    });
  });
});
