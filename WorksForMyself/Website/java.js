function klo(){
        $('#tree').data('price', '25');
        console.log($('#tree').data('price'));
        $('#tree').data('id', '5');
        console.log($('#tree').data('id'));
        document.getElementById('srty').style.display = "block";
          document.getElementById('main').style.width = "0px";
          document.getElementById('main').style.height = "0px";
          document.getElementById('wrapper1').style.display = "none";
      }
 function poty1() {
  let d = document,
      g = d.getElementById("org"),
      f = d.getElementById("red"),
      j = d.getElementById("wrapper1"),
      o = d.getElementById("ujpo");
  g.style.background = "none";
  g.style.position = "absolute";
  g.style.top = "105px";
  g.style.background = "white";
  g.style.overflow = "hidden";
  g.style.bottom = "auto";
  j.style.display = "none";
  f.style.width = "100%";
  g.style.margin = "0% 10%";
  o.style.display = "block";
  d.getElementById("srty").style.display = "none";
  d.getElementById("la34").style.display = "none";
}
function poty2() {
  let d = document,
    j = d.getElementById("wrapper1");
    j.style.display = "flex";
}
function asdf() {
            setInterval(function() {
                      document.getElementById('sad2').style.display = "block";
                      document.getElementById('sad2').style.display = "none";
                    }, 3000);
            document.getElementById('sad2').style.display = "block";
          }
function asdf1() {
            setInterval(function() {
                      document.getElementById('sad3').style.display = "block";
                      document.getElementById('sad3').style.display = "none";
                    }, 3000);
            document.getElementById('sad3').style.display = "block";
          }
$(function() {
                  'use strict';
                  // инициализация плагина
                  $.jqCart({
                    buttons: '.add_item',
                    buttons1: '.add_item1',
                    handler: './php/handler.php',
                    cartLabel: '.label-place',
                    visibleLabel: true,
                    openByAdding: false,
                    currency: 'грн;'
                  });
                  // Пример с дополнительными методами
                  $('#open').click(function() {
                    $.jqCart('openCart'); // открыть корзину
                  });
                  $('#open1').click(function() {
                    $.jqCart('openCart'); // открыть корзину
                  });
                  $('#clear').click(function() {
                    $.jqCart('clearCart'); // очистить корзину
                  });
                });
function eee() {
  window.href("https://www.dveri-optom.com/index2.html","_self");
}
function poty20() {
  window.href("https://www.dveri-optom.com/index.html","_self");
}
function openModal() {
  document.getElementById('myModal').style.display = "block";
  document.querySelector('body').style.overflow = "hidden";
}
function closeModal() {
  document.getElementById('myModal').style.display = "none";
  document.querySelector('body').style.overflow = "scroll";
}
var slideIndex = 1;
showSlides(slideIndex);
function plusSlides(n) {
  showSlides(slideIndex += n);
}
function currentSlide(n) {
  showSlides(slideIndex = n);
}
function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}
function myFunctio() {
                  var input, filter, ul, li, a, i;
                  input = document.getElementById("myInput");
                  filter = input.value.toUpperCase();
                  ul = document.getElementById("wrapper1");
                  li = ul.getElementsByClassName("item_box");
                  for (i = 0; i < li.length; i++) {
                    a = li[i].getElementsByClassName("item_title")[0];
                    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                      li[i].style.display = "";
                    } else {
                      li[i].style.display = "none";

                    }
                  }
                }
function qws() {
            document.getElementById('sw').style.display = "flex";
            document.querySelector('body').style.overflow = "hidden";
          }
function pppp() {
                document.getElementById('sw').style.display = "none";
                document.querySelector('body').style.overflow = "scroll";
              }
function dfg() {
  document.getElementById('w1').style.background = "green";
}
