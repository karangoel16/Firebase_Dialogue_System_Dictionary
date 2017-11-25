var wordnet = require('wordnet');


wordnet.lookup('ace', function(err, definitions) {
  var a=""
  //console.log(definitions[0]["glossary"])
  definitions[0].meta.words.forEach(function(word)
  {
    a+=word.word+"; ";
  })
  //console.log(a);
  /*definitions.forEach(function(definition) {
    //console.log('  words: %s', words.trim());
    console.log('  %s', definition.glossary);
  });*/

});

var wn= require("wordnetjs")

var antonyms=""
wn.antonyms("hard").forEach(function(word){
  word["words"].forEach(function(val){
    antonyms+=val+";"
  })
})

console.log(antonyms)