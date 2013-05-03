points = 38; // start with 38 points
updatePointsInterval = 0;

function updatePoints(num) {
  $('#points').find('.number').text(num);
}

function getPoints() {
  return parseInt($('#points').find('.number').text());
}



function incrPoints(num) {
  clearInterval(updatePointsInterval);

  points += num;

  updatePointsInterval = setInterval(function() {
    var cur = getPoints();
    if (cur >= points) { clearInterval(updatePointsInterval); return };
    updatePoints(cur+1);
  }, 60);

}

