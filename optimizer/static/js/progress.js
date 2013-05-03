function updateProgress(obj, percent) {
  $(obj).find('#number').text(percent+'%');
  $(obj).find('#progress-inner').transition({width:percent+'%'});
}

function getProgress(obj) {
  var text = $(obj).find('#number').text();
  var num = parseInt(text);
  return num;
}

function incrProgress(obj, incr) {
  var cur = getProgress(obj);
  updateProgress(obj, _.min([cur+incr, 100]));
}