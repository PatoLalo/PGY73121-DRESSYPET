$(document).ready(function() {
    $.ajax({
      url: "https://maps.googleapis.com/maps/api/js?key=AIzaSyD-q3q95sDNygTrEFgnS0PGfCk8LeZCE8w&callback=initMap&libraries=places,geometry&solution_channel=GMP_QB_locatorplus_v6_cA",
      type: "GET",
      dataType: "script",
      success: function() {
        initMap();
      },
      error: function() {
        console.error("Error al cargar la API.");
      }
    });
  });
  
function initMap() {
  // Coordenadas de la dirección
  var coordenadas = { lat: -33.6793871, lng: -71.1948636 };

  // Configuración del mapa deseado
  var mapOptions = {
    center: coordenadas,
    zoom: 19
  };

  // Crear el mapa y asignarlo al elemento de HTML con el id "mapa"
  var map = new google.maps.Map(document.getElementById("mapa"), mapOptions);

  // Crear un marcador en las coordenadas especificadas
  var marker = new google.maps.Marker({
    position: coordenadas,
    map: map,
    title: "Pudeto 18, Melipilla, Región Metropolitana, Chile"
  });

  // Crear una ventana de información para mostrar la descripción
  var infoWindow = new google.maps.InfoWindow({
    content: "<div class='info-window'>Pudeto 18, Melipilla, Región Metropolitana, Chile</div>",
    pixelOffset: new google.maps.Size(0, -40) // Ajusta la posición del globo de diálogo
  });

  // Mostrar la ventana de información automáticamente
  infoWindow.open(map, marker);
}
