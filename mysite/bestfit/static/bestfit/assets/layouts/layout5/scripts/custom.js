// 1nd section prev-next

$(function(){
  var $cur = $('#group .current');
  var $questions = $('#group .question');
  
  function hideButtons() {
    $cur = $('#group .current');
    var index = $cur.index();
    if(index > 0) {
      $('#prev').show();
    } else {
      $('#prev').hide();
    }
    
    if(index < $questions.length - 1) {
      $('#next').show();
    } else {
      $('#next').hide();
    }  
  }
  
  hideButtons();
  
  $('#next').click(function(){
    $cur.next().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
  $('#prev').click(function(){
    $cur.prev().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
});

// 2nd section prev-next

$(function(){
  var $cur = $('#queGroup .current');
  var $questions = $('#queGroup .question');
  
  function hideButtons() {
    $cur = $('#queGroup .current');
    var index = $cur.index();
    if(index > 0) {
      $('#preev').show();
    } else {
      $('#preev').hide();
    }
    
    if(index < $questions.length - 1) {
      $('#nexxt').show();
    } else {
      $('#nexxt').hide();
    }
  }
  
  hideButtons();
  
  $('#nexxt').click(function(){
    $cur.next().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
  $('#preev').click(function(){
    $cur.prev().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
});

// 3rd section prev-next

$(function(){
  var $cur = $('#queList .current');
  var $questions = $('#queList .question');
  
  function hideButtons() {
    $cur = $('#queList .current');
    var index = $cur.index();
    if(index > 0) {
      $('#pre').show();
    } else {
      $('#pre').hide();
    }
    
    if(index < $questions.length - 1) {
      $('#nex').show();
    } else {
      $('#nex').hide();
    }
  }
  
  hideButtons();
  
  $('#nex').click(function(){
    $cur.next().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
  $('#pre').click(function(){
    $cur.prev().addClass('current');
    $cur.removeClass('current');
    hideButtons();
  });
});

// data title

 $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
 });


// Face Reactions

$(".otro").faceMocion();
$('.prueba').faceMocion();