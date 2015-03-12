require(['/js/config.js'], function() {
  requirejs.config({
    paths : {
      'life': 'lib/life'
    }
  });

  requirejs(['life/life'], function(Life) {
    new Life();
  });
});
