from ext import app, db
from models import Anime, User

with app.app_context():
    db.drop_all()
    db.create_all()


    admin = User(username="admin", password="Betty.bought.abit.of.butter", role="Admin")
    admin.create()

    initial_animes = [
        Anime(
            title="Jujutsu Kaisen", release_year=2020, image="jjk.jpg",
            description_en="A high school student swallows a cursed talisman and joins a secret school for sorcerers.",
            description_ka="სკოლის მოსწავლე ყლაპავს დაწყევლილ თილისმას და უერთდება ჯადოქრების საიდუმლო სკოლას.",
            description_ja="特級呪物「両面宿儺の指」を喰らった少年・虎杖悠仁が呪いの戦いに身投じる。"
        ),
        Anime(
            title="Solo Leveling", release_year=2024, image="solo leveling.jpg",
            description_en="In a world where hunters must battle deadly monsters, Sung Jinwoo, the weakest hunter, gains a mysterious system.",
            description_ka="სამყაროში, სადაც მონადირეები ებრძვიან მონსტრებს, ყველაზე სუსტი მონადირე სუნგ ჯინვუ იღებს მისტიკურ სისტემას.",
            description_ja="人類 ინოვაციურიアクション, 最弱ハンターの水篠旬が特別なシステムを得て世界最強へと駆け上がる。"
        ),
        Anime(
            title="Oshi no Ko", release_year=2023, image="oshi no ko.jpg",
            description_en="A gynecologist and his deceased patient are reborn as twins to a famous Japanese pop idol star.",
            description_ka="ექიმი გინეკოლოგი და მისი გარდაცვლილი პაციენტი რეინკარნაციას განიცდიან და იბადებიან ცნობილი აიდოლის ტყუპებად.",
            description_ja="芸能界の光と影を描く、アイドルの子どもに転生した双子の衝撃の物語。"
        ),
        Anime(
            title="Horimiya", release_year=2021, image="horimiya.jpg",
            description_en="A sweet high school romance between a popular girl and an introverted, hidden punk classmate.",
            description_ka="თბილი სასკოლო რომანტიკა პოპულარულ გოგონასა და ინტროვერტ, დამალული სტილის მქონე კლასელს შორის.",
            description_ja="クラス一のモテ女子・堀さんと、実はネクラ男子の宮村くんの甘酸っぱい青春ラブコメ。"
        ),
        Anime(
            title="Bungo Stray Dogs", release_year=2016, image="bungo stray dogs.jpg",
            description_en="An orphan joins an agency filled with individuals possessing supernatural powers based on literary figures.",
            description_ka="ობოლი ბიჭი უერთდება დეტექტივების სააგენტოს, რომლის წევრებსაც აქვთ ზებუნებრივი ლიტერატურული ნიჭი.",
            description_ja="実在の文豪の名を持つキャラクターたちが超能力で戦う異能アクションバトル。"
        ),
        Anime(
            title="Your Name", release_year=2016, image="ur name.jpg",
            description_en="Two strangers find themselves linked in a bizarre way after body-swapping and dreaming of each other.",
            description_ka="ორი უცნობი აღმოაჩენს, რომ უცნაურად უკავშირდებიან ერთმანეთს სხეულების გაცვლითა და სიზმრებით.",
            description_ja="東京の少年と田舎の少女の身が入れ替わる、新海誠監督の大ヒットアニメ映画。"
        ),
        Anime(
            title="Tokyo Ghoul", release_year=2014, image="tokyo ghoul.jpg",
            description_en="A college student is turned into a half-ghoul and must learn to live in a dark, predatory society.",
            description_ka="სტუდენტი გადაიქცევა ნახევრად გულად და უწევს გადარჩენისთვის ბრძოლა ორ სამყაროს შორის.",
            description_ja="人間を喰らう怪人「喰種」の世界に足を踏み入れた青年の悲劇と成長。"
        ),
        Anime(
            title="Demon Slayer (KNY)", release_year=2019, image="KNY.jpg",
            description_en="Tanjiro Kamado sets out to become a demon slayer after his family is slaughtered and his sister turned.",
            description_ka="ტანჯირო კამადო ხდება დემონებზე მონადირე, რათა იხსნას თავისი და, რომელიც დემონად იქცა.",
            description_ja="鬼に変貌した妹を人間に戻すため、少年・炭治郎が過酷な旅に出る。"
        ),
        Anime(
            title="Haikyuu!!", release_year=2014, image="Haikyuu.jpg",
            description_en="Shoyo Hinata, determined to become a great volleyball player despite his small height, joins Karasuno High.",
            description_ka="შოიო ჰინატა, რომელსაც სურს გახდეს ფრენბურთის ვარსკვლავი მიუხედავად დაბალი სიმაღლისა, უერთდება კარასუნოს გუნდს.",
            description_ja="小柄な少年・日向翔陽がバレーボールにかける熱い青春スポーツアニメ。"
        ),
        Anime(
            title="Death Note", release_year=2006, image="Death Note.jpg",
            description_en="A brilliant high school student discovers a supernatural notebook that grants him the power to kill anyone.",
            description_ka="გენიალური მოსწავლე პოულობს მისტიკურ რვეულს, რომლის დახმარებითაც შეუძლია ნებისმიერი ადამიანის მოკვლა მისი სახელის ჩაწერით.",
            description_ja="名前を書かれた人間は死ぬ「死神のノート」を巡る天才たちの頭脳戦。"
        ),
        Anime(
            title="Wind Breaker", release_year=2024, image="wind breaker.jpg",
            description_en="Haruka Sakura wants nothing to do with weaklings—he's only interested in the strongest of the strong at Furin High.",
            description_ka="ჰარუკა საკურას მხოლოდ ძლიერებთან ბრძოლა აინტერესებს ფურინის სკოლაში, რომელიც ქალაქს იცავს.",
            description_ja="街を守る英雄となった不良高校生たちの喧嘩と友情を描く、新世代ヤンキーアニメ。"
        ),
        Anime(
            title="Paprika", release_year=2006, image="paprika.jpg",
            description_en="In the near future, a revolutionary device allows therapists to enter into patients' dreams.",
            description_ka="ახლო მომავალში, რევოლუციური მოწყობილობა ფსიქოთერაპევტებს საშუალებას აძლევს შევიდნენ პაციენტების სიზმრებში.",
            description_ja="今敏監督による、他人の夢を共有するデバイスを巡るサイケデリックな傑作SF映画。"
        )
    ]

    for anime in initial_animes:
        anime.create()

    print("seccesful")