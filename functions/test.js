var wordnet = require('wordnet');


wordnet.lookup('ace', function(err, definitions) {
  var a=""
  definitions[0].meta.words.forEach(function(word)
  {
    a+=word.word+"; ";
  })
  console.log(a);
  /*definitions.forEach(function(definition) {
    //console.log('  words: %s', words.trim());
    console.log('  %s', definition.glossary);
  });*/

});
