(function() {
  requirejs.config({
    baseUrl : '/js',
    paths : { 'require' : '.' }
  });

  requirejs(['snake/snake'], function(SnakeGame) {
    new SnakeGame();
  });
})();
