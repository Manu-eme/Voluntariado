window.addEventListener('scroll', function() {
  var info = document.querySelector('.info');
  var infoPosition = info.getBoundingClientRect().top;
  var triggerPosition = window.innerHeight / 1; // Ajusta esto según tus necesidades

  if (infoPosition < triggerPosition) {
    if (window.innerWidth > 992) { // Pantallas grandes
      info.classList.add('animate-large');
    } else if (window.innerWidth >= 768) { // Pantallas medianas
      info.classList.add('animate-medium');
    } else { // Pantallas pequeñas (móviles)
      info.classList.add('animate-small');
    }
  } else {
    info.classList.remove('animate-large');
    info.classList.remove('animate-medium');
    info.classList.remove('animate-small');
  }
});


$(document).ready(function(){
  // Activar el carousel con un intervalo de 2000 milisegundos (2 segundos)
  $('.carousel').carousel({
    interval: 50
  });
});