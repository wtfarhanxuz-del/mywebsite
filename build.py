html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Farhan | My World</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    background: #050505;
    color: #fff;
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

nav {
    position: fixed;
    top: 0;
    width: 100%;
    padding: 18px 7%;
    background: rgba(5,5,5,.9);
    backdrop-filter: blur(12px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    border-bottom: 1px solid #222;
}

.logo {
    font-size: 22px;
    font-weight: bold;
    letter-spacing: 3px;
}

nav a {
    color: #aaa;
    text-decoration: none;
    margin-left: 20px;
    font-size: 14px;
}

nav a:hover {
    color: white;
}

section {
    min-height: 100vh;
    padding: 110px 8% 70px;
}

.hero {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    background: radial-gradient(circle at 70% 40%, #202020 0%, #050505 45%);
}

.small {
    color: #888;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-size: 13px;
}

h1 {
    font-size: clamp(55px, 12vw, 130px);
    line-height: .9;
    letter-spacing: -5px;
    margin: 20px 0;
}

.hero p {
    max-width: 600px;
    color: #aaa;
    font-size: 18px;
}

.button {
    display: inline-block;
    margin-top: 30px;
    padding: 13px 25px;
    border: 1px solid #555;
    border-radius: 30px;
    color: white;
    text-decoration: none;
}

.title {
    font-size: 45px;
    margin-bottom: 15px;
}

.subtitle {
    color: #888;
    margin-bottom: 35px;
}

.about-text {
    max-width: 800px;
    color: #bbb;
    font-size: 19px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
}

.card {
    border: 1px solid #222;
    border-radius: 18px;
    padding: 28px;
    background: #0b0b0b;
    transition: .3s;
}

.card:hover {
    transform: translateY(-6px);
    border-color: #555;
}

.card h3 {
    margin-bottom: 10px;
}

.card p {
    color: #888;
}

.note {
    max-width: 800px;
    padding: 35px;
    border-left: 2px solid white;
    background: #0b0b0b;
}

.note p {
    color: #bbb;
    font-size: 20px;
}

.socials a {
    display: inline-block;
    margin: 8px;
    padding: 12px 20px;
    border: 1px solid #333;
    border-radius: 30px;
    color: white;
    text-decoration: none;
}

.ai {
    background: #080808;
}

.chat {
    max-width: 700px;
    border: 1px solid #222;
    border-radius: 20px;
    padding: 25px;
    background: #0d0d0d;
}

.message {
    padding: 15px;
    margin-bottom: 12px;
    border-radius: 12px;
    background: #161616;
    color: #bbb;
}

footer {
    padding: 35px;
    text-align: center;
    color: #666;
    border-top: 1px solid #222;
}

@media(max-width:700px) {
    nav {
        padding: 15px 5%;
    }

    nav .links {
        display: none;
    }

    section {
        padding-left: 6%;
        padding-right: 6%;
    }

    h1 {
        font-size: 70px;
    }

    .title {
        font-size: 36px;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">FARHAN</div>

    <div class="links">
        <a href="#about">About</a>
        <a href="#movies">Movies</a>
        <a href="#gaming">Gaming</a>
        <a href="#football">Football</a>
        <a href="#music">Music</a>
        <a href="#note">Note</a>
        <a href="#ai">AI</a>
    </div>
</nav>

<section class="hero">
    <span class="small">Welcome to my world</span>

    <h1>FARHAN</h1>

    <p>
        A small place on the internet where I keep
        the things I like, the memories I have,
        and a little bit of who I am.
    </p>

    <a class="button" href="#about">Explore My World ↓</a>
</section>

<section id="about">
    <h2 class="title">About Me</h2>
    <p class="subtitle">A little about the person behind this website.</p>

    <p class="about-text">
        I'm Farhan Talukdar. I'm an HSC student who enjoys
        movies, series, gaming, music, football and WWE.
        I'm also interested in Accounting and ICT.
        This website is my own little corner of the internet.
    </p>
</section>

<section id="movies">
    <h2 class="title">Movies & Series</h2>
    <p class="subtitle">Stories that I enjoy.</p>

    <div class="grid">
        <div class="card">
            <h3>Avengers: Infinity War</h3>
            <p>One of my favorite movies.</p>
        </div>

        <div class="card">
            <h3>Stranger Things</h3>
            <p>Mystery, adventure and the unknown.</p>
        </div>

        <div class="card">
            <h3>From</h3>
            <p>A mysterious town full of questions.</p>
        </div>

        <div class="card">
            <h3>Horror & Mystery</h3>
            <p>I enjoy stories that keep me guessing.</p>
        </div>
    </div>
</section>

<section id="gaming">
    <h2 class="title">Gaming</h2>
    <p class="subtitle">Games I've spent time with.</p>

    <div class="grid">
        <div class="card">
            <h3>PUBG</h3>
            <p>Battle royale and competitive gameplay.</p>
        </div>

        <div class="card">
            <h3>GTA San Andreas</h3>
            <p>One of those games that never gets old.</p>
        </div>
    </div>
</section>

<section id="football">
    <h2 class="title">Football & WWE</h2>
    <p class="subtitle">Two things I enjoy watching.</p>

    <div class="grid">
        <div class="card">
            <h3>Football</h3>
            <p>Haaland, Cristiano Ronaldo and the beautiful game.</p>
        </div>

        <div class="card">
            <h3>WWE</h3>
            <p>Matches, characters and unforgettable moments.</p>
        </div>
    </div>
</section>

<section id="music">
    <h2 class="title">Music</h2>
    <p class="subtitle">A space for the songs and artists I like.</p>

    <div class="card">
        <h3>My Music</h3>
        <p>
            This section can later become a full music collection
            with favorite artists, albums and playlists.
        </p>
    </div>
</section>

<section id="note">
    <h2 class="title">A Note From Me</h2>

    <div class="note">
        <p>
            This website isn't here to impress anyone.
            It's simply a small personal place on the internet.
            Maybe nobody will visit it, and that's okay.
            I made it because it's mine.
        </p>
    </div>
</section>

<section id="ai" class="ai">
    <h2 class="title">Farhan AI</h2>
    <p class="subtitle">Ask me something about Farhan.</p>

    <div class="chat">
        <div class="message">
            🤖 Hi! I'm Farhan's AI.
        </div>

        <div class="message">
            Ask me about his interests, favorite things,
            studies or life story.
        </div>
    </div>
</section>

<section id="find">
    <h2 class="title">Find Me</h2>
    <p class="subtitle">You can find me here.</p>

    <div class="socials">
        <a href="https://instagram.com/farhan21112009">Instagram</a>
        <a href="https://facebook.com/">Facebook</a>
        <a href="https://x.com/wtfarhanxuz">X</a>
        <a href="https://boxd.it/mnCnn">Letterboxd</a>
    </div>
</section>

<footer>
    © 2026 Farhan. Made from my phone.
</footer>

</body>
</html>'''

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Website created successfully!")
