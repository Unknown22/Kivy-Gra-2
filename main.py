from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random

'''
Klasa odpowiedzialna za spadajace magnesy
'''

class Magnes(Widget):
    narysowany = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(-3)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    pozycja_x = NumericProperty(0)
    pozycja_y = NumericProperty(0)
    pozycja = ReferenceListProperty(pozycja_x, pozycja_y)
    #magnet_image = ObjectProperty(Image())

    '''
    Metoda przyspieszajaca magnesy
    '''
    def przyspiesz(self):
        self.velocity_y -= 1
    '''
    Metoda ktora czysci ekran po zderzeniu
    '''
    def wyczysc(self, race):
        self.narysowany = 0
        self.pos = (random.randrange(race.width - self.width),race.height)
        self.velocity_y = -3
    '''
    Metoda obslugujaca zderzenie
    '''
    def zderzenie(self, ball, race):
        if self.collide_widget(ball):
            self.narysowany = 0
            self.pos = (random.randrange(race.width - self.width),race.height)
            self.velocity_y = -3
            return True
    '''
    Metoda przesuwajaca magnesy
    '''
    def move_obstacle(self, race):
        if self.narysowany == 0:
            self.pos = (random.randrange(race.width - self.width), race.height)
            self.size = (race.width * 4/10, race.height * 1/10)
            self.narysowany = 1
        self.pos = Vector(*self.velocity) + self.pos
        self.pozycja = self.pos
        if self.pozycja_y + self.height < 0:
            self.narysowany = 0

'''
Klasa odpowiedzialna za wyswietlanie poczatkowego intra
'''
class Intro(Widget):
    czas_trwania = NumericProperty(0)

    def pokaz_intro(self, dodge):
        if self.czas_trwania < 4 * 60:
            self.size = (dodge.width, dodge.height)
            self.czas_trwania += 1
        else:
            self.pos = (-2000, -2000)
            dodge.etap_menu = 1

'''
Klasa odpowiedzialna za wyswietlanie loga gry nad przyciskami w glownym menu
'''
class LogoGry(Widget):
    pozycja_x_logo = NumericProperty(-500)
    pozycja_y_logo = NumericProperty(-500)
    rozmiar_szerokosc_logo = NumericProperty(0)
    rozmiar_wysokosc_logo = NumericProperty(0)

    def pokaz_logo(self, dodge):
        self.rozmiar_szerokosc_logo = dodge.width
        self.rozmiar_wysokosc_logo = dodge.height * 0.2
        self.pozycja_x_logo = dodge.center_x - self.rozmiar_szerokosc_logo/2
        self.pozycja_y_logo = dodge.height - self.rozmiar_wysokosc_logo

    def ukryj_logo(self, dodge):
        self.rozmiar_szerokosc_logo = 0
        self.rozmiar_wysokosc_logo = 0
        self.pozycja_x_logo = -500
        self.pozycja_y_logo = -500

