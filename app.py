from flask import Flask, render_template_string, render_template, send_file
import os

app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Priyadarshini College of Engineering | IT Department</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f4f9fc;
            color: #123f70;
        }


        /* =====================================================
           NAVBAR
        ===================================================== */

        .navbar {
            min-height: 72px;
            background: #063b70;

            display: flex;
            align-items: center;

            padding: 7px 5.5%;

            color: white;

            position: relative;
            z-index: 10;

            box-shadow: 0 3px 15px rgba(0,0,0,0.18);
        }


        .logo {
            width: 56px;
            height: 56px;

            background: white;

            border: 3px solid #19d5e3;
            border-radius: 13px;

            display: flex;
            align-items: center;
            justify-content: center;

            overflow: hidden;

            flex-shrink: 0;

            margin-right: 13px;
        }


        .logo img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }


        .college-name {
            flex: 1;
        }


        .college-name h1 {
            font-size: 23px;
            line-height: 1.1;
            white-space: nowrap;
        }


        .college-name span {
            color: #19cbd8;
            font-size: 14px;
            font-weight: bold;
        }


        .nav {
            display: flex;
            align-items: center;
            gap: 27px;
        }


        .nav a {
            color: white;
            text-decoration: none;

            font-size: 14px;
            font-weight: bold;

            white-space: nowrap;

            transition: 0.25s;
        }


        .nav a:hover {
            color: #18d5df;
        }


        /* =====================================================
           HERO SECTION
        ===================================================== */

        .hero {
            min-height: 620px;

            position: relative;

            display: flex;

            align-items: center;
            justify-content: center;

            text-align: center;

            overflow: hidden;

            background: #0b5d8a;
        }


        .hero::before {
            content: "";

            position: absolute;

            inset: 0;

            background-image: url("/college-image");

            background-size: cover;

            background-position: center;

            background-repeat: no-repeat;

            opacity: 0.42;

            transform: scale(1.02);

            z-index: 0;
        }


        .hero::after {
            content: "";

            position: absolute;

            inset: 0;

            background:
                linear-gradient(
                    135deg,
                    rgba(3, 59, 112, 0.52),
                    rgba(7, 142, 160, 0.38)
                );

            z-index: 1;
        }


        /* =====================================================
           HERO CONTENT
        ===================================================== */

        .hero-content {
            position: relative;

            z-index: 2;

            max-width: 950px;

            padding: 40px 25px;

            color: white;
        }


        .hero-badge {
            display: inline-block;

            padding: 9px 22px;

            border: 1px solid rgba(255,255,255,0.65);

            border-radius: 30px;

            background: rgba(255,255,255,0.12);

            backdrop-filter: blur(4px);

            font-size: 14px;

            font-weight: bold;

            letter-spacing: 1.5px;

            margin-bottom: 22px;

            color: white;

            box-shadow:
                0 4px 15px rgba(0,0,0,0.15);
        }


        .hero h2 {
            font-size: 56px;

            line-height: 1.08;

            margin-bottom: 18px;

            font-weight: 700;

            color: white;

            text-shadow:
                0 3px 12px rgba(0,0,0,0.55);
        }


        .hero h2 span {
            color: #20e0e5;

            text-shadow:
                0 3px 12px rgba(0,0,0,0.45);
        }


        .hero-line {
            width: 95px;

            height: 4px;

            background: #20d4df;

            margin: 0 auto 22px;

            border-radius: 10px;

            box-shadow:
                0 2px 8px rgba(0,0,0,0.25);
        }


        .hero p {
            max-width: 760px;

            margin: auto;

            font-size: 18px;

            line-height: 1.7;

            color: #ffffff;

            text-shadow:
                0 2px 7px rgba(0,0,0,0.55);
        }


        /* =====================================================
           BUTTONS
        ===================================================== */

        .buttons {
            display: flex;

            justify-content: center;

            gap: 15px;

            flex-wrap: wrap;

            margin-top: 32px;
        }


        .btn {
            display: inline-block;

            padding: 13px 27px;

            border-radius: 7px;

            background: #10c4d2;

            color: white;

            text-decoration: none;

            font-weight: bold;

            border: 2px solid #10c4d2;

            transition: 0.25s;

            box-shadow:
                0 5px 15px rgba(0,0,0,0.18);
        }


        .btn:hover {
            background: white;

            color: #063b70;

            border-color: white;

            transform: translateY(-2px);
        }


        .btn-outline {
            background: rgba(255,255,255,0.08);

            border: 2px solid white;

            color: white;

            backdrop-filter: blur(3px);
        }


        .btn-outline:hover {
            background: white;

            color: #063b70;
        }


        /* =====================================================
           STATISTICS
        ===================================================== */

        .stats-wrapper {
            position: relative;

            margin-top: -55px;

            z-index: 5;

            padding: 0 6%;
        }


        .stats {
            max-width: 1100px;

            margin: auto;

            display: grid;

            grid-template-columns: repeat(3, 1fr);

            background: white;

            border-radius: 14px;

            overflow: hidden;

            box-shadow:
                0 10px 35px rgba(0,50,90,0.18);
        }


        .stat {
            padding: 24px;

            display: flex;

            align-items: center;

            justify-content: center;

            gap: 15px;

            border-right: 1px solid #e2eaf0;
        }


        .stat:last-child {
            border-right: none;
        }


        .stat-icon {
            width: 55px;

            height: 55px;

            border-radius: 50%;

            background: #e3f8fb;

            color: #0da8bb;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 24px;

            flex-shrink: 0;
        }


        .stat h3 {
            color: #063b70;

            font-size: 28px;

            margin-bottom: 2px;
        }


        .stat strong {
            display: block;

            color: #234e73;

            font-size: 14px;
        }


        .stat small {
            color: #7890a5;

            font-size: 11px;
        }


        /* =====================================================
           SECTION
        ===================================================== */

        .section {
            max-width: 1200px;

            margin: auto;

            padding: 75px 25px 25px;
        }


        .section-title {
            text-align: center;

            font-size: 31px;

            color: #063b70;

            margin-bottom: 8px;
        }


        .section-title span {
            color: #0db5c7;
        }


        .subtitle {
            text-align: center;

            color: #687f96;

            font-size: 15px;

            margin-bottom: 35px;
        }


        /* =====================================================
           CARDS
        ===================================================== */

        .cards {
            display: grid;

            grid-template-columns: repeat(3, 1fr);

            gap: 22px;
        }


        .card {
            background: white;

            border-radius: 13px;

            padding: 25px;

            box-shadow:
                0 5px 20px rgba(0,50,90,0.10);

            border: 1px solid #e3edf3;

            transition: 0.3s;
        }


        .card:hover {
            transform: translateY(-6px);

            box-shadow:
                0 12px 28px rgba(0,50,90,0.16);
        }


        .icon {
            width: 58px;

            height: 58px;

            border-radius: 14px;

            background: #e2f8fb;

            color: #0da8bb;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 26px;

            margin-bottom: 17px;
        }


        .card h3 {
            color: #063b70;

            font-size: 19px;

            margin-bottom: 9px;
        }


        .card p {
            color: #687f96;

            font-size: 14px;

            line-height: 1.6;
        }


        /* =====================================================
           FACULTY
        ===================================================== */

        .faculty-card {
            border-top: 4px solid #13c5d4;
        }


        .faculty-card:nth-child(2) {
            border-top-color: #8064e9;
        }


        .faculty-card:nth-child(3) {
            border-top-color: #20b88b;
        }


        .tag {
            display: inline-block;

            padding: 5px 12px;

            border-radius: 20px;

            background: #e3f8fb;

            color: #078da0;

            font-size: 12px;

            font-weight: bold;

            margin-bottom: 12px;
        }


        .purple {
            background: #eee8ff;

            color: #7458dc;
        }


        .green {
            background: #dff8ef;

            color: #13a879;
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        footer {
            background: #063b70;

            color: white;

            margin-top: 75px;

            text-align: center;

            padding: 30px 20px;
        }


        footer h3 {
            font-size: 18px;

            margin-bottom: 6px;
        }


        footer span {
            color: #19d5e3;
        }


        footer p {
            color: #c9ddea;

            font-size: 13px;

            margin-top: 7px;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media(max-width: 1000px) {

            .navbar {
                flex-wrap: wrap;

                padding: 12px 25px;
            }


            .college-name h1 {
                font-size: 19px;

                white-space: normal;
            }


            .nav {
                width: 100%;

                justify-content: center;

                margin-top: 10px;

                flex-wrap: wrap;

                gap: 18px;
            }


            .hero {
                min-height: 560px;
            }


            .hero h2 {
                font-size: 45px;
            }


            .cards {
                grid-template-columns: 1fr 1fr;
            }

        }


        @media(max-width: 700px) {

            .hero {
                min-height: 580px;
            }


            .hero h2 {
                font-size: 36px;
            }


            .hero p {
                font-size: 15px;
            }


            .hero-badge {
                font-size: 11px;

                letter-spacing: 1px;
            }


            .stats-wrapper {
                margin-top: 20px;
            }


            .stats {
                grid-template-columns: 1fr;
            }


            .stat {
                border-right: none;

                border-bottom: 1px solid #e2eaf0;
            }


            .stat:last-child {
                border-bottom: none;
            }


            .cards {
                grid-template-columns: 1fr;
            }


            .section {
                padding-top: 55px;
            }


            .section-title {
                font-size: 25px;
            }

        }


        @media(max-width: 500px) {

            .logo {
                width: 48px;

                height: 48px;
            }


            .college-name h1 {
                font-size: 16px;
            }


            .college-name span {
                font-size: 12px;
            }


            .hero h2 {
                font-size: 31px;
            }


            .hero-badge {
                font-size: 10px;

                padding: 8px 12px;
            }


            .buttons {
                flex-direction: column;

                align-items: center;
            }


            .btn {
                width: 210px;
            }

        }

    </style>

</head>


<body>


<!-- =========================================================
     NAVBAR
========================================================= -->

<header class="navbar">

    <div class="logo">

        <img
            src="/college-logo.png"
            alt="Priyadarshini College Logo">

    </div>


    <div class="college-name">

        <h1>
            Priyadarshini College of Engineering
        </h1>

        <span>
            Nagpur
        </span>

    </div>


    <nav class="nav">

        <a href="/">
            Home
        </a>

        <a href="/labs">
            Labs
        </a>

        <a href="/courses">
            Courses
        </a>

        <a href="/faculty">
            Faculty
        </a>

        <a href="/placement">
            Placement
        </a>

        <!-- CONTACT LINK FIXED -->
        <a href="/contact">
            Contact
        </a>

    </nav>

</header>


<!-- =========================================================
     HERO
========================================================= -->

<section class="hero">

    <div class="hero-content">


        <div class="hero-badge">
            DEPARTMENT OF INFORMATION TECHNOLOGY
        </div>


        <h2>

            Information Technology

            <br>

            <span>Learn. Innovate. Build the Future.</span>

        </h2>


        <div class="hero-line"></div>


        <p>

            Empowering students with advanced technology,
            practical skills and industry-oriented education
            for a brighter future.

        </p>


        <div class="buttons">

            <a href="/courses" class="btn">
                Explore Programs →
            </a>


            <a href="/labs" class="btn btn-outline">
                Explore Our Labs
            </a>

        </div>

    </div>

</section>


<!-- =========================================================
     STATISTICS
========================================================= -->

<div class="stats-wrapper">

    <section class="stats">


        <div class="stat">

            <div class="stat-icon">
                👥
            </div>

            <div>

                <h3>120+</h3>

                <strong>
                    Students
                </strong>

                <small>
                    Enrolled in IT Programs
                </small>

            </div>

        </div>


        <div class="stat">

            <div class="stat-icon">
                ⚗
            </div>

            <div>

                <h3>3+</h3>

                <strong>
                    IT Labs
                </strong>

                <small>
                    Hands-on Learning Spaces
                </small>

            </div>

        </div>


        <div class="stat">

            <div class="stat-icon">
                ◎
            </div>

            <div>

                <h3>70%</h3>

                <strong>
                    Placement
                </strong>

                <small>
                    Placement Success Rate
                </small>

            </div>

        </div>


    </section>

</div>


<!-- =========================================================
     IT LABS
========================================================= -->

<section class="section" id="labs">

    <h2 class="section-title">
        Our <span>IT Laboratories</span>
    </h2>

    <p class="subtitle">
        Modern practical learning facilities for developing
        real-world technical skills.
    </p>


    <div class="cards">


        <div class="card">

            <div class="icon">
                ▣
            </div>

            <h3>
                FCIP Lab
            </h3>

            <p>
                Practical learning environment for programming,
                computer fundamentals and application development.
            </p>

        </div>


        <div class="card">

            <div class="icon">
                ◉
            </div>

            <h3>
                Data Structure Lab
            </h3>

            <p>
                Hands-on implementation of arrays, linked lists,
                stacks, queues, trees and searching techniques.
            </p>

        </div>


        <div class="card">

            <div class="icon">
                &lt;/&gt;
            </div>

            <h3>
                Web Technology Lab
            </h3>

            <p>
                Develop modern websites and applications using
                HTML, CSS, JavaScript, PHP and databases.
            </p>

        </div>


    </div>

</section>


<!-- =========================================================
     FACULTY
========================================================= -->

<section class="section" id="faculty">

    <h2 class="section-title">
        Our <span>Faculty</span>
    </h2>

    <p class="subtitle">
        Faculty members supporting students through focused
        technical and practical learning.
    </p>


    <div class="cards">


        <div class="card faculty-card">

            <div class="icon">
                🐍
            </div>

            <h3>
                Lalita Charpe
            </h3>

            <span class="tag">
                Python
            </span>

            <p>
                Python fundamentals, programming concepts,
                functions and object-oriented programming.
            </p>

        </div>


        <div class="card faculty-card">

            <div class="icon">
                ◉
            </div>

            <h3>
                Pradip Fale
            </h3>

            <span class="tag purple">
                Data Structure
            </span>

            <p>
                Arrays, linked lists, stacks, queues, trees,
                graphs and searching techniques.
            </p>

        </div>


        <div class="card faculty-card">

            <div class="icon">
                &lt;/&gt;
            </div>

            <h3>
                Ajinkya Gujar
            </h3>

            <span class="tag green">
                Web Technology
            </span>

            <p>
                HTML, CSS, JavaScript, PHP and database
                connectivity for modern web development.
            </p>

        </div>


    </div>

</section>


<!-- =========================================================
     FOOTER
========================================================= -->

<footer>

    <h3>
        Priyadarshini College of Engineering
    </h3>

    <span>
        Department of Information Technology
    </span>

    <p>
        Nagpur | Learn • Innovate • Build the Future
    </p>

    <p>
        © 2026 Priyadarshini College of Engineering.
        All Rights Reserved.
    </p>

</footer>


</body>

</html>
"""


# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    return render_template_string(HTML)


def display_html_page(filename):
    """Display an HTML page from templates/ or the same folder as app.py."""
    template_path = os.path.join(app.root_path, "templates", filename)
    root_path = os.path.join(app.root_path, filename)

    if os.path.isfile(template_path):
        return render_template(filename)
    if os.path.isfile(root_path):
        return send_file(root_path, mimetype="text/html")

    return (
        f"Page file '{filename}' was not found. Place it in the templates folder "
        "or beside app.py.",
        404,
    )


@app.route("/courses")
@app.route("/courses.html")
def courses():
    return display_html_page("courses.html")


@app.route("/labs")
@app.route("/labs.html")
def labs():
    return display_html_page("labs.html")


@app.route("/faculty")
@app.route("/faculty.html")
def faculty():
    return display_html_page("faculty.html")


# ============================================================
# PLACEMENT PAGE
# ============================================================

@app.route("/placement")
@app.route("/placement.html")
def placement():
    return display_html_page("placement.html")


# ============================================================
# CONTACT PAGE
# ============================================================

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return display_html_page("contact.html")


# ============================================================
# COLLEGE LOGO
# ============================================================

@app.route("/college-logo.png")
def college_logo():

    return send_file(
        os.path.join(
            app.root_path,
            "college-logo.png"
        ),
        mimetype="image/png"
    )


# ============================================================
# COLLEGE IMAGE
# ============================================================

@app.route("/college-image")
def college_image():

    return send_file(
        os.path.join(
            app.root_path,
            "Pce-college.jpeg"
        ),
        mimetype="image/jpeg"
    )


# ============================================================
# RUN APPLICATION       
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)