from flask import Flask

app = Flask(__name__)


@app.route('/')
def start_page():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                   <title>Startpage</title>
                    <style>
                    html {
                        background:url(static/img/main_pic.png) no-repeat center center fixed;
                         -webkit-background-size:cover;
                         -moz-background-size:cover;
                         -o-background-size:cover;
                         background-size: cover;
                          }
                    .button {
                        border: none;
                        outline: none;
                        display: inline-block;
                        text-align: center;
                        text-decoration: none;
                        margin-top: 150px;

                        cursor: pointer;
                        font-size: 16px;
                        font-family: ar_Aquaguy;
                        padding: 20px 26px;
                        border-radius: 150px;
                        color: #000;
                            }
                    .button i {
                        margin-right: 4px;
                               }
                    .button + .button {
                        margin-left: 6px;
                                      }
                    .button.pink {
                        background: #f9a1e0;
                                 }
                    .button.yell {
                         background: #f9e6a1;
                                   }
                    .button.mint {
                         background: #a1f9ba;
                                   }

                    .button:hover {
                         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
                                  }
                    .button:hover.pink {
                         background: #fbb9e8;
                                       }
                    .button:hover.yell {
                         background: #fbecb9;
                                          }
                    .button:hover.mint {
                         background: #b9fbcc;
                                          }
                    .button:active {
                         box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
                         text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
                                   }
                    .under {
                        display: inline-block;
                        margin-top: 380px;
                        margin-right: 30px;
                           }
                    .text {
                        margin-top: 150px;
                        margin-right: 30px;
                          }
                    </style>
                  </head>
                  <body>
                   <h1 class="text" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                   size=7><center>НАЗВАНИЕ ПОТОМ ПРИДУМАЕМ</center></font></h1>
                   <h2 style="text-align:center; font-family: AnotherCastle3"><font color="#a1f9ba" 
                   size=5>Этот проект является<br>
                   новым взглядом на прекрасную игру - heartstone компании Bilzard</font></h2>
                   <p style="text-align:center; font-family: AnotherCastle3;"><font color="#a1f9ba" 
                   size=5>В игре зарегистрировано уже больше 10000000 человек<br>
                   Мы уже десять лет на рынке<br>это все опыт, который очень важен в нашей сфере</font></p>
                   <div style="text-align:center;">
                    <button id="login" class="button pink">
                     <i class="fa fa-unlock"></i>
                     <span>Войти в аккаунт</span>
                    </button>
                    <a class="button yell" href="http://127.0.0.11:8000/wikipedia">
                     <i class="fa fa-user-plus"></i>
                     <span>Игровая википедия</span>
                    </a>
                    <a class="button mint" href="" download=les.png>
                     <i class="fa fa-user-plus"></i>
                     <span>Установить игру</span>
                    </a>
                    <div>
                     <div class="under"><a href="https://vk.com/chainblubler"><img src="static/img/vk.png" width="50" 
                     height="50"></a></div>
                     <div class="under"><a href="https://vk.com/hellother"><img src="static/img/vk.png" width="50" 
                     height="50"></a></div>
                     <div class="under"><a href="https://www.instagram.com/_just_roman__/"><img src="static/img/inst.png" 
                     width="50" height="50"></a></div>
                     <div class="under"><a href="https://www.instagram.com/chainloverrr/"><img src="static/img/inst.png" 
                     width="50" height="50"></a></div>
                    </div>
                   </div>
                  </body>
                </html>'''


@app.route('/wikipedia')
def wiki():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                   <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                   <title>Startpage</title>
                    <style>
                    body {
		                background: url(static/img/main_pic.png) no-repeat center center fixed; 
		                -webkit-background-size:cover;
                        -moz-background-size:cover;
                        -o-background-size:cover;
                        background-size: cover;
                    </style>
                  </head>
                  <body>
                   <h1 style="text-align:center; font-family: Fita Vjaz;"><font color="#00ff7f" 
                   size=7><center>Wikipedia</center></font></h1>
                   <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
                   integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" 
                   crossorigin="anonymous"></script>
                   <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
                   integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" 
                   crossorigin="anonymous"></script>
                   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
                   integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" 
                   crossorigin="anonymous"></script>
                   <div id="carousel-example-generic" class="carousel slide" data-ride="carousel" 
                   style="text-align:center;">
                    <ol class="carousel-indicators">
                     <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                     <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                     <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                    </ol>
                    <div class="carousel-inner" role="listbox" style="text-align:center;">
                     <div class="carousel-item active">
                      <img src="static/img/mars1.jpg" alt="1">
                     </div>
                     <div class="carousel-item" style="text-align:center;">
                      <img src="static/img/mars2.jpg" alt="2">
                     </div>
                     <div class="carousel-item" style="text-align:center;">
                      <img src="static/img/mars3.jpg" alt="3">
                     </div>
                    </div>
                    <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
                     <span class="icon-prev" aria-hidden="true"></span>
                     <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
                     <span class="icon-next" aria-hidden="true"></span>
                     <span class="sr-only">Next</span>
                    </a>
                   </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.16')