'''
Klasa odpowiedzialna za obsluge calego menu
'''
class Menu(Widget):

    ekran_height = NumericProperty(0)
    ekran_width = NumericProperty(0)

    #tekst = StringProperty("START")
    pozycja_x = NumericProperty(-500)
    pozycja_y = NumericProperty(-500)
    rozmiar_szerokosc = NumericProperty(0)
    rozmiar_wysokosc = NumericProperty(0)

    #tekst_wybor_trudnosci = StringProperty("WYBIERZ POZIOM TRUDNOSCI")
    pozycja_x_wybor_trudnosci = NumericProperty(-500)
    pozycja_y_wybor_trudnosci = NumericProperty(-500)
    rozmiar_szerokosc_wybor_trudnosci = NumericProperty(0)
    rozmiar_wysokosc_wybor_trudnosci = NumericProperty(0)

    pozycja_x_latwy = NumericProperty(-500)
    pozycja_y_latwy = NumericProperty(-500)
    rozmiar_szerokosc_latwy = NumericProperty(0)
    rozmiar_wysokosc_latwy = NumericProperty(0)


    pozycja_x_sredni = NumericProperty(-500)
    pozycja_y_sredni = NumericProperty(-500)
    rozmiar_szerokosc_sredni = NumericProperty(0)
    rozmiar_wysokosc_sredni = NumericProperty(0)


    pozycja_x_trudny = NumericProperty(-500)
    pozycja_y_trudny = NumericProperty(-500)
    rozmiar_szerokosc_trudny = NumericProperty(0)
    rozmiar_wysokosc_trudny = NumericProperty(0)

    gra = ObjectProperty(None)

    '''
    Metoda pokazujaca menu
    '''
    def pokaz_menu(self, dodge):
        #self.opacity -= 0.1
        self.gra = dodge
        self.ekran_height = self.gra.height
        self.ekran_width = self.gra.width

        self.rozmiar_szerokosc = self.gra.width * 0.8
        self.rozmiar_wysokosc = self.gra.height * 0.2
        self.pozycja_x = self.gra.width * 0.2 / 2
        self.pozycja_y = self.gra.height - self.gra.height * 0.2 - self.rozmiar_wysokosc

        self.rozmiar_szerokosc_wybor_trudnosci = self.gra.width * 0.8
        self.rozmiar_wysokosc_wybor_trudnosci = self.gra.height * 0.2
        self.pozycja_x_wybor_trudnosci = self.pozycja_x
        self.pozycja_y_wybor_trudnosci = self.pozycja_y - self.rozmiar_wysokosc_wybor_trudnosci - self.rozmiar_wysokosc_wybor_trudnosci * 0.1

    '''
    Metoda wywolujaca start gry
    '''
    def wystartuj_gre(self):
        self.gra.etap_menu = 3
        #self.rozmiar_szerokosc = 0
        #self.rozmiar_wysokosc = 0
        self.pozycja_x = -2000
        self.pozycja_y = -2000

        self.pozycja_x_wybor_trudnosci = -2000
        self.pozycja_y_wybor_trudnosci = -2000
        #self.rozmiar_szerokosc_wybor_trudnosci = 0
        #self.rozmiar_wysokosc_wybor_trudnosci = 0

        self.pozycja_x_latwy = -2000
        self.pozycja_y_latwy = -2000
        self.pozycja_x_sredni = -2000
        self.pozycja_y_sredni = -2000
        self.pozycja_x_trudny = -2000
        self.pozycja_y_trudny = -2000

    '''
    Metoda pokazujaca poziomy trudnosci
    '''
    def pokaz_wybierz_poziom_menu(self):
        self.gra.etap_menu = 2
        self.gra.pozycja_rekord_top = -1000

    '''
    Metoda wyswietlajaca przyciski do wyboru trudnosci
    '''
    def pokaz_wybierz_poziom(self):
        #self.rozmiar_szerokosc = 0
        #self.rozmiar_wysokosc = 0
        self.pozycja_x = -2000
        self.pozycja_y = -2000

        #self.rozmiar_szerokosc_wybor_trudnosci = 0
        #self.rozmiar_wysokosc_wybor_trudnosci = 0
        self.pozycja_x_wybor_trudnosci = -2000
        self.pozycja_y_wybor_trudnosci = -2000

        self.rozmiar_szerokosc_latwy = self.ekran_width * 0.8
        self.rozmiar_wysokosc_latwy = self.ekran_height * 0.2
        self.pozycja_x_latwy = self.ekran_width * 0.1
        self.pozycja_y_latwy = self.ekran_height - self.ekran_height * 0.2 - self.rozmiar_wysokosc_latwy - self.ekran_height * 0.05


        self.rozmiar_szerokosc_sredni = self.ekran_width * 0.8
        self.rozmiar_wysokosc_sredni = self.ekran_height * 0.2
        self.pozycja_x_sredni = self.ekran_width * 0.1
        self.pozycja_y_sredni = self.pozycja_y_latwy - self.rozmiar_wysokosc_sredni - self.ekran_height * 0.05


        self.rozmiar_szerokosc_trudny = self.ekran_width * 0.8
        self.rozmiar_wysokosc_trudny = self.ekran_height * 0.2
        self.pozycja_x_trudny = self.ekran_width * 0.1
        self.pozycja_y_trudny = self.pozycja_y_sredni -self.rozmiar_wysokosc_trudny - self.ekran_height * 0.05


    '''
    Metoda wybierajaca poziom
    '''
    def wybierz_poziom(self, trudnosc):
        self.gra.poziom_trudnosci = trudnosc
        self.gra.etap_menu = 1
        self.gra.pozycja_rekord_top = self.gra.height * 1/3


        """
        Przyciski do ustawiania poziomu trudnosci
        """
        #self.rozmiar_szerokosc_latwy = 0
        #self.rozmiar_wysokosc_latwy = 0
        self.pozycja_x_latwy = -2000
        self.pozycja_y_latwy = -2000


        #self.rozmiar_szerokosc_sredni = 0
        #self.rozmiar_wysokosc_sredni = 0
        self.pozycja_x_sredni = -2000
        self.pozycja_y_sredni = -2000


        #self.rozmiar_szerokosc_trudny = 0
        #self.rozmiar_wysokosc_trudny = 0
        self.pozycja_x_trudny = -2000
        self.pozycja_y_trudny = -2000

