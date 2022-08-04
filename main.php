<?php?>
<!DOCTYPE HTML>
<html lang=EN>
    <header>
        <meta charset="UTF-8">
        <meta name="keywords" content="HTML, CSS, JavaScript">
        <meta name="description" content="Free Web tutorials">
        <meta name="author" content="KUN">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <base href="https://www.mymemolist.com/" target="_blank">
        <link rel="stylesheet" href="styles.css">
    </header>
    <body>
    <div class="slideshow-container">

    <div class="mySlides fade">
      <div class="numbertext">1 / 3</div>
      <img src="city.jpeg" style="width:100%">
      <div class="text">Caption Text</div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">2 / 3</div>
      <img src="umi.jpeg" style="width:100%">
      <div class="text">Caption Two</div>
    </div>
    <a class="prev" onclick="plusSlides(-1)">❮</a>
    <a class="next" onclick="plusSlides(1)">❯</a>

    </div>
    <br>

    <div style="text-align:center">
      <span class="dot" onclick="currentSlide(1)"></span> 
      <span class="dot" onclick="currentSlide(2)"></span> 
      <span class="dot" onclick="currentSlide(3)"></span> 
    </div>

    </body>
</html>