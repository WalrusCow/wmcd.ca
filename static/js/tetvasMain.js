require(['/js/config.js'], function() {
  requirejs.config({
    paths : {
      'tetvas': 'lib/tetvas/tetvas'
    }
  });

  requirejs(['tetvas/tetvas'], function(Tetvas) {
    new Tetvas();
  });
});
