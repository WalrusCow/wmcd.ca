require(['/js/config.js'], function() {
  requirejs.config({
  urlArgs: 'v=2',
    paths : {
      'snake': 'lib/snake'
    }
  });

  requirejs(['snake/snake'], function(SnakeGame) {
    new SnakeGame({
      // Colors should match the site eh?
      snakeOptions: {
        blockConfig: {
          fill: '#ff9800'
        },
        foodConfig: {
          fill: '#00bcd4'
        }
      }
    });
  });
});
