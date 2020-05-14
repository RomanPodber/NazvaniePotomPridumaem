from flask import Flask, redirect, render_template, request
from data import db_session
from data.users import RegisterForm, User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'z_k.,k._gbwwe'


@app.route('/')
def start_page():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                   <title>Startpage</title>
                    <style>
                    html {
                        background:url(static/img/main_pic2.png) no-repeat center center fixed;
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
                        font-family: AnotherCastle3;
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
                    .button.yell {
                         background: #f9e6a1;
                                   }
                    .button.mint {
                         background: #a1f9ba;
                                   }
                    .button:hover {
                         box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
                                  }
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
                        display: inline-table;
                        margin-top: 90px;
                           }
                    .text {
                        margin-top: 250px;
                        margin-right: 30px;
                          }
                    </style>
                  </head>
                  <body>
                   <h1 class="text" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                   size=7><center>НАЗВАНИЕ ПОТОМ ПРИДУМАЕМ</center></font></h1>
                   <h2 style="text-align:center; font-family: AnotherCastle3"><font color="#a1f9ba" 
                   size=5>Добро пожаловать<br>
                   Это основная страница нашего проекта.</font></h2>
                   <p style="text-align:center; font-family: AnotherCastle3;"><font color="#a1f9ba" 
                   size=5>В игре зарегистрировано уже больше 10000000 человек<br>
                   На этой странице вы можете установить игру, узнать о ней через нашу мини-Wiki,
                   <br>а так же зарегистрироваться
                   или войти уже в существующий аккаунт</font></p>
                   <p style="text-align:center; font-family: AnotherCastle3;"><font color="#a1f9ba" 
                   size=5>Предлагаю собственноручно опробовать возможности нашего сайта</font></p>
                   <div style="text-align:center;">
                    <a id="login" class="button yell" href="/reg">
                     <i class="fa fa-unlock"></i>
                     <span>Регистрация</span>
                    </a>
                    <a class="button yell" href="/wikipedia">
                     <i class="fa fa-user-plus"></i>
                     <span>Об игре</span>
                    </a>
                    <a class="button mint" href="https://drive.google.com/file/d/17GHaKUu6bIynaFVh8akSaja9I2C6vUj0/view">
                     <i class="fa fa-user-plus"></i>
                     <span>Установить игру</span>
                    </a>
                    <a class="button mint" href="/table">
                     <i class="fa fa-user-plus"></i>
                     <span>Таблица лидеров.</span>
                    </a>
                    <div>
                     <div class="under"><a href="https://vk.com/chainblubler"><img src="static/img/vk.png" width="25" 
                     height="25" style="position:absolute;left:25px;margin-top:30px"></a></div>
                     <div class="under"><a href="https://vk.com/hellother"><img src="static/img/vk.png" width="25" 
                     height="25" style="position:absolute;left:25px;margin-top:60px"></a></div>
                     <div class="under"><a href="https://www.instagram.com/chainloverrr/"><img src="static/img/inst.png" 
                     width="25" height="25" style="position:absolute;left:25px;margin-top:90px"></a></div>
                     <div class="under"><a href="https://www.instagram.com/_just_roman__/"><img src="static/img/inst.png" 
                     width="25" height="25" style="position:absolute;left:25px;margin-top:120px"></a></div>
                     <div class="under"><a href="https://github.com/RomanPodber/NazvaniePotomPridumaem">
                     <img src="static/img/github.png" width="25" height="25" 
                     style="position:absolute;left:65px;margin-top:30px;"></a></div>
                    </div>
                    <div>
                     <div style="position:absolute;left:350px;margin-top:30px">ООО DOL Tech Pictures 
                     Electronics International Inc Enterprise Mobile Company Group</div>
                     <div style="position:absolute;left:350px;margin-top:60px;">Совместно с кукольным заводом 
                     "Танцуй, Ваня"</div>
                     <div style="position:absolute;left:350px;margin-top:90px;">При поддержке правительства 
                     Татарстана</div>
                     <div style="position:absolute;left:970px;margin-top:90px">Создаем сайты</div>
                     <div style="position:absolute;left:970px;margin-top:30px;">Пишем музыку</div>
                     <div style="position:absolute;left:970px;margin-top:60px;">Профессиональные игроки в 
                     Rocket League</div>
                     <div style="position:absolute;left:1120px;margin-top:90px;">+7-800-555-35-35</div>
                     <div style="position:absolute;left:1120px;margin-top:120px;">Звонок платный</div>
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
		                 background: url(static/img/main_pic3.png) no-repeat;
                         -moz-background-size: 100%;
                         -webkit-background-size: 100%;
                         -o-background-size: 100%;
                         background-size: 100%;
                    .button {
                        border: none;
                        outline: none;
                        display: inline-block;
                        text-align: center;
                        text-decoration: none;
                        margin-top: 150px;
                        cursor: pointer;
                        font-size: 16px;
                        font-family: AnotherCastle3;
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
                        margin-top: 350px;
                        margin-right: 30px;
                           }  
                    </style>
                  </head>
                  <body>
                   <h1 class="under" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                   size=7><center>ОБ ИГРЕ</center></font></h1>
                   <h2 class="under" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                   size=7><center>Боевая система</center></font></h2>
                   <h2 style="display: inline-block; margin-top:50px margin-bottom:300px">
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:110px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Боевая система - это "изюминка" нашего проекта.<br>
                       Пользователь по мере продвижения по игровому процессу, <br>
                       Открывает новые заклинания, для активации которых игрок <br>
                       Должен самостоятельно вызвать магию в особом поле<br>
                       Для кастования магии нужна мана, очки которой рандомно появляются на поле</font></p>
                       <img src = "static/img/pattern.jpg" tab="photo" 
                       style="position:absolute;right:10px;top:150px" width=347 height=195>
                   </h2>
                   <h3 style="text-align:center; font-family: AnotherCastle3; margin-top:100px;"><font color="#00ff7f" 
                   size=7><center>История мира</center></font></h3>
                    <h3>
                       <p style="text-align:center; font-family: AnotherCastle3;left:10px;top:110px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Давным-давно в стране K (Казахстан), на город В (Варшава), напали властелины тьмы.<br>
                       Они убили всех, кроме главного героя, который из-за перенесенных ужасов (работал на угольных шахтах)
                       переродился в скелета и отправился мстить за свою семью.<br>
                       Ему предстоит пройти через множество испытаний, чтобы встретиться 
                       с властелином тьмы - самим воплощением ужаса.<p>
                    </h3>
                    <h2 class="under" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                   size=7><center>Персонажи и мобы</center></font></h2>
                   <h2 style="display: inline-block; margin-top:50px margin-bottom:300px">
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:110px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Охотник<br>
                       Это самый первый босс, он обрел свои способности благодаря укусу летучей мыши<br>
                       Здоровье: 25ед.<br>
                       Количество атак: 2шт.<br>
                       Опасность: Средняя<br>
                       Является стражем подземелья</font></p>
                       <img src = "static/img/boss1.png" tab="photo" 
                       style="position:absolute;right:10px;top:720px" width=250 height=250>
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:150px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Миньон лорда<br>
                       Самый верный слуга властелина тьмы, в прошлом - пекарь в захваченном городе<br>
                       Здоровье: 50ед.<br>
                       Количество атак: 2шт.<br>
                       Опасность: Высокая<br>
                       Любит солизняков.</font></p>
                       <img src = "static/img/boss2.png" tab="photo" 
                       style="position:absolute;right:10px;top:980px" width=250 height=250>
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:150px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Властелин тьмы<br>
                       Само воплощение зла, был партнером главного героя на шахтах<br>
                       Здоровье: 100ед.<br>
                       Количество атак: 3шт.<br>
                       Опасность: Пройти невозможно<br>
                       Жуткий тип. Само воплощение мрака и агрессии в нашем мире</font></p>
                       <img src = "static/img/boss3.png" tab="photo" 
                       style="position:absolute;right:10px;top:1240px" width=250 height=250>
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:150px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Слизняк<br>
                       Не самый легкий моб, друган Миньона<br>
                       Здоровье: 9ед.<br>
                       Количество атак: 1шт.<br>
                       Опасность: Низкая<br>
                       Скользкий тип, на первый взгляд безобидный моб, который может задать жару</font></p>
                       <img src = "static/img/mob1.png" tab="photo" 
                       style="position:absolute;right:10px;top:1500px" width=250 height=250>
                       <p style="text-align:left; font-family: AnotherCastle3;left:10px;top:150px margin-left:100px">
                       <font color="#a1f9ba" 
                       size=4.5>Летучая мышь<br>
                       Самый безобидный и простой противник<br>
                       Здоровье: 5ед.<br>
                       Количество атак: 1шт.<br>
                       Опасность: Очень низкая<br>
                       Самый простой, практически безобидный моб, с которым все-таки<br>
                       надо быть аккуратней.</font></p>
                       <img src = "static/img/mob2.png" tab="photo" 
                       style="position:absolute;right:10px;top:1740px" width=250 height=250>
                   </h2>
                   <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
                   integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" 
                   crossorigin="anonymous"></script>
                   <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
                   integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" 
                   crossorigin="anonymous"></script>
                   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
                   integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" 
                   crossorigin="anonymous"></script>
                   <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner" style="text-align:center">
                     <div class="carousel-item active">
                      <img src="static/img/1slide.jpg">
                     </div>
                     <div class="carousel-item">
                      <img src="static/img/2slide.jpg">
                     </div>
                     <div class="carousel-item">
                      <img src="static/img/3slide.jpg">
                     </div>
                     <div class="carousel-item">
                      <img src="static/img/4slide.jpg">
                     </div>
                    </div>
                    <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                     <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                     <span class="sr-only">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                     <span class="carousel-control-next-icon" aria-hidden="true"></span>
                     <span class="sr-only">Next</span>
                    </a>
                    <div>
                     <div style='text-align:center;size=6;margin-bottom:30px'>Слайдер</div>
                    </div>
                    <div style="text-align:center">
                     <a class="button mint" href="/">
                      <i class="fa fa-user-plus"></i>
                       <span>Вернуться в меню</span>
                     </a>
                    </div>
                    <div>
                     <div class="under"><a href="https://vk.com/chainblubler"><img src="static/img/vk.png" width="25" 
                     height="25" style="position:absolute;left:25px;margin-top:61px"></a></div>
                     <div class="under"><a href="https://vk.com/hellother"><img src="static/img/vk.png" width="25" 
                     height="25" style="position:absolute;left:25px;margin-top:91px"></a></div>
                     <div class="under"><a href="https://www.instagram.com/chainloverrr/"><img src="static/img/inst.png" 
                     width="25" height="25" style="position:absolute;left:25px;margin-top:121px"></a></div>
                     <div class="under"><a href="https://www.instagram.com/_just_roman__/"><img src="static/img/inst.png" 
                     width="25" height="25" style="position:absolute;left:25px;margin-top:151px"></a></div>
                     <div class="under"><a href="https://github.com/RomanPodber/NazvaniePotomPridumaem">
                     <img src="static/img/github.png" width="25" height="25" 
                     style="position:absolute;left:65px;margin-top:61px;"></a></div>
                    </div>
                    <div>
                     <div style="position:absolute;left:250px;margin-top:61px"><font color="black" size=4>
                     ООО DOL Tech Pictures Electronics International Inc Enterprise Mobile Company Group</div>
                     <div style="position:absolute;left:250px;margin-top:91px;"><font color="black" size=3>
                     Совместно с кукольным заводом 
                     "Танцуй, Ваня"</div>
                     <div style="position:absolute;left:250px;margin-top:121px;"><font color="black" size=3>
                     При поддержке правительства 
                     Татарстана</div>
                     <div style="position:absolute;left:970px;margin-top:151px"><font color="black" size=3>Создаем сайты
                     </font></div>
                     <div style="position:absolute;left:970px;margin-top:61px;"><font color="black" size=3>
                     Пишем музыку</div>
                     <div style="position:absolute;left:970px;margin-top:91px;"><font color="black" size=3>
                     Профессиональные игроки в Rocket League</div>
                     <div style="position:absolute;left:1120px;margin-top:121px;">+7-800-555-35-35</div>
                     <div style="position:absolute;left:1120px;margin-top:151px;">Звонок платный</div>
                    </div>
                   </div>
                  </body>
                </html>'''




@app.route('/congrats', methods=['GET', 'POST'])
def congrat():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                       <title>Startpage</title>
                        <style>
                        html {
                            background:url(static/img/main_pic2.png) no-repeat center center fixed;
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
                            font-family: AnotherCastle3;
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
                        .button.yell {
                             background: #f9e6a1;
                                       }
                        .button.mint {
                             background: #a1f9ba;
                                       }
                        .button:hover {
                             box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
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
                            margin-top: 150px;
                            margin-right: 30px;
                               }
                        .text {
                            margin-top: 250px;
                            margin-right: 30px;
                              }
                        </style>
                      </head>
                      <body>
                       <h1 class="text" style="text-align:center; font-family: AnotherCastle3;"><font color="#00ff7f" 
                       size=7><center>Вы успешно прошли регистрацию!<br>
                       Нажмите кнопку, чтобы вернуться в главное меню</center></font></h1>
                       <div style="text-align: center">
                        <a class="button yell" href="/">
                         <i class="fa fa-user-plus"></i>
                         <span>Вернуться в меню</span>
                        </a>
                        <div>
                         <div class="under"><a href="https://vk.com/chainblubler"><img src="static/img/vk.png" width="25" 
                         height="25" style="position:absolute;left:25px;margin-top:92px"></a></div>
                         <div class="under"><a href="https://vk.com/hellother"><img src="static/img/vk.png" width="25" 
                         height="25" style="position:absolute;left:25px;margin-top:122px"></a></div>
                         <div class="under"><a href="https://www.instagram.com/chainloverrr/"><img src="static/img/inst.png" 
                         width="25" height="25" style="position:absolute;left:25px;margin-top:152px"></a></div>
                         <div class="under"><a href="https://www.instagram.com/_just_roman__/"><img src="static/img/inst.png" 
                         width="25" height="25" style="position:absolute;left:25px;margin-top:182px"></a></div>
                         <div class="under"><a href="https://github.com/RomanPodber/NazvaniePotomPridumaem">
                         <img src="static/img/github.png" width="25" height="25" 
                         style="position:absolute;left:65px;margin-top:92px;"></a></div>
                        </div>
                        <div>
                         <div style="position:absolute;left:350px;margin-top:92px">ООО DOL Tech Pictures 
                         Electronics International Inc Enterprise Mobile Company Group</div>
                         <div style="position:absolute;left:350px;margin-top:122px;">Совместно с кукольным заводом 
                         "Танцуй, Ваня"</div>
                         <div style="position:absolute;left:350px;margin-top:152px;">При поддержке правительства 
                         Татарстана</div>
                         <div style="position:absolute;left:970px;margin-top:152px">Создаем сайты</div>
                         <div style="position:absolute;left:970px;margin-top:92px;">Пишем музыку</div>
                         <div style="position:absolute;left:970px;margin-top:122px;">Профессиональные игроки в 
                         Rocket League</div>
                         <div style="position:absolute;left:1120px;margin-top:152px;">+7-800-555-35-35</div>
                         <div style="position:absolute;left:1120px;margin-top:182px;">Звонок платный</div>
                        </div>
                       </div>
                      </body>
                    </html>'''


@app.route('/log', methods=['GET', 'POST'])
def logging():
    return 'ok'


def connecting(func):
    db_session.global_init("db/userstable.sqlite")

    def function():
        func()
    return function


@connecting
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        if session.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такое имя пользователя уже занято")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/congrats')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == "__main__":
    app.run()
