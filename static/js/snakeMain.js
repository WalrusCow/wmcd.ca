require(['/js/config.js'], function() {
  requirejs.config({
    paths : {
      'snake': 'lib/snake'
    }
  });

  requirejs(['snake/snake'], function(SnakeGame) {
    new SnakeGame();
  });
});
