from flask import Flask, redirect, render_template
from data import db_session
from data.users import RegisterForm, User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'z_k.,k._zyltrc_kbwtq'


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
                   size=7><center>НАЗВАНИЕ ПОТОМ ПРИДУМАЕМ</center></font></h1>
                   <h2 style="text-align:center; font-family: AnotherCastle3"><font color="#a1f9ba" 
                   size=5>Добро пожаловать!<br>
                   Это основная страница нашего проекта</font></h2>
                   <p style="text-align:center; font-family: AnotherCastle3;"><font color="#a1f9ba" 
                   size=5>В игре зарегистрировано уже больше 10000000 человек<br>
                   На этой странице вы можете установить игру, узнать о ней через нашу мини-Wiki,
                   <br>а так же зарегистрироваться
                   или войти уже в существующий аккаунт</font></p>
                   <p style="text-align:center; font-family: AnotherCastle3;"><font color="#a1f9ba" 
                   size=5>Предлагаю собственноручно опробовать возможности нашего сайта</font></p>
                   <div style="text-align:center;">
                    <a id="login" class="button pink" href="http://127.0.0.16:8000/reg">
                     <i class="fa fa-unlock"></i>
                     <span>Регистрация</span>
                    </a>
                    <a class="button yell" href="http://127.0.0.16:8000/wikipedia">
                     <i class="fa fa-user-plus"></i>
                     <span>Об игре</span>
                    </a>
                    <a class="button mint" href="http://127.0.0.16:8000/download">
                     <i class="fa fa-user-plus"></i>
                     <span>Установить игру</span>
                    </a>
                    <div>
                     <div class="under"><a href="https://vk.com/chainblubler"><img src="static/img/vk.png" width="50" 
                     height="50"></a></div>
                     <div class="under"><a href="https://vk.com/hellother"><img src="static/img/vk.png" width="50" 
                     height="50"></a></div>
                     <div class="under"><a href="https://www.instagram.com/chainloverrr/"><img src="static/img/inst.png" 
                     width="50" height="50"></a></div>
                     <div class="under"><a href="https://www.instagram.com/_just_roman__/"><img src="static/img/inst.png" 
                     width="50" height="50"></a></div>
                     <div class="under"><a href="https://github.com/RomanPodber/NazvaniePotomPridumaem">
                     <img src="static/img/github.png" width="50" height="50"></a></div>
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
                       size=4.5>Кароче наш чел ненавидит черных<p>
                    </h3>
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
                   style="text-align:center; margin-top:50px">
                    <ol class="carousel-indicators">
                     <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                     <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                     <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                     <li data-target="#carousel-example-generic" data-slide-to="3"></li>
                    </ol>
                    <div class="carousel-inner role="listbox" style="text-align:center;">
                     <div class="carousel-item active">
                      <img src="static/img/1slide.jpg" alt="1">
                     </div>
                     <div class="carousel-item" style="text-align:center;">
                      <img src="static/img/2slide.jpg" alt="2">
                     </div>
                     <div class="carousel-item" style="text-align:center;">
                      <img src="static/img/3slide.jpg" alt="3">
                     </div>
                     <div class="carousel-item" style="text-align:center;">
                      <img src="static/img/4slide.jpg" alt="3">
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


@app.route('/download')
def download():
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
                   size=7><center>ВЫБЕРИТЕ НУЖНЫЙ УСТАНОВЩИК</center></font></h1>
                   <div style="text-align: center">
                    <a class="button yell" href="" download=les.png>
                     <i class="fa fa-user-plus"></i>
                     <span>Установить для MAC</span>
                    </a>
                    <a class="button mint" href="" download=les.png>
                     <i class="fa fa-user-plus"></i>
                     <span>Установить для Windows</span>
                    </a>
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
                        <a class="button yell" href="http://127.0.0.16:8000/">
                         <i class="fa fa-user-plus"></i>
                         <span>Вернуться в меню</span>
                        </a>
                       </div>
                      </body>
                    </html>'''


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
    app.run(port=8000, host="127.0.0.16")