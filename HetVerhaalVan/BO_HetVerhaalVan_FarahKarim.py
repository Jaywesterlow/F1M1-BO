import os
import sys
from time import sleep


#Start
def intro():
    text = """\n
    Je bent Farah Karim, je bent 28 jaar oud en je woont alleen, niet ver van het oorlogsgebied. 
    Je werkt bij de gemeente, maar moet daarvoor elke dag een klein stukje heen en terug door een gevaarlijk gebied. 
    De meeste dagen gebeurd er niets en zie je hooguit dat militairen iemand aanspreken of intimideren, 
    maar gaan altijd weer verder om iemand anders lastig te vallen.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part1()
def part1():
    text = """\n
    Je loopt op een normale dag naar je werk. Het is ongeveer 20 minuten lopen. 
    Na een kwartier lopen hoor je in de verte een knal. 
    Na nog 5 minuten lopen kom je aan bij je werk, 
    maar zie je voordat je het gebouw binnen loopt links in de verte een groepje van 4 militairen jouw kant op patrouilleren. 
    Eenmaal achter je computer krijg je van je baas te horen dat hij de formulieren vandaag nog op zijn bureau wilt zien liggen. 
    Ook al schreeuwde je baas zowat tegen je, zit je met je gedachten alleen maar bij de oorlog. Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je krijgt het waarschijnlijk niet af- maar begint te werken aan het formulier.")
    print("b). Je zoekt op het internet nieuws over de oorlog.")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part2()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part3()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")   
def part2():
    text = """\n
    De dag zit er alweer op en je hebt het formulier net op tijd af. 
    Je loopt naar je baas z’n kantoor en legt het papier op zijn bureau, 
    waarna je onderweg naar de lift je collega’s nog even gedag zegt. 
    Je stapt naar buiten, ademt diep in en zucht alles uit na een lange dag werk. 
    Je begint terug naar huis te lopen. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part4()
def part3():
    text = """\n
    Je bent zo verdiept in de research die je uitvoert dat je de tijd helemaal bent vergeten.
    Je ziet je baas naar zijn kantoor lopen en zit na te denken over wat je zal doen. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je probeert stiekem het gebouw uit te sluipen zonder dat je baas je ziet.")
    print("b). Je besluit je baas te confronteren in de hoop dat hij je nog een kans geeft.")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part5()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part6()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part4():
    text = """\n
    Onder weg naar huis hoor je in de richting waar je naartoe loopt gerumoer. 
    Hoe dichterbij je komt, des te duidelijker je hoort waar het over gaat. 
    Terwijl je de hoek om loopt zie je een groep mensen staan, 
    je loopt iets verder en ziet een militair met een gasmasker op en een machinegeweer in zijn hand een man lastig vallen. 
    Je wilt er op af lopen om er iets van te zeggen, maar denkt terug naar vroeger. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part8A()
def part5():
    text = """\n
    Je wacht tot het juiste moment om te gaan. 
    Het duurt wel even voordat je de kans hebt, 
    maar het lukt je uiteindelijk om bij de lift te komen voordat je baas uit zijn kantoor komt en begint 
    te schreeuwen dat je terug moet komen als jij je baan wilt houden, 
    maar de liftdeuren gaan al dicht. Je komt beneden en stapt naar buiten. Wat ga je nu doen zonder baan? 
    Terwijl je besluit maar naar huis te lopen hoor je ineens een knal in de richting van je huis. Je vertrekt gehaast. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part7()
