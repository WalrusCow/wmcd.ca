require(['/js/config.js'], function() {
  requirejs.config({
  urlArgs: 'v=2',
    paths : {
      'tetvas': 'lib/tetvas/tetvas'
    }
  });

  requirejs(['tetvas/tetvas'], function(Tetvas) {
    new Tetvas();
  });
});
