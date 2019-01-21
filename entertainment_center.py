import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/pixar/images/1/10/Buzz-lightyear-disney-toy-story_1_803ffb6c3041cf8eec7d599c38657ff6.jpg/revision/latest?cb=20170510124704",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                      "https://vignette.wikia.nocookie.net/ppc/images/d/d6/Avatar-movie-poster.jpg/revision/latest?cb=20110913151129",
                      "http://www.youtube.com/watch?v=-9ceBgWV8io")

idiocracy = media.Movie("idiocracy", "idiots democracy",
                        "http://wearecult.rocks/moviedrome-redux-idiocracy-2006/idiocracy-poster",
                        "https://www.youtube.com/watch?v=BBvIweCIgwk")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://vignette.wikia.nocookie.net/schoolofrockseries/images/a/a4/School_of_Rock_poster.jpg/revision/latest?cb=20160716051012",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "Storyline",
                          "https://vignette.wikia.nocookie.net/disney/images/c/c8/Ratatouille_poster.jpg/revision/latest?cb=20130328084644",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "https://static.squarespace.com/static/52d6d1ede4b0b322e9c7a2ea/52de8be5e4b09af5e9c166ab/52de8befe4b09af5e9c16fca/1390316527765/1000w/",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Storyline",
                            "https://vignette.wikia.nocookie.net/thehungergames/images/8/8c/The-hunger-games.jpg/revision/latest?cb=20120624000043",
                            "https://www.youtube.com/watch?v=RCDHJ6P_y0I")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)