def part6():
    text = """\n
    Je loopt naar je baas zijn kantoor toe en doet de deur open. 
    Je baas is boos en zegt dat je op deze manier je baan zal verliezen, 
    maar zegt dat hij de formulieren de volgende dag wilt hebben, of je moet naar een andere baan zoeken. 
    Eenmaal buiten ben je opgelucht dat je de dag hebt doorleefd zonder je baan te verliezen en begint naar huis te lopen. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part4()
def part7():
    text = """\n
    Je weet niet precies waar de knal vandaan kwam, maar je wilt zo snel mogelijk kijken of het wel goed gaat met je ouders, 
    die ook in dezelfde buurt wonen. Je komt aan bij- waar je dacht dat, het schot vandaan kwam. 
    Je loopt de hoek om en ziet een groep mensen bij elkaar staan en naar beneden kijken en je hoort ze huilen. 
    Je komt dichterbij en ziet dat ze over een man staan gebogen. Hij is doodgeschoten. 
    Je hebt naar gevoel in je onderbuik. Dit voelt niet echt aan. Je denkt terug aan vroeger. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part8B()
def part8A():
    text = """\n
     20 jaar geleden, je was 8 jaar oud. Je ging met je vader naar huis na een dag helpen op de markt. 
     Onderweg naar huis loop je langs een zijweg waar je ziet dat er een man lastig gevallen word door de politie, 
     je denkt er niks van. 
     Je loopt met je vader de hoek om, je vader zegt tegen je even te wachten buiten de winkel en dat hij zo terug is. 
     Je hoort gerumoer om de hoek bij de politie en vraagt je af wat er aan de hand is. Zal je kijken, 
     of blijven wachten zoals je vader vroeg?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je blijft netjes wachten waar je vader zei dat je moest wachten. ")
    print("b). Je gaat kijken wat er aan de hand is. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part9A()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part10A()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part8B():
    text = """\n
     20 jaar geleden, je was 8 jaar oud. Je ging met je vader naar huis na een dag helpen op de markt. 
     Onderweg naar huis loop je langs een zijweg waar je ziet dat er een man lastig gevallen word door de politie, 
     je denkt er niks van. 
     Je loopt met je vader de hoek om, je vader zegt tegen je even te wachten buiten de winkel en dat hij zo terug is. 
     Je hoort gerumoer om de hoek bij de politie en vraagt je af wat er aan de hand is. Zal je kijken, 
     of blijven wachten zoals je vader vroeg?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je blijft netjes wachten waar je vader zei dat je moest wachten. ")
    print("b). Je gaat kijken wat er aan de hand is. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part9B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part10B()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part9A():
    text = """\n
    Je vader is terug. Het gerumoer is nu geschreeuw en je vraagt je vader wat er aan de hand, 
    maar hij kijkt je niet aan en loopt gewoon door naar huis. Jullie komen veilig thuis aan. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part11A()
def part9B():
    text = """\n
    Je vader is terug. Het gerumoer is nu geschreeuw en je vraagt je vader wat er aan de hand, 
    maar hij kijkt je niet aan en loopt gewoon door naar huis. Jullie komen veilig thuis aan. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part12()
def part10A():
    text = """\n
    Je loopt richting het geluid, wanneer je de hoek om komt zie je dat een politieagent een man aanvalt terwijl de man zich overgeeft. 
    Na het onnodige geweld arresteert de politieagent hem en de mensen eromheen zijn boos. Ze zeggen dat de man niks had gedaan.
    Dat was de eerste keer van vele waarin je ware onrecht hebt meegemaakt. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part13()
def part10B():
    text = """\n
    Je loopt richting het geluid, wanneer je de hoek om komt zie je dat een politieagent een man aanvalt terwijl de man zich overgeeft. 
    Na het onnodige geweld arresteert de politieagent hem en de mensen eromheen zijn boos. Ze zeggen dat de man niks had gedaan.
    Dat was de eerste keer van vele waarin je ware onrecht hebt meegemaakt. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part16()
def part11A():
    text = """\n
    Je komt uit je eigen gedachten. 
    Je kijkt net als alle andere toe hoe de man bedreigt, en uiteindelijk weggevoerd wordt. 
    Je denkt na, hoelang duurt het totdat jijzelf in die positie komt en je gaat spoedig naar huis. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part11B()
def part11B():
    text = """\n
    Eenmaal thuis pak je jouw spullen in, maar denk je bij jezelf of je hier echt mee doorgaat. 
    Het land uit vluchten is niet zomaar iets. Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je stopt met inpakken en je blijft hier. ")
    print("b). Je gaat verder met je spullen pakken en vertrekt naar je ouders om ze gedag te zeggen. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end1()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part19()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part12():
    text = """\n
    Je komt uit je eigen gedachten en belt een ambulance. 
    Nadat ze de man hebben weggevoerd denk je bij jezelf: “Hoelang tot dit mij overkomt?”. 
    Ineens komt je goede vriendin Nadia bij je staan. Ze zegt dat ze in de buurt was en dat ze ontevredenheid in je ogen ziet. 
    Ze vraagt je of je hier iets aan wilt doen. 
    Je wist dat ze betrokken was bij het protesteren om een einde te maken aan de oorlog, 
    maar de manier waarop ze het vraagt voelt apart en hoewel je hier iets aan wilt doen, 
    weet je niet zeker of je dit aanbod aan moet nemen. 
    Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je slaat haar aanbod af en gaat naar huis. Je er komt vast wel een einde aan. ")
    print("b). Je neemt haar aanbod aan, hier moet iets aan gedaan worden. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part11B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part17()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part13():
    text = """\n
    Je komt uit je eigen gedachte. Je bent niet een persoon die graag tegen de wet in gaat, maar dit is verkeerd. 
    Deze man beschermt ons niet, het is een pestkop en hier moet iets aan gedaan worden. 
    Je twijfelt tussen wat je doet. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je gaat naar huis, dit komt wel goed. ")
    print("b). Je spreekt de man aan. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part11B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part14()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part14():
    text = """\n
    Je schreeuwt tussen het gerumoer van de menigte heen dat de man moet ophouden. 
    De man draait zich om, kijkt je even aan, en gaat weer verder. 
    Hij biedt je geen aandacht, maar wat hij doet moet echt stoppen. 
    Je kijkt rond en je ziet een steen liggen, je denkt bij jezelf dat de steen zijn aandacht wel zou trekken. 
    Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Het is het niet waard, je gaat naar huis. ")
    print("b). Je pakt de steen op en gooit het naar de militair. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part11B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part15()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part15():
    text = """\n
    Je gooit de steen naar de militair en raakt hem tegen zijn rug. 
    Terwijl hij zich rustig omdraait bedenkt jij je wat voor een slechte keuze dat was. 
    Je kijkt rechtstreeks in de emotieloze, donkere glazen. 
    Hij heft zijn wapen op in jouw richting, je durft niet te bewegen. 
    Ineens kijkt hij om, één van de andere militairen die blijkbaar in zijn groep is, roept om hulp. 
    De militair kijkt je aan en draait zich daarna om en gaat de andere kant op. 
    Je zit helemaal in je gedachten en bedenkt je wat een stomme keuze dat was. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part12()
def part16():
    text = """\n
    Je komt uit je eigen gedachten. 
    Je bent woedend over hoe wreed mensen kunnen zijn. 
    Je kijkt naast je en ziet je goeie vriendin Nadia naast je staan (hoelang staat ze daar al?). 
    Je denkt bij jezelf dat hier iets aan gedaan moet worden en dat je niet zal toekijken terwijl deze oorlog escaleert 
    en zich steeds meer in jouw dagelijks leven wikkelt. 
    Je weet dat Nadia betrokken is bij de protesteren en vraagt haar of je de volgende keer mee kan, 
    ze zegt dat ze dat graag zou willen.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part17()
def part17():
    text = """\n
    Je bent op de afgesproken plek aan het protesteren en ziet heel veel andere die er ook genoeg van hebben. 
    Je ziet Nadia net vanaf de andere kant van de straat aanlopen wanneer je ineens een oorverdovende 
    knal bij de voorste protestanten hoort. Je oren suizen en je hoort bijna niks van je omgeving, 
    maar kan wel horen dat er nog meer knallen volgen. 
    Je rent met de menigte mee, de andere kant op van waar de knallen vandaan komen, 
    maar je ziet dat sommige mensen naast je terwijl ze wegrennen voorover neervallen en niet meer opstaan. 
    Je kijkt om je heen en ziet Nadia weer, ze rent net een zijweg in. Je vraagt je af waar je zelf eigenlijk heen gaat. 
    Tot nu toe ren je alleen maar met de menigte mee.
    Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je rent vooruit tot je ver genoeg van het voorgaand protest bent. ")
    print("b). Je rent de zijweg in waar Nadia net heen is gegaan. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end2()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part18()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part18():
    text = """\n
    Je draait ineens snel 90 graden naar rechts en rent de steeg in waar Nadia op je staat te wachten. 
    Voor je iets kan zeggen pakt ze je bij je pols en begint ze verder te rennen. 
    Tussen de happen naar adem en het ongeloof van wat er net is gebeurd door lukt het je een moment te vinden 
    te vragen waar jullie heen gaan. Ze stopt met rennen, draait zich om en kijkt je lang en serieus aan. 
    Na 4 of 5 seconden zegt ze: 
    ‘Ik ga naar mijn voormalige vrienden die ik niet wilde geloven toen ze zeiden dat een verzet nodig was. 
    Ik ga een ECHT verschil in deze oorlog maken, de vraag is; wat ga jij doen?’.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Dit gaat mij echt te ver, ik kan daar niet aan mee doen. Ik ga naar huis. ")
    print("""\
           b). Ik ga met je mee, dit is een oorlog, dus een vreedzaam protest was gedoemd te mislukken, 
               maar dit is ongelooflijk en zal ik goed onthouden wanneer ik twijfel waarom ik bij het verzet zit. 
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part11B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            end3()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part19():
    text = """\n
    Je hebt een rugtas met kleren, een beetje eten en al het geld dat je hebt (S£300k) ingepakt en gaat richting het huis van je ouders.
    Na een kwartier kom je aan en klop je op de deur. Je moeder doet open en ziet de zorg in je ogen. 
    Ze vraagt wat er aan de hand is in gebaart je binnen te komen. 
    Je legt de situatie uit en zegt dat je het niet meer aan kunt op deze manier te leven en dat jij je niet meer veilig voelt. 
    Je ouders snappen het en zeggen dat ze er ook over na dachten te vertrekken, 
    maar er niet helemaal klaar voor zijn alles achter te laten, maar je kleine broertje snapt niet waarom je weg gaat. 
    Je weet niet hoe je het aan hem moet uitleggen maar je ouders zeggen dat het goed is. 
    Je kent nog iemand waarvan je weet dat hij je de grens over kan brengen. 
    Je belt hem en vertelt wat er aan de hand is en dat je eraan komt. Wanneer je bij hem aankomt vraagt hij meteen om geld.   
    Ook al ken je hem, heb je hem nooit ontmoet, en hij ziet er niet als een erg vertrouwbaar persoon uit. 
    Wat doe je?
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je geeft hem al het geld dat je hebt (S£300k) en zegt dat het alles is dat je hebt. ")
    print("b). Je geeft hem de helft (S£150k) en zegt dat het alles is dat je hebt")
    print("c). Je zegt dat je geen geld bij je hebt en of hij je alsjeblieft alsnog wilt brengen. ")

    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part20A()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part20B()
            incorrect = False
        elif awnser == "c":
            sleep(1)
            part23()
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")

#Start Endings
def end1():
    text = """\n
    Je stopt met inpakken, ademt even diep in, en hoopt dat hier snel een einde aan komt.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    
    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")   
def end2():
    text = """\n
    Je rent verder en ziet steeds minder mensen naast je rennen. Je denkt bij jezelf: ‘Ik red het wel’. 
    Maar net na die gedachten voelt het alsof iemand je heel hard voorover duwt. 
    Na even bijkomen probeer je op te staan en verder te rennen maar het voelt alsof je geen kracht meer in je benen hebt, 
    nu je het denkt voel je jouw benen helemaal niet meer. 
    Na een laatste poging om jezelf omhoog te duwen met je armen plof je neer. 
    Je voelt een nat gevoel over je onderrug sijpelen en je ogen voelen zwaar aan. 
    Je weet niet wat je overkomt maar je gedachten drijven langzaam weg.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")
def end3():
    text = """\n
    Je bent op komen dagen op de plek dat Nadia zei dat jullie zouden afspreken. 
    Je ziet haar komen aanlopen en ze zegt haar te volgen. Jullie gaan een appartement binnen waar een paar andere mensen zijn. 
    Ze vragen aan Nadia wie jij bent en wat je hier doet, 
    maar ze stelt hen gerust en zegt dat jij bij het protest was en je steentje wilt bijdragen.
    Na een paar uurtjes elkaar leren kennen gaan jullie naar een andere kamer waar je wapens ziet liggen
    en een bord met daarop een kaart met foto’s, sommige doorstreept. Je vraagt je af of dit wel een goed idee was. 
    Ze wilden net iets uitleggen, maar de deur wordt ineens ingetrapt door politie en militairen. 
    Ze stormen het huis binnen en richten hun wapens op jullie. 
    Eén van de mannen in de kamer wilt een wapen oppakken maar stopt direct nadat een politieagent tegen het plafond schiet. 
    Jullie worden allemaal opgepakt.
    Na een tijd achterin een busje met handboeien om vervoer word je een gevangenis in gebracht. 
    Je probeert te vragen waarom je rechtstreeks naar een gevangenis gaat, maar wordt alleen maar vooruit geduwd. 
    Je loopt een lange hal met isoleercellen in  en word in een donkere, koude cel gegooid. 
    De agenten lopen weg, je denkt na over je slechte beslissingen en begint te huilen.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")

#Journey
def part20A():
    text = """\n
    Je pakt het geld uit je tas en steekt je hand naar hem uit. 
    Hij kijkt je eventjes aan en snauwt het geld dan uit je hand. 
    Hij seint je in te stappen en jullie beginnen te rijden. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part21A()
def part20B():
    text = """\n
    Je pakt het geld uit je tas en steekt je hand naar hem uit. 
    Hij kijkt je eventjes aan en snauwt het geld dan uit je hand. 
    Hij seint je in te stappen en jullie beginnen te rijden. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part21B()
def part21A():
    text = """\n
    Jullie zijn al een aantal uur aan het rijden en je bent heel moe. 
    Het is al een paar uurtjes pikdonker, maar elke keer dat je vraagt hoelang het nog duurt is hij stil. 
    Hij zei dat jullie naar Instaboel gingen. 
    Na nog een aantal uur stopt hij bij een garage waar hij de auto uit stapt en zegt dat je moet wachten. 
    Nadat hij, met wat lijkt op overleggen, klaar is komt hij terug en haalt je op. Hij brengt je naar 2 mannen. 
    1 zegt dat hij met de boot naar Italië gaat en de ander zegt met de auto naar Nederland te gaan. 
    Terwijl je aan het denken ben hoor je ineens een auto opstarten. 
    Je rent naar buiten en ziet de man waarmee je hier naartoe bent gekomen wegrijden. 
    Je zit hier nu vast en moet kiezen wat je doet.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je gaat mee met de man die je naar Nederland zal brengen. ")
    print("b). Je gaat mee met de man die je naar Italië zal brengen. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part22()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            end4()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part21B():
    text = """\n
    Jullie zijn al een aantal uur aan het rijden en je bent heel moe. 
    Het is al een paar uurtjes pikdonker, maar elke keer dat je vraagt hoelang het nog duurt is hij stil. 
    Hij zei dat jullie naar Instaboel gingen. 
    Na nog een aantal uur stopt hij bij een garage waar hij de auto uit stapt en zegt dat je moet wachten. 
    Nadat hij, met wat lijkt op overleggen, klaar is komt hij terug en haalt je op. Hij brengt je naar 2 mannen. 
    1 zegt dat hij met de boot naar Italië gaat en de ander zegt met de auto naar Nederland te gaan. 
    Terwijl je aan het denken ben hoor je ineens een auto opstarten. 
    Je rent naar buiten en ziet de man waarmee je hier naartoe bent gekomen wegrijden. 
    Je zit hier nu vast en moet kiezen wat je doet.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je gaat mee met de man die je naar Nederland zal brengen. ")
    print("b). Je gaat mee met de man die je naar Italië zal brengen. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part25A()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            end4()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part21C():
    text = """\n
    Jullie zijn al een aantal uur aan het rijden en je bent heel moe. 
    Het is al een paar uurtjes pikdonker, maar elke keer dat je vraagt hoelang het nog duurt is hij stil. 
    Hij zei dat jullie naar Instaboel gingen. 
    Na nog een aantal uur stopt hij bij een garage waar hij de auto uit stapt en zegt dat je moet wachten. 
    Nadat hij, met wat lijkt op overleggen, klaar is komt hij terug en haalt je op. Hij brengt je naar 2 mannen. 
    1 zegt dat hij met de boot naar Italië gaat en de ander zegt met de auto naar Nederland te gaan. 
    Terwijl je aan het denken ben hoor je ineens een auto opstarten. 
    Je rent naar buiten en ziet de man waarmee je hier naartoe bent gekomen wegrijden. 
    Je zit hier nu vast en moet kiezen wat je doet.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je gaat mee met de man die je naar Nederland zal brengen. ")
    print("b). Je gaat mee met de man die je naar Italië zal brengen. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part25B()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            end4()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part22():
    text = """\n
    Je zegt mee te willen gaan naar Nederland, maar hij vraagt om S£100k, 
    je verteld hem dat je niet genoeg hebt maar dat je echt met hem mee wilt, maar hij seint naar de andere man. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    end4()
def part23():
    text = """\n
    Hij kijkt je een paar seconden serieus aan en lacht je daarna heel hard uit. 
    Hij vraagt wat hij dan ervoor krijgt als je hem toch niet betaald. 
    Je denkt even na. 
    Je vraagt aan hem of als je een ander persoon regelt die wel betaald, je met hem mee mag rijden. 
    Hij denkt er even over na en zegt dat dat zou kunnen. Je denkt bij jezelf na wie je kan vragen mee te gaan.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je vraagt je goede vriendin Nadia. ")
    print("b). Je vraagt aan je ouders of ze mee komen. ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end5()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part24()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part24():
    text = """\n
    Je gaat naar jouw ouders hun huis en klopt aan de deur. Je moeder doet open , straalt en omhelst je. 
    Ze zegt dat ze niet had verwacht jou ooit nog terug te zien. Je komt binnen en legt de situatie uit. 
    Je ouders twijfelen maar komen uiteindelijk tot het besluit mee te komen, aangezien ze ook wilden vertrekken. 
    Nadat ze hun spullen hebben gepakt vertrekken jullie. 
    Je komt met je vader, moeder en kleine broertje aan bij de man en je vader betaald de man. 
    De man kijkt jouw familie aan en daarna jou. Hij seint jullie in te stappen en jullie beginnen te rijden. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part21C()
def part25A():
    text = """\n
    Je wilt meegaan met de man die je naar Nederland kan brengen, maar hij vraagt om S£100k. 
    Je kijkt in je tas en je hebt gelukkig nog S£150k over en overhandigt het geld dat hij vraagt. 
    Je stapt in zijn auto en jullie beginnen te rijden. Na iets meer dan een dag rijden zegt de man dat je in Nederland bent. 
    Je stapt uit en zegt de man gedag. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part26A()
def part25B():
    text = """\n
    Je wilt meegaan met de man die je naar Nederland kan brengen, maar hij vraagt om S£100k. 
    je kijkt in je tas en je hebt gelukkig nog S£300k en overhandigt het geld dat hij vraagt. 
    Jullie stappen in zijn auto en beginnen te rijden. Na iets meer dan een dag rijden zegt de man dat jullie in Nederland zijn. 
    Je stapt uit en zegt de man gedag.  
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part26B()
def part26A():
    text = """\n
    Aan de ene kant ben je opgelucht, je hebt het gehaald. 
    Je kan eindelijk slapen zonder de gedachte in je achterhoofd dat er een kans is dat je niet meer wakker wordt. 
    Aan de andere kant zit je bij jezelf te denken wat de volgende stap is. 
    Je hebt alles achter gelaten voor een nieuwe kans in een stabielere leefomgeving en nu moet je beginnen. 
    Het eerste idee dat je krijgt is naar een politiebureau, 
    hoewel je de autoriteit door je voorgaande ervaringen niet helemaal vertrouwd. 
    Wanneer je daar aankomt bouw je de moed op om naar binnen te gaan. 
    Eenmaal binnen zie je dat iedereen rustig bezig is en er niemand raar opkijkt van jouw binnenkomst. 
    Je loopt naar voren en de mevrouw die voor de toonbank staat vraagt vriendelijk waarmee ze u kan helpen. 
    Dit geeft je al gelijk een beter gevoel en wat zelfvertrouwen om vragen te stellen. 
    Je legt uit wat de situatie is en waarom je hier bent. 
    De vrouw vraagt om jouw gegevens en na alles geregistreerd te hebben zegt ze tegen jullie dat
    jullie waarschijnlijk een lange weg te gaan hebt voordat jullie helemaal ingeburgerd zijn 
    en jullie je plek hebben gevonden, 
    maar dat het helemaal goed komt en jullie je geen zorgen meer hoeven te maken over de oorlog.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    end6A()
def part26B():
    text = """\n
    Aan de ene kant ben je opgelucht, je hebt het gehaald. 
    Je kan eindelijk slapen zonder de gedachte in je achterhoofd dat er een kans is dat je niet meer wakker wordt. 
    Aan de andere kant zit je bij jezelf te denken wat de volgende stap is. 
    Je hebt bijna alles achter gelaten voor een nieuwe kans in een stabielere leefomgeving en nu moet je beginnen. 
    Het eerste idee dat je krijgt is naar een politiebureau, 
    hoewel je de autoriteit door je voorgaande ervaringen niet helemaal vertrouwd. 
    Wanneer jullie daar aankomen bouw je de moed op om naar binnen te gaan. 
    Eenmaal binnen zie je dat iedereen rustig bezig is en er niemand raar opkijkt van jullie binnenkomst. 
    Je loopt naar voren en de mevrouw die voor de toonbank staat vraagt vriendelijk waarmee ze u kan helpen. 
    Dit geeft je al gelijk een beter gevoel en wat zelfvertrouwen om vragen te stellen. 
    Je legt uit wat de situatie is en waarom je hier bent. 
    De vrouw vraagt om jouw en je families gegevens en na alles geregistreerd te hebben zegt ze tegen je dat 
    je waarschijnlijk een lange weg te gaan hebt voordat je helemaal ingeburgerd bent en je plek hebt gevonden, 
    maar dat het helemaal goed komt en jij je geen zorgen meer hoeft te maken over de oorlog. 
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    end6B()

#Journey Endings
def end4():
    text = """\n
    Je loopt met de man mee die zegt dat hij je naar Italië zal brengen. 
    Jullie stappen in zijn auto en na een uurtje rijden komen jullie aan op een soort zelfgebouwde haven. 
    Er staan al tientallen andere mensen te wachten. Na nog een uur wachten word er gezegd allemaal aan boord te komen, 
    maar er is niet genoeg plek voor iedereen. Mensen zitten erg op elkaar gepropt en je bent bang. 
    Na een paar dagen varen denk je dat dit het einde is. 
    Zelfs wanneer je de kapitein vraagt waar jullie heen gaan geeft hij een onduidelijk en onzeker antwoord. 
    Nog een uur is voorbij en de storm wat een half uur geleden rustig begon gooit het schip nu met elke golf heen en weer. 
    Als het zo door gaat duurt het niet lang meer voordat de boot omkiept. 
    Net wanneer je dacht dat alle hoop was vergaan zie je een groot vrachtschip. 
    Je rent naar bakboord en begint te roepen en zwaaien, als ze niet snel helpen dan zal de boot ten onder gaan. 
    Het lijkt alsof het vrachtschip jullie kant op draait. 
    Meerdere mensen hebben het schip ook gezien en staan met jou te zwaaien, maar ineens merk je dat het schip naar links kiept. 
    De volgende golf komt recht in je gezicht aan en je word het water in gesleurd. 
    Je krijgt je hoofd weer even boven water maar dat duurt niet lang, 
    want de volgende golf komt met nog meer kracht en duwt je onderwater. 
    Je probeert naar boven te zwemmen maar je zicht wordt wazig en het oppervlak lijkt alleen maar verder weg te gaan. 
    Je doet nog een laatste poging maar tevergeefs.

    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")
def end5():
    text = """\n
    Je gaat naar je goede vriendin Nadia’s huis om te vragen of ze mee komt. 
    Je weet dat zij al een hele tijd druk bezig is geweest met protesteren en andere methode om de oorlog te bestrijden. 
    Je hoopt dat ze meekomt, want anders kom je het land niet uit. 
    Je komt aan bij haar huis en kijkt door het raam of ze thuis is, maar je kunt niet naar binnen kijken. 
    Je gaat naar de voordeur en heft je hand om te kloppen, maar merkt dat de deur open is dus je besluit haar te verassen. 
    Je sluipt door het huis opzoek naar haar wanneer je geluiden hoort in de woonkamer. 
    Je loopt rustig naar de woonkamer zonder geluid te maken, 
    maar wanneer je door de kier van de deur kijkt zie je een paar andere mensen die je niet kent. 
    Je ziet ook wapens liggen. Je beseft je dat dit een fout was en je sluipt rustig weer achteruit. 
    Terwijl je naar achter loopt raak je een kast en valt een vaas eraf. De vaas breekt en maakt een hard geluid. 
    Zodra het breekt zie je door de kier een plotselinge beweging en hoor je 3 of 4 achtereenvolgende knallen. 
    Je oren suizen en stukken van de deur voor je zijn versplinterd. 
    Je wilt wegrennen maar word tegengehouden door een naar gevoel in je buik; het voelt brandend en vochtig aan. 
    Plotseling opent Nadia de deur en kijkt ze je geschokt aan, en daarna naar je buik. 
    Je kijkt naar beneden en ziet een donkerrode vlek van je bloes dat je broek in sijpelt en je valt achterover naar de vloer. 
    Het laatste wat je ziet voor je zicht weg valt is je vriendin Nadia die over je heen gebogen aan het huilen en schreeuwen is.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")

#Destination Endings
def end6A():
    text = """\n
    Er is 2 jaar voorbij sinds je Nederland in bent gekomen. 
    Je woont in je eigen huis in Amersfoort, je werkt als verpleegster en doet ook nog vluchtelingenwerk. 
    Je hebt tijdens je inburgering je MBO diploma gehaald en werkt nu bijna een jaar aan je HBO opleiding. 
    Je belt regelmatig nog met je familie, 
    maar wordt altijd een beetje emotioneel wanneer je jouw broertje ziet opgroeien zonder jou. 
    Al met al ziet de toekomst er mooi uit.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")
def end6B():
    text = """\n
    Er is 2 jaar voorbij sinds je Nederland in bent gekomen. 
    Je woont in je eigen huis in Amersfoort, je werkt als verpleegster en doet ook nog vluchtelingenwerk. 
    Je hebt tijdens je inburgering je MBO diploma gehaald en werkt nu bijna een jaar aan je HBO opleiding. 
    Je gaat regelmatig nog op bezoek bij je familie die in een ander huis wonen 
    en wordt altijd heel blij dat je jouw broertje kan zien opgroeien. 
    Je had niet voor een betere uitkomst van een ellendig verhaal kunnen wensen.
    """
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")

intro()