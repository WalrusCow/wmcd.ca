require(['/js/config.js'], function() {
  requirejs.config({
  urlArgs: 'v=2',
    paths : {
      'life': 'lib/life'
    }
  });

  requirejs(['life/life'], function(Life) {
    new Life({
      cellFill: '#00bcd4'
    });
  });
});