class Electron(Widget):
    score = NumericProperty(0)
    record = NumericProperty(0)
    life = NumericProperty(2)

class DodgeGame(Widget):
    intro_logo = ObjectProperty(None)
    etap_menu = NumericProperty(0)
    przycisk1 = ObjectProperty(None)
    przycisk2 = ObjectProperty(None)
    logo_gra = ObjectProperty(None)
    przycisk_poziom_trudnosci1 = ObjectProperty(None)
    przycisk_poziom_trudnosci2 = ObjectProperty(None)
    przycisk_poziom_trudnosci3 = ObjectProperty(None)
    poziom_trudnosci = NumericProperty(2)
    ball = ObjectProperty(None)
    czy_poczatek = NumericProperty(1)
    licznik = NumericProperty(0)
    pozycja_x_licznik = NumericProperty(-500)
    pozycja_y_licznik = NumericProperty(-500)
    pozycja_licznik = ReferenceListProperty(pozycja_x_licznik, pozycja_y_licznik)
    button_lewy_ekran = ObjectProperty(None)
    button_prawy_ekran = ObjectProperty(None)
    pozycja_x_lewa_strona = NumericProperty(-2000)
    pozycja_x_prawa_strona = NumericProperty(-2000)

    magnes1 = ObjectProperty(None)
    magnes2 = ObjectProperty(None)
    magnes3 = ObjectProperty(None)
    move = NumericProperty(0)
    first_draw = NumericProperty(0)
    first_draw_magnes2 = NumericProperty(0)
    first_draw_magnes3 = NumericProperty(0)
    przyspieszenie_kulki = NumericProperty(5)
    przyrost_odleglosci = NumericProperty(1)
    poziom_przyspieszenia = NumericProperty(0)
    prog_przyspieszenia = NumericProperty(500)

    pozycja_linii_srodka = NumericProperty(-50)
    pozycja_dystans = NumericProperty(-1000)
    pozycja_liczba_zyc = NumericProperty(-1000)
    pozycja_rekord_x = NumericProperty(-1000)
    pozycja_rekord_top = NumericProperty(-5000)
    rekord_font_size = NumericProperty(30)

    def update(self, dt):
        if self.etap_menu == 0:
            self.ball.center_x = -1000
            Intro.pokaz_intro(self.intro_logo, self)
        elif self.etap_menu == 1:
            LogoGry.pokaz_logo(self.logo_gra, self)
            Menu.pokaz_menu(self.przycisk1, self)
        elif self.etap_menu == 2:
            Menu.pokaz_wybierz_poziom(self.przycisk1)
        elif self.etap_menu == 3:
            LogoGry.ukryj_logo(self.logo_gra,self)
            self.pozycja_x_lewa_strona = 0
            self.pozycja_x_prawa_strona = self.width/2
            self.pozycja_linii_srodka = self.center_x
            self.pozycja_dystans = self.width/2
            self.pozycja_liczba_zyc = self.width * 1/5
            self.pozycja_rekord_x = self.width * 4/5
            self.pozycja_rekord_top = self.top
            self.rekord_font_size = 30

            if self.ball.score > self.prog_przyspieszenia and self.poziom_przyspieszenia < 15:
                self.poziom_przyspieszenia += 1
                self.prog_przyspieszenia += self.poziom_trudnosci * 1000 * self.poziom_przyspieszenia
                self.magnes1.przyspiesz()
                self.magnes2.przyspiesz()
                self.magnes3.przyspiesz()
                self.przyrost_odleglosci += self.poziom_przyspieszenia
                self.przyspieszenie_kulki += 1


            Magnes.move_obstacle(self.magnes1, self)
            if self.magnes1.pozycja_y + self.magnes1.height / 2 < self.height * 2/3 or self.first_draw_magnes2 == 1:
                Magnes.move_obstacle(self.magnes2, self)
                self.first_draw_magnes2 = 1
                if self.magnes2.pozycja_y + self.magnes2.height / 2 < self.height * 2/3 or self.first_draw_magnes3 == 1:
                    Magnes.move_obstacle(self.magnes3, self)
                    self.first_draw_magnes3 = 1

            if self.first_draw == 0:
                self.ball.score = 0
                self.ball.center_x = self.center_x
                self.first_draw = 1
            self.ball.center_y = self.center_y * 1/10
            self.ball.score += self.przyrost_odleglosci


            if self.move == 1 and self.ball.center_x > self.width - self.width + 25:
                if self.ball.center_x - self.przyspieszenie_kulki < self.width - self.width + 25:
                    self.ball.center_x = self.width - self.width + 25
                else:
                    self.ball.center_x -= self.przyspieszenie_kulki
            elif self.move == 2 and self.ball.center_x < self.width - 25:
                if self.ball.center_x + self.przyspieszenie_kulki > self.width - 25:
                    self.ball.center_x = self.width - 25
                else:
                    self.ball.center_x += self.przyspieszenie_kulki

            """
            Czyszczenie ekranu po kolizji
            """
            if Magnes.zderzenie(self.magnes1, self.ball, self)\
                or Magnes.zderzenie(self.magnes2, self.ball, self)\
                or Magnes.zderzenie(self.magnes3, self.ball, self):
                if self.ball.life > 0:
                    self.ball.life -= 1
                    self.first_draw_magnes2 = 0
                    self.first_draw_magnes3 = 0
                    Magnes.wyczysc(self.magnes1, self)
                    Magnes.wyczysc(self.magnes2, self)
                    Magnes.wyczysc(self.magnes3, self)
                else:
                    if self.ball.score > self.ball.record:
                        self.ball.record = self.ball.score
                    self.first_draw = 0
                    self.first_draw_magnes2 = 0
                    self.first_draw_magnes3 = 0
                    Magnes.wyczysc(self.magnes1, self)
                    Magnes.wyczysc(self.magnes2, self)
                    Magnes.wyczysc(self.magnes3, self)
                    self.przyrost_odleglosci = 1
                    self.poziom_przyspieszenia = 0
                    self.prog_przyspieszenia = 500
                    self.ball.life = 2
                    #self.etap_menu = 1
                    self.ukryj_gre()




    def dotyk_down_lewy(self):
        if self.ball.center_x > self.width - self.width + 25:
            self.move = 1
    def dotyk_up_lewy(self):
        self.move = 0
    def dotyk_down_prawy(self):
        if self.ball.center_x < self.width - 25:
            self.move = 2
    def dotyk_up_prawy(self):
        self.move = 0


    def ukryj_gre(self):
        self.pozycja_linii_srodka = -50
        self.pozycja_x_lewa_strona = -2000
        self.pozycja_x_prawa_strona = -2000
        self.pozycja_dystans = -2000
        self.pozycja_liczba_zyc = -2000
        self.rekord_font_size = 50
        self.pozycja_rekord_x = self.width * 1/2
        self.pozycja_rekord_top = self.height * 1/3
        self.ball.center_x = -1000
        self.etap_menu = 1

class DodgeApp(App):
    def build(self):
        game = DodgeGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    DodgeApp().run()