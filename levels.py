LEVELS = {
    1: [
        {
            "statement": "Select the title and director columns from the movies table.",
            "solution_code": 'movies[["title", "director"]]',
            "hint": "Use double brackets df[['col1', 'col2']] to select multiple columns.",
            "category": "select-columns",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,year,budget_millions,rating\n"
                        "Jaws,Steven Spielberg,1975,9,8.0\n"
                        "The Godfather,Francis Ford Coppola,1972,6,9.2\n"
                        "Star Wars,George Lucas,1977,11,8.6\n"
                        "Alien,Ridley Scott,1979,11,8.5\n"
                        "A Clockwork Orange,Stanley Kubrick,1971,2,8.3"
                    ),
                }
            ],
            "expected_csv": (
                "title,director\n"
                "Jaws,Steven Spielberg\n"
                "The Godfather,Francis Ford Coppola\n"
                "Star Wars,George Lucas\n"
                "Alien,Ridley Scott\n"
                "A Clockwork Orange,Stanley Kubrick"
            ),
        },
        {
            "statement": "Select the title and rating columns from the classics table.",
            "solution_code": 'classics[["title", "rating"]]',
            "hint": "Use double brackets df[['col1', 'col2']] to select multiple columns.",
            "category": "select-columns",
            "tables": [
                {
                    "name": "classics",
                    "csv": (
                        "title,director,year,rating,genre\n"
                        "Apocalypse Now,Francis Ford Coppola,1979,8.4,War\n"
                        "Raiders of the Lost Ark,Steven Spielberg,1981,8.4,Adventure\n"
                        "Blade Runner,Ridley Scott,1982,8.1,Sci-Fi\n"
                        "The Shining,Stanley Kubrick,1980,8.4,Horror\n"
                        "Return of the Jedi,George Lucas,1983,8.3,Sci-Fi"
                    ),
                }
            ],
            "expected_csv": (
                "title,rating\n"
                "Apocalypse Now,8.4\n"
                "Raiders of the Lost Ark,8.4\n"
                "Blade Runner,8.1\n"
                "The Shining,8.4\n"
                "Return of the Jedi,8.3"
            ),
        },
        {
            "statement": "Select the director and year columns from the blockbusters table.",
            "solution_code": 'blockbusters[["director", "year"]]',
            "hint": "Use double brackets df[['col1', 'col2']] to select multiple columns.",
            "category": "select-columns",
            "tables": [
                {
                    "name": "blockbusters",
                    "csv": (
                        "title,director,year,box_office_millions\n"
                        "E.T. the Extra-Terrestrial,Steven Spielberg,1982,435\n"
                        "The Empire Strikes Back,George Lucas,1980,538\n"
                        "The Godfather Part II,Francis Ford Coppola,1974,57\n"
                        "Full Metal Jacket,Stanley Kubrick,1987,46\n"
                        "Alien,Ridley Scott,1979,104"
                    ),
                }
            ],
            "expected_csv": (
                "director,year\n"
                "Steven Spielberg,1982\n"
                "George Lucas,1980\n"
                "Francis Ford Coppola,1974\n"
                "Stanley Kubrick,1987\n"
                "Ridley Scott,1979"
            ),
        },
        {
            "statement": "Select the title and budget_millions columns from the productions table.",
            "solution_code": 'productions[["title", "budget_millions"]]',
            "hint": "Use double brackets df[['col1', 'col2']] to select multiple columns.",
            "category": "select-columns",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "title,director,year,budget_millions,genre\n"
                        "Close Encounters of the Third Kind,Steven Spielberg,1977,20,Sci-Fi\n"
                        "The Conversation,Francis Ford Coppola,1974,2,Thriller\n"
                        "2001 A Space Odyssey,Stanley Kubrick,1968,12,Sci-Fi\n"
                        "Star Wars,George Lucas,1977,11,Sci-Fi\n"
                        "Alien,Ridley Scott,1979,11,Horror"
                    ),
                }
            ],
            "expected_csv": (
                "title,budget_millions\n"
                "Close Encounters of the Third Kind,20\n"
                "The Conversation,2\n"
                "2001 A Space Odyssey,12\n"
                "Star Wars,11\n"
                "Alien,11"
            ),
        },
        {
            "statement": "Filter the movies table to show only movies with a rating greater than 8.5.",
            "solution_code": 'movies[movies["rating"] > 8.5]',
            "hint": "Use boolean indexing: df[df['column'] > value].",
            "category": "filter-gt",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,year,rating\n"
                        "The Godfather,Francis Ford Coppola,1972,9.2\n"
                        "Jaws,Steven Spielberg,1975,8.0\n"
                        "Star Wars,George Lucas,1977,8.6\n"
                        "Apocalypse Now,Francis Ford Coppola,1979,8.4\n"
                        "The Shining,Stanley Kubrick,1980,8.4"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "The Godfather,Francis Ford Coppola,1972,9.2\n"
                "Star Wars,George Lucas,1977,8.6"
            ),
        },
        {
            "statement": "Filter the box_office table to show only films that earned less than 200 million dollars.",
            "solution_code": 'box_office[box_office["revenue_millions"] < 200]',
            "hint": "Use boolean indexing: df[df['column'] < value].",
            "category": "filter-lt",
            "tables": [
                {
                    "name": "box_office",
                    "csv": (
                        "title,director,revenue_millions\n"
                        "Jaws,Steven Spielberg,471\n"
                        "The Godfather,Francis Ford Coppola,245\n"
                        "Alien,Ridley Scott,104\n"
                        "A Clockwork Orange,Stanley Kubrick,27\n"
                        "Star Wars,George Lucas,775"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,revenue_millions\n"
                "Alien,Ridley Scott,104\n"
                "A Clockwork Orange,Stanley Kubrick,27"
            ),
        },
        {
            "statement": "Filter the releases table to show only films released in 1977.",
            "solution_code": 'releases[releases["year"] == 1977]',
            "hint": "Use boolean indexing with ==: df[df['column'] == value].",
            "category": "filter-eq",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "title,director,year,genre\n"
                        "Star Wars,George Lucas,1977,Sci-Fi\n"
                        "Close Encounters of the Third Kind,Steven Spielberg,1977,Sci-Fi\n"
                        "The Godfather Part II,Francis Ford Coppola,1974,Crime\n"
                        "Alien,Ridley Scott,1979,Horror\n"
                        "Barry Lyndon,Stanley Kubrick,1975,Drama"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,genre\n"
                "Star Wars,George Lucas,1977,Sci-Fi\n"
                "Close Encounters of the Third Kind,Steven Spielberg,1977,Sci-Fi"
            ),
        },
        {
            "statement": "Filter the budgets table to show only films with a budget of at least 15 million dollars.",
            "solution_code": 'budgets[budgets["budget_millions"] >= 15]',
            "hint": "Use boolean indexing: df[df['column'] >= value].",
            "category": "filter-gte",
            "tables": [
                {
                    "name": "budgets",
                    "csv": (
                        "title,director,budget_millions,year\n"
                        "Close Encounters of the Third Kind,Steven Spielberg,20,1977\n"
                        "Apocalypse Now,Francis Ford Coppola,31,1979\n"
                        "The Shining,Stanley Kubrick,19,1980\n"
                        "Star Wars,George Lucas,11,1977\n"
                        "Blade Runner,Ridley Scott,28,1982"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_millions,year\n"
                "Close Encounters of the Third Kind,Steven Spielberg,20,1977\n"
                "Apocalypse Now,Francis Ford Coppola,31,1979\n"
                "The Shining,Stanley Kubrick,19,1980\n"
                "Blade Runner,Ridley Scott,28,1982"
            ),
        },
        {
            "statement": "Filter the awards table to show only films with fewer than 8 Oscar nominations.",
            "solution_code": 'awards[awards["nominations"] < 8]',
            "hint": "Use boolean indexing: df[df['column'] < value].",
            "category": "filter-lt",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "title,director,nominations,wins\n"
                        "Star Wars,George Lucas,10,6\n"
                        "Jaws,Steven Spielberg,4,3\n"
                        "The Godfather,Francis Ford Coppola,11,3\n"
                        "Alien,Ridley Scott,2,1\n"
                        "A Clockwork Orange,Stanley Kubrick,4,0"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,nominations,wins\n"
                "Jaws,Steven Spielberg,4,3\n"
                "Alien,Ridley Scott,2,1\n"
                "A Clockwork Orange,Stanley Kubrick,4,0"
            ),
        },
        {
            "statement": "Filter the sequels table to show only films with a rating of 7.5 or below.",
            "solution_code": 'sequels[sequels["rating"] <= 7.5]',
            "hint": "Use boolean indexing: df[df['column'] <= value].",
            "category": "filter-lte",
            "tables": [
                {
                    "name": "sequels",
                    "csv": (
                        "title,director,year,rating\n"
                        "The Empire Strikes Back,George Lucas,1980,8.7\n"
                        "Indiana Jones and the Temple of Doom,Steven Spielberg,1984,7.5\n"
                        "The Godfather Part II,Francis Ford Coppola,1974,9.0\n"
                        "Aliens,James Cameron,1986,8.4\n"
                        "Return of the Jedi,George Lucas,1983,8.3"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Indiana Jones and the Temple of Doom,Steven Spielberg,1984,7.5"
            ),
        },
    ],
    2: [
        {
            "statement": "Filter the movies table to show only films directed by Quentin Tarantino.",
            "solution_code": 'movies[movies["director"] == "Quentin Tarantino"]',
            "hint": "Use df[df['column'] == 'value'] to filter rows by a string value.",
            "category": "filter-string",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,year,genre\n"
                        "Pulp Fiction,Quentin Tarantino,1994,Crime\n"
                        "Fargo,Coen Brothers,1996,Thriller\n"
                        "Titanic,James Cameron,1997,Romance\n"
                        "Fight Club,David Fincher,1999,Drama\n"
                        "Jackie Brown,Quentin Tarantino,1997,Crime"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,genre\n"
                "Pulp Fiction,Quentin Tarantino,1994,Crime\n"
                "Jackie Brown,Quentin Tarantino,1997,Crime"
            ),
        },
        {
            "statement": "Get all Crime movies from the films table.",
            "solution_code": 'films[films["genre"] == "Crime"]',
            "hint": "Use df[df['column'] == 'value'] to filter rows matching a string.",
            "category": "filter-string",
            "tables": [
                {
                    "name": "films",
                    "csv": (
                        "title,director,genre,rating\n"
                        "Pulp Fiction,Quentin Tarantino,Crime,8.9\n"
                        "Se7en,David Fincher,Thriller,8.6\n"
                        "The Usual Suspects,Bryan Singer,Crime,8.5\n"
                        "Schindlers List,Steven Spielberg,Drama,9.0\n"
                        "Reservoir Dogs,Quentin Tarantino,Crime,8.3"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,genre,rating\n"
                "Pulp Fiction,Quentin Tarantino,Crime,8.9\n"
                "The Usual Suspects,Bryan Singer,Crime,8.5\n"
                "Reservoir Dogs,Quentin Tarantino,Crime,8.3"
            ),
        },
        {
            "statement": "Filter the releases table to show only films distributed by Miramax.",
            "solution_code": 'releases[releases["studio"] == "Miramax"]',
            "hint": "Use df[df['column'] == 'value'] to select rows where a column equals a string.",
            "category": "filter-string",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "title,studio,budget_m,revenue_m\n"
                        "Titanic,20th Century Fox,200,2187\n"
                        "True Lies,20th Century Fox,115,379\n"
                        "Pulp Fiction,Miramax,8,214\n"
                        "Jackie Brown,Miramax,12,74\n"
                        "The Thin Red Line,20th Century Fox,52,98"
                    ),
                }
            ],
            "expected_csv": (
                "title,studio,budget_m,revenue_m\n"
                "Pulp Fiction,Miramax,8,214\n"
                "Jackie Brown,Miramax,12,74"
            ),
        },
        {
            "statement": "Filter the nominations table to only show actors who Won their Oscar.",
            "solution_code": 'nominations[nominations["result"] == "Won"]',
            "hint": "Use df[df['column'] == 'value'] to filter by a string match.",
            "category": "filter-string",
            "tables": [
                {
                    "name": "nominations",
                    "csv": (
                        "actor,film,result,year\n"
                        "Tom Hanks,Forrest Gump,Won,1994\n"
                        "John Travolta,Pulp Fiction,Nominated,1994\n"
                        "Morgan Freeman,The Shawshank Redemption,Nominated,1994\n"
                        "Nicolas Cage,Leaving Las Vegas,Won,1995\n"
                        "Kevin Spacey,American Beauty,Won,1999"
                    ),
                }
            ],
            "expected_csv": (
                "actor,film,result,year\n"
                "Tom Hanks,Forrest Gump,Won,1994\n"
                "Nicolas Cage,Leaving Las Vegas,Won,1995\n"
                "Kevin Spacey,American Beauty,Won,1999"
            ),
        },
        {
            "statement": "Get all Steven Spielberg films from the catalog table. Show only the title and year columns.",
            "solution_code": 'catalog[catalog["director"] == "Steven Spielberg"][["title", "year"]]',
            "hint": "First filter rows with df[df['col'] == 'value'], then select columns with double brackets.",
            "category": "filter-string-select",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,director,genre,year\n"
                        "Schindlers List,Steven Spielberg,Drama,1993\n"
                        "The Big Lebowski,Coen Brothers,Comedy,1998\n"
                        "Saving Private Ryan,Steven Spielberg,War,1998\n"
                        "Jurassic Park,Steven Spielberg,Sci-Fi,1993\n"
                        "Se7en,David Fincher,Thriller,1995"
                    ),
                }
            ],
            "expected_csv": (
                "title,year\n"
                "Schindlers List,1993\n"
                "Saving Private Ryan,1998\n"
                "Jurassic Park,1993"
            ),
        },
        {
            "statement": "Sort the classics table by rating in ascending order.",
            "solution_code": 'classics.sort_values("rating")',
            "hint": "Use df.sort_values('column') to sort in ascending order (the default).",
            "category": "sort-asc",
            "tables": [
                {
                    "name": "classics",
                    "csv": (
                        "title,director,rating\n"
                        "Fight Club,David Fincher,8.8\n"
                        "Fargo,Coen Brothers,8.1\n"
                        "Pulp Fiction,Quentin Tarantino,8.9\n"
                        "The Big Lebowski,Coen Brothers,8.2\n"
                        "Se7en,David Fincher,8.6"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,rating\n"
                "Fargo,Coen Brothers,8.1\n"
                "The Big Lebowski,Coen Brothers,8.2\n"
                "Se7en,David Fincher,8.6\n"
                "Fight Club,David Fincher,8.8\n"
                "Pulp Fiction,Quentin Tarantino,8.9"
            ),
        },
        {
            "statement": "Sort the blockbusters table by box_office_m from highest to lowest.",
            "solution_code": 'blockbusters.sort_values("box_office_m", ascending=False)',
            "hint": "Use df.sort_values('column', ascending=False) to sort in descending order.",
            "category": "sort-desc",
            "tables": [
                {
                    "name": "blockbusters",
                    "csv": (
                        "title,year,box_office_m\n"
                        "Titanic,1997,2187\n"
                        "Saving Private Ryan,1998,482\n"
                        "Forrest Gump,1994,678\n"
                        "Pulp Fiction,1994,214\n"
                        "The Matrix,1999,463"
                    ),
                }
            ],
            "expected_csv": (
                "title,year,box_office_m\n"
                "Titanic,1997,2187\n"
                "Forrest Gump,1994,678\n"
                "Saving Private Ryan,1998,482\n"
                "The Matrix,1999,463\n"
                "Pulp Fiction,1994,214"
            ),
        },
        {
            "statement": "Sort the nineties table by year from earliest to latest.",
            "solution_code": 'nineties.sort_values("year")',
            "hint": "Use df.sort_values('column') to sort in ascending order.",
            "category": "sort-asc",
            "tables": [
                {
                    "name": "nineties",
                    "csv": (
                        "title,director,year,budget_m\n"
                        "Jurassic Park,Steven Spielberg,1993,63\n"
                        "Fight Club,David Fincher,1999,63\n"
                        "Fargo,Coen Brothers,1996,7\n"
                        "Pulp Fiction,Quentin Tarantino,1994,8\n"
                        "Titanic,James Cameron,1997,200"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,budget_m\n"
                "Jurassic Park,Steven Spielberg,1993,63\n"
                "Pulp Fiction,Quentin Tarantino,1994,8\n"
                "Fargo,Coen Brothers,1996,7\n"
                "Titanic,James Cameron,1997,200\n"
                "Fight Club,David Fincher,1999,63"
            ),
        },
        {
            "statement": "Sort the productions table by budget_m in descending order. Show only the title and budget_m columns.",
            "solution_code": 'productions.sort_values("budget_m", ascending=False)[["title", "budget_m"]]',
            "hint": "Sort with df.sort_values('col', ascending=False), then select columns with double brackets.",
            "category": "sort-desc-select",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "title,director,budget_m,year\n"
                        "Titanic,James Cameron,200,1997\n"
                        "True Lies,James Cameron,115,1994\n"
                        "Jurassic Park,Steven Spielberg,63,1993\n"
                        "Pulp Fiction,Quentin Tarantino,8,1994\n"
                        "Fargo,Coen Brothers,7,1996"
                    ),
                }
            ],
            "expected_csv": (
                "title,budget_m\n"
                "Titanic,200\n"
                "True Lies,115\n"
                "Jurassic Park,63\n"
                "Pulp Fiction,8\n"
                "Fargo,7"
            ),
        },
        {
            "statement": "Sort the screenings table by runtime_min from shortest to longest.",
            "solution_code": 'screenings.sort_values("runtime_min")',
            "hint": "Use df.sort_values('column') to sort in ascending order.",
            "category": "sort-asc",
            "tables": [
                {
                    "name": "screenings",
                    "csv": (
                        "title,director,runtime_min\n"
                        "Fargo,Coen Brothers,98\n"
                        "Reservoir Dogs,Quentin Tarantino,99\n"
                        "Se7en,David Fincher,127\n"
                        "Schindlers List,Steven Spielberg,195\n"
                        "Titanic,James Cameron,194"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,runtime_min\n"
                "Fargo,Coen Brothers,98\n"
                "Reservoir Dogs,Quentin Tarantino,99\n"
                "Se7en,David Fincher,127\n"
                "Titanic,James Cameron,194\n"
                "Schindlers List,Steven Spielberg,195"
            ),
        },
    ],
    3: [
        {
            "statement": "Drop the studio column from the movies table.",
            "solution_code": 'movies.drop(columns=["studio"])',
            "hint": "Use df.drop(columns=['column_name']) to remove a column.",
            "category": "drop-column",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,year,budget_m,studio\n"
                        "The Dark Knight,Christopher Nolan,2008,185,Warner Bros\n"
                        "Inception,Christopher Nolan,2010,160,Warner Bros\n"
                        "Gladiator,Ridley Scott,2000,103,DreamWorks\n"
                        "The Fellowship of the Ring,Peter Jackson,2001,93,New Line\n"
                        "Slumdog Millionaire,Danny Boyle,2008,15,Fox Searchlight"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,budget_m\n"
                "The Dark Knight,Christopher Nolan,2008,185\n"
                "Inception,Christopher Nolan,2010,160\n"
                "Gladiator,Ridley Scott,2000,103\n"
                "The Fellowship of the Ring,Peter Jackson,2001,93\n"
                "Slumdog Millionaire,Danny Boyle,2008,15"
            ),
        },
        {
            "statement": "Drop the runtime_min and rating columns from the blockbusters table.",
            "solution_code": 'blockbusters.drop(columns=["runtime_min", "rating"])',
            "hint": "Use df.drop(columns=['col1', 'col2']) to remove multiple columns at once.",
            "category": "drop-columns",
            "tables": [
                {
                    "name": "blockbusters",
                    "csv": (
                        "title,director,year,runtime_min,rating,genre\n"
                        "The Dark Knight,Christopher Nolan,2008,152,9.0,Action\n"
                        "The Return of the King,Peter Jackson,2003,201,9.0,Fantasy\n"
                        "Brokeback Mountain,Ang Lee,2005,134,7.7,Drama\n"
                        "Gladiator,Ridley Scott,2000,155,8.5,Action\n"
                        "28 Days Later,Danny Boyle,2002,113,7.6,Horror"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,genre\n"
                "The Dark Knight,Christopher Nolan,2008,Action\n"
                "The Return of the King,Peter Jackson,2003,Fantasy\n"
                "Brokeback Mountain,Ang Lee,2005,Drama\n"
                "Gladiator,Ridley Scott,2000,Action\n"
                "28 Days Later,Danny Boyle,2002,Horror"
            ),
        },
        {
            "statement": "Drop the nominations column from the awards table.",
            "solution_code": 'awards.drop(columns=["nominations"])',
            "hint": "Use df.drop(columns=['column_name']) to remove a single column.",
            "category": "drop-column",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "title,year,revenue_m,awards_won,nominations\n"
                        "The Dark Knight,2008,1005,2,8\n"
                        "The Two Towers,2002,936,2,6\n"
                        "Crouching Tiger Hidden Dragon,2000,213,4,10\n"
                        "Slumdog Millionaire,2008,378,8,10\n"
                        "28 Days Later,2002,85,0,3"
                    ),
                }
            ],
            "expected_csv": (
                "title,year,revenue_m,awards_won\n"
                "The Dark Knight,2008,1005,2\n"
                "The Two Towers,2002,936,2\n"
                "Crouching Tiger Hidden Dragon,2000,213,4\n"
                "Slumdog Millionaire,2008,378,8\n"
                "28 Days Later,2002,85,0"
            ),
        },
        {
            "statement": "Drop the genre and rating columns from the catalog table.",
            "solution_code": 'catalog.drop(columns=["genre", "rating"])',
            "hint": "Pass a list of column names to df.drop(columns=[...]) to remove multiple columns.",
            "category": "drop-columns",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,director,genre,budget_m,revenue_m,rating\n"
                        "Inception,Christopher Nolan,Sci-Fi,160,836,8.8\n"
                        "The Two Towers,Peter Jackson,Fantasy,94,936,8.8\n"
                        "Kingdom of Heaven,Ridley Scott,Epic,130,211,7.2\n"
                        "Life of Pi,Ang Lee,Adventure,120,609,7.9\n"
                        "127 Hours,Danny Boyle,Drama,18,60,7.5"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,revenue_m\n"
                "Inception,Christopher Nolan,160,836\n"
                "The Two Towers,Peter Jackson,94,936\n"
                "Kingdom of Heaven,Ridley Scott,130,211\n"
                "Life of Pi,Ang Lee,120,609\n"
                "127 Hours,Danny Boyle,18,60"
            ),
        },
        {
            "statement": "Rename the box_office_m column to revenue_m in the earnings table.",
            "solution_code": 'earnings.rename(columns={"box_office_m": "revenue_m"})',
            "hint": 'Use df.rename(columns={"old_name": "new_name"}) to rename a column.',
            "category": "rename-column",
            "tables": [
                {
                    "name": "earnings",
                    "csv": (
                        "title,director,box_office_m,year\n"
                        "The Dark Knight,Christopher Nolan,1005,2008\n"
                        "The Return of the King,Peter Jackson,1142,2003\n"
                        "Gladiator,Ridley Scott,460,2000\n"
                        "Crouching Tiger Hidden Dragon,Ang Lee,213,2000\n"
                        "Slumdog Millionaire,Danny Boyle,378,2008"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,revenue_m,year\n"
                "The Dark Knight,Christopher Nolan,1005,2008\n"
                "The Return of the King,Peter Jackson,1142,2003\n"
                "Gladiator,Ridley Scott,460,2000\n"
                "Crouching Tiger Hidden Dragon,Ang Lee,213,2000\n"
                "Slumdog Millionaire,Danny Boyle,378,2008"
            ),
        },
        {
            "statement": "Rename the columns film to title, helmer to director, and yr to year in the productions table.",
            "solution_code": 'productions.rename(columns={"film": "title", "helmer": "director", "yr": "year"})',
            "hint": 'Use df.rename(columns={"old1": "new1", "old2": "new2"}) to rename multiple columns.',
            "category": "rename-columns",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "film,helmer,yr,budget_m\n"
                        "Inception,Christopher Nolan,2010,160\n"
                        "The Fellowship of the Ring,Peter Jackson,2001,93\n"
                        "Black Hawk Down,Ridley Scott,2001,92\n"
                        "Hulk,Ang Lee,2003,137\n"
                        "Trainspotting,Danny Boyle,1996,3"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,budget_m\n"
                "Inception,Christopher Nolan,2010,160\n"
                "The Fellowship of the Ring,Peter Jackson,2001,93\n"
                "Black Hawk Down,Ridley Scott,2001,92\n"
                "Hulk,Ang Lee,2003,137\n"
                "Trainspotting,Danny Boyle,1996,3"
            ),
        },
        {
            "statement": "Rename the score column to imdb_rating in the ratings table.",
            "solution_code": 'ratings.rename(columns={"score": "imdb_rating"})',
            "hint": 'Use df.rename(columns={"old_name": "new_name"}) to rename a column.',
            "category": "rename-column",
            "tables": [
                {
                    "name": "ratings",
                    "csv": (
                        "title,director,score,votes\n"
                        "The Dark Knight,Christopher Nolan,9.0,2500000\n"
                        "The Return of the King,Peter Jackson,9.0,1800000\n"
                        "Gladiator,Ridley Scott,8.5,1400000\n"
                        "Brokeback Mountain,Ang Lee,7.7,300000\n"
                        "28 Days Later,Danny Boyle,7.6,370000"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,imdb_rating,votes\n"
                "The Dark Knight,Christopher Nolan,9.0,2500000\n"
                "The Return of the King,Peter Jackson,9.0,1800000\n"
                "Gladiator,Ridley Scott,8.5,1400000\n"
                "Brokeback Mountain,Ang Lee,7.7,300000\n"
                "28 Days Later,Danny Boyle,7.6,370000"
            ),
        },
        {
            "statement": "Rename the columns name to title, dir to director, and money to revenue_m in the releases table.",
            "solution_code": 'releases.rename(columns={"name": "title", "dir": "director", "money": "revenue_m"})',
            "hint": 'Pass a dictionary with all old-to-new mappings: df.rename(columns={"a": "b", "c": "d"}).',
            "category": "rename-columns",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "name,dir,money,released\n"
                        "Inception,Christopher Nolan,836,2010\n"
                        "The Two Towers,Peter Jackson,936,2002\n"
                        "Kingdom of Heaven,Ridley Scott,211,2005\n"
                        "Life of Pi,Ang Lee,609,2012\n"
                        "Slumdog Millionaire,Danny Boyle,378,2008"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,revenue_m,released\n"
                "Inception,Christopher Nolan,836,2010\n"
                "The Two Towers,Peter Jackson,936,2002\n"
                "Kingdom of Heaven,Ridley Scott,211,2005\n"
                "Life of Pi,Ang Lee,609,2012\n"
                "Slumdog Millionaire,Danny Boyle,378,2008"
            ),
        },
        {
            "statement": "Filter the nolan_films table to movies with revenue_m greater than 300, then drop the studio and budget_m columns.",
            "solution_code": 'nolan_films[nolan_films["revenue_m"] > 300].drop(columns=["studio", "budget_m"])',
            "hint": "First filter with boolean indexing, then chain .drop(columns=[...]).",
            "category": "drop-filter",
            "tables": [
                {
                    "name": "nolan_films",
                    "csv": (
                        "title,year,budget_m,revenue_m,studio\n"
                        "The Dark Knight,2008,185,1005,Warner Bros\n"
                        "Inception,2010,160,836,Warner Bros\n"
                        "Batman Begins,2005,150,373,Warner Bros\n"
                        "The Prestige,2006,40,109,Buena Vista\n"
                        "Insomnia,2002,46,113,Warner Bros"
                    ),
                }
            ],
            "expected_csv": (
                "title,year,revenue_m\n"
                "The Dark Knight,2008,1005\n"
                "Inception,2010,836\n"
                "Batman Begins,2005,373"
            ),
        },
        {
            "statement": "Rename the earnings_m column to revenue_m in the jackson_films table, then sort by revenue_m in ascending order.",
            "solution_code": 'jackson_films.rename(columns={"earnings_m": "revenue_m"}).sort_values("revenue_m")',
            "hint": "Chain .rename(columns={...}) with .sort_values('column') to rename and sort.",
            "category": "rename-sort",
            "tables": [
                {
                    "name": "jackson_films",
                    "csv": (
                        "title,director,earnings_m\n"
                        "The Return of the King,Peter Jackson,1142\n"
                        "The Two Towers,Peter Jackson,936\n"
                        "The Fellowship of the Ring,Peter Jackson,871\n"
                        "King Kong,Peter Jackson,550\n"
                        "The Lovely Bones,Peter Jackson,73"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,revenue_m\n"
                "The Lovely Bones,Peter Jackson,73\n"
                "King Kong,Peter Jackson,550\n"
                "The Fellowship of the Ring,Peter Jackson,871\n"
                "The Two Towers,Peter Jackson,936\n"
                "The Return of the King,Peter Jackson,1142"
            ),
        },
    ],
    4: [
        {
            "statement": "Add a profit_m column that is revenue_m minus budget_m.",
            "solution_code": 'movies.assign(profit_m=movies["revenue_m"] - movies["budget_m"])',
            "hint": "Use df.assign(new_col=df['a'] - df['b']) to create a computed column.",
            "category": "assign-subtract",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,budget_m,revenue_m\n"
                        "Arrival,Denis Villeneuve,47,203\n"
                        "Whiplash,Damien Chazelle,3,49\n"
                        "Get Out,Jordan Peele,5,255\n"
                        "Lady Bird,Greta Gerwig,10,79\n"
                        "Parasite,Bong Joon-ho,11,263"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,revenue_m,profit_m\n"
                "Arrival,Denis Villeneuve,47,203,156\n"
                "Whiplash,Damien Chazelle,3,49,46\n"
                "Get Out,Jordan Peele,5,255,250\n"
                "Lady Bird,Greta Gerwig,10,79,69\n"
                "Parasite,Bong Joon-ho,11,263,252"
            ),
        },
        {
            "statement": "Add a cost_per_min column by dividing budget_m by runtime_min, rounded to 2 decimal places.",
            "solution_code": 'films.assign(cost_per_min=(films["budget_m"] / films["runtime_min"]).round(2))',
            "hint": "Use df.assign(col=(df['a'] / df['b']).round(2)) for rounded division.",
            "category": "assign-divide",
            "tables": [
                {
                    "name": "films",
                    "csv": (
                        "title,director,budget_m,runtime_min\n"
                        "Blade Runner 2049,Denis Villeneuve,150,163\n"
                        "La La Land,Damien Chazelle,30,128\n"
                        "Us,Jordan Peele,20,116\n"
                        "Little Women,Greta Gerwig,40,135\n"
                        "Snowpiercer,Bong Joon-ho,40,126"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,runtime_min,cost_per_min\n"
                "Blade Runner 2049,Denis Villeneuve,150,163,0.92\n"
                "La La Land,Damien Chazelle,30,128,0.23\n"
                "Us,Jordan Peele,20,116,0.17\n"
                "Little Women,Greta Gerwig,40,135,0.3\n"
                "Snowpiercer,Bong Joon-ho,40,126,0.32"
            ),
        },
        {
            "statement": "Add an roi column calculated as revenue_m divided by budget_m, rounded to 1 decimal place.",
            "solution_code": 'box_office.assign(roi=(box_office["revenue_m"] / box_office["budget_m"]).round(1))',
            "hint": "ROI is revenue divided by budget. Use .round(1) to round to 1 decimal.",
            "category": "assign-divide",
            "tables": [
                {
                    "name": "box_office",
                    "csv": (
                        "title,director,budget_m,revenue_m\n"
                        "Sicario,Denis Villeneuve,30,85\n"
                        "First Man,Damien Chazelle,59,105\n"
                        "Get Out,Jordan Peele,5,255\n"
                        "Parasite,Bong Joon-ho,11,263\n"
                        "Lady Bird,Greta Gerwig,10,79"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,revenue_m,roi\n"
                "Sicario,Denis Villeneuve,30,85,2.8\n"
                "First Man,Damien Chazelle,59,105,1.8\n"
                "Get Out,Jordan Peele,5,255,51.0\n"
                "Parasite,Bong Joon-ho,11,263,23.9\n"
                "Lady Bird,Greta Gerwig,10,79,7.9"
            ),
        },
        {
            "statement": "Add a cost_per_nom column by dividing budget_m by oscar_noms, rounded to 1 decimal place.",
            "solution_code": 'awards.assign(cost_per_nom=(awards["budget_m"] / awards["oscar_noms"]).round(1))',
            "hint": "Divide budget by nominations and round to 1 decimal with .round(1).",
            "category": "assign-divide",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "title,director,budget_m,oscar_noms\n"
                        "Arrival,Denis Villeneuve,47,8\n"
                        "La La Land,Damien Chazelle,30,14\n"
                        "Get Out,Jordan Peele,5,4\n"
                        "Little Women,Greta Gerwig,40,6\n"
                        "Parasite,Bong Joon-ho,11,6"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,oscar_noms,cost_per_nom\n"
                "Arrival,Denis Villeneuve,47,8,5.9\n"
                "La La Land,Damien Chazelle,30,14,2.1\n"
                "Get Out,Jordan Peele,5,4,1.2\n"
                "Little Women,Greta Gerwig,40,6,6.7\n"
                "Parasite,Bong Joon-ho,11,6,1.8"
            ),
        },
        {
            "statement": "Add a total_gross_m column that is domestic_m plus international_m.",
            "solution_code": 'earnings.assign(total_gross_m=earnings["domestic_m"] + earnings["international_m"])',
            "hint": "Use df.assign(new_col=df['a'] + df['b']) to add two columns together.",
            "category": "assign-add",
            "tables": [
                {
                    "name": "earnings",
                    "csv": (
                        "title,director,domestic_m,international_m\n"
                        "Dune,Denis Villeneuve,108,292\n"
                        "Whiplash,Damien Chazelle,13,36\n"
                        "Nope,Jordan Peele,123,48\n"
                        "Barbie,Greta Gerwig,636,809\n"
                        "Parasite,Bong Joon-ho,53,210"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,domestic_m,international_m,total_gross_m\n"
                "Dune,Denis Villeneuve,108,292,400\n"
                "Whiplash,Damien Chazelle,13,36,49\n"
                "Nope,Jordan Peele,123,48,171\n"
                "Barbie,Greta Gerwig,636,809,1445\n"
                "Parasite,Bong Joon-ho,53,210,263"
            ),
        },
        {
            "statement": "Filter movies released in 2017 or later with a rating of 8.0 or above.",
            "solution_code": 'releases[(releases["year"] >= 2017) & (releases["rating"] >= 8.0)]',
            "hint": "Combine conditions with & and wrap each in parentheses: df[(cond1) & (cond2)].",
            "category": "filter-and",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "title,director,year,rating\n"
                        "Arrival,Denis Villeneuve,2016,7.9\n"
                        "Get Out,Jordan Peele,2017,7.7\n"
                        "Parasite,Bong Joon-ho,2019,8.5\n"
                        "La La Land,Damien Chazelle,2016,8.0\n"
                        "Little Women,Greta Gerwig,2019,7.8\n"
                        "Blade Runner 2049,Denis Villeneuve,2017,8.0"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Parasite,Bong Joon-ho,2019,8.5\n"
                "Blade Runner 2049,Denis Villeneuve,2017,8.0"
            ),
        },
        {
            "statement": "Find movies with a budget under 20 million that earned over 100 million in revenue.",
            "solution_code": 'productions[(productions["budget_m"] < 20) & (productions["revenue_m"] > 100)]',
            "hint": "Use & to combine two numeric conditions: (budget < 20) & (revenue > 100).",
            "category": "filter-and",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "title,director,budget_m,revenue_m\n"
                        "Whiplash,Damien Chazelle,3,49\n"
                        "Get Out,Jordan Peele,5,255\n"
                        "Lady Bird,Greta Gerwig,10,79\n"
                        "Parasite,Bong Joon-ho,11,263\n"
                        "Us,Jordan Peele,20,175"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,revenue_m\n"
                "Get Out,Jordan Peele,5,255\n"
                "Parasite,Bong Joon-ho,11,263"
            ),
        },
        {
            "statement": "Filter to only Denis Villeneuve films longer than 150 minutes.",
            "solution_code": 'catalog[(catalog["director"] == "Denis Villeneuve") & (catalog["runtime_min"] > 150)]',
            "hint": "Combine a string equality check with a numeric comparison using &.",
            "category": "filter-and",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,director,runtime_min,year\n"
                        "Arrival,Denis Villeneuve,116,2016\n"
                        "Blade Runner 2049,Denis Villeneuve,163,2017\n"
                        "Dune,Denis Villeneuve,155,2021\n"
                        "La La Land,Damien Chazelle,128,2016\n"
                        "Parasite,Bong Joon-ho,132,2019"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,runtime_min,year\n"
                "Blade Runner 2049,Denis Villeneuve,163,2017\n"
                "Dune,Denis Villeneuve,155,2021"
            ),
        },
        {
            "statement": "Get all movies directed by Jordan Peele or Greta Gerwig.",
            "solution_code": 'lineup[(lineup["director"] == "Jordan Peele") | (lineup["director"] == "Greta Gerwig")]',
            "hint": "Use | to combine two equality conditions: (dir == X) | (dir == Y).",
            "category": "filter-or",
            "tables": [
                {
                    "name": "lineup",
                    "csv": (
                        "title,director,year,rating\n"
                        "Arrival,Denis Villeneuve,2016,7.9\n"
                        "Get Out,Jordan Peele,2017,7.7\n"
                        "Lady Bird,Greta Gerwig,2017,7.4\n"
                        "Parasite,Bong Joon-ho,2019,8.5\n"
                        "Us,Jordan Peele,2019,6.8\n"
                        "Barbie,Greta Gerwig,2023,6.9"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Get Out,Jordan Peele,2017,7.7\n"
                "Lady Bird,Greta Gerwig,2017,7.4\n"
                "Us,Jordan Peele,2019,6.8\n"
                "Barbie,Greta Gerwig,2023,6.9"
            ),
        },
        {
            "statement": "Find movies that either received more than 10 Oscar nominations or had a budget under 10 million.",
            "solution_code": 'contenders[(contenders["oscar_noms"] > 10) | (contenders["budget_m"] < 10)]',
            "hint": "Use | (or) to match rows meeting either condition.",
            "category": "filter-or",
            "tables": [
                {
                    "name": "contenders",
                    "csv": (
                        "title,director,budget_m,oscar_noms\n"
                        "Blade Runner 2049,Denis Villeneuve,150,5\n"
                        "La La Land,Damien Chazelle,30,14\n"
                        "Get Out,Jordan Peele,5,4\n"
                        "Whiplash,Damien Chazelle,3,5\n"
                        "Parasite,Bong Joon-ho,11,6"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m,oscar_noms\n"
                "La La Land,Damien Chazelle,30,14\n"
                "Get Out,Jordan Peele,5,4\n"
                "Whiplash,Damien Chazelle,3,5"
            ),
        },
    ],
    5: [
        {
            "statement": "Filter the movies table to only show films directed by Martin Scorsese or Quentin Tarantino.",
            "solution_code": 'movies[movies["director"].isin(["Martin Scorsese", "Quentin Tarantino"])]',
            "hint": "Use df[df['column'].isin(['val1', 'val2'])] to filter rows matching any value in a list.",
            "category": "isin",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "title,director,year,rating\n"
                        "Goodfellas,Martin Scorsese,1990,8.7\n"
                        "The Shining,Stanley Kubrick,1980,8.4\n"
                        "Pulp Fiction,Quentin Tarantino,1994,8.9\n"
                        "Schindlers List,Steven Spielberg,1993,9.0\n"
                        "Inception,Christopher Nolan,2010,8.8\n"
                        "The Departed,Martin Scorsese,2006,8.5"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Goodfellas,Martin Scorsese,1990,8.7\n"
                "Pulp Fiction,Quentin Tarantino,1994,8.9\n"
                "The Departed,Martin Scorsese,2006,8.5"
            ),
        },
        {
            "statement": "Get all films from the films table that belong to the Sci-Fi or Thriller genre.",
            "solution_code": 'films[films["genre"].isin(["Sci-Fi", "Thriller"])]',
            "hint": "Use df[df['column'].isin(['val1', 'val2'])] to match multiple values at once.",
            "category": "isin",
            "tables": [
                {
                    "name": "films",
                    "csv": (
                        "title,genre,runtime_min,oscar_wins\n"
                        "The Godfather,Crime,175,3\n"
                        "Forrest Gump,Drama,142,6\n"
                        "Alien,Sci-Fi,117,1\n"
                        "Blade Runner,Sci-Fi,117,0\n"
                        "The Silence of the Lambs,Thriller,118,5\n"
                        "Se7en,Thriller,127,0"
                    ),
                }
            ],
            "expected_csv": (
                "title,genre,runtime_min,oscar_wins\n"
                "Alien,Sci-Fi,117,1\n"
                "Blade Runner,Sci-Fi,117,0\n"
                "The Silence of the Lambs,Thriller,118,5\n"
                "Se7en,Thriller,127,0"
            ),
        },
        {
            "statement": "From the classics table, get the title and revenue_m columns for films directed by Stanley Kubrick or Steven Spielberg.",
            "solution_code": 'classics[classics["director"].isin(["Stanley Kubrick", "Steven Spielberg"])][["title", "revenue_m"]]',
            "hint": "First filter with .isin(), then select columns with double brackets.",
            "category": "isin-select",
            "tables": [
                {
                    "name": "classics",
                    "csv": (
                        "title,director,year,budget_m,revenue_m\n"
                        "2001 A Space Odyssey,Stanley Kubrick,1968,12,190\n"
                        "Jaws,Steven Spielberg,1975,9,472\n"
                        "Taxi Driver,Martin Scorsese,1976,1,28\n"
                        "A Clockwork Orange,Stanley Kubrick,1971,2,27\n"
                        "Raiders of the Lost Ark,Steven Spielberg,1981,20,389\n"
                        "Raging Bull,Martin Scorsese,1980,18,23"
                    ),
                }
            ],
            "expected_csv": (
                "title,revenue_m\n"
                "2001 A Space Odyssey,190\n"
                "Jaws,472\n"
                "A Clockwork Orange,27\n"
                "Raiders of the Lost Ark,389"
            ),
        },
        {
            "statement": "Filter the catalog table to show only movies released between 1980 and 1999 (inclusive).",
            "solution_code": 'catalog[catalog["year"].between(1980, 1999)]',
            "hint": "Use df[df['column'].between(low, high)] to filter values within a range (inclusive).",
            "category": "between",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,year,runtime_min,rating\n"
                        "The Godfather,1972,175,9.2\n"
                        "Apocalypse Now,1979,147,8.4\n"
                        "Scarface,1983,170,8.3\n"
                        "Goodfellas,1990,146,8.7\n"
                        "Fight Club,1999,139,8.8\n"
                        "The Dark Knight,2008,152,9.0"
                    ),
                }
            ],
            "expected_csv": (
                "title,year,runtime_min,rating\n"
                "Scarface,1983,170,8.3\n"
                "Goodfellas,1990,146,8.7\n"
                "Fight Club,1999,139,8.8"
            ),
        },
        {
            "statement": "Filter blockbusters to movies with a budget between 100 and 200 million, then sort by worldwide_gross_m descending.",
            "solution_code": 'blockbusters[blockbusters["budget_m"].between(100, 200)].sort_values("worldwide_gross_m", ascending=False)',
            "hint": "First use .between() to filter, then chain .sort_values() with ascending=False.",
            "category": "between-sort",
            "tables": [
                {
                    "name": "blockbusters",
                    "csv": (
                        "title,budget_m,worldwide_gross_m,year\n"
                        "Titanic,200,2187,1997\n"
                        "Jurassic Park,63,1029,1993\n"
                        "The Matrix,63,463,1999\n"
                        "Gladiator,103,460,2000\n"
                        "Inception,160,836,2010\n"
                        "Interstellar,165,677,2014"
                    ),
                }
            ],
            "expected_csv": (
                "title,budget_m,worldwide_gross_m,year\n"
                "Titanic,200,2187,1997\n"
                "Inception,160,836,2010\n"
                "Interstellar,165,677,2014\n"
                "Gladiator,103,460,2000"
            ),
        },
        {
            "statement": "Get the top 3 highest-grossing movies from the box_office table by worldwide_gross_m.",
            "solution_code": 'box_office.nlargest(3, "worldwide_gross_m")',
            "hint": "Use df.nlargest(n, 'column') to get the n rows with the largest values.",
            "category": "nlargest",
            "tables": [
                {
                    "name": "box_office",
                    "csv": (
                        "title,year,worldwide_gross_m\n"
                        "Titanic,1997,2187\n"
                        "The Dark Knight,2008,1005\n"
                        "Inception,2010,836\n"
                        "Interstellar,2014,677\n"
                        "Dunkirk,2017,527\n"
                        "Tenet,2020,363"
                    ),
                }
            ],
            "expected_csv": (
                "title,year,worldwide_gross_m\n"
                "Titanic,1997,2187\n"
                "The Dark Knight,2008,1005\n"
                "Inception,2010,836"
            ),
        },
        {
            "statement": "Get the title and oscar_wins columns for the 3 movies with the most Oscar wins from the oscar_movies table.",
            "solution_code": 'oscar_movies.nlargest(3, "oscar_wins")[["title", "oscar_wins"]]',
            "hint": "Use df.nlargest(n, 'column') first, then select columns with double brackets.",
            "category": "nlargest-select",
            "tables": [
                {
                    "name": "oscar_movies",
                    "csv": (
                        "title,director,oscar_noms,oscar_wins\n"
                        "The Return of the King,Peter Jackson,11,11\n"
                        "Titanic,James Cameron,14,11\n"
                        "Ben-Hur,William Wyler,12,11\n"
                        "Schindlers List,Steven Spielberg,12,7\n"
                        "Forrest Gump,Robert Zemeckis,13,6\n"
                        "Amadeus,Milos Forman,11,8"
                    ),
                }
            ],
            "expected_csv": (
                "title,oscar_wins\n"
                "The Return of the King,11\n"
                "Titanic,11\n"
                "Ben-Hur,11"
            ),
        },
        {
            "statement": "Find the 3 movies with the smallest budgets from the indie table.",
            "solution_code": 'indie.nsmallest(3, "budget_m")',
            "hint": "Use df.nsmallest(n, 'column') to get the n rows with the smallest values.",
            "category": "nsmallest",
            "tables": [
                {
                    "name": "indie",
                    "csv": (
                        "title,budget_m,year,rating\n"
                        "Reservoir Dogs,1.2,1992,8.3\n"
                        "Clerks,0.03,1994,7.7\n"
                        "Pi,0.06,1998,7.4\n"
                        "Memento,9.0,2000,8.4\n"
                        "Whiplash,3.3,2014,8.5\n"
                        "Get Out,4.5,2017,7.7"
                    ),
                }
            ],
            "expected_csv": (
                "title,budget_m,year,rating\n"
                "Clerks,0.03,1994,7.7\n"
                "Pi,0.06,1998,7.4\n"
                "Reservoir Dogs,1.2,1992,8.3"
            ),
        },
        {
            "statement": "Get the unique directors from the filmography table as a DataFrame.",
            "solution_code": 'filmography[["director"]].drop_duplicates()',
            "hint": "Select the column with double brackets to keep it as a DataFrame, then use .drop_duplicates().",
            "category": "drop-duplicates",
            "tables": [
                {
                    "name": "filmography",
                    "csv": (
                        "title,director,year\n"
                        "Goodfellas,Martin Scorsese,1990\n"
                        "The Departed,Martin Scorsese,2006\n"
                        "Pulp Fiction,Quentin Tarantino,1994\n"
                        "Kill Bill,Quentin Tarantino,2003\n"
                        "Inception,Christopher Nolan,2010\n"
                        "The Dark Knight,Christopher Nolan,2008"
                    ),
                }
            ],
            "expected_csv": (
                "director\n"
                "Martin Scorsese\n"
                "Quentin Tarantino\n"
                "Christopher Nolan"
            ),
        },
        {
            "statement": "From the awards table, get one row per year (drop duplicate years) and select only the year and film columns.",
            "solution_code": 'awards.drop_duplicates(subset=["year"])[["year", "film"]]',
            "hint": "Use df.drop_duplicates(subset=['col']) to keep only the first occurrence, then select columns.",
            "category": "drop-duplicates-select",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "year,category,winner,film\n"
                        "2020,Best Picture,Nomadland,Nomadland\n"
                        "2020,Best Director,Chloe Zhao,Nomadland\n"
                        "2019,Best Picture,Parasite,Parasite\n"
                        "2019,Best Director,Bong Joon-ho,Parasite\n"
                        "2018,Best Picture,Green Book,Green Book\n"
                        "2018,Best Director,Alfonso Cuaron,Roma"
                    ),
                }
            ],
            "expected_csv": (
                "year,film\n"
                "2020,Nomadland\n"
                "2019,Parasite\n"
                "2018,Green Book"
            ),
        },
    ],

    6: [
        {
            "statement": "Find the total box office revenue per director from the films table.",
            "solution_code": 'films.groupby("director")["revenue_m"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "films",
                    "csv": (
                        "title,director,revenue_m\n"
                        "Goodfellas,Martin Scorsese,47\n"
                        "The Departed,Martin Scorsese,132\n"
                        "Pulp Fiction,Quentin Tarantino,214\n"
                        "Inglourious Basterds,Quentin Tarantino,321\n"
                        "No Country for Old Men,Coen Brothers,171\n"
                        "Fargo,Coen Brothers,60"
                    ),
                }
            ],
            "expected_csv": (
                "director,revenue_m\n"
                "Coen Brothers,231\n"
                "Martin Scorsese,179\n"
                "Quentin Tarantino,535"
            ),
        },
        {
            "statement": "Count how many films each lead actor has in the roles table.",
            "solution_code": 'roles.groupby("actor")["title"].count().reset_index()',
            "hint": "Use groupby('col')['any_col'].count() then reset_index() to count rows per group.",
            "category": "groupby-count",
            "tables": [
                {
                    "name": "roles",
                    "csv": (
                        "title,actor,year\n"
                        "Forrest Gump,Tom Hanks,1994\n"
                        "Cast Away,Tom Hanks,2000\n"
                        "The Green Mile,Tom Hanks,1999\n"
                        "Se7en,Brad Pitt,1995\n"
                        "Fight Club,Brad Pitt,1999\n"
                        "Goodfellas,Robert De Niro,1990"
                    ),
                }
            ],
            "expected_csv": (
                "actor,title\n"
                "Brad Pitt,2\n"
                "Robert De Niro,1\n"
                "Tom Hanks,3"
            ),
        },
        {
            "statement": "Calculate the total budget spent per director in the productions table.",
            "solution_code": 'productions.groupby("director")["budget_m"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "title,director,budget_m,year\n"
                        "Avatar,James Cameron,237,2009\n"
                        "Titanic,James Cameron,200,1997\n"
                        "Aliens,James Cameron,18,1986\n"
                        "Gravity,Alfonso Cuaron,100,2013\n"
                        "Roma,Alfonso Cuaron,15,2018"
                    ),
                }
            ],
            "expected_csv": (
                "director,budget_m\n"
                "Alfonso Cuaron,115\n"
                "James Cameron,455"
            ),
        },
        {
            "statement": "Count the number of films per actor in the cast table.",
            "solution_code": 'cast.groupby("actor")["title"].count().reset_index()',
            "hint": "Use groupby('col')['any_col'].count() to count rows in each group.",
            "category": "groupby-count",
            "tables": [
                {
                    "name": "cast",
                    "csv": (
                        "title,actor,genre\n"
                        "The Shawshank Redemption,Morgan Freeman,Drama\n"
                        "Se7en,Morgan Freeman,Thriller\n"
                        "Million Dollar Baby,Morgan Freeman,Drama\n"
                        "Good Will Hunting,Matt Damon,Drama\n"
                        "The Martian,Matt Damon,Sci-Fi\n"
                        "The Bourne Identity,Matt Damon,Action"
                    ),
                }
            ],
            "expected_csv": (
                "actor,title\n"
                "Matt Damon,3\n"
                "Morgan Freeman,3"
            ),
        },
        {
            "statement": "Find the total budget per genre in the releases table.",
            "solution_code": 'releases.groupby("genre")["budget_m"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "title,director,genre,budget_m\n"
                        "Get Out,Jordan Peele,Horror,5\n"
                        "Us,Jordan Peele,Horror,20\n"
                        "Whiplash,Damien Chazelle,Drama,3\n"
                        "La La Land,Damien Chazelle,Drama,30\n"
                        "First Man,Damien Chazelle,Drama,59\n"
                        "Midsommar,Ari Aster,Horror,9"
                    ),
                }
            ],
            "expected_csv": (
                "genre,budget_m\n"
                "Drama,92\n"
                "Horror,34"
            ),
        },
        {
            "statement": "Sum the total Oscar wins per director in the awards table.",
            "solution_code": 'awards.groupby("director")["oscar_wins"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "title,director,studio,oscar_wins\n"
                        "The Godfather,Francis Ford Coppola,Paramount,3\n"
                        "Apocalypse Now,Francis Ford Coppola,United Artists,2\n"
                        "The Conversation,Francis Ford Coppola,Paramount,0\n"
                        "Taxi Driver,Martin Scorsese,Columbia,0\n"
                        "Raging Bull,Martin Scorsese,United Artists,2\n"
                        "Goodfellas,Martin Scorsese,Warner Bros,1"
                    ),
                }
            ],
            "expected_csv": (
                "director,oscar_wins\n"
                "Francis Ford Coppola,5\n"
                "Martin Scorsese,3"
            ),
        },
        {
            "statement": "Count how many Oscar nominations each actor received in the nominees table.",
            "solution_code": 'nominees.groupby("actor")["film"].count().reset_index()',
            "hint": "Use groupby('col')['any_col'].count() to count rows in each group.",
            "category": "groupby-count",
            "tables": [
                {
                    "name": "nominees",
                    "csv": (
                        "actor,film,year\n"
                        "Meryl Streep,The Iron Lady,2011\n"
                        "Meryl Streep,August Osage County,2013\n"
                        "Meryl Streep,Florence Foster Jenkins,2016\n"
                        "Cate Blanchett,Blue Jasmine,2013\n"
                        "Cate Blanchett,Carol,2015"
                    ),
                }
            ],
            "expected_csv": (
                "actor,film\n"
                "Cate Blanchett,2\n"
                "Meryl Streep,3"
            ),
        },
        {
            "statement": "Find the total worldwide revenue per genre in the blockbusters table.",
            "solution_code": 'blockbusters.groupby("genre")["revenue_m"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "blockbusters",
                    "csv": (
                        "title,actor,genre,revenue_m\n"
                        "Iron Man,Robert Downey Jr,Action,585\n"
                        "The Avengers,Robert Downey Jr,Action,1519\n"
                        "Guardians of the Galaxy,Chris Pratt,Action,774\n"
                        "Harry Potter 1,Daniel Radcliffe,Fantasy,977\n"
                        "Harry Potter 2,Daniel Radcliffe,Fantasy,879"
                    ),
                }
            ],
            "expected_csv": (
                "genre,revenue_m\n"
                "Action,2878\n"
                "Fantasy,1856"
            ),
        },
        {
            "statement": "Filter the box_office table to films with revenue over 200 million, then count how many qualifying films each actor has.",
            "solution_code": 'box_office[box_office["revenue_m"] > 200].groupby("actor")["title"].count().reset_index()',
            "hint": "First filter with boolean indexing, then chain .groupby()['col'].count().reset_index().",
            "category": "groupby-count",
            "tables": [
                {
                    "name": "box_office",
                    "csv": (
                        "title,actor,year,revenue_m\n"
                        "Titanic,Leonardo DiCaprio,1997,2187\n"
                        "The Revenant,Leonardo DiCaprio,2015,533\n"
                        "Catch Me If You Can,Leonardo DiCaprio,2002,352\n"
                        "The Aviator,Leonardo DiCaprio,2004,213\n"
                        "Mission Impossible,Tom Cruise,1996,457\n"
                        "Top Gun Maverick,Tom Cruise,2022,1488\n"
                        "Jerry Maguire,Tom Cruise,1996,274"
                    ),
                }
            ],
            "expected_csv": (
                "actor,title\n"
                "Leonardo DiCaprio,4\n"
                "Tom Cruise,3"
            ),
        },
        {
            "statement": "Calculate the total budget per director in the catalog table.",
            "solution_code": 'catalog.groupby("director")["budget_m"].sum().reset_index()',
            "hint": "Use groupby('col')['value_col'].sum() then reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,director,genre,budget_m\n"
                        "The Silence of the Lambs,Jonathan Demme,Thriller,19\n"
                        "Philadelphia,Jonathan Demme,Drama,26\n"
                        "The Manchurian Candidate,Jonathan Demme,Thriller,80\n"
                        "Se7en,David Fincher,Thriller,33\n"
                        "Fight Club,David Fincher,Drama,63\n"
                        "Gone Girl,David Fincher,Thriller,61"
                    ),
                }
            ],
            "expected_csv": (
                "director,budget_m\n"
                "David Fincher,157\n"
                "Jonathan Demme,125"
            ),
        },
    ],
    7: [
        {
            "statement": "Find the average IMDb rating per genre from the screenings table.",
            "solution_code": 'screenings.groupby("genre")["rating"].mean().reset_index()',
            "hint": "Use groupby('col')['value_col'].mean() then reset_index().",
            "category": "groupby-mean",
            "tables": [
                {
                    "name": "screenings",
                    "csv": (
                        "title,director,genre,rating\n"
                        "The Dark Knight,Christopher Nolan,Action,9.0\n"
                        "Inception,Christopher Nolan,Action,8.8\n"
                        "The Prestige,Christopher Nolan,Drama,8.2\n"
                        "Dunkirk,Christopher Nolan,Drama,8.0\n"
                        "Memento,Christopher Nolan,Thriller,8.4\n"
                        "Insomnia,Christopher Nolan,Thriller,8.6"
                    ),
                }
            ],
            "expected_csv": (
                "genre,rating\n"
                "Action,8.9\n"
                "Drama,8.1\n"
                "Thriller,8.5"
            ),
        },
        {
            "statement": "Find the highest box office revenue per actor from the earnings table.",
            "solution_code": 'earnings.groupby("actor")["revenue_m"].max().reset_index()',
            "hint": "Use groupby('col')['value_col'].max() then reset_index().",
            "category": "groupby-max",
            "tables": [
                {
                    "name": "earnings",
                    "csv": (
                        "title,actor,revenue_m\n"
                        "Forrest Gump,Tom Hanks,678\n"
                        "Cast Away,Tom Hanks,429\n"
                        "The Dark Knight,Christian Bale,1004\n"
                        "American Psycho,Christian Bale,34\n"
                        "Interstellar,Matthew McConaughey,677\n"
                        "Dallas Buyers Club,Matthew McConaughey,55"
                    ),
                }
            ],
            "expected_csv": (
                "actor,revenue_m\n"
                "Christian Bale,1004\n"
                "Matthew McConaughey,677\n"
                "Tom Hanks,678"
            ),
        },
        {
            "statement": "Find the lowest budget per director from the productions table.",
            "solution_code": 'productions.groupby("director")["budget_m"].min().reset_index()',
            "hint": "Use groupby('col')['value_col'].min() then reset_index().",
            "category": "groupby-min",
            "tables": [
                {
                    "name": "productions",
                    "csv": (
                        "title,director,budget_m\n"
                        "The Departed,Martin Scorsese,90\n"
                        "Goodfellas,Martin Scorsese,25\n"
                        "The Royal Tenenbaums,Wes Anderson,21\n"
                        "Moonrise Kingdom,Wes Anderson,16\n"
                        "Lost in Translation,Sofia Coppola,4\n"
                        "Marie Antoinette,Sofia Coppola,40"
                    ),
                }
            ],
            "expected_csv": (
                "director,budget_m\n"
                "Martin Scorsese,25\n"
                "Sofia Coppola,4\n"
                "Wes Anderson,16"
            ),
        },
        {
            "statement": "Count how many films each genre has in the catalog table using value_counts.",
            "solution_code": 'catalog["genre"].value_counts().reset_index()',
            "hint": "Use df['column'].value_counts() to count occurrences, then reset_index().",
            "category": "value-counts",
            "tables": [
                {
                    "name": "catalog",
                    "csv": (
                        "title,actor,genre\n"
                        "The Godfather,Al Pacino,Crime\n"
                        "Scarface,Al Pacino,Crime\n"
                        "Heat,Al Pacino,Crime\n"
                        "Collateral,Tom Cruise,Action\n"
                        "Mission Impossible,Tom Cruise,Action\n"
                        "Cast Away,Tom Hanks,Drama"
                    ),
                }
            ],
            "expected_csv": (
                "genre,count\n"
                "Crime,3\n"
                "Action,2\n"
                "Drama,1"
            ),
        },
        {
            "statement": "Find the average salary per actor from the contracts table.",
            "solution_code": 'contracts.groupby("actor")["salary_m"].mean().reset_index()',
            "hint": "Use groupby('col')['value_col'].mean() then reset_index().",
            "category": "groupby-mean",
            "tables": [
                {
                    "name": "contracts",
                    "csv": (
                        "title,actor,salary_m\n"
                        "Ocean's Eleven,George Clooney,20\n"
                        "Gravity,George Clooney,14\n"
                        "Mr. & Mrs. Smith,Angelina Jolie,20\n"
                        "Maleficent,Angelina Jolie,30\n"
                        "The Departed,Jack Nicholson,15\n"
                        "As Good as It Gets,Jack Nicholson,25"
                    ),
                }
            ],
            "expected_csv": (
                "actor,salary_m\n"
                "Angelina Jolie,25.0\n"
                "George Clooney,17.0\n"
                "Jack Nicholson,20.0"
            ),
        },
        {
            "statement": "Count how many films were released each decade in the releases table.",
            "solution_code": 'releases["decade"].value_counts().reset_index()',
            "hint": "Use df['column'].value_counts() to count occurrences per category, then reset_index().",
            "category": "value-counts",
            "tables": [
                {
                    "name": "releases",
                    "csv": (
                        "title,actor,decade\n"
                        "Pulp Fiction,John Travolta,1990s\n"
                        "Fargo,Frances McDormand,1990s\n"
                        "Goodfellas,Ray Liotta,1990s\n"
                        "Gladiator,Russell Crowe,2000s\n"
                        "The Departed,Leonardo DiCaprio,2000s\n"
                        "Parasite,Song Kang-ho,2010s"
                    ),
                }
            ],
            "expected_csv": (
                "decade,count\n"
                "1990s,3\n"
                "2000s,2\n"
                "2010s,1"
            ),
        },
        {
            "statement": "Filter the films table to Sci-Fi movies only, then find the average rating per director.",
            "solution_code": 'films[films["genre"] == "Sci-Fi"].groupby("director")["rating"].mean().reset_index()',
            "hint": "First filter with boolean indexing, then chain .groupby()['col'].mean().reset_index().",
            "category": "groupby-mean",
            "tables": [
                {
                    "name": "films",
                    "csv": (
                        "title,director,genre,rating\n"
                        "Interstellar,Christopher Nolan,Sci-Fi,8.6\n"
                        "Inception,Christopher Nolan,Sci-Fi,8.8\n"
                        "Prometheus,Ridley Scott,Sci-Fi,7.0\n"
                        "The Martian,Ridley Scott,Sci-Fi,8.0\n"
                        "The Dark Knight,Christopher Nolan,Action,9.0\n"
                        "Gladiator,Ridley Scott,Action,8.5"
                    ),
                }
            ],
            "expected_csv": (
                "director,rating\n"
                "Christopher Nolan,8.7\n"
                "Ridley Scott,7.5"
            ),
        },
        {
            "statement": "Find the longest runtime per studio from the showtimes table.",
            "solution_code": 'showtimes.groupby("studio")["runtime_min"].max().reset_index()',
            "hint": "Use groupby('col')['value_col'].max() then reset_index().",
            "category": "groupby-max",
            "tables": [
                {
                    "name": "showtimes",
                    "csv": (
                        "title,studio,runtime_min\n"
                        "The Dark Knight,Warner Bros,152\n"
                        "Interstellar,Warner Bros,169\n"
                        "Dunkirk,Warner Bros,106\n"
                        "Jaws,Universal,124\n"
                        "Schindlers List,Universal,195\n"
                        "E.T.,Universal,115"
                    ),
                }
            ],
            "expected_csv": (
                "studio,runtime_min\n"
                "Universal,195\n"
                "Warner Bros,169"
            ),
        },
        {
            "statement": "Count how many times each actor appears in the filmography table.",
            "solution_code": 'filmography["actor"].value_counts().reset_index()',
            "hint": "Use df['column'].value_counts().reset_index() to count entries per value.",
            "category": "value-counts",
            "tables": [
                {
                    "name": "filmography",
                    "csv": (
                        "title,actor,year\n"
                        "The Godfather,Al Pacino,1972\n"
                        "Scarface,Al Pacino,1983\n"
                        "Scent of a Woman,Al Pacino,1992\n"
                        "Fight Club,Edward Norton,1999\n"
                        "American History X,Edward Norton,1998\n"
                        "Birdman,Edward Norton,2014"
                    ),
                }
            ],
            "expected_csv": (
                "actor,count\n"
                "Al Pacino,3\n"
                "Edward Norton,3"
            ),
        },
        {
            "statement": "Find the average Oscar wins per genre from the awards table.",
            "solution_code": 'awards.groupby("genre")["oscar_wins"].mean().reset_index()',
            "hint": "Use groupby('col')['value_col'].mean() then reset_index().",
            "category": "groupby-mean",
            "tables": [
                {
                    "name": "awards",
                    "csv": (
                        "title,director,genre,oscar_wins\n"
                        "The Dark Knight,Christopher Nolan,Action,2\n"
                        "Mad Max Fury Road,George Miller,Action,6\n"
                        "The Godfather,Francis Ford Coppola,Crime,3\n"
                        "No Country for Old Men,Coen Brothers,Crime,4\n"
                        "Schindlers List,Steven Spielberg,Drama,7\n"
                        "Forrest Gump,Robert Zemeckis,Drama,6\n"
                        "Saving Private Ryan,Steven Spielberg,Drama,5"
                    ),
                }
            ],
            "expected_csv": (
                "genre,oscar_wins\n"
                "Action,4.0\n"
                "Crime,3.5\n"
                "Drama,6.0"
            ),
        },
    ],
    8: [
        {
            "statement": "Fill missing ratings in the pta_films table with 7.5.",
            "solution_code": 'pta_films.fillna({"rating": 7.5})',
            "hint": "Use df.fillna({'column': value}) to fill NaN in a specific column.",
            "category": "fillna",
            "tables": [
                {
                    "name": "pta_films",
                    "csv": (
                        "title,director,year,rating\n"
                        "Punch-Drunk Love,Paul Thomas Anderson,2002,\n"
                        "Magnolia,Paul Thomas Anderson,1999,8.0\n"
                        "There Will Be Blood,Paul Thomas Anderson,2007,8.2\n"
                        "The Master,Paul Thomas Anderson,2012,\n"
                        "Inherent Vice,Paul Thomas Anderson,2014,7.0"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Punch-Drunk Love,Paul Thomas Anderson,2002,7.5\n"
                "Magnolia,Paul Thomas Anderson,1999,8.0\n"
                "There Will Be Blood,Paul Thomas Anderson,2007,8.2\n"
                "The Master,Paul Thomas Anderson,2012,7.5\n"
                "Inherent Vice,Paul Thomas Anderson,2014,7.0"
            ),
        },
        {
            "statement": "Fill missing studio values in the coen_films table with 'Unknown'.",
            "solution_code": "coen_films.fillna({\"studio\": \"Unknown\"})",
            "hint": "Use df.fillna({'column': 'string'}) to fill NaN strings in a specific column.",
            "category": "fillna",
            "tables": [
                {
                    "name": "coen_films",
                    "csv": (
                        "title,director,year,studio\n"
                        "Fargo,Coen Brothers,1996,PolyGram\n"
                        "No Country for Old Men,Coen Brothers,2007,\n"
                        "True Grit,Coen Brothers,2010,Paramount\n"
                        "Inside Llewyn Davis,Coen Brothers,2013,\n"
                        "The Big Lebowski,Coen Brothers,1998,Universal"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,studio\n"
                "Fargo,Coen Brothers,1996,PolyGram\n"
                "No Country for Old Men,Coen Brothers,2007,Unknown\n"
                "True Grit,Coen Brothers,2010,Paramount\n"
                "Inside Llewyn Davis,Coen Brothers,2013,Unknown\n"
                "The Big Lebowski,Coen Brothers,1998,Universal"
            ),
        },
        {
            "statement": "Fill missing oscar_wins values in the fincher_films table with 0.",
            "solution_code": 'fincher_films.fillna({"oscar_wins": 0})',
            "hint": "Use df.fillna({'column': 0}) to replace NaN with zero. The column stays as float.",
            "category": "fillna",
            "tables": [
                {
                    "name": "fincher_films",
                    "csv": (
                        "title,director,oscar_noms,oscar_wins\n"
                        "Se7en,David Fincher,0,\n"
                        "The Social Network,David Fincher,8,3\n"
                        "Fight Club,David Fincher,0,\n"
                        "Gone Girl,David Fincher,1,\n"
                        "The Girl with the Dragon Tattoo,David Fincher,5,1"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,oscar_noms,oscar_wins\n"
                "Se7en,David Fincher,0,0.0\n"
                "The Social Network,David Fincher,8,3.0\n"
                "Fight Club,David Fincher,0,0.0\n"
                "Gone Girl,David Fincher,1,0.0\n"
                "The Girl with the Dragon Tattoo,David Fincher,5,1.0"
            ),
        },
        {
            "statement": "Fill missing budget_m values in the wes_films table with the mean budget.",
            "solution_code": 'wes_films.fillna({"budget_m": wes_films["budget_m"].mean()})',
            "hint": "Compute the column mean with df['col'].mean() and pass it as the fill value.",
            "category": "fillna",
            "tables": [
                {
                    "name": "wes_films",
                    "csv": (
                        "title,director,budget_m\n"
                        "Rushmore,Wes Anderson,10.0\n"
                        "The Grand Budapest Hotel,Wes Anderson,\n"
                        "The Royal Tenenbaums,Wes Anderson,30.0\n"
                        "Fantastic Mr. Fox,Wes Anderson,\n"
                        "Moonrise Kingdom,Wes Anderson,20.0"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,budget_m\n"
                "Rushmore,Wes Anderson,10.0\n"
                "The Grand Budapest Hotel,Wes Anderson,20.0\n"
                "The Royal Tenenbaums,Wes Anderson,30.0\n"
                "Fantastic Mr. Fox,Wes Anderson,20.0\n"
                "Moonrise Kingdom,Wes Anderson,20.0"
            ),
        },
        {
            "statement": "In the scott_films table, replace the genre 'Sci-Fi' with 'Science Fiction'.",
            "solution_code": 'scott_films.replace({"genre": {"Sci-Fi": "Science Fiction"}})',
            "hint": "Use df.replace({'column': {'old_value': 'new_value'}}) to remap values.",
            "category": "replace",
            "tables": [
                {
                    "name": "scott_films",
                    "csv": (
                        "title,director,genre\n"
                        "Alien,Ridley Scott,Sci-Fi\n"
                        "Blade Runner,Ridley Scott,Sci-Fi\n"
                        "Gladiator,Ridley Scott,Action\n"
                        "Hannibal,Ridley Scott,Thriller\n"
                        "The Martian,Ridley Scott,Sci-Fi"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,genre\n"
                "Alien,Ridley Scott,Science Fiction\n"
                "Blade Runner,Ridley Scott,Science Fiction\n"
                "Gladiator,Ridley Scott,Action\n"
                "Hannibal,Ridley Scott,Thriller\n"
                "The Martian,Ridley Scott,Science Fiction"
            ),
        },
        {
            "statement": "In the scorsese_films table, replace 'R' with 'Restricted', 'PG' with 'Parental Guidance', and 'PG-13' with 'PG-13 Rated' in the mpaa column.",
            "solution_code": 'scorsese_films.replace({"mpaa": {"R": "Restricted", "PG": "Parental Guidance", "PG-13": "PG-13 Rated"}})',
            "hint": "Pass a nested dict to df.replace({'col': {'old1': 'new1', 'old2': 'new2'}}) to remap multiple values.",
            "category": "replace",
            "tables": [
                {
                    "name": "scorsese_films",
                    "csv": (
                        "title,director,mpaa\n"
                        "Goodfellas,Martin Scorsese,R\n"
                        "Casino,Martin Scorsese,R\n"
                        "Hugo,Martin Scorsese,PG\n"
                        "The Wolf of Wall Street,Martin Scorsese,R\n"
                        "The Aviator,Martin Scorsese,PG-13"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,mpaa\n"
                "Goodfellas,Martin Scorsese,Restricted\n"
                "Casino,Martin Scorsese,Restricted\n"
                "Hugo,Martin Scorsese,Parental Guidance\n"
                "The Wolf of Wall Street,Martin Scorsese,Restricted\n"
                "The Aviator,Martin Scorsese,PG-13 Rated"
            ),
        },
        {
            "statement": "In the nominations table, replace 'Won' with 'Winner' and 'Nominated' with 'Nomination' in the outcome column.",
            "solution_code": 'nominations.replace({"outcome": {"Won": "Winner", "Nominated": "Nomination"}})',
            "hint": "Use df.replace({'col': {'old': 'new'}}) with multiple pairs to remap several values.",
            "category": "replace",
            "tables": [
                {
                    "name": "nominations",
                    "csv": (
                        "actor,film,year,outcome\n"
                        "Natalie Portman,Black Swan,2010,Won\n"
                        "Cate Blanchett,Blue Jasmine,2013,Won\n"
                        "Saoirse Ronan,Lady Bird,2017,Nominated\n"
                        "Meryl Streep,The Iron Lady,2011,Won\n"
                        "Jennifer Lawrence,Silver Linings Playbook,2012,Won"
                    ),
                }
            ],
            "expected_csv": (
                "actor,film,year,outcome\n"
                "Natalie Portman,Black Swan,2010,Winner\n"
                "Cate Blanchett,Blue Jasmine,2013,Winner\n"
                "Saoirse Ronan,Lady Bird,2017,Nomination\n"
                "Meryl Streep,The Iron Lady,2011,Winner\n"
                "Jennifer Lawrence,Silver Linings Playbook,2012,Winner"
            ),
        },
        {
            "statement": "Cast the revenue_m column in the cameron_films table from float to int.",
            "solution_code": 'cameron_films.astype({"revenue_m": int})',
            "hint": "Use df.astype({'column': int}) to convert a float column to integer.",
            "category": "astype",
            "tables": [
                {
                    "name": "cameron_films",
                    "csv": (
                        "title,director,year,revenue_m\n"
                        "Avatar,James Cameron,2009,2788.0\n"
                        "Titanic,James Cameron,1997,2187.0\n"
                        "The Terminator,James Cameron,1984,78.0\n"
                        "Aliens,James Cameron,1986,183.0\n"
                        "True Lies,James Cameron,1994,378.0"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,revenue_m\n"
                "Avatar,James Cameron,2009,2788\n"
                "Titanic,James Cameron,1997,2187\n"
                "The Terminator,James Cameron,1984,78\n"
                "Aliens,James Cameron,1986,183\n"
                "True Lies,James Cameron,1994,378"
            ),
        },
        {
            "statement": "Cast the year column in the eighties_films table from float to int.",
            "solution_code": 'eighties_films.astype({"year": int})',
            "hint": "Use df.astype({'column': int}) to convert float year values to integers.",
            "category": "astype",
            "tables": [
                {
                    "name": "eighties_films",
                    "csv": (
                        "title,director,year,rating\n"
                        "E.T. the Extra-Terrestrial,Steven Spielberg,1982.0,7.9\n"
                        "Scarface,Brian De Palma,1983.0,8.3\n"
                        "Amadeus,Milos Forman,1984.0,8.0\n"
                        "Platoon,Oliver Stone,1986.0,8.1\n"
                        "Rain Man,Barry Levinson,1988.0,7.9"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "E.T. the Extra-Terrestrial,Steven Spielberg,1982,7.9\n"
                "Scarface,Brian De Palma,1983,8.3\n"
                "Amadeus,Milos Forman,1984,8.0\n"
                "Platoon,Oliver Stone,1986,8.1\n"
                "Rain Man,Barry Levinson,1988,7.9"
            ),
        },
        {
            "statement": "In the spielberg_films table, fill missing ratings with 7.5, then cast the year column from float to int.",
            "solution_code": 'spielberg_films.fillna({"rating": 7.5}).astype({"year": int})',
            "hint": "Chain .fillna({'col': value}) with .astype({'col': int}) to fill then convert types.",
            "category": "fillna",
            "tables": [
                {
                    "name": "spielberg_films",
                    "csv": (
                        "title,director,year,rating\n"
                        "Schindlers List,Steven Spielberg,1993.0,9.0\n"
                        "Jurassic Park,Steven Spielberg,1993.0,\n"
                        "E.T. the Extra-Terrestrial,Steven Spielberg,1982.0,7.9\n"
                        "Jaws,Steven Spielberg,1975.0,\n"
                        "Saving Private Ryan,Steven Spielberg,1998.0,8.6"
                    ),
                }
            ],
            "expected_csv": (
                "title,director,year,rating\n"
                "Schindlers List,Steven Spielberg,1993,9.0\n"
                "Jurassic Park,Steven Spielberg,1993,7.5\n"
                "E.T. the Extra-Terrestrial,Steven Spielberg,1982,7.9\n"
                "Jaws,Steven Spielberg,1975,7.5\n"
                "Saving Private Ryan,Steven Spielberg,1998,8.6"
            ),
        },
    ],
    9: [
        {
            "statement": "Join the actors table with the movies table on movie_id using an inner join.",
            "solution_code": "pd.merge(actors, movies, on='movie_id', how='inner')",
            "hint": "Use pd.merge(left, right, on='key', how='inner') to keep only rows that match in both tables.",
            "category": "merge-inner",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,movie_id\n"
                        "1,Tom Hanks,101\n"
                        "2,Meryl Streep,102\n"
                        "3,Leonardo DiCaprio,103\n"
                        "4,Scarlett Johansson,104"
                    ),
                },
                {
                    "name": "movies",
                    "csv": (
                        "movie_id,title,year\n"
                        "101,Forrest Gump,1994\n"
                        "102,Kramer vs. Kramer,1979\n"
                        "103,Titanic,1997\n"
                        "105,Oppenheimer,2023"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,movie_id,title,year\n"
                "1,Tom Hanks,101,Forrest Gump,1994\n"
                "2,Meryl Streep,102,Kramer vs. Kramer,1979\n"
                "3,Leonardo DiCaprio,103,Titanic,1997"
            ),
        },
        {
            "statement": "Left join the movies table with the awards table on movie_id. Keep all movies even if they have no award entry.",
            "solution_code": "pd.merge(movies, awards, on='movie_id', how='left')",
            "hint": "Use how='left' to keep every row from the left table, filling unmatched columns with NaN.",
            "category": "merge-left",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "movie_id,title,release_year\n"
                        "101,Forrest Gump,1994\n"
                        "102,The Silence of the Lambs,1991\n"
                        "103,Titanic,1997\n"
                        "104,Inception,2010\n"
                        "105,Dunkirk,2017"
                    ),
                },
                {
                    "name": "awards",
                    "csv": (
                        "movie_id,award,year_won\n"
                        "101,Best Picture,1995\n"
                        "102,Best Picture,1992\n"
                        "103,Best Picture,1998"
                    ),
                },
            ],
            "expected_csv": (
                "movie_id,title,release_year,award,year_won\n"
                "101,Forrest Gump,1994,Best Picture,1995.0\n"
                "102,The Silence of the Lambs,1991,Best Picture,1992.0\n"
                "103,Titanic,1997,Best Picture,1998.0\n"
                "104,Inception,2010,,\n"
                "105,Dunkirk,2017,,"
            ),
        },
        {
            "statement": "Inner join the actors table with the studios table on studio_id to find which studio each actor is contracted with.",
            "solution_code": "pd.merge(actors, studios, on='studio_id', how='inner')",
            "hint": "An inner join returns only rows where the key exists in both tables.",
            "category": "merge-inner",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,studio_id\n"
                        "1,Brad Pitt,10\n"
                        "2,Angelina Jolie,20\n"
                        "3,Jennifer Aniston,10\n"
                        "4,Cate Blanchett,30\n"
                        "5,Chris Evans,40"
                    ),
                },
                {
                    "name": "studios",
                    "csv": (
                        "studio_id,studio_name\n"
                        "10,Warner Bros\n"
                        "20,Universal Pictures\n"
                        "30,Sony Pictures"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,studio_id,studio_name\n"
                "1,Brad Pitt,10,Warner Bros\n"
                "2,Angelina Jolie,20,Universal Pictures\n"
                "3,Jennifer Aniston,10,Warner Bros\n"
                "4,Cate Blanchett,30,Sony Pictures"
            ),
        },
        {
            "statement": "Left join the actors table with the box_office table on movie_id. Keep all actors even if their film has no box office record.",
            "solution_code": "pd.merge(actors, box_office, on='movie_id', how='left')",
            "hint": "A left join keeps all rows from the left DataFrame and fills missing right-side values with NaN.",
            "category": "merge-left",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,movie_id\n"
                        "1,Dwayne Johnson,201\n"
                        "2,Ryan Reynolds,202\n"
                        "3,Vin Diesel,203\n"
                        "4,Chris Pratt,204"
                    ),
                },
                {
                    "name": "box_office",
                    "csv": (
                        "movie_id,gross_millions\n"
                        "201,800\n"
                        "202,320\n"
                        "203,1200"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,movie_id,gross_millions\n"
                "1,Dwayne Johnson,201,800.0\n"
                "2,Ryan Reynolds,202,320.0\n"
                "3,Vin Diesel,203,1200.0\n"
                "4,Chris Pratt,204,"
            ),
        },
        {
            "statement": "Inner join the movies table with the directors table on director_id to attach each film's director name.",
            "solution_code": "pd.merge(movies, directors, on='director_id', how='inner')",
            "hint": "Use pd.merge with how='inner' and on='director_id' to match films to their directors.",
            "category": "merge-inner",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "movie_id,title,director_id\n"
                        "301,Schindler's List,1\n"
                        "302,The Dark Knight,2\n"
                        "303,Pulp Fiction,3\n"
                        "304,1917,4\n"
                        "305,Avatar,5"
                    ),
                },
                {
                    "name": "directors",
                    "csv": (
                        "director_id,director_name\n"
                        "1,Steven Spielberg\n"
                        "2,Christopher Nolan\n"
                        "3,Quentin Tarantino\n"
                        "5,James Cameron"
                    ),
                },
            ],
            "expected_csv": (
                "movie_id,title,director_id,director_name\n"
                "301,Schindler's List,1,Steven Spielberg\n"
                "302,The Dark Knight,2,Christopher Nolan\n"
                "303,Pulp Fiction,3,Quentin Tarantino\n"
                "305,Avatar,5,James Cameron"
            ),
        },
        {
            "statement": "Left join the studios table with the movies table on studio_id. Keep all studios even if they have no movie listed.",
            "solution_code": "pd.merge(studios, movies, on='studio_id', how='left')",
            "hint": "When the left table row matches multiple right rows, it appears multiple times in the result.",
            "category": "merge-left",
            "tables": [
                {
                    "name": "studios",
                    "csv": (
                        "studio_id,studio_name\n"
                        "1,Paramount Pictures\n"
                        "2,Disney\n"
                        "3,Netflix\n"
                        "4,A24"
                    ),
                },
                {
                    "name": "movies",
                    "csv": (
                        "studio_id,title,box_office_millions\n"
                        "1,Top Gun Maverick,1491\n"
                        "1,Mission Impossible,567\n"
                        "2,Black Panther,1347\n"
                        "3,Marriage Story,2"
                    ),
                },
            ],
            "expected_csv": (
                "studio_id,studio_name,title,box_office_millions\n"
                "1,Paramount Pictures,Top Gun Maverick,1491.0\n"
                "1,Paramount Pictures,Mission Impossible,567.0\n"
                "2,Disney,Black Panther,1347.0\n"
                "3,Netflix,Marriage Story,2.0\n"
                "4,A24,,"
            ),
        },
        {
            "statement": "Inner join the actors table with the roles table on actor_id to see which character each actor played.",
            "solution_code": "pd.merge(actors, roles, on='actor_id', how='inner')",
            "hint": "An inner join discards any actor who has no matching row in the roles table.",
            "category": "merge-inner",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,nationality\n"
                        "1,Robert Downey Jr.,American\n"
                        "2,Chris Hemsworth,Australian\n"
                        "3,Mark Ruffalo,American\n"
                        "4,Jeremy Renner,American"
                    ),
                },
                {
                    "name": "roles",
                    "csv": (
                        "actor_id,character_name,movie\n"
                        "1,Tony Stark,Iron Man\n"
                        "2,Thor,Thor\n"
                        "3,Bruce Banner,The Avengers"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,nationality,character_name,movie\n"
                "1,Robert Downey Jr.,American,Tony Stark,Iron Man\n"
                "2,Chris Hemsworth,Australian,Thor,Thor\n"
                "3,Mark Ruffalo,American,Bruce Banner,The Avengers"
            ),
        },
        {
            "statement": "Left join the movies table with the ratings table on movie_id. Retain all movies even if they have no rating on record.",
            "solution_code": "pd.merge(movies, ratings, on='movie_id', how='left')",
            "hint": "Use how='left' so movies without a matching rating still appear with NaN values.",
            "category": "merge-left",
            "tables": [
                {
                    "name": "movies",
                    "csv": (
                        "movie_id,title,genre\n"
                        "401,The Godfather,Drama\n"
                        "402,Goodfellas,Crime\n"
                        "403,Interstellar,Sci-Fi\n"
                        "404,La La Land,Musical\n"
                        "405,Parasite,Thriller"
                    ),
                },
                {
                    "name": "ratings",
                    "csv": (
                        "movie_id,imdb_score,rotten_tomatoes\n"
                        "401,9.2,98\n"
                        "402,8.7,96\n"
                        "403,8.6,72\n"
                        "405,8.5,99"
                    ),
                },
            ],
            "expected_csv": (
                "movie_id,title,genre,imdb_score,rotten_tomatoes\n"
                "401,The Godfather,Drama,9.2,98.0\n"
                "402,Goodfellas,Crime,8.7,96.0\n"
                "403,Interstellar,Sci-Fi,8.6,72.0\n"
                "404,La La Land,Musical,,\n"
                "405,Parasite,Thriller,8.5,99.0"
            ),
        },
        {
            "statement": "Inner join the actors table with the awards table on actor_id to show only actors who have won an Oscar.",
            "solution_code": "pd.merge(actors, awards, on='actor_id', how='inner')",
            "hint": "An inner join keeps only actors who have a matching entry in the awards table.",
            "category": "merge-inner",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,birth_year\n"
                        "1,Joaquin Phoenix,1974\n"
                        "2,Anthony Hopkins,1937\n"
                        "3,Frances McDormand,1957\n"
                        "4,Halle Berry,1966\n"
                        "5,Natalie Portman,1981"
                    ),
                },
                {
                    "name": "awards",
                    "csv": (
                        "actor_id,award_name,film\n"
                        "1,Best Actor Oscar,Joker\n"
                        "2,Best Actor Oscar,The Silence of the Lambs\n"
                        "3,Best Actress Oscar,Nomadland\n"
                        "4,Best Actress Oscar,Monster's Ball"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,birth_year,award_name,film\n"
                "1,Joaquin Phoenix,1974,Best Actor Oscar,Joker\n"
                "2,Anthony Hopkins,1937,Best Actor Oscar,The Silence of the Lambs\n"
                "3,Frances McDormand,1957,Best Actress Oscar,Nomadland\n"
                "4,Halle Berry,1966,Best Actress Oscar,Monster's Ball"
            ),
        },
        {
            "statement": "Left join the actors table with the salaries table on actor_id. Keep all actors, filling salary_millions with NaN where data is missing.",
            "solution_code": "pd.merge(actors, salaries, on='actor_id', how='left')",
            "hint": "A left join preserves every actor from the left table, even those with no salary entry.",
            "category": "merge-left",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor_id,name,movie\n"
                        "1,Emma Stone,La La Land\n"
                        "2,Ryan Gosling,La La Land\n"
                        "3,Anne Hathaway,Interstellar\n"
                        "4,Jessica Chastain,Interstellar\n"
                        "5,Charlize Theron,Mad Max Fury Road"
                    ),
                },
                {
                    "name": "salaries",
                    "csv": (
                        "actor_id,salary_millions\n"
                        "1,26\n"
                        "2,29\n"
                        "3,35\n"
                        "5,14"
                    ),
                },
            ],
            "expected_csv": (
                "actor_id,name,movie,salary_millions\n"
                "1,Emma Stone,La La Land,26.0\n"
                "2,Ryan Gosling,La La Land,29.0\n"
                "3,Anne Hathaway,Interstellar,35.0\n"
                "4,Jessica Chastain,Interstellar,\n"
                "5,Charlize Theron,Mad Max Fury Road,14.0"
            ),
        },
    ],
    10: [
        {
            "statement": "Concatenate the action_heroes and scifi_leads tables into one DataFrame of actors and their films.",
            "solution_code": "pd.concat([action_heroes, scifi_leads], ignore_index=True)",
            "hint": "Use pd.concat([df1, df2], ignore_index=True) to stack two DataFrames vertically.",
            "category": "concat",
            "tables": [
                {
                    "name": "action_heroes",
                    "csv": (
                        "actor,film,year\n"
                        "Tom Cruise,Top Gun,1986\n"
                        "Arnold Schwarzenegger,Terminator 2,1991\n"
                        "Sylvester Stallone,Rocky IV,1985"
                    ),
                },
                {
                    "name": "scifi_leads",
                    "csv": (
                        "actor,film,year\n"
                        "Keanu Reeves,The Matrix,1999\n"
                        "Will Smith,Independence Day,1996\n"
                        "Harrison Ford,Star Wars,1977"
                    ),
                },
            ],
            "expected_csv": (
                "actor,film,year\n"
                "Tom Cruise,Top Gun,1986\n"
                "Arnold Schwarzenegger,Terminator 2,1991\n"
                "Sylvester Stallone,Rocky IV,1985\n"
                "Keanu Reeves,The Matrix,1999\n"
                "Will Smith,Independence Day,1996\n"
                "Harrison Ford,Star Wars,1977"
            ),
        },
        {
            "statement": "Concatenate the oscar_winners_90s and oscar_winners_00s tables into one combined winners table.",
            "solution_code": "pd.concat([oscar_winners_90s, oscar_winners_00s], ignore_index=True)",
            "hint": "Use pd.concat([df1, df2], ignore_index=True) to combine two tables of the same shape.",
            "category": "concat",
            "tables": [
                {
                    "name": "oscar_winners_90s",
                    "csv": (
                        "actor,film,year,award\n"
                        "Tom Hanks,Forrest Gump,1994,Best Actor\n"
                        "Susan Sarandon,Dead Man Walking,1995,Best Actress\n"
                        "Nicolas Cage,Leaving Las Vegas,1995,Best Actor"
                    ),
                },
                {
                    "name": "oscar_winners_00s",
                    "csv": (
                        "actor,film,year,award\n"
                        "Halle Berry,Monsters Ball,2001,Best Actress\n"
                        "Adrien Brody,The Pianist,2002,Best Actor\n"
                        "Charlize Theron,Monster,2003,Best Actress"
                    ),
                },
            ],
            "expected_csv": (
                "actor,film,year,award\n"
                "Tom Hanks,Forrest Gump,1994,Best Actor\n"
                "Susan Sarandon,Dead Man Walking,1995,Best Actress\n"
                "Nicolas Cage,Leaving Las Vegas,1995,Best Actor\n"
                "Halle Berry,Monsters Ball,2001,Best Actress\n"
                "Adrien Brody,The Pianist,2002,Best Actor\n"
                "Charlize Theron,Monster,2003,Best Actress"
            ),
        },
        {
            "statement": "Merge the actors table with the films table on film_id, then filter to movies that earned more than 200 million at the box office.",
            "solution_code": "actors.merge(films, on='film_id')[actors.merge(films, on='film_id')['box_office_m'] > 200]",
            "hint": "Merge first with df1.merge(df2, on='key'), then apply boolean indexing on the result.",
            "category": "merge-filter",
            "tables": [
                {
                    "name": "actors",
                    "csv": (
                        "actor,film_id\n"
                        "Leonardo DiCaprio,1\n"
                        "Tom Hanks,2\n"
                        "Brad Pitt,3\n"
                        "Matt Damon,4"
                    ),
                },
                {
                    "name": "films",
                    "csv": (
                        "film_id,title,box_office_m\n"
                        "1,Titanic,2187\n"
                        "2,Cast Away,233\n"
                        "3,Fight Club,101\n"
                        "4,The Martian,630"
                    ),
                },
            ],
            "expected_csv": (
                "actor,film_id,title,box_office_m\n"
                "Leonardo DiCaprio,1,Titanic,2187\n"
                "Tom Hanks,2,Cast Away,233\n"
                "Matt Damon,4,The Martian,630"
            ),
        },
        {
            "statement": "Merge the cast table with the movies table on movie_id, then select only the actor, title, and year columns.",
            "solution_code": "cast.merge(movies, on='movie_id')[['actor', 'title', 'year']]",
            "hint": "Merge with df1.merge(df2, on='key'), then select columns using double brackets.",
            "category": "merge-select",
            "tables": [
                {
                    "name": "cast",
                    "csv": (
                        "actor,movie_id\n"
                        "Jennifer Lawrence,101\n"
                        "Meryl Streep,102\n"
                        "Cate Blanchett,103\n"
                        "Sandra Bullock,104"
                    ),
                },
                {
                    "name": "movies",
                    "csv": (
                        "movie_id,title,studio,year\n"
                        "101,The Hunger Games,Lionsgate,2012\n"
                        "102,The Devil Wears Prada,Fox,2006\n"
                        "103,Blue Jasmine,Sony Pictures Classics,2013\n"
                        "104,Gravity,Warner Bros,2013"
                    ),
                },
            ],
            "expected_csv": (
                "actor,title,year\n"
                "Jennifer Lawrence,The Hunger Games,2012\n"
                "Meryl Streep,The Devil Wears Prada,2006\n"
                "Cate Blanchett,Blue Jasmine,2013\n"
                "Sandra Bullock,Gravity,2013"
            ),
        },
        {
            "statement": "Concatenate the marvel_actors and dc_actors tables, then filter to only Robert Downey Jr, Scarlett Johansson, and Gal Gadot.",
            "solution_code": "pd.concat([marvel_actors, dc_actors], ignore_index=True)[pd.concat([marvel_actors, dc_actors], ignore_index=True)['actor'].isin(['Robert Downey Jr', 'Scarlett Johansson', 'Gal Gadot'])]",
            "hint": "Concat the tables first, then use .isin([...]) to filter the combined result.",
            "category": "concat",
            "tables": [
                {
                    "name": "marvel_actors",
                    "csv": (
                        "actor,character,film\n"
                        "Robert Downey Jr,Iron Man,Avengers Endgame\n"
                        "Scarlett Johansson,Black Widow,Avengers Endgame\n"
                        "Chris Evans,Captain America,Avengers Endgame"
                    ),
                },
                {
                    "name": "dc_actors",
                    "csv": (
                        "actor,character,film\n"
                        "Ben Affleck,Batman,Batman v Superman\n"
                        "Gal Gadot,Wonder Woman,Wonder Woman\n"
                        "Ezra Miller,The Flash,Justice League"
                    ),
                },
            ],
            "expected_csv": (
                "actor,character,film\n"
                "Robert Downey Jr,Iron Man,Avengers Endgame\n"
                "Scarlett Johansson,Black Widow,Avengers Endgame\n"
                "Gal Gadot,Wonder Woman,Wonder Woman"
            ),
        },
        {
            "statement": "Merge the actor_roles table with the awards table on movie, then filter to films with 2 or more Oscar wins.",
            "solution_code": "actor_roles.merge(awards, on='movie')[actor_roles.merge(awards, on='movie')['oscar_wins'] >= 2]",
            "hint": "Merge on the shared column, then filter the merged result with boolean indexing.",
            "category": "merge-filter",
            "tables": [
                {
                    "name": "actor_roles",
                    "csv": (
                        "actor,movie\n"
                        "Daniel Day-Lewis,There Will Be Blood\n"
                        "Philip Seymour Hoffman,Capote\n"
                        "Sean Penn,Milk\n"
                        "Jeff Bridges,Crazy Heart\n"
                        "Colin Firth,The Kings Speech"
                    ),
                },
                {
                    "name": "awards",
                    "csv": (
                        "movie,oscar_wins\n"
                        "There Will Be Blood,2\n"
                        "Capote,1\n"
                        "Milk,2\n"
                        "Crazy Heart,1\n"
                        "The Kings Speech,4"
                    ),
                },
            ],
            "expected_csv": (
                "actor,movie,oscar_wins\n"
                "Daniel Day-Lewis,There Will Be Blood,2\n"
                "Sean Penn,Milk,2\n"
                "Colin Firth,The Kings Speech,4"
            ),
        },
        {
            "statement": "Merge the actor_contracts table with the studios table on studio_id, then select only the actor and studio_name columns.",
            "solution_code": "actor_contracts.merge(studios, on='studio_id')[['actor', 'studio_name']]",
            "hint": "After merging, use double brackets to select only the columns you need.",
            "category": "merge-select",
            "tables": [
                {
                    "name": "actor_contracts",
                    "csv": (
                        "actor,studio_id\n"
                        "Tom Cruise,10\n"
                        "Julia Roberts,20\n"
                        "Will Smith,30\n"
                        "Denzel Washington,20"
                    ),
                },
                {
                    "name": "studios",
                    "csv": (
                        "studio_id,studio_name,country\n"
                        "10,Paramount,USA\n"
                        "20,Universal,USA\n"
                        "30,Columbia,USA"
                    ),
                },
            ],
            "expected_csv": (
                "actor,studio_name\n"
                "Tom Cruise,Paramount\n"
                "Julia Roberts,Universal\n"
                "Will Smith,Columbia\n"
                "Denzel Washington,Universal"
            ),
        },
        {
            "statement": "Concatenate the original_trilogy and prequel_trilogy Star Wars tables into one complete saga DataFrame.",
            "solution_code": "pd.concat([original_trilogy, prequel_trilogy], ignore_index=True)",
            "hint": "Use pd.concat([df1, df2], ignore_index=True) to stack both trilogies into one table.",
            "category": "concat",
            "tables": [
                {
                    "name": "original_trilogy",
                    "csv": (
                        "title,year,box_office_m\n"
                        "Star Wars,1977,775\n"
                        "The Empire Strikes Back,1980,538\n"
                        "Return of the Jedi,1983,475"
                    ),
                },
                {
                    "name": "prequel_trilogy",
                    "csv": (
                        "title,year,box_office_m\n"
                        "The Phantom Menace,1999,1027\n"
                        "Attack of the Clones,2002,649\n"
                        "Revenge of the Sith,2005,868"
                    ),
                },
            ],
            "expected_csv": (
                "title,year,box_office_m\n"
                "Star Wars,1977,775\n"
                "The Empire Strikes Back,1980,538\n"
                "Return of the Jedi,1983,475\n"
                "The Phantom Menace,1999,1027\n"
                "Attack of the Clones,2002,649\n"
                "Revenge of the Sith,2005,868"
            ),
        },
        {
            "statement": "Merge the headliners table with the salaries table on film, filter to actors who earned at least 16 million, then select only actor and salary_m.",
            "solution_code": "headliners.merge(salaries, on='film')[headliners.merge(salaries, on='film')['salary_m'] >= 16][['actor', 'salary_m']]",
            "hint": "Chain merge, then filter with boolean indexing, then select columns.",
            "category": "merge-filter",
            "tables": [
                {
                    "name": "headliners",
                    "csv": (
                        "actor,film\n"
                        "Jim Carrey,The Mask\n"
                        "Tom Cruise,Mission Impossible\n"
                        "Will Smith,Men in Black\n"
                        "Harrison Ford,Air Force One\n"
                        "Bruce Willis,The Fifth Element"
                    ),
                },
                {
                    "name": "salaries",
                    "csv": (
                        "film,salary_m\n"
                        "The Mask,15\n"
                        "Mission Impossible,70\n"
                        "Men in Black,5\n"
                        "Air Force One,20\n"
                        "The Fifth Element,16"
                    ),
                },
            ],
            "expected_csv": (
                "actor,salary_m\n"
                "Tom Cruise,70\n"
                "Harrison Ford,20\n"
                "Bruce Willis,16"
            ),
        },
        {
            "statement": "Concatenate the nominees_a and nominees_b tables, then filter to actresses with 4 or more nominations and select only actor and film.",
            "solution_code": "pd.concat([nominees_a, nominees_b], ignore_index=True)[pd.concat([nominees_a, nominees_b], ignore_index=True)['nominations'] >= 4][['actor', 'film']]",
            "hint": "Concat first, then chain boolean indexing on the nominations column, then select columns.",
            "category": "concat",
            "tables": [
                {
                    "name": "nominees_a",
                    "csv": (
                        "actor,film,nominations\n"
                        "Natalie Portman,Black Swan,5\n"
                        "Annette Bening,The Kids Are All Right,4\n"
                        "Nicole Kidman,Rabbit Hole,1"
                    ),
                },
                {
                    "name": "nominees_b",
                    "csv": (
                        "actor,film,nominations\n"
                        "Meryl Streep,The Iron Lady,3\n"
                        "Viola Davis,The Help,4\n"
                        "Glenn Close,Albert Nobbs,1"
                    ),
                },
            ],
            "expected_csv": (
                "actor,film\n"
                "Natalie Portman,Black Swan\n"
                "Annette Bening,The Kids Are All Right\n"
                "Viola Davis,The Help"
            ),
        },
    ],

    11: [
        {
            "statement": "Filter the movies table to show only films whose title contains 'Man'.",
            "solution_code": 'movies[movies["title"].str.contains("Man", case=False, na=False)]',
            "hint": "Use df['col'].str.contains('pattern', case=False, na=False) to filter rows by substring.",
            "category": 'str-contains',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,studio,year\n"
                        "Iron Man,Marvel Studios,2008\n"
                        "Spider-Man,Columbia Pictures,2002\n"
                        "Gladiator,DreamWorks,2000\n"
                        "The Dark Knight,Warner Bros,2008\n"
                        "Ant-Man,Marvel Studios,2015"
                    ),
                },
            ],
            "expected_csv": (
                "title,studio,year\n"
                "Iron Man,Marvel Studios,2008\n"
                "Spider-Man,Columbia Pictures,2002\n"
                "Ant-Man,Marvel Studios,2015"
            ),
        },
        {
            "statement": "Filter the films table to rows where the director's name contains 'Nolan'.",
            "solution_code": 'films[films["director"].str.contains("Nolan", case=False, na=False)]',
            "hint": 'str.contains works on any string column — not just titles.',
            "category": 'str-contains',
            "tables": [
                {
                    "name": 'films',
                    "csv": (
                        "title,director,box_office_millions\n"
                        "Inception,Christopher Nolan,836\n"
                        "The Dark Knight,Christopher Nolan,1005\n"
                        "Interstellar,Christopher Nolan,773\n"
                        "Avengers Endgame,Anthony Russo,2798\n"
                        "Mad Max Fury Road,George Miller,375"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,box_office_millions\n"
                "Inception,Christopher Nolan,836\n"
                "The Dark Knight,Christopher Nolan,1005\n"
                "Interstellar,Christopher Nolan,773"
            ),
        },
        {
            "statement": "Filter the cast table to rows where the actor's name contains 'Brad'.",
            "solution_code": 'cast[cast["actor"].str.contains("Brad", case=False, na=False)]',
            "hint": 'Apply str.contains on the actor column with case=False for a case-insensitive match.',
            "category": 'str-contains',
            "tables": [
                {
                    "name": 'cast',
                    "csv": (
                        "actor,movie,year\n"
                        "Brad Pitt,Fight Club,1999\n"
                        "Leonardo DiCaprio,Inception,2010\n"
                        "Brad Pitt,Troy,2004\n"
                        "Tom Hanks,Cast Away,2000\n"
                        "Cate Blanchett,Carol,2015"
                    ),
                },
            ],
            "expected_csv": (
                "actor,movie,year\n"
                "Brad Pitt,Fight Club,1999\n"
                "Brad Pitt,Troy,2004"
            ),
        },
        {
            "statement": "Filter the catalog table to films whose genre contains 'Action'.",
            "solution_code": 'catalog[catalog["genre"].str.contains("Action", case=False, na=False)]',
            "hint": "str.contains matches a substring anywhere in the string, so 'Action Thriller' is also a match.",
            "category": 'str-contains',
            "tables": [
                {
                    "name": 'catalog',
                    "csv": (
                        "title,director,genre\n"
                        "Mad Max Fury Road,George Miller,Action\n"
                        "The Notebook,Nick Cassavetes,Romance\n"
                        "John Wick,Chad Stahelski,Action Thriller\n"
                        "La La Land,Damien Chazelle,Musical\n"
                        "Mission Impossible,Brian De Palma,Action"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,genre\n"
                "Mad Max Fury Road,George Miller,Action\n"
                "John Wick,Chad Stahelski,Action Thriller\n"
                "Mission Impossible,Brian De Palma,Action"
            ),
        },
        {
            "statement": "Filter the movies table to films whose title starts with 'The'.",
            "solution_code": 'movies[movies["title"].str.startswith("The")]',
            "hint": "Use df['col'].str.startswith('prefix') to keep only rows beginning with that prefix.",
            "category": 'str-startswith',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,director,year\n"
                        "The Godfather,Francis Ford Coppola,1972\n"
                        "Jaws,Steven Spielberg,1975\n"
                        "The Shining,Stanley Kubrick,1980\n"
                        "Alien,Ridley Scott,1979\n"
                        "The Revenant,Alejandro Inarritu,2015"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,year\n"
                "The Godfather,Francis Ford Coppola,1972\n"
                "The Shining,Stanley Kubrick,1980\n"
                "The Revenant,Alejandro Inarritu,2015"
            ),
        },
        {
            "statement": "Filter the releases table to films distributed by a studio whose name starts with 'Warner'.",
            "solution_code": 'releases[releases["studio"].str.startswith("Warner")]',
            "hint": 'str.startswith checks the beginning of each string value in the column.',
            "category": 'str-startswith',
            "tables": [
                {
                    "name": 'releases',
                    "csv": (
                        "title,studio,year\n"
                        "The Dark Knight,Warner Bros,2008\n"
                        "Inception,Warner Bros,2010\n"
                        "Titanic,Paramount Pictures,1997\n"
                        "Gravity,Warner Bros,2013\n"
                        "Avatar,20th Century Fox,2009"
                    ),
                },
            ],
            "expected_csv": (
                "title,studio,year\n"
                "The Dark Knight,Warner Bros,2008\n"
                "Inception,Warner Bros,2010\n"
                "Gravity,Warner Bros,2013"
            ),
        },
        {
            "statement": "Filter the directors table to rows where the director's name starts with 'Steven'.",
            "solution_code": 'directors[directors["director"].str.startswith("Steven")]',
            "hint": "str.startswith is exact at the start — 'Steven Spielberg' and 'Steven Soderbergh' both match 'Steven'.",
            "category": 'str-startswith',
            "tables": [
                {
                    "name": 'directors',
                    "csv": (
                        "director,movie,award\n"
                        "Steven Spielberg,Schindler's List,Oscar\n"
                        "Quentin Tarantino,Pulp Fiction,Palme d'Or\n"
                        "Steven Soderbergh,Traffic,Oscar\n"
                        "Martin Scorsese,The Departed,Oscar\n"
                        "Steven Spielberg,Saving Private Ryan,Oscar"
                    ),
                },
            ],
            "expected_csv": (
                "director,movie,award\n"
                "Steven Spielberg,Schindler's List,Oscar\n"
                "Steven Soderbergh,Traffic,Oscar\n"
                "Steven Spielberg,Saving Private Ryan,Oscar"
            ),
        },
        {
            "statement": 'Filter the movies table to films whose title is longer than 10 characters.',
            "solution_code": 'movies[movies["title"].str.len() > 10]',
            "hint": "df['col'].str.len() returns the character count of each string; use it in a boolean filter.",
            "category": 'str-len',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,year,rating\n"
                        "Jaws,1975,8.0\n"
                        "The Godfather,1972,9.2\n"
                        "Alien,1979,8.5\n"
                        "Schindler's List,1993,9.0\n"
                        "Up,2009,8.2"
                    ),
                },
            ],
            "expected_csv": (
                "title,year,rating\n"
                "The Godfather,1972,9.2\n"
                "Schindler's List,1993,9.0"
            ),
        },
        {
            "statement": "Add a column called 'title_length' to the awards table showing the number of characters in each title.",
            "solution_code": 'awards.assign(title_length=awards["title"].str.len())',
            "hint": "Use df.assign(new_col=df['col'].str.len()) to add a character-count column without modifying the original.",
            "category": 'str-len',
            "tables": [
                {
                    "name": 'awards',
                    "csv": (
                        "title,director\n"
                        "Parasite,Bong Joon-ho\n"
                        "Joker,Todd Phillips\n"
                        "Interstellar,Christopher Nolan\n"
                        "Dunkirk,Christopher Nolan\n"
                        "1917,Sam Mendes"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,title_length\n"
                "Parasite,Bong Joon-ho,8\n"
                "Joker,Todd Phillips,5\n"
                "Interstellar,Christopher Nolan,12\n"
                "Dunkirk,Christopher Nolan,7\n"
                "1917,Sam Mendes,4"
            ),
        },
        {
            "statement": 'Filter the performances table to actors whose name is 12 or more characters long.',
            "solution_code": 'performances[performances["actor"].str.len() >= 12]',
            "hint": "str.len() counts characters including spaces, so 'Meryl Streep' has 12 characters.",
            "category": 'str-len',
            "tables": [
                {
                    "name": 'performances',
                    "csv": (
                        "actor,movie,year\n"
                        "Tom Hanks,Forrest Gump,1994\n"
                        "Meryl Streep,The Devil Wears Prada,2006\n"
                        "Al Pacino,The Godfather,1972\n"
                        "Cate Blanchett,Blue Jasmine,2013\n"
                        "Denzel Washington,Training Day,2001"
                    ),
                },
            ],
            "expected_csv": (
                "actor,movie,year\n"
                "Meryl Streep,The Devil Wears Prada,2006\n"
                "Cate Blanchett,Blue Jasmine,2013\n"
                "Denzel Washington,Training Day,2001"
            ),
        },
    ],
    12: [
        {
            "statement": "Split each actor's full name in the cast table and add a new column called first_name containing only their first name.",
            "solution_code": 'cast.assign(first_name=cast["name"].str.split(" ").str[0])',
            "hint": "Use .str.split(' ').str[0] to get the first token before the space.",
            "category": 'str-split',
            "tables": [
                {
                    "name": 'cast',
                    "csv": (
                        "name,film,role\n"
                        "Leonardo DiCaprio,Inception,Dom Cobb\n"
                        "Brad Pitt,Fight Club,Tyler Durden\n"
                        "Tom Hanks,Cast Away,Chuck Noland\n"
                        "Natalie Portman,Black Swan,Nina Sayers\n"
                        "Charlize Theron,Monster,Aileen Wuornos"
                    ),
                },
            ],
            "expected_csv": (
                "name,film,role,first_name\n"
                "Leonardo DiCaprio,Inception,Dom Cobb,Leonardo\n"
                "Brad Pitt,Fight Club,Tyler Durden,Brad\n"
                "Tom Hanks,Cast Away,Chuck Noland,Tom\n"
                "Natalie Portman,Black Swan,Nina Sayers,Natalie\n"
                "Charlize Theron,Monster,Aileen Wuornos,Charlize"
            ),
        },
        {
            "statement": 'Add a column first_word to the films table containing the first word of each film title.',
            "solution_code": 'films.assign(first_word=films["title"].str.split(" ").str[0])',
            "hint": 'Split the title on spaces and take index 0 to get the first word.',
            "category": 'str-split',
            "tables": [
                {
                    "name": 'films',
                    "csv": (
                        "title,studio,year\n"
                        "The Dark Knight,Warner Bros,2008\n"
                        "Pulp Fiction,Miramax Films,1994\n"
                        "The Godfather,Paramount Pictures,1972\n"
                        "Jaws,Universal Pictures,1975\n"
                        "Goodfellas,Warner Bros,1990"
                    ),
                },
            ],
            "expected_csv": (
                "title,studio,year,first_word\n"
                "The Dark Knight,Warner Bros,2008,The\n"
                "Pulp Fiction,Miramax Films,1994,Pulp\n"
                "The Godfather,Paramount Pictures,1972,The\n"
                "Jaws,Universal Pictures,1975,Jaws\n"
                "Goodfellas,Warner Bros,1990,Goodfellas"
            ),
        },
        {
            "statement": "Add a last_name column to the directors table by extracting the last word of each director's full name.",
            "solution_code": 'directors.assign(last_name=directors["full_name"].str.split(" ").str[-1])',
            "hint": "Use .str.split(' ').str[-1] to get the last token after splitting on spaces.",
            "category": 'str-split',
            "tables": [
                {
                    "name": 'directors',
                    "csv": (
                        "full_name,genre,debut_year\n"
                        "Christopher Nolan,Sci-Fi,1998\n"
                        "Quentin Tarantino,Crime,1992\n"
                        "Steven Spielberg,Adventure,1971\n"
                        "Martin Scorsese,Drama,1963\n"
                        "Ridley Scott,Thriller,1977"
                    ),
                },
            ],
            "expected_csv": (
                "full_name,genre,debut_year,last_name\n"
                "Christopher Nolan,Sci-Fi,1998,Nolan\n"
                "Quentin Tarantino,Crime,1992,Tarantino\n"
                "Steven Spielberg,Adventure,1971,Spielberg\n"
                "Martin Scorsese,Drama,1963,Scorsese\n"
                "Ridley Scott,Thriller,1977,Scott"
            ),
        },
        {
            "statement": 'The studio names in the studios table use underscores instead of spaces. Add a column studio_clean with the underscores replaced by spaces.',
            "solution_code": 'studios.assign(studio_clean=studios["studio"].str.replace("_", " ", regex=False))',
            "hint": "Use str.replace('_', ' ', regex=False) to swap underscores for spaces.",
            "category": 'str-replace',
            "tables": [
                {
                    "name": 'studios',
                    "csv": (
                        "studio,country\n"
                        "Warner_Bros,USA\n"
                        "Universal_Pictures,USA\n"
                        "Paramount_Pictures,USA\n"
                        "20th_Century_Fox,USA\n"
                        "DreamWorks_Animation,USA"
                    ),
                },
            ],
            "expected_csv": (
                "studio,country,studio_clean\n"
                "Warner_Bros,USA,Warner Bros\n"
                "Universal_Pictures,USA,Universal Pictures\n"
                "Paramount_Pictures,USA,Paramount Pictures\n"
                "20th_Century_Fox,USA,20th Century Fox\n"
                "DreamWorks_Animation,USA,DreamWorks Animation"
            ),
        },
        {
            "statement": 'The gross column in the revenues table has a leading dollar sign. Add a column gross_clean with the dollar sign removed.',
            "solution_code": 'revenues.assign(gross_clean=revenues["gross"].str.replace("$", "", regex=False))',
            "hint": "Use str.replace('$', '', regex=False) — pass regex=False so $ is treated as a literal character, not a regex anchor.",
            "category": 'str-replace',
            "tables": [
                {
                    "name": 'revenues',
                    "csv": (
                        "film,gross\n"
                        "Avatar,$2.9B\n"
                        "Avengers Endgame,$2.8B\n"
                        "Titanic,$2.2B\n"
                        "Star Wars The Force Awakens,$2.0B\n"
                        "Jurassic World,$1.7B"
                    ),
                },
            ],
            "expected_csv": (
                "film,gross,gross_clean\n"
                "Avatar,$2.9B,2.9B\n"
                "Avengers Endgame,$2.8B,2.8B\n"
                "Titanic,$2.2B,2.2B\n"
                "Star Wars The Force Awakens,$2.0B,2.0B\n"
                "Jurassic World,$1.7B,1.7B"
            ),
        },
        {
            "statement": "Shorten the award label in the awards table: replace 'Best Picture Winner' with 'BP Winner' and store the result in a new column called award_short.",
            "solution_code": 'awards.assign(award_short=awards["award"].str.replace("Best Picture Winner", "BP Winner", regex=False))',
            "hint": 'Use str.replace with regex=False to do a plain text substitution.',
            "category": 'str-replace',
            "tables": [
                {
                    "name": 'awards',
                    "csv": (
                        "film,award\n"
                        "Parasite,Best Picture Winner\n"
                        "Nomadland,Best Picture Winner\n"
                        "Green Book,Best Picture Winner\n"
                        "The Shape of Water,Best Picture Winner\n"
                        "Moonlight,Best Picture Winner"
                    ),
                },
            ],
            "expected_csv": (
                "film,award,award_short\n"
                "Parasite,Best Picture Winner,BP Winner\n"
                "Nomadland,Best Picture Winner,BP Winner\n"
                "Green Book,Best Picture Winner,BP Winner\n"
                "The Shape of Water,Best Picture Winner,BP Winner\n"
                "Moonlight,Best Picture Winner,BP Winner"
            ),
        },
        {
            "statement": "The role_note column in the cast2 table has a 'Nominated - ' prefix before each film title. Remove that prefix so only the film title remains, updating the role_note column via assign.",
            "solution_code": 'cast2.assign(role_note=cast2["role_note"].str.replace("Nominated - ", "", regex=False))',
            "hint": "Use str.replace('Nominated - ', '', regex=False) to strip the prefix from every value.",
            "category": 'str-replace',
            "tables": [
                {
                    "name": 'cast2',
                    "csv": (
                        "actor,role_note\n"
                        "Cate Blanchett,Nominated - Tar\n"
                        "Anthony Hopkins,Nominated - The Father\n"
                        "Frances McDormand,Nominated - Nomadland\n"
                        "Joaquin Phoenix,Nominated - Joker\n"
                        "Glenn Close,Nominated - Hillbilly Elegy"
                    ),
                },
            ],
            "expected_csv": (
                "actor,role_note\n"
                "Cate Blanchett,Tar\n"
                "Anthony Hopkins,The Father\n"
                "Frances McDormand,Nomadland\n"
                "Joaquin Phoenix,Joker\n"
                "Glenn Close,Hillbilly Elegy"
            ),
        },
        {
            "statement": "The entry column in the catalog table contains film titles followed by a release year in parentheses, e.g. 'Inception (2010)'. Extract the 4-digit year into a new column called year.",
            "solution_code": 'catalog.assign(year=catalog["entry"].str.extract(r"(\\d{4})")[0].astype(int))',
            "hint": "Use str.extract(r'(\\d{4})') — the parentheses form the capture group that returns the year.",
            "category": 'str-extract',
            "tables": [
                {
                    "name": 'catalog',
                    "csv": (
                        "entry,notes\n"
                        "Inception (2010),Sci-Fi thriller\n"
                        "The Matrix (1999),Action classic\n"
                        "Interstellar (2014),Space epic\n"
                        "The Prestige (2006),Mystery drama\n"
                        "Dunkirk (2017),War film"
                    ),
                },
            ],
            "expected_csv": (
                "entry,notes,year\n"
                "Inception (2010),Sci-Fi thriller,2010\n"
                "The Matrix (1999),Action classic,1999\n"
                "Interstellar (2014),Space epic,2014\n"
                "The Prestige (2006),Mystery drama,2006\n"
                "Dunkirk (2017),War film,2017"
            ),
        },
        {
            "statement": 'The info column in the contacts table holds email addresses. Extract the domain (everything after the @) into a new column called domain.',
            "solution_code": 'contacts.assign(domain=contacts["info"].str.extract(r"@([A-Za-z0-9.]+)"))',
            "hint": "Use str.extract(r'@([A-Za-z0-9.]+)') to capture everything after the @ symbol.",
            "category": 'str-extract',
            "tables": [
                {
                    "name": 'contacts',
                    "csv": (
                        "person,info\n"
                        "Sylvester Stallone,director@stallone.com\n"
                        "Arnold Schwarzenegger,agent@arnie.net\n"
                        "Bruce Willis,pr@brucepr.org\n"
                        "Denzel Washington,office@denzel.com\n"
                        "Will Smith,booking@willsmith.net"
                    ),
                },
            ],
            "expected_csv": (
                "person,info,domain\n"
                "Sylvester Stallone,director@stallone.com,stallone.com\n"
                "Arnold Schwarzenegger,agent@arnie.net,arnie.net\n"
                "Bruce Willis,pr@brucepr.org,brucepr.org\n"
                "Denzel Washington,office@denzel.com,denzel.com\n"
                "Will Smith,booking@willsmith.net,willsmith.net"
            ),
        },
        {
            "statement": "The tagline column in the scripts table begins with a two-word setting phrase before a colon, e.g. 'In space: ...'. Extract that phrase into a new column called setting.",
            "solution_code": 'scripts.assign(setting=scripts["tagline"].str.extract(r"^([A-Za-z]+ [A-Za-z]+):"))',
            "hint": "Use str.extract(r'^([A-Za-z]+ [A-Za-z]+):') to capture the two-word phrase that comes before the colon.",
            "category": 'str-extract',
            "tables": [
                {
                    "name": 'scripts',
                    "csv": (
                        "film,tagline\n"
                        "Alien,In space: no one can hear you scream\n"
                        "Jaws,On land: everyone hears you scream\n"
                        "Psycho,At home: terror finds you\n"
                        "The Shining,In winter: madness takes hold\n"
                        "Gravity,In orbit: silence is deadly"
                    ),
                },
            ],
            "expected_csv": (
                "film,tagline,setting\n"
                "Alien,In space: no one can hear you scream,In space\n"
                "Jaws,On land: everyone hears you scream,On land\n"
                "Psycho,At home: terror finds you,At home\n"
                "The Shining,In winter: madness takes hold,In winter\n"
                "Gravity,In orbit: silence is deadly,In orbit"
            ),
        },
    ],
    13: [
        {
            "statement": 'Convert the release_date column in the movies table to datetime and return only the title and release_date columns, with release_date as a proper datetime.',
            "solution_code": 'movies.assign(release_date=pd.to_datetime(movies["release_date"]))[["title", "release_date"]]',
            "hint": 'Use pd.to_datetime() and assign the result back to the same column, then select the two columns.',
            "category": 'to-datetime',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,release_date\n"
                        "Titanic,1997-12-19\n"
                        "The Matrix,1999-03-31\n"
                        "Gladiator,2000-05-05\n"
                        "Inception,2010-07-16\n"
                        "Interstellar,2014-11-07"
                    ),
                },
            ],
            "expected_csv": (
                "title,release_date\n"
                "Titanic,1997-12-19\n"
                "The Matrix,1999-03-31\n"
                "Gladiator,2000-05-05\n"
                "Inception,2010-07-16\n"
                "Interstellar,2014-11-07"
            ),
        },
        {
            "statement": 'Convert the premiere_date column in the premieres table to datetime and return only the title and premiere_date columns.',
            "solution_code": 'premieres.assign(premiere_date=pd.to_datetime(premieres["premiere_date"]))[["title", "premiere_date"]]',
            "hint": 'Use pd.to_datetime() on premiere_date, assign it back with the same name, then select the two columns.',
            "category": 'to-datetime',
            "tables": [
                {
                    "name": 'premieres',
                    "csv": (
                        "title,premiere_date,city\n"
                        "Avatar,2009-12-10,London\n"
                        "The Dark Knight,2008-07-14,New York\n"
                        "Mad Max Fury Road,2015-05-07,Hollywood\n"
                        "La La Land,2016-08-31,Venice\n"
                        "Parasite,2019-05-21,Cannes"
                    ),
                },
            ],
            "expected_csv": (
                "title,premiere_date\n"
                "Avatar,2009-12-10\n"
                "The Dark Knight,2008-07-14\n"
                "Mad Max Fury Road,2015-05-07\n"
                "La La Land,2016-08-31\n"
                "Parasite,2019-05-21"
            ),
        },
        {
            "statement": 'Convert the wrap_date column in the shoots table to datetime and return only the title and wrap_date columns.',
            "solution_code": 'shoots.assign(wrap_date=pd.to_datetime(shoots["wrap_date"]))[["title", "wrap_date"]]',
            "hint": 'pd.to_datetime() converts string dates to datetime64. Assign back with the same column name, then select.',
            "category": 'to-datetime',
            "tables": [
                {
                    "name": 'shoots',
                    "csv": (
                        "title,director,wrap_date\n"
                        "Dunkirk,Christopher Nolan,2016-12-10\n"
                        "Get Out,Jordan Peele,2016-10-14\n"
                        "Hereditary,Ari Aster,2017-09-22\n"
                        "1917,Sam Mendes,2019-05-18\n"
                        "The Revenant,Alejandro Inarritu,2015-08-01"
                    ),
                },
            ],
            "expected_csv": (
                "title,wrap_date\n"
                "Dunkirk,2016-12-10\n"
                "Get Out,2016-10-14\n"
                "Hereditary,2017-09-22\n"
                "1917,2019-05-18\n"
                "The Revenant,2015-08-01"
            ),
        },
        {
            "statement": 'Add a release_year column to the releases table by extracting the year from the release_date column.',
            "solution_code": 'releases.assign(release_year=pd.to_datetime(releases["release_date"]).dt.year)',
            "hint": 'Use pd.to_datetime() on the column and chain .dt.year to extract just the year as an integer.',
            "category": 'dt-accessor',
            "tables": [
                {
                    "name": 'releases',
                    "csv": (
                        "title,release_date\n"
                        "Titanic,1997-12-19\n"
                        "The Matrix,1999-03-31\n"
                        "Gladiator,2000-05-05\n"
                        "Inception,2010-07-16\n"
                        "Interstellar,2014-11-07"
                    ),
                },
            ],
            "expected_csv": (
                "title,release_date,release_year\n"
                "Titanic,1997-12-19,1997\n"
                "The Matrix,1999-03-31,1999\n"
                "Gladiator,2000-05-05,2000\n"
                "Inception,2010-07-16,2010\n"
                "Interstellar,2014-11-07,2014"
            ),
        },
        {
            "statement": 'Add a premiere_month column to the premieres table by extracting the month number from the premiere_date column.',
            "solution_code": 'premieres.assign(premiere_month=pd.to_datetime(premieres["premiere_date"]).dt.month)',
            "hint": 'Convert the column with pd.to_datetime() and use .dt.month to get the numeric month (1-12).',
            "category": 'dt-accessor',
            "tables": [
                {
                    "name": 'premieres',
                    "csv": (
                        "title,premiere_date\n"
                        "Avatar,2009-12-10\n"
                        "The Dark Knight,2008-07-14\n"
                        "Mad Max Fury Road,2015-05-07\n"
                        "La La Land,2016-08-31\n"
                        "Parasite,2019-05-21"
                    ),
                },
            ],
            "expected_csv": (
                "title,premiere_date,premiere_month\n"
                "Avatar,2009-12-10,12\n"
                "The Dark Knight,2008-07-14,7\n"
                "Mad Max Fury Road,2015-05-07,5\n"
                "La La Land,2016-08-31,8\n"
                "Parasite,2019-05-21,5"
            ),
        },
        {
            "statement": 'Add a shoot_start_day column to the shoots table by extracting the day of the month from the start_date column.',
            "solution_code": 'shoots.assign(shoot_start_day=pd.to_datetime(shoots["start_date"]).dt.day)',
            "hint": 'Use .dt.day after pd.to_datetime() to get the day-of-month as an integer.',
            "category": 'dt-accessor',
            "tables": [
                {
                    "name": 'shoots',
                    "csv": (
                        "title,director,start_date\n"
                        "Dunkirk,Christopher Nolan,2016-05-23\n"
                        "Get Out,Jordan Peele,2016-07-15\n"
                        "Hereditary,Ari Aster,2017-06-05\n"
                        "1917,Sam Mendes,2018-04-10\n"
                        "The Revenant,Alejandro Inarritu,2014-10-11"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,start_date,shoot_start_day\n"
                "Dunkirk,Christopher Nolan,2016-05-23,23\n"
                "Get Out,Jordan Peele,2016-07-15,15\n"
                "Hereditary,Ari Aster,2017-06-05,5\n"
                "1917,Sam Mendes,2018-04-10,10\n"
                "The Revenant,Alejandro Inarritu,2014-10-11,11"
            ),
        },
        {
            "statement": 'Filter the catalog table to keep only movies whose release_date falls in a summer month (June, July, or August — months 6, 7, or 8).',
            "solution_code": 'catalog[pd.to_datetime(catalog["release_date"]).dt.month.isin([6, 7, 8])]',
            "hint": 'Extract the month with pd.to_datetime().dt.month and use .isin([6, 7, 8]) to filter.',
            "category": 'dt-accessor',
            "tables": [
                {
                    "name": 'catalog',
                    "csv": (
                        "title,release_date\n"
                        "Jaws,1975-06-20\n"
                        "Star Wars,1977-05-25\n"
                        "Alien,1979-05-25\n"
                        "Raiders of the Lost Ark,1981-06-12\n"
                        "Back to the Future,1985-07-03\n"
                        "Top Gun,1986-05-16"
                    ),
                },
            ],
            "expected_csv": (
                "title,release_date\n"
                "Jaws,1975-06-20\n"
                "Raiders of the Lost Ark,1981-06-12\n"
                "Back to the Future,1985-07-03"
            ),
        },
        {
            "statement": 'Add a shoot_days column to the shoots table showing the number of days between start_date and end_date.',
            "solution_code": 'shoots.assign(shoot_days=(pd.to_datetime(shoots["end_date"]) - pd.to_datetime(shoots["start_date"])).dt.days)',
            "hint": 'Subtract two pd.to_datetime() columns to get a Timedelta Series, then use .dt.days to extract the integer count.',
            "category": 'timedelta',
            "tables": [
                {
                    "name": 'shoots',
                    "csv": (
                        "title,start_date,end_date\n"
                        "Titanic,1995-09-08,1997-03-23\n"
                        "The Revenant,2014-10-15,2015-08-20\n"
                        "Dunkirk,2016-05-23,2016-12-10\n"
                        "Mad Max Fury Road,2012-07-05,2013-12-01\n"
                        "Interstellar,2013-08-06,2014-01-24"
                    ),
                },
            ],
            "expected_csv": (
                "title,start_date,end_date,shoot_days\n"
                "Titanic,1995-09-08,1997-03-23,562\n"
                "The Revenant,2014-10-15,2015-08-20,309\n"
                "Dunkirk,2016-05-23,2016-12-10,201\n"
                "Mad Max Fury Road,2012-07-05,2013-12-01,514\n"
                "Interstellar,2013-08-06,2014-01-24,171"
            ),
        },
        {
            "statement": 'Add a days_to_us_release column to the releases table showing how many days elapsed between the festival_date and the us_release_date.',
            "solution_code": 'releases.assign(days_to_us_release=(pd.to_datetime(releases["us_release_date"]) - pd.to_datetime(releases["festival_date"])).dt.days)',
            "hint": 'Subtract pd.to_datetime(festival_date) from pd.to_datetime(us_release_date), then use .dt.days.',
            "category": 'timedelta',
            "tables": [
                {
                    "name": 'releases',
                    "csv": (
                        "title,festival_date,us_release_date\n"
                        "Parasite,2019-05-21,2019-10-11\n"
                        "La La Land,2016-08-31,2016-12-09\n"
                        "The Shape of Water,2017-08-31,2017-12-08\n"
                        "Nomadland,2020-09-11,2021-02-19\n"
                        "Everything Everywhere All at Once,2022-03-08,2022-03-25"
                    ),
                },
            ],
            "expected_csv": (
                "title,festival_date,us_release_date,days_to_us_release\n"
                "Parasite,2019-05-21,2019-10-11,143\n"
                "La La Land,2016-08-31,2016-12-09,100\n"
                "The Shape of Water,2017-08-31,2017-12-08,99\n"
                "Nomadland,2020-09-11,2021-02-19,161\n"
                "Everything Everywhere All at Once,2022-03-08,2022-03-25,17"
            ),
        },
        {
            "statement": 'Add a wide_release_date column to the openings table that is 14 days after the limited_release_date.',
            "solution_code": 'openings.assign(wide_release_date=pd.to_datetime(openings["limited_release_date"]) + pd.Timedelta(days=14))',
            "hint": 'Convert the date column with pd.to_datetime() and add pd.Timedelta(days=14) to shift each date forward two weeks.',
            "category": 'timedelta',
            "tables": [
                {
                    "name": 'openings',
                    "csv": (
                        "title,limited_release_date\n"
                        "Moonlight,2016-10-21\n"
                        "Birdman,2014-10-17\n"
                        "Whiplash,2014-10-10\n"
                        "Spotlight,2015-11-06\n"
                        "The Artist,2011-11-25"
                    ),
                },
            ],
            "expected_csv": (
                "title,limited_release_date,wide_release_date\n"
                "Moonlight,2016-10-21,2016-11-04\n"
                "Birdman,2014-10-17,2014-10-31\n"
                "Whiplash,2014-10-10,2014-10-24\n"
                "Spotlight,2015-11-06,2015-11-20\n"
                "The Artist,2011-11-25,2011-12-09"
            ),
        },
    ],
    14: [
        {
            "statement": "Add a column 'rolling_mean' to the 'daily' table with the 2-day rolling mean of 'revenue' for Avatar: The Way of Water.",
            "solution_code": 'daily.assign(rolling_mean=daily["revenue"].rolling(2).mean())',
            "hint": 'Use .rolling(2).mean() and assign it as a new column. The first row will be NaN.',
            "category": 'rolling-mean',
            "tables": [
                {
                    "name": 'daily',
                    "csv": (
                        "date,movie,revenue\n"
                        "2022-12-16,Avatar: The Way of Water,100\n"
                        "2022-12-17,Avatar: The Way of Water,80\n"
                        "2022-12-18,Avatar: The Way of Water,60\n"
                        "2022-12-19,Avatar: The Way of Water,40\n"
                        "2022-12-20,Avatar: The Way of Water,20"
                    ),
                },
            ],
            "expected_csv": (
                "date,movie,revenue,rolling_mean\n"
                "2022-12-16,Avatar: The Way of Water,100,\n"
                "2022-12-17,Avatar: The Way of Water,80,90.0\n"
                "2022-12-18,Avatar: The Way of Water,60,70.0\n"
                "2022-12-19,Avatar: The Way of Water,40,50.0\n"
                "2022-12-20,Avatar: The Way of Water,20,30.0"
            ),
        },
        {
            "statement": "Add a column 'rolling_mean' to the 'sales' table with the 3-day rolling mean of 'tickets' for Top Gun: Maverick.",
            "solution_code": 'sales.assign(rolling_mean=sales["tickets"].rolling(3).mean())',
            "hint": 'With a window of 3, the first two rows will be NaN.',
            "category": 'rolling-mean',
            "tables": [
                {
                    "name": 'sales',
                    "csv": (
                        "date,movie,tickets\n"
                        "2022-05-27,Top Gun: Maverick,90\n"
                        "2022-05-28,Top Gun: Maverick,120\n"
                        "2022-05-29,Top Gun: Maverick,150\n"
                        "2022-05-30,Top Gun: Maverick,180\n"
                        "2022-05-31,Top Gun: Maverick,210"
                    ),
                },
            ],
            "expected_csv": (
                "date,movie,tickets,rolling_mean\n"
                "2022-05-27,Top Gun: Maverick,90,\n"
                "2022-05-28,Top Gun: Maverick,120,\n"
                "2022-05-29,Top Gun: Maverick,150,120.0\n"
                "2022-05-30,Top Gun: Maverick,180,150.0\n"
                "2022-05-31,Top Gun: Maverick,210,180.0"
            ),
        },
        {
            "statement": "Add a column 'rolling_mean' to the 'weekly' table with the 2-week rolling mean of 'gross' for Oppenheimer.",
            "solution_code": 'weekly.assign(rolling_mean=weekly["gross"].rolling(2).mean())',
            "hint": 'Use .rolling(2).mean(). Only the first row will be NaN.',
            "category": 'rolling-mean',
            "tables": [
                {
                    "name": 'weekly',
                    "csv": (
                        "week,movie,gross\n"
                        "2023-W30,Oppenheimer,200\n"
                        "2023-W31,Oppenheimer,400\n"
                        "2023-W32,Oppenheimer,300\n"
                        "2023-W33,Oppenheimer,500\n"
                        "2023-W34,Oppenheimer,600"
                    ),
                },
            ],
            "expected_csv": (
                "week,movie,gross,rolling_mean\n"
                "2023-W30,Oppenheimer,200,\n"
                "2023-W31,Oppenheimer,400,300.0\n"
                "2023-W32,Oppenheimer,300,350.0\n"
                "2023-W33,Oppenheimer,500,400.0\n"
                "2023-W34,Oppenheimer,600,550.0"
            ),
        },
        {
            "statement": "Add a column 'rolling_sum' to the 'daily' table with the 2-day rolling sum of 'revenue' for Barbie.",
            "solution_code": 'daily.assign(rolling_sum=daily["revenue"].rolling(2).sum())',
            "hint": 'Use .rolling(2).sum(). The first row will be NaN.',
            "category": 'rolling-sum',
            "tables": [
                {
                    "name": 'daily',
                    "csv": (
                        "date,movie,revenue\n"
                        "2023-07-21,Barbie,300\n"
                        "2023-07-22,Barbie,500\n"
                        "2023-07-23,Barbie,400\n"
                        "2023-07-24,Barbie,600\n"
                        "2023-07-25,Barbie,700"
                    ),
                },
            ],
            "expected_csv": (
                "date,movie,revenue,rolling_sum\n"
                "2023-07-21,Barbie,300,\n"
                "2023-07-22,Barbie,500,800.0\n"
                "2023-07-23,Barbie,400,900.0\n"
                "2023-07-24,Barbie,600,1000.0\n"
                "2023-07-25,Barbie,700,1300.0"
            ),
        },
        {
            "statement": "Add a column 'rolling_sum' to the 'sales' table with the 3-day rolling sum of 'tickets' for The Dark Knight.",
            "solution_code": 'sales.assign(rolling_sum=sales["tickets"].rolling(3).sum())',
            "hint": 'With a window of 3, the first two rows will be NaN.',
            "category": 'rolling-sum',
            "tables": [
                {
                    "name": 'sales',
                    "csv": (
                        "date,movie,tickets\n"
                        "2008-07-18,The Dark Knight,100\n"
                        "2008-07-19,The Dark Knight,200\n"
                        "2008-07-20,The Dark Knight,300\n"
                        "2008-07-21,The Dark Knight,400\n"
                        "2008-07-22,The Dark Knight,500\n"
                        "2008-07-23,The Dark Knight,600"
                    ),
                },
            ],
            "expected_csv": (
                "date,movie,tickets,rolling_sum\n"
                "2008-07-18,The Dark Knight,100,\n"
                "2008-07-19,The Dark Knight,200,\n"
                "2008-07-20,The Dark Knight,300,600.0\n"
                "2008-07-21,The Dark Knight,400,900.0\n"
                "2008-07-22,The Dark Knight,500,1200.0\n"
                "2008-07-23,The Dark Knight,600,1500.0"
            ),
        },
        {
            "statement": "Resample the 'box_office' table by week ('W') and compute the total weekly 'revenue' for Barbie. The table has a 'date' column with daily entries.",
            "solution_code": 'box_office.set_index(pd.to_datetime(box_office["date"])).drop(columns="date").resample("W").sum().reset_index()',
            "hint": "Set the DatetimeIndex with .set_index(pd.to_datetime(...)), drop the original date column, then use .resample('W').sum().",
            "category": 'resample',
            "tables": [
                {
                    "name": 'box_office',
                    "csv": (
                        "date,revenue\n"
                        "2023-07-01,400\n"
                        "2023-07-02,600\n"
                        "2023-07-05,500\n"
                        "2023-07-08,300\n"
                        "2023-07-10,700\n"
                        "2023-07-14,800"
                    ),
                },
            ],
            "expected_csv": (
                "date,revenue\n"
                "2023-07-02,1000\n"
                "2023-07-09,800\n"
                "2023-07-16,1500"
            ),
        },
        {
            "statement": "Resample the 'ticket_data' table by week ('W') and compute the mean weekly 'tickets' sold for Spider-Man: No Way Home.",
            "solution_code": 'ticket_data.set_index(pd.to_datetime(ticket_data["date"])).drop(columns="date").resample("W").mean().reset_index()',
            "hint": "Use .resample('W').mean() after setting the DatetimeIndex.",
            "category": 'resample',
            "tables": [
                {
                    "name": 'ticket_data',
                    "csv": (
                        "date,tickets\n"
                        "2021-12-18,200\n"
                        "2021-12-19,400\n"
                        "2021-12-20,300\n"
                        "2021-12-25,500\n"
                        "2021-12-26,700\n"
                        "2021-12-27,600"
                    ),
                },
            ],
            "expected_csv": (
                "date,tickets\n"
                "2021-12-19,300.0\n"
                "2021-12-26,500.0\n"
                "2022-01-02,600.0"
            ),
        },
        {
            "statement": "Resample the 'monthly' table by month end ('ME') and compute the total monthly 'revenue' for Oppenheimer.",
            "solution_code": 'monthly.set_index(pd.to_datetime(monthly["date"])).drop(columns="date").resample("ME").sum().reset_index()',
            "hint": "Use .resample('ME').sum() to aggregate by month end.",
            "category": 'resample',
            "tables": [
                {
                    "name": 'monthly',
                    "csv": (
                        "date,revenue\n"
                        "2023-06-05,500\n"
                        "2023-06-15,800\n"
                        "2023-06-28,600\n"
                        "2023-07-05,700\n"
                        "2023-07-20,900\n"
                        "2023-07-28,400"
                    ),
                },
            ],
            "expected_csv": (
                "date,revenue\n"
                "2023-06-30,1900\n"
                "2023-07-31,2000"
            ),
        },
        {
            "statement": "Resample the 'sales' table by month end ('ME') and compute the mean monthly 'tickets' for Interstellar.",
            "solution_code": 'sales.set_index(pd.to_datetime(sales["date"])).drop(columns="date").resample("ME").mean().reset_index()',
            "hint": "Use .resample('ME').mean() to get the monthly average.",
            "category": 'resample',
            "tables": [
                {
                    "name": 'sales',
                    "csv": (
                        "date,tickets\n"
                        "2014-11-07,600\n"
                        "2014-11-21,400\n"
                        "2014-12-05,800\n"
                        "2014-12-19,600\n"
                        "2015-01-09,400\n"
                        "2015-01-23,200"
                    ),
                },
            ],
            "expected_csv": (
                "date,tickets\n"
                "2014-11-30,500.0\n"
                "2014-12-31,700.0\n"
                "2015-01-31,300.0"
            ),
        },
        {
            "statement": "Resample the 'grossing' table by month end ('ME') and compute the total monthly 'gross' for The Dark Knight Rises.",
            "solution_code": 'grossing.set_index(pd.to_datetime(grossing["date"])).drop(columns="date").resample("ME").sum().reset_index()',
            "hint": "Use .resample('ME').sum() after creating the DatetimeIndex.",
            "category": 'resample',
            "tables": [
                {
                    "name": 'grossing',
                    "csv": (
                        "date,gross\n"
                        "2012-07-20,2000\n"
                        "2012-07-21,1500\n"
                        "2012-07-27,1200\n"
                        "2012-07-28,900\n"
                        "2012-08-03,700\n"
                        "2012-08-10,500\n"
                        "2012-08-17,400"
                    ),
                },
            ],
            "expected_csv": (
                "date,gross\n"
                "2012-07-31,5600\n"
                "2012-08-31,1600"
            ),
        },
    ],
    15: [
        {
            "statement": 'Pivot the box_office table so each region becomes a column showing revenue, indexed by movie title.',
            "solution_code": 'box_office.pivot(index="title", columns="region", values="revenue").reset_index().rename_axis(None, axis=1)',
            "hint": "Use df.pivot(index='title', columns='region', values='revenue') then .reset_index().rename_axis(None, axis=1).",
            "category": 'pivot',
            "tables": [
                {
                    "name": 'box_office',
                    "csv": (
                        "title,region,revenue\n"
                        "Inception,Asia,287\n"
                        "Inception,Europe,453\n"
                        "Inception,US,836\n"
                        "The Dark Knight,Asia,395\n"
                        "The Dark Knight,Europe,522\n"
                        "The Dark Knight,US,1004\n"
                        "Interstellar,Asia,312\n"
                        "Interstellar,Europe,441\n"
                        "Interstellar,US,675"
                    ),
                },
            ],
            "expected_csv": (
                "title,Asia,Europe,US\n"
                "Inception,287,453,836\n"
                "Interstellar,312,441,675\n"
                "The Dark Knight,395,522,1004"
            ),
        },
        {
            "statement": 'Pivot the critic_scores table so each critic becomes a column showing their score, indexed by movie title.',
            "solution_code": 'critic_scores.pivot(index="title", columns="critic", values="score").reset_index().rename_axis(None, axis=1)',
            "hint": "Use df.pivot(index='title', columns='critic', values='score') then .reset_index().rename_axis(None, axis=1).",
            "category": 'pivot',
            "tables": [
                {
                    "name": 'critic_scores',
                    "csv": (
                        "title,critic,score\n"
                        "Avatar,Ebert,8\n"
                        "Avatar,Kermode,7\n"
                        "Avatar,Travers,9\n"
                        "Titanic,Ebert,9\n"
                        "Titanic,Kermode,8\n"
                        "Titanic,Travers,10\n"
                        "Gladiator,Ebert,8\n"
                        "Gladiator,Kermode,9\n"
                        "Gladiator,Travers,7"
                    ),
                },
            ],
            "expected_csv": (
                "title,Ebert,Kermode,Travers\n"
                "Avatar,8,7,9\n"
                "Gladiator,8,9,7\n"
                "Titanic,9,8,10"
            ),
        },
        {
            "statement": 'Pivot the seasonal_revenue table so each season becomes a column showing revenue, indexed by movie title.',
            "solution_code": 'seasonal_revenue.pivot(index="title", columns="season", values="revenue").reset_index().rename_axis(None, axis=1)',
            "hint": "Use df.pivot(index='title', columns='season', values='revenue') then .reset_index().rename_axis(None, axis=1).",
            "category": 'pivot',
            "tables": [
                {
                    "name": 'seasonal_revenue',
                    "csv": (
                        "title,season,revenue\n"
                        "Avengers Endgame,Spring,852\n"
                        "Avengers Endgame,Summer,1203\n"
                        "Avengers Endgame,Fall,441\n"
                        "Spider-Man No Way Home,Spring,612\n"
                        "Spider-Man No Way Home,Summer,987\n"
                        "Spider-Man No Way Home,Fall,734\n"
                        "Top Gun Maverick,Spring,723\n"
                        "Top Gun Maverick,Summer,1109\n"
                        "Top Gun Maverick,Fall,312"
                    ),
                },
            ],
            "expected_csv": (
                "title,Fall,Spring,Summer\n"
                "Avengers Endgame,441,852,1203\n"
                "Spider-Man No Way Home,734,612,987\n"
                "Top Gun Maverick,312,723,1109"
            ),
        },
        {
            "statement": 'Pivot the platform_revenue table so each distribution platform becomes a column showing revenue, indexed by movie title.',
            "solution_code": 'platform_revenue.pivot(index="title", columns="platform", values="revenue").reset_index().rename_axis(None, axis=1)',
            "hint": "Use df.pivot(index='title', columns='platform', values='revenue') then .reset_index().rename_axis(None, axis=1).",
            "category": 'pivot',
            "tables": [
                {
                    "name": 'platform_revenue',
                    "csv": (
                        "title,platform,revenue\n"
                        "The Batman,Digital,145\n"
                        "The Batman,Physical,89\n"
                        "The Batman,Streaming,210\n"
                        "No Time to Die,Digital,178\n"
                        "No Time to Die,Physical,134\n"
                        "No Time to Die,Streaming,95\n"
                        "Dune,Digital,163\n"
                        "Dune,Physical,112\n"
                        "Dune,Streaming,187"
                    ),
                },
            ],
            "expected_csv": (
                "title,Digital,Physical,Streaming\n"
                "Dune,163,112,187\n"
                "No Time to Die,178,134,95\n"
                "The Batman,145,89,210"
            ),
        },
        {
            "statement": 'Pivot the award_wins table so each award category becomes a column showing wins, indexed by movie title.',
            "solution_code": 'award_wins.pivot(index="title", columns="category", values="wins").reset_index().rename_axis(None, axis=1)',
            "hint": "Use df.pivot(index='title', columns='category', values='wins') then .reset_index().rename_axis(None, axis=1).",
            "category": 'pivot',
            "tables": [
                {
                    "name": 'award_wins',
                    "csv": (
                        "title,category,wins\n"
                        "The Shape of Water,Actor,0\n"
                        "The Shape of Water,Director,1\n"
                        "The Shape of Water,Picture,1\n"
                        "Parasite,Actor,0\n"
                        "Parasite,Director,1\n"
                        "Parasite,Picture,1\n"
                        "CODA,Actor,1\n"
                        "CODA,Director,0\n"
                        "CODA,Picture,1"
                    ),
                },
            ],
            "expected_csv": (
                "title,Actor,Director,Picture\n"
                "CODA,1,0,1\n"
                "Parasite,0,1,1\n"
                "The Shape of Water,0,1,1"
            ),
        },
        {
            "statement": 'Melt the wide_box_office table from wide format (one column per region) into long format with columns title, region, and revenue.',
            "solution_code": 'wide_box_office.melt(id_vars=["title"], value_vars=["US","Europe","Asia"], var_name="region", value_name="revenue")',
            "hint": "Use df.melt(id_vars=['title'], value_vars=['US','Europe','Asia'], var_name='region', value_name='revenue').",
            "category": 'melt',
            "tables": [
                {
                    "name": 'wide_box_office',
                    "csv": (
                        "title,US,Europe,Asia\n"
                        "Inception,836,453,287\n"
                        "The Dark Knight,1004,522,395\n"
                        "Interstellar,675,441,312"
                    ),
                },
            ],
            "expected_csv": (
                "title,region,revenue\n"
                "Inception,US,836\n"
                "The Dark Knight,US,1004\n"
                "Interstellar,US,675\n"
                "Inception,Europe,453\n"
                "The Dark Knight,Europe,522\n"
                "Interstellar,Europe,441\n"
                "Inception,Asia,287\n"
                "The Dark Knight,Asia,395\n"
                "Interstellar,Asia,312"
            ),
        },
        {
            "statement": 'Melt the quarterly_revenue table from wide format (one column per quarter) into long format with columns title, quarter, and revenue.',
            "solution_code": 'quarterly_revenue.melt(id_vars=["title"], value_vars=["Q1","Q2","Q3","Q4"], var_name="quarter", value_name="revenue")',
            "hint": "Use df.melt(id_vars=['title'], value_vars=['Q1','Q2','Q3','Q4'], var_name='quarter', value_name='revenue').",
            "category": 'melt',
            "tables": [
                {
                    "name": 'quarterly_revenue',
                    "csv": (
                        "title,Q1,Q2,Q3,Q4\n"
                        "Avengers Endgame,412,1203,387,241\n"
                        "Spider-Man No Way Home,289,987,456,312\n"
                        "Top Gun Maverick,198,1109,523,287"
                    ),
                },
            ],
            "expected_csv": (
                "title,quarter,revenue\n"
                "Avengers Endgame,Q1,412\n"
                "Spider-Man No Way Home,Q1,289\n"
                "Top Gun Maverick,Q1,198\n"
                "Avengers Endgame,Q2,1203\n"
                "Spider-Man No Way Home,Q2,987\n"
                "Top Gun Maverick,Q2,1109\n"
                "Avengers Endgame,Q3,387\n"
                "Spider-Man No Way Home,Q3,456\n"
                "Top Gun Maverick,Q3,523\n"
                "Avengers Endgame,Q4,241\n"
                "Spider-Man No Way Home,Q4,312\n"
                "Top Gun Maverick,Q4,287"
            ),
        },
        {
            "statement": 'Melt the wide_critic_scores table from wide format (one column per critic) into long format with columns title, critic, and score.',
            "solution_code": 'wide_critic_scores.melt(id_vars=["title"], value_vars=["Ebert","Kermode","Travers"], var_name="critic", value_name="score")',
            "hint": "Use df.melt(id_vars=['title'], value_vars=[...], var_name='critic', value_name='score').",
            "category": 'melt',
            "tables": [
                {
                    "name": 'wide_critic_scores',
                    "csv": (
                        "title,Ebert,Kermode,Travers\n"
                        "Avatar,8,7,9\n"
                        "Titanic,9,8,10\n"
                        "Gladiator,8,9,7"
                    ),
                },
            ],
            "expected_csv": (
                "title,critic,score\n"
                "Avatar,Ebert,8\n"
                "Titanic,Ebert,9\n"
                "Gladiator,Ebert,8\n"
                "Avatar,Kermode,7\n"
                "Titanic,Kermode,8\n"
                "Gladiator,Kermode,9\n"
                "Avatar,Travers,9\n"
                "Titanic,Travers,10\n"
                "Gladiator,Travers,7"
            ),
        },
        {
            "statement": 'Melt the wide_platform_revenue table from wide format (one column per platform) into long format with columns title, platform, and revenue.',
            "solution_code": 'wide_platform_revenue.melt(id_vars=["title"], value_vars=["Digital","Physical","Streaming"], var_name="platform", value_name="revenue")',
            "hint": "Use df.melt(id_vars=['title'], value_vars=[...], var_name='platform', value_name='revenue').",
            "category": 'melt',
            "tables": [
                {
                    "name": 'wide_platform_revenue',
                    "csv": (
                        "title,Digital,Physical,Streaming\n"
                        "The Batman,145,89,210\n"
                        "No Time to Die,178,134,95\n"
                        "Dune,163,112,187"
                    ),
                },
            ],
            "expected_csv": (
                "title,platform,revenue\n"
                "The Batman,Digital,145\n"
                "No Time to Die,Digital,178\n"
                "Dune,Digital,163\n"
                "The Batman,Physical,89\n"
                "No Time to Die,Physical,134\n"
                "Dune,Physical,112\n"
                "The Batman,Streaming,210\n"
                "No Time to Die,Streaming,95\n"
                "Dune,Streaming,187"
            ),
        },
        {
            "statement": 'Melt the wide_award_wins table from wide format (one column per award category) into long format with columns title, category, and wins.',
            "solution_code": 'wide_award_wins.melt(id_vars=["title"], value_vars=["Actor","Director","Picture"], var_name="category", value_name="wins")',
            "hint": "Use df.melt(id_vars=['title'], value_vars=[...], var_name='category', value_name='wins').",
            "category": 'melt',
            "tables": [
                {
                    "name": 'wide_award_wins',
                    "csv": (
                        "title,Actor,Director,Picture\n"
                        "CODA,1,0,1\n"
                        "Parasite,0,1,1\n"
                        "The Shape of Water,0,1,1"
                    ),
                },
            ],
            "expected_csv": (
                "title,category,wins\n"
                "CODA,Actor,1\n"
                "Parasite,Actor,0\n"
                "The Shape of Water,Actor,0\n"
                "CODA,Director,0\n"
                "Parasite,Director,1\n"
                "The Shape of Water,Director,1\n"
                "CODA,Picture,1\n"
                "Parasite,Picture,1\n"
                "The Shape of Water,Picture,1"
            ),
        },
    ],
    16: [
        {
            "statement": 'Create a pivot table showing the average IMDb rating by decade and genre from the classics table.',
            "solution_code": 'classics.pivot_table(index="decade", columns="genre", values="rating", aggfunc="mean").reset_index().rename_axis(None, axis=1)',
            "hint": "Use pivot_table with aggfunc='mean', then reset_index().rename_axis(None, axis=1).",
            "category": 'pivot-table',
            "tables": [
                {
                    "name": 'classics',
                    "csv": (
                        "title,genre,decade,rating\n"
                        "The Godfather,Drama,1970s,9.2\n"
                        "Chinatown,Drama,1970s,8.2\n"
                        "Star Wars,Sci-Fi,1970s,8.6\n"
                        "Alien,Sci-Fi,1970s,8.4\n"
                        "Raging Bull,Drama,1980s,8.2\n"
                        "Goodfellas,Drama,1980s,8.7\n"
                        "The Terminator,Sci-Fi,1980s,8.0\n"
                        "Blade Runner,Sci-Fi,1980s,8.1"
                    ),
                },
            ],
            "expected_csv": (
                "decade,Drama,Sci-Fi\n"
                "1970s,8.7,8.5\n"
                "1980s,8.45,8.05"
            ),
        },
        {
            "statement": 'Create a pivot table showing the total box office gross (in millions) by studio and genre from the revenues table.',
            "solution_code": 'revenues.pivot_table(index="studio", columns="genre", values="gross_m", aggfunc="sum").reset_index().rename_axis(None, axis=1)',
            "hint": "Use pivot_table with aggfunc='sum', then reset_index().rename_axis(None, axis=1).",
            "category": 'pivot-table',
            "tables": [
                {
                    "name": 'revenues',
                    "csv": (
                        "title,studio,genre,gross_m\n"
                        "Avengers: Endgame,Disney,Action,2798\n"
                        "Home Alone,Disney,Comedy,476\n"
                        "Mission: Impossible,Paramount,Action,790\n"
                        "Grease,Paramount,Comedy,396\n"
                        "Jurassic Park,Universal,Action,1030\n"
                        "Bridesmaids,Universal,Comedy,288\n"
                        "The Dark Knight,Warner,Action,1005\n"
                        "The Hangover,Warner,Comedy,467"
                    ),
                },
            ],
            "expected_csv": (
                "studio,Action,Comedy\n"
                "Disney,2798,476\n"
                "Paramount,790,396\n"
                "Universal,1030,288\n"
                "Warner,1005,467"
            ),
        },
        {
            "statement": 'Create a pivot table showing the count of films per lead actor and genre from the filmography table.',
            "solution_code": 'filmography.pivot_table(index="actor", columns="genre", values="title", aggfunc="count").reset_index().rename_axis(None, axis=1)',
            "hint": "Use pivot_table with aggfunc='count' and values='title', then reset_index().rename_axis(None, axis=1).",
            "category": 'pivot-table',
            "tables": [
                {
                    "name": 'filmography',
                    "csv": (
                        "title,actor,genre\n"
                        "The Godfather,Al Pacino,Drama\n"
                        "Scarface,Al Pacino,Drama\n"
                        "Heat,Al Pacino,Thriller\n"
                        "Raging Bull,Robert De Niro,Drama\n"
                        "Goodfellas,Robert De Niro,Drama\n"
                        "Cape Fear,Robert De Niro,Thriller\n"
                        "Philadelphia,Tom Hanks,Drama\n"
                        "Cast Away,Tom Hanks,Thriller"
                    ),
                },
            ],
            "expected_csv": (
                "actor,Drama,Thriller\n"
                "Al Pacino,2,1\n"
                "Robert De Niro,2,1\n"
                "Tom Hanks,1,1"
            ),
        },
        {
            "statement": 'Create a pivot table showing the average Rotten Tomatoes score by decade and director from the directors table.',
            "solution_code": 'directors.pivot_table(index="decade", columns="director", values="rt_score", aggfunc="mean").reset_index().rename_axis(None, axis=1)',
            "hint": "Use pivot_table with aggfunc='mean', then reset_index().rename_axis(None, axis=1).",
            "category": 'pivot-table',
            "tables": [
                {
                    "name": 'directors',
                    "csv": (
                        "title,director,decade,rt_score\n"
                        "Jaws,Spielberg,1970s,98\n"
                        "Close Encounters,Spielberg,1970s,96\n"
                        "Annie Hall,Woody Allen,1970s,97\n"
                        "Manhattan,Woody Allen,1970s,93\n"
                        "E.T.,Spielberg,1980s,99\n"
                        "Indiana Jones,Spielberg,1980s,85\n"
                        "Hannah and Her Sisters,Woody Allen,1980s,94\n"
                        "Crimes and Misdemeanors,Woody Allen,1980s,88"
                    ),
                },
            ],
            "expected_csv": (
                "decade,Spielberg,Woody Allen\n"
                "1970s,97.0,95.0\n"
                "1980s,92.0,91.0"
            ),
        },
        {
            "statement": 'Create a pivot table showing the total Oscar wins by decade and studio from the oscars table.',
            "solution_code": 'oscars.pivot_table(index="decade", columns="studio", values="wins", aggfunc="sum").reset_index().rename_axis(None, axis=1)',
            "hint": "Use pivot_table with aggfunc='sum', then reset_index().rename_axis(None, axis=1).",
            "category": 'pivot-table',
            "tables": [
                {
                    "name": 'oscars',
                    "csv": (
                        "film,studio,decade,wins\n"
                        "The Godfather,Paramount,1970s,3\n"
                        "Chinatown,Paramount,1970s,0\n"
                        "Annie Hall,UA,1970s,4\n"
                        "Rocky,UA,1970s,3\n"
                        "Ordinary People,Paramount,1980s,4\n"
                        "Terms of Endearment,Paramount,1980s,5\n"
                        "Rain Man,UA,1980s,4\n"
                        "Platoon,UA,1980s,4"
                    ),
                },
            ],
            "expected_csv": (
                "decade,Paramount,UA\n"
                "1970s,3,7\n"
                "1980s,9,8"
            ),
        },
        {
            "statement": 'Create a crosstab showing how many films fall into each combination of genre and rating category from the catalog table.',
            "solution_code": 'pd.crosstab(catalog["genre"], catalog["rating_cat"]).reset_index().rename_axis(None, axis=1)',
            "hint": "Use pd.crosstab(df['col1'], df['col2']), then reset_index().rename_axis(None, axis=1).",
            "category": 'crosstab',
            "tables": [
                {
                    "name": 'catalog',
                    "csv": (
                        "title,genre,rating_cat\n"
                        "The Shawshank Redemption,Drama,Excellent\n"
                        "Schindler's List,Drama,Excellent\n"
                        "Forrest Gump,Drama,Good\n"
                        "Die Hard,Action,Good\n"
                        "Speed,Action,Good\n"
                        "Con Air,Action,Average\n"
                        "Ace Ventura,Comedy,Good\n"
                        "Dumb and Dumber,Comedy,Average"
                    ),
                },
            ],
            "expected_csv": (
                "genre,Average,Excellent,Good\n"
                "Action,1,0,2\n"
                "Comedy,1,0,1\n"
                "Drama,0,2,1"
            ),
        },
        {
            "statement": 'Create a crosstab showing how many films each studio produced per decade from the productions table.',
            "solution_code": 'pd.crosstab(productions["studio"], productions["decade"]).reset_index().rename_axis(None, axis=1)',
            "hint": "Use pd.crosstab(df['col1'], df['col2']), then reset_index().rename_axis(None, axis=1).",
            "category": 'crosstab',
            "tables": [
                {
                    "name": 'productions',
                    "csv": (
                        "title,studio,decade\n"
                        "The Dark Knight,Warner,2000s\n"
                        "Inception,Warner,2010s\n"
                        "Dunkirk,Warner,2010s\n"
                        "Iron Man,Marvel,2000s\n"
                        "Thor,Marvel,2010s\n"
                        "Captain America,Marvel,2010s\n"
                        "Ratatouille,Pixar,2000s\n"
                        "WALL-E,Pixar,2000s"
                    ),
                },
            ],
            "expected_csv": (
                "studio,2000s,2010s\n"
                "Marvel,1,2\n"
                "Pixar,2,0\n"
                "Warner,1,2"
            ),
        },
        {
            "statement": 'Create a crosstab showing how many roles each actor played per genre from the roles table.',
            "solution_code": 'pd.crosstab(roles["actor"], roles["genre"]).reset_index().rename_axis(None, axis=1)',
            "hint": "Use pd.crosstab(df['col1'], df['col2']), then reset_index().rename_axis(None, axis=1).",
            "category": 'crosstab',
            "tables": [
                {
                    "name": 'roles',
                    "csv": (
                        "film,actor,genre\n"
                        "The Revenant,Leonardo DiCaprio,Drama\n"
                        "Django Unchained,Leonardo DiCaprio,Western\n"
                        "The Wolf of Wall Street,Leonardo DiCaprio,Drama\n"
                        "There Will Be Blood,Daniel Day-Lewis,Drama\n"
                        "Lincoln,Daniel Day-Lewis,Drama\n"
                        "Gangs of New York,Daniel Day-Lewis,Western\n"
                        "No Country for Old Men,Javier Bardem,Thriller\n"
                        "Skyfall,Javier Bardem,Thriller"
                    ),
                },
            ],
            "expected_csv": (
                "actor,Drama,Thriller,Western\n"
                "Daniel Day-Lewis,2,0,1\n"
                "Javier Bardem,0,2,0\n"
                "Leonardo DiCaprio,2,0,1"
            ),
        },
        {
            "statement": "Create a crosstab showing the total budget (in millions) by studio and genre from the budgets table using values and aggfunc='sum'.",
            "solution_code": 'pd.crosstab(budgets["studio"], budgets["genre"], values=budgets["budget_m"], aggfunc="sum").reset_index().rename_axis(None, axis=1)',
            "hint": 'Use pd.crosstab with the values= and aggfunc= parameters, then reset_index().rename_axis(None, axis=1).',
            "category": 'crosstab',
            "tables": [
                {
                    "name": 'budgets',
                    "csv": (
                        "film,studio,genre,budget_m\n"
                        "Avatar,Fox,Sci-Fi,237\n"
                        "Bohemian Rhapsody,Fox,Drama,52\n"
                        "Gravity,Warner,Sci-Fi,100\n"
                        "Joker,Warner,Drama,55\n"
                        "Interstellar,Paramount,Sci-Fi,165\n"
                        "A Quiet Place,Paramount,Drama,17\n"
                        "Dune,Legendary,Sci-Fi,165\n"
                        "Oppenheimer,Legendary,Drama,100"
                    ),
                },
            ],
            "expected_csv": (
                "studio,Drama,Sci-Fi\n"
                "Fox,52.0,237.0\n"
                "Legendary,100.0,165.0\n"
                "Paramount,17.0,165.0\n"
                "Warner,55.0,100.0"
            ),
        },
        {
            "statement": 'Create a crosstab showing how many films each actress appeared in per rating certificate from the femme_leads table.',
            "solution_code": 'pd.crosstab(femme_leads["actress"], femme_leads["certificate"]).reset_index().rename_axis(None, axis=1)',
            "hint": "Use pd.crosstab(df['col1'], df['col2']), then reset_index().rename_axis(None, axis=1).",
            "category": 'crosstab',
            "tables": [
                {
                    "name": 'femme_leads',
                    "csv": (
                        "film,actress,certificate\n"
                        "Erin Brockovich,Julia Roberts,PG-13\n"
                        "Pretty Woman,Julia Roberts,R\n"
                        "My Best Friend's Wedding,Julia Roberts,PG-13\n"
                        "Monster,Charlize Theron,R\n"
                        "Mad Max: Fury Road,Charlize Theron,R\n"
                        "Bombshell,Charlize Theron,R\n"
                        "La La Land,Emma Stone,PG-13\n"
                        "Easy A,Emma Stone,PG-13"
                    ),
                },
            ],
            "expected_csv": (
                "actress,PG-13,R\n"
                "Charlize Theron,0,3\n"
                "Emma Stone,2,0\n"
                "Julia Roberts,2,1"
            ),
        },
    ],
    17: [
        {
            "statement": "Add a 'rank' column that ranks the movies by revenue_m from highest to lowest (rank 1 = highest) in the worldwide_gross table.",
            "solution_code": 'worldwide_gross.assign(rank=worldwide_gross["revenue_m"].rank(ascending=False))',
            "hint": "Use df['col'].rank(ascending=False) so the highest value gets rank 1.",
            "category": 'rank',
            "tables": [
                {
                    "name": 'worldwide_gross',
                    "csv": (
                        "title,revenue_m\n"
                        "Avatar: The Way of Water,2320\n"
                        "Top Gun: Maverick,1491\n"
                        "Doctor Strange in the Multiverse of Madness,956\n"
                        "Jurassic World Dominion,1001\n"
                        "The Batman,770"
                    ),
                },
            ],
            "expected_csv": (
                "title,revenue_m,rank\n"
                "Avatar: The Way of Water,2320,1.0\n"
                "Top Gun: Maverick,1491,2.0\n"
                "Doctor Strange in the Multiverse of Madness,956,4.0\n"
                "Jurassic World Dominion,1001,3.0\n"
                "The Batman,770,5.0"
            ),
        },
        {
            "statement": "Add a 'rank' column that ranks films by their rating from highest to lowest in the critic_scores table. Ties should share the average rank.",
            "solution_code": 'critic_scores.assign(rank=critic_scores["rating"].rank(ascending=False))',
            "hint": "The default rank method is 'average', so tied values share the mean of their positions.",
            "category": 'rank',
            "tables": [
                {
                    "name": 'critic_scores',
                    "csv": (
                        "title,rating\n"
                        "Oppenheimer,9.2\n"
                        "Barbie,8.1\n"
                        "Dune: Part Two,9.2\n"
                        "Mission: Impossible Dead Reckoning,8.5\n"
                        "Killers of the Flower Moon,8.5"
                    ),
                },
            ],
            "expected_csv": (
                "title,rating,rank\n"
                "Oppenheimer,9.2,1.5\n"
                "Barbie,8.1,5.0\n"
                "Dune: Part Two,9.2,1.5\n"
                "Mission: Impossible Dead Reckoning,8.5,3.5\n"
                "Killers of the Flower Moon,8.5,3.5"
            ),
        },
        {
            "statement": "Add a 'cumulative_revenue' column showing the running total of weekly_revenue_m in the weekly_sales table.",
            "solution_code": 'weekly_sales.assign(cumulative_revenue=weekly_sales["weekly_revenue_m"].cumsum())',
            "hint": 'Use .cumsum() on the revenue column to get a running total.',
            "category": 'cumsum',
            "tables": [
                {
                    "name": 'weekly_sales',
                    "csv": (
                        "week,title,weekly_revenue_m\n"
                        "1,Spider-Man: No Way Home,450\n"
                        "2,Spider-Man: No Way Home,380\n"
                        "3,Spider-Man: No Way Home,290\n"
                        "4,Spider-Man: No Way Home,510\n"
                        "5,Spider-Man: No Way Home,340"
                    ),
                },
            ],
            "expected_csv": (
                "week,title,weekly_revenue_m,cumulative_revenue\n"
                "1,Spider-Man: No Way Home,450,450\n"
                "2,Spider-Man: No Way Home,380,830\n"
                "3,Spider-Man: No Way Home,290,1120\n"
                "4,Spider-Man: No Way Home,510,1630\n"
                "5,Spider-Man: No Way Home,340,1970"
            ),
        },
        {
            "statement": "Add a 'cumulative_budget' column with the running total of budget_m across films in the mcu_budgets table.",
            "solution_code": 'mcu_budgets.assign(cumulative_budget=mcu_budgets["budget_m"].cumsum())',
            "hint": 'cumsum() adds each value to the running total of all previous values.',
            "category": 'cumsum',
            "tables": [
                {
                    "name": 'mcu_budgets',
                    "csv": (
                        "title,budget_m\n"
                        "The Avengers,220\n"
                        "Iron Man 3,200\n"
                        "Thor: The Dark World,170\n"
                        "Captain America: The Winter Soldier,170\n"
                        "Guardians of the Galaxy,170"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget_m,cumulative_budget\n"
                "The Avengers,220,220\n"
                "Iron Man 3,200,420\n"
                "Thor: The Dark World,170,590\n"
                "Captain America: The Winter Soldier,170,760\n"
                "Guardians of the Galaxy,170,930"
            ),
        },
        {
            "statement": "Add a 'pct_change' column showing the week-over-week percentage change in revenue_m for Interstellar in the inter_weekly table.",
            "solution_code": 'inter_weekly.assign(pct_change=inter_weekly["revenue_m"].pct_change())',
            "hint": 'pct_change() returns (current - previous) / previous. The first row will be NaN.',
            "category": 'pct-change',
            "tables": [
                {
                    "name": 'inter_weekly',
                    "csv": (
                        "week,revenue_m\n"
                        "1,100\n"
                        "2,150\n"
                        "3,120\n"
                        "4,180\n"
                        "5,90"
                    ),
                },
            ],
            "expected_csv": (
                "week,revenue_m,pct_change\n"
                "1,100,\n"
                "2,150,0.5\n"
                "3,120,-0.2\n"
                "4,180,0.5\n"
                "5,90,-0.5"
            ),
        },
        {
            "statement": "Add a 'weekly_change' column showing the percentage change in gross_m week over week for The Dark Knight in the tdk_weekly table.",
            "solution_code": 'tdk_weekly.assign(weekly_change=tdk_weekly["gross_m"].pct_change())',
            "hint": 'pct_change() computes the relative change from one row to the next.',
            "category": 'pct-change',
            "tables": [
                {
                    "name": 'tdk_weekly',
                    "csv": (
                        "week,gross_m\n"
                        "1,200\n"
                        "2,250\n"
                        "3,200\n"
                        "4,300\n"
                        "5,150"
                    ),
                },
            ],
            "expected_csv": (
                "week,gross_m,weekly_change\n"
                "1,200,\n"
                "2,250,0.25\n"
                "3,200,-0.2\n"
                "4,300,0.5\n"
                "5,150,-0.5"
            ),
        },
        {
            "statement": "Add a 'budget_diff' column showing the difference in budget_m compared to the previous film in the nolan_films table.",
            "solution_code": 'nolan_films.assign(budget_diff=nolan_films["budget_m"].diff())',
            "hint": 'diff() computes current - previous. The first row will be NaN.',
            "category": 'diff',
            "tables": [
                {
                    "name": 'nolan_films',
                    "csv": (
                        "title,budget_m\n"
                        "Inception,150\n"
                        "Interstellar,165\n"
                        "Tenet,200\n"
                        "Dunkirk,100\n"
                        "Oppenheimer,100"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget_m,budget_diff\n"
                "Inception,150,\n"
                "Interstellar,165,15.0\n"
                "Tenet,200,35.0\n"
                "Dunkirk,100,-100.0\n"
                "Oppenheimer,100,0.0"
            ),
        },
        {
            "statement": "Add a 'score_diff' column that shows the change in avg_score from one week to the next in the audience_scores table.",
            "solution_code": 'audience_scores.assign(score_diff=audience_scores["avg_score"].diff())',
            "hint": "diff() subtracts the previous row's value from the current one.",
            "category": 'diff',
            "tables": [
                {
                    "name": 'audience_scores',
                    "csv": (
                        "week,avg_score\n"
                        "1,85\n"
                        "2,90\n"
                        "3,78\n"
                        "4,95\n"
                        "5,88"
                    ),
                },
            ],
            "expected_csv": (
                "week,avg_score,score_diff\n"
                "1,85,\n"
                "2,90,5.0\n"
                "3,78,-12.0\n"
                "4,95,17.0\n"
                "5,88,-7.0"
            ),
        },
        {
            "statement": "Add a 'prev_revenue' column containing the previous week's revenue_m (shifted down by 1) in the avatar_weekly table.",
            "solution_code": 'avatar_weekly.assign(prev_revenue=avatar_weekly["revenue_m"].shift(1))',
            "hint": 'shift(1) moves values down by one row; the first row becomes NaN.',
            "category": 'shift',
            "tables": [
                {
                    "name": 'avatar_weekly',
                    "csv": (
                        "week,revenue_m\n"
                        "1,100\n"
                        "2,150\n"
                        "3,120\n"
                        "4,180\n"
                        "5,90"
                    ),
                },
            ],
            "expected_csv": (
                "week,revenue_m,prev_revenue\n"
                "1,100,\n"
                "2,150,100.0\n"
                "3,120,150.0\n"
                "4,180,120.0\n"
                "5,90,180.0"
            ),
        },
        {
            "statement": "Add a 'prev_week_gross' column with the previous week's gross_m value (shifted by 1) in the joker_weekly table.",
            "solution_code": 'joker_weekly.assign(prev_week_gross=joker_weekly["gross_m"].shift(1))',
            "hint": 'Use shift(1) to look back one row; the first entry will be NaN since there is no prior week.',
            "category": 'shift',
            "tables": [
                {
                    "name": 'joker_weekly',
                    "csv": (
                        "week,gross_m\n"
                        "1,200\n"
                        "2,250\n"
                        "3,200\n"
                        "4,300\n"
                        "5,150"
                    ),
                },
            ],
            "expected_csv": (
                "week,gross_m,prev_week_gross\n"
                "1,200,\n"
                "2,250,200.0\n"
                "3,200,250.0\n"
                "4,300,200.0\n"
                "5,150,300.0"
            ),
        },
    ],
    18: [
        {
            "statement": "Add a 'tier' column to movies that bins budget_m into 'Low' (0–50M), 'Mid' (50–150M), and 'High' (150–400M) using pd.cut.",
            "solution_code": 'movies.assign(tier=pd.cut(movies["budget_m"], bins=[0, 50, 150, 400], labels=["Low", "Mid", "High"], include_lowest=True))',
            "hint": 'Use pd.cut with a list of bin edges and matching labels. include_lowest=True ensures the minimum value is included.',
            "category": 'cut',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,budget_m\n"
                        "Parasite,15\n"
                        "Get Out,5\n"
                        "Spider-Man,139\n"
                        "Inception,160\n"
                        "Mad Max Fury Road,185\n"
                        "La La Land,30"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget_m,tier\n"
                "Parasite,15,Low\n"
                "Get Out,5,Low\n"
                "Spider-Man,139,Mid\n"
                "Inception,160,High\n"
                "Mad Max Fury Road,185,High\n"
                "La La Land,30,Low"
            ),
        },
        {
            "statement": "Add a 'tier' column to films that labels each movie's IMDB rating as 'Poor' (0–5), 'Good' (5–7), or 'Great' (7–10) using pd.cut.",
            "solution_code": 'films.assign(tier=pd.cut(films["rating"], bins=[0, 5, 7, 10], labels=["Poor", "Good", "Great"], include_lowest=True))',
            "hint": 'Pass a list of bin edges to pd.cut. include_lowest=True makes the first bin closed on the left.',
            "category": 'cut',
            "tables": [
                {
                    "name": 'films',
                    "csv": (
                        "title,rating\n"
                        "Morbius,3.9\n"
                        "Batman v Superman,6.4\n"
                        "Transformers,5.9\n"
                        "The Dark Knight,9.0\n"
                        "Parasite,8.6\n"
                        "Citizen Kane,8.3"
                    ),
                },
            ],
            "expected_csv": (
                "title,rating,tier\n"
                "Morbius,3.9,Poor\n"
                "Batman v Superman,6.4,Good\n"
                "Transformers,5.9,Good\n"
                "The Dark Knight,9.0,Great\n"
                "Parasite,8.6,Great\n"
                "Citizen Kane,8.3,Great"
            ),
        },
        {
            "statement": "Add a 'category' column to box_office that classifies each film's gross into 'Flop' (0–100M), 'Hit' (100–500M), or 'Blockbuster' (500–3000M) using pd.cut.",
            "solution_code": 'box_office.assign(category=pd.cut(box_office["box_office_m"], bins=[0, 100, 500, 3000], labels=["Flop", "Hit", "Blockbuster"], include_lowest=True))',
            "hint": 'Define bin edges covering all values and use matching labels list.',
            "category": 'cut',
            "tables": [
                {
                    "name": 'box_office',
                    "csv": (
                        "title,box_office_m\n"
                        "Dredd,36\n"
                        "Knives Out,311\n"
                        "Black Panther,1346\n"
                        "Avengers Infinity War,2048\n"
                        "Whiplash,49\n"
                        "Jurassic World,1671"
                    ),
                },
            ],
            "expected_csv": (
                "title,box_office_m,category\n"
                "Dredd,36,Flop\n"
                "Knives Out,311,Hit\n"
                "Black Panther,1346,Blockbuster\n"
                "Avengers Infinity War,2048,Blockbuster\n"
                "Whiplash,49,Flop\n"
                "Jurassic World,1671,Blockbuster"
            ),
        },
        {
            "statement": "Add a 'tier' column to budgets using pd.qcut with 3 equal-sized groups labeled 'Low', 'Mid', and 'High'.",
            "solution_code": 'budgets.assign(tier=pd.qcut(budgets["budget_m"], q=3, labels=["Low", "Mid", "High"]))',
            "hint": 'pd.qcut divides data into q groups of equal size by rank. Use q=3 and supply three labels.',
            "category": 'qcut',
            "tables": [
                {
                    "name": 'budgets',
                    "csv": (
                        "title,budget_m\n"
                        "Moonlight,1.5\n"
                        "Get Out,4.5\n"
                        "Whiplash,8.5\n"
                        "La La Land,30.0\n"
                        "Gravity,100.0\n"
                        "Inception,160.0"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget_m,tier\n"
                "Moonlight,1.5,Low\n"
                "Get Out,4.5,Low\n"
                "Whiplash,8.5,Mid\n"
                "La La Land,30.0,Mid\n"
                "Gravity,100.0,High\n"
                "Inception,160.0,High"
            ),
        },
        {
            "statement": "Add a 'tier' column to scores using pd.qcut with 3 quantile-based groups labeled 'Rotten', 'Fresh', and 'Certified Fresh'.",
            "solution_code": 'scores.assign(tier=pd.qcut(scores["rating"], q=3, labels=["Rotten", "Fresh", "Certified Fresh"]))',
            "hint": 'pd.qcut splits data by percentile rank. With q=3 you get three equal-count groups.',
            "category": 'qcut',
            "tables": [
                {
                    "name": 'scores',
                    "csv": (
                        "title,rating\n"
                        "Speed Racer,5.0\n"
                        "Morbius,5.5\n"
                        "Doctor Strange,7.0\n"
                        "Shang-Chi,7.4\n"
                        "Everything Everywhere,7.8\n"
                        "Oppenheimer,8.5"
                    ),
                },
            ],
            "expected_csv": (
                "title,rating,tier\n"
                "Speed Racer,5.0,Rotten\n"
                "Morbius,5.5,Rotten\n"
                "Doctor Strange,7.0,Fresh\n"
                "Shang-Chi,7.4,Fresh\n"
                "Everything Everywhere,7.8,Certified Fresh\n"
                "Oppenheimer,8.5,Certified Fresh"
            ),
        },
        {
            "statement": "Add a 'tier' column to grosses using pd.qcut with 2 groups labeled 'Below Median' and 'Above Median'.",
            "solution_code": 'grosses.assign(tier=pd.qcut(grosses["box_office_m"], q=2, labels=["Below Median", "Above Median"]))',
            "hint": 'With q=2, pd.qcut splits at the median, giving two equal-sized groups.',
            "category": 'qcut',
            "tables": [
                {
                    "name": 'grosses',
                    "csv": (
                        "title,box_office_m\n"
                        "Dredd,36\n"
                        "Whiplash,49\n"
                        "Knives Out,311\n"
                        "Black Panther,700\n"
                        "Avengers Infinity War,1346\n"
                        "Avengers Endgame,2048"
                    ),
                },
            ],
            "expected_csv": (
                "title,box_office_m,tier\n"
                "Dredd,36,Below Median\n"
                "Whiplash,49,Below Median\n"
                "Knives Out,311,Below Median\n"
                "Black Panther,700,Above Median\n"
                "Avengers Infinity War,1346,Above Median\n"
                "Avengers Endgame,2048,Above Median"
            ),
        },
        {
            "statement": 'Clip the budget_m column in productions so that no value falls below 20 or above 250.',
            "solution_code": 'productions.assign(budget_m=productions["budget_m"].clip(lower=20, upper=250))',
            "hint": 'Use .clip(lower=, upper=) on a Series to bound values within a range.',
            "category": 'clip',
            "tables": [
                {
                    "name": 'productions',
                    "csv": (
                        "title,budget_m\n"
                        "Moonlight,1.5\n"
                        "Parasite,15.5\n"
                        "Mad Max Fury Road,185.0\n"
                        "Titanic,200.0\n"
                        "Avengers Endgame,356.0\n"
                        "The Dark Knight Rises,250.0"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget_m\n"
                "Moonlight,20.0\n"
                "Parasite,20.0\n"
                "Mad Max Fury Road,185.0\n"
                "Titanic,200.0\n"
                "Avengers Endgame,250.0\n"
                "The Dark Knight Rises,250.0"
            ),
        },
        {
            "statement": 'Clip the box_office_m column in revenues so that values below 50 are raised to 50 and values above 800 are capped at 800.',
            "solution_code": 'revenues.assign(box_office_m=revenues["box_office_m"].clip(lower=50, upper=800))',
            "hint": 'clip() works on any numeric Series — supply lower and upper keyword arguments.',
            "category": 'clip',
            "tables": [
                {
                    "name": 'revenues',
                    "csv": (
                        "title,box_office_m\n"
                        "Dredd,36\n"
                        "Whiplash,13\n"
                        "Interstellar,701\n"
                        "Inception,836\n"
                        "Spider-Man No Way Home,1901\n"
                        "Avengers Endgame,2798"
                    ),
                },
            ],
            "expected_csv": (
                "title,box_office_m\n"
                "Dredd,50\n"
                "Whiplash,50\n"
                "Interstellar,701\n"
                "Inception,800\n"
                "Spider-Man No Way Home,800\n"
                "Avengers Endgame,800"
            ),
        },
        {
            "statement": "Compute the 25th, 50th, and 75th percentiles of budget_m in film_data and return them as a DataFrame with columns 'quantile' and 'budget_m'.",
            "solution_code": 'film_data["budget_m"].quantile([0.25, 0.5, 0.75]).reset_index().rename(columns={"index": "quantile"})',
            "hint": 'Call .quantile() with a list of probabilities, then .reset_index() to turn the index into a column, and rename it.',
            "category": 'quantile',
            "tables": [
                {
                    "name": 'film_data',
                    "csv": (
                        "title,budget_m\n"
                        "Moonlight,1.5\n"
                        "Get Out,4.5\n"
                        "Whiplash,8.5\n"
                        "La La Land,30.0\n"
                        "Gravity,100.0\n"
                        "Inception,160.0"
                    ),
                },
            ],
            "expected_csv": (
                "quantile,budget_m\n"
                "0.25,5.5\n"
                "0.5,19.25\n"
                "0.75,82.5"
            ),
        },
        {
            "statement": "Compute the 25th, 50th, and 75th percentiles of the rating column in critic_scores and return them as a DataFrame with columns 'quantile' and 'rating'.",
            "solution_code": 'critic_scores["rating"].quantile([0.25, 0.5, 0.75]).reset_index().rename(columns={"index": "quantile"})',
            "hint": 'Pass a list of floats between 0 and 1 to .quantile(), then convert the result to a DataFrame with reset_index().',
            "category": 'quantile',
            "tables": [
                {
                    "name": 'critic_scores',
                    "csv": (
                        "title,rating\n"
                        "Speed Racer,5.0\n"
                        "Morbius,5.5\n"
                        "Doctor Strange,7.0\n"
                        "Shang-Chi,7.4\n"
                        "Everything Everywhere,7.8\n"
                        "Oppenheimer,8.5"
                    ),
                },
            ],
            "expected_csv": (
                "quantile,rating\n"
                "0.25,5.875\n"
                "0.5,7.2\n"
                "0.75,7.7"
            ),
        },
    ],
    19: [
        {
            "statement": "Add a column 'genre_avg_budget' showing the average budget (millions) for each movie's genre using transform.",
            "solution_code": 'movies.assign(genre_avg_budget=movies.groupby("genre")["budget"].transform("mean"))',
            "hint": "Use groupby('col')['value'].transform('mean') to broadcast the group mean to every row.",
            "category": 'transform',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,genre,budget\n"
                        "The Dark Knight,Action,150\n"
                        "Gladiator,Action,200\n"
                        "The Notebook,Drama,80\n"
                        "Crash,Drama,60\n"
                        "Interstellar,Sci-Fi,120"
                    ),
                },
            ],
            "expected_csv": (
                "title,genre,budget,genre_avg_budget\n"
                "The Dark Knight,Action,150,175.0\n"
                "Gladiator,Action,200,175.0\n"
                "The Notebook,Drama,80,70.0\n"
                "Crash,Drama,60,70.0\n"
                "Interstellar,Sci-Fi,120,120.0"
            ),
        },
        {
            "statement": "Add a column 'director_avg_rating' showing the mean IMDb rating of all films by the same director, using transform.",
            "solution_code": 'films.assign(director_avg_rating=films.groupby("director")["rating"].transform("mean"))',
            "hint": "Group by director, then transform rating with 'mean' to broadcast the group average to each row.",
            "category": 'transform',
            "tables": [
                {
                    "name": 'films',
                    "csv": (
                        "title,director,rating\n"
                        "Inception,Nolan,8.6\n"
                        "The Dark Knight,Nolan,9.0\n"
                        "Jaws,Spielberg,8.0\n"
                        "Schindler's List,Spielberg,9.0\n"
                        "Fight Club,Fincher,8.8"
                    ),
                },
            ],
            "expected_csv": (
                "title,director,rating,director_avg_rating\n"
                "Inception,Nolan,8.6,8.8\n"
                "The Dark Knight,Nolan,9.0,8.8\n"
                "Jaws,Spielberg,8.0,8.5\n"
                "Schindler's List,Spielberg,9.0,8.5\n"
                "Fight Club,Fincher,8.8,8.8"
            ),
        },
        {
            "statement": "Add a column 'revenue_rank' showing each movie's rank by revenue within its genre (1 = highest revenue), using transform.",
            "solution_code": 'movies.assign(revenue_rank=movies.groupby("genre")["revenue"].transform("rank", ascending=False))',
            "hint": "Use transform('rank', ascending=False) to rank each row within its group and keep the result aligned to the original DataFrame.",
            "category": 'transform',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,genre,revenue\n"
                        "Avengers: Endgame,Action,2797\n"
                        "The Dark Knight,Action,1005\n"
                        "Gladiator,Action,460\n"
                        "Titanic,Romance,2187\n"
                        "The Notebook,Romance,115"
                    ),
                },
            ],
            "expected_csv": (
                "title,genre,revenue,revenue_rank\n"
                "Avengers: Endgame,Action,2797,1.0\n"
                "The Dark Knight,Action,1005,2.0\n"
                "Gladiator,Action,460,3.0\n"
                "Titanic,Romance,2187,1.0\n"
                "The Notebook,Romance,115,2.0"
            ),
        },
        {
            "statement": "Add a column 'roi' showing the return on investment percentage for each movie — (revenue - budget) / budget * 100 — computed with apply row-wise.",
            "solution_code": 'movies.assign(roi=movies.apply(lambda row: (row["revenue"] - row["budget"]) / row["budget"] * 100, axis=1))',
            "hint": 'Use df.apply(lambda row: ..., axis=1) to compute a derived value from multiple columns for each row.',
            "category": 'apply',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,budget,revenue\n"
                        "Avatar,100,300\n"
                        "The Dark Knight,50,200\n"
                        "Interstellar,200,1000\n"
                        "Parasite,25,100\n"
                        "Get Out,10,30"
                    ),
                },
            ],
            "expected_csv": (
                "title,budget,revenue,roi\n"
                "Avatar,100,300,200.0\n"
                "The Dark Knight,50,200,300.0\n"
                "Interstellar,200,1000,400.0\n"
                "Parasite,25,100,300.0\n"
                "Get Out,10,30,200.0"
            ),
        },
        {
            "statement": 'For each genre, return only the highest-rated movie using groupby apply. Reset the index afterward.',
            "solution_code": 'movies.groupby("genre").apply(lambda g: g.nlargest(1, "rating")).reset_index(drop=True)',
            "hint": "Use groupby().apply() with a lambda that calls nlargest(1, 'rating') on each group, then reset_index(drop=True).",
            "category": 'apply',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,genre,rating\n"
                        "The Dark Knight,Action,9.0\n"
                        "Gladiator,Action,8.5\n"
                        "Titanic,Romance,7.8\n"
                        "The Notebook,Romance,7.2\n"
                        "The Silence of the Lambs,Thriller,8.6\n"
                        "Psycho,Thriller,8.5"
                    ),
                },
            ],
            "expected_csv": (
                "title,rating\n"
                "The Dark Knight,9.0\n"
                "Titanic,7.8\n"
                "The Silence of the Lambs,8.6"
            ),
        },
        {
            "statement": 'For each studio, compute the mean and sum of production budget (millions). Flatten the MultiIndex columns and reset the index.',
            "solution_code": "(lambda df: df.set_axis([f'{a}_{b}' for a, b in df.columns], axis=1).reset_index())(movies.groupby('studio').agg({'budget': ['mean', 'sum']}))",
            "hint": "After groupby().agg(), flatten the MultiIndex columns with set_axis([f'{a}_{b}' for a,b in df.columns], axis=1) before reset_index().",
            "category": 'agg',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,studio,budget\n"
                        "Top Gun,Paramount,38\n"
                        "Titanic,Paramount,200\n"
                        "Jaws,Universal,7\n"
                        "E.T.,Universal,10\n"
                        "The Dark Knight,Warner Bros,185\n"
                        "Inception,Warner Bros,160"
                    ),
                },
            ],
            "expected_csv": (
                "studio,budget_mean,budget_sum\n"
                "Paramount,119.0,238\n"
                "Universal,8.5,17\n"
                "Warner Bros,172.5,345"
            ),
        },
        {
            "statement": 'For each genre, compute the mean and maximum of IMDb rating. Flatten the MultiIndex columns and reset the index.',
            "solution_code": "(lambda df: df.set_axis([f'{a}_{b}' for a, b in df.columns], axis=1).reset_index())(movies.groupby('genre').agg({'rating': ['mean', 'max']}))",
            "hint": "Use groupby().agg({'rating': ['mean','max']}), then flatten the MultiIndex columns before resetting the index.",
            "category": 'agg',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,genre,rating\n"
                        "Gladiator,Action,8.5\n"
                        "Mad Max Fury Road,Action,8.1\n"
                        "The Godfather,Drama,9.2\n"
                        "Forrest Gump,Drama,8.8\n"
                        "Blade Runner,Sci-Fi,8.1\n"
                        "Arrival,Sci-Fi,7.9"
                    ),
                },
            ],
            "expected_csv": (
                "genre,rating_mean,rating_max\n"
                "Action,8.3,8.5\n"
                "Drama,9.0,9.2\n"
                "Sci-Fi,8.0,8.1"
            ),
        },
        {
            "statement": 'For each director, compute the count and mean of worldwide revenue (millions). Flatten the MultiIndex columns and reset the index.',
            "solution_code": "(lambda df: df.set_axis([f'{a}_{b}' for a, b in df.columns], axis=1).reset_index())(films.groupby('director').agg({'revenue': ['count', 'mean']}))",
            "hint": "Use groupby().agg({'revenue': ['count','mean']}), flatten columns with set_axis, then reset_index().",
            "category": 'agg',
            "tables": [
                {
                    "name": 'films',
                    "csv": (
                        "title,director,revenue\n"
                        "Inception,Nolan,800\n"
                        "The Dark Knight,Nolan,1000\n"
                        "Interstellar,Nolan,600\n"
                        "Jaws,Spielberg,400\n"
                        "Schindler's List,Spielberg,600"
                    ),
                },
            ],
            "expected_csv": (
                "director,revenue_count,revenue_mean\n"
                "Nolan,3,800.0\n"
                "Spielberg,2,500.0"
            ),
        },
        {
            "statement": "Compute the correlation matrix between a movie's production budget and its worldwide revenue.",
            "solution_code": 'movies[["budget", "revenue"]].corr().reset_index()',
            "hint": 'Select the two numeric columns and call .corr() to get a 2x2 Pearson correlation matrix.',
            "category": 'corr',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,budget,revenue\n"
                        "The Avengers,100,200\n"
                        "Iron Man,200,400\n"
                        "Thor,300,600\n"
                        "Captain America,400,800\n"
                        "Black Widow,500,1000"
                    ),
                },
            ],
            "expected_csv": (
                "index,budget,revenue\n"
                "budget,1.0,1.0\n"
                "revenue,1.0,1.0"
            ),
        },
        {
            "statement": "Compute the correlation matrix between a movie's IMDb rating and its runtime in minutes.",
            "solution_code": 'movies[["rating", "runtime"]].corr().reset_index()',
            "hint": 'Select the two numeric columns and call .corr() — a perfect negative correlation means shorter films always score higher in this dataset.',
            "category": 'corr',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,rating,runtime\n"
                        "The Godfather,9.0,90\n"
                        "Titanic,7.0,110\n"
                        "Transformers,5.0,130\n"
                        "Ballistic: Ecks vs. Sever,3.0,150"
                    ),
                },
            ],
            "expected_csv": (
                "index,rating,runtime\n"
                "rating,1.0,-1.0\n"
                "runtime,-1.0,1.0"
            ),
        },
    ],
    20: [
        {
            "statement": 'Merge the cast table with the films table on film_id, filter to films released after 2010, then find the total box office revenue per actor sorted from highest to lowest.',
            "solution_code": "cast.merge(films, on='film_id')[cast.merge(films, on='film_id')['year'] > 2010].groupby('actor')['box_office_m'].sum().reset_index().sort_values('box_office_m', ascending=False).reset_index(drop=True)",
            "hint": 'Chain: merge on film_id, boolean filter year > 2010, groupby actor + sum, sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'cast',
                    "csv": (
                        "film_id,actor\n"
                        "1,Leonardo DiCaprio\n"
                        "2,Matthew McConaughey\n"
                        "3,Leonardo DiCaprio\n"
                        "4,Tom Hardy\n"
                        "5,Matthew McConaughey"
                    ),
                },
                {
                    "name": 'films',
                    "csv": (
                        "film_id,title,year,box_office_m\n"
                        "1,Inception,2010,836\n"
                        "2,Interstellar,2014,701\n"
                        "3,The Revenant,2015,533\n"
                        "4,Mad Max Fury Road,2015,378\n"
                        "5,Dallas Buyers Club,2013,55"
                    ),
                },
            ],
            "expected_csv": (
                "actor,box_office_m\n"
                "Matthew McConaughey,756\n"
                "Leonardo DiCaprio,533\n"
                "Tom Hardy,378"
            ),
        },
        {
            "statement": 'Concatenate the blockbusters_a and blockbusters_b tables, assign a new column profit_m equal to box_office_m minus budget_m, then select only title and profit_m sorted by profit_m descending.',
            "solution_code": "pd.concat([blockbusters_a, blockbusters_b], ignore_index=True).assign(profit_m=lambda df: df['box_office_m'] - df['budget_m'])[['title', 'profit_m']].sort_values('profit_m', ascending=False).reset_index(drop=True)",
            "hint": 'concat first, then assign profit_m with a lambda, then select columns and sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'blockbusters_a',
                    "csv": (
                        "title,year,budget_m,box_office_m\n"
                        "The Dark Knight,2008,185,1005\n"
                        "Gladiator,2000,103,457\n"
                        "Inception,2010,160,836"
                    ),
                },
                {
                    "name": 'blockbusters_b',
                    "csv": (
                        "title,year,budget_m,box_office_m\n"
                        "Mad Max Fury Road,2015,150,378\n"
                        "The Martian,2015,108,630\n"
                        "Gravity,2013,100,723"
                    ),
                },
            ],
            "expected_csv": (
                "title,profit_m\n"
                "The Dark Knight,820\n"
                "Inception,676\n"
                "Gravity,623\n"
                "The Martian,522\n"
                "Gladiator,354\n"
                "Mad Max Fury Road,228"
            ),
        },
        {
            "statement": 'Merge the directors table with the films table on director_id, assign a profit_m column as revenue_m minus budget_m, filter to films where profit_m exceeds 300, then select director, title, and profit_m sorted by profit_m descending.',
            "solution_code": "directors.merge(films, on='director_id').assign(profit_m=lambda df: df['revenue_m'] - df['budget_m'])[directors.merge(films, on='director_id').assign(profit_m=lambda df: df['revenue_m'] - df['budget_m'])['profit_m'] > 300][['director', 'title', 'profit_m']].sort_values('profit_m', ascending=False).reset_index(drop=True)",
            "hint": 'merge, assign profit_m, filter profit_m > 300 with boolean indexing (double-expression pattern), select columns, sort.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'directors',
                    "csv": (
                        "director_id,director\n"
                        "1,Christopher Nolan\n"
                        "2,Martin Scorsese\n"
                        "3,James Cameron\n"
                        "4,Quentin Tarantino\n"
                        "5,Ridley Scott"
                    ),
                },
                {
                    "name": 'films',
                    "csv": (
                        "director_id,title,budget_m,revenue_m\n"
                        "1,The Dark Knight,185,1005\n"
                        "2,The Departed,90,290\n"
                        "3,Avatar,237,2923\n"
                        "4,Pulp Fiction,8,214\n"
                        "5,Gladiator,103,457"
                    ),
                },
            ],
            "expected_csv": (
                "director,title,profit_m\n"
                "James Cameron,Avatar,2686\n"
                "Christopher Nolan,The Dark Knight,820\n"
                "Ridley Scott,Gladiator,354"
            ),
        },
        {
            "statement": 'Group the movies table by director, compute the number of films (film_count) and total box office revenue (total_revenue), keep only directors whose total_revenue exceeds 500, and sort by total_revenue descending.',
            "solution_code": "movies.groupby('director').agg(film_count=('title', 'count'), total_revenue=('box_office_m', 'sum')).reset_index()[movies.groupby('director').agg(film_count=('title', 'count'), total_revenue=('box_office_m', 'sum')).reset_index()['total_revenue'] > 500].sort_values('total_revenue', ascending=False).reset_index(drop=True)",
            "hint": 'groupby + named agg, reset_index, filter with boolean indexing, sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'movies',
                    "csv": (
                        "title,director,box_office_m\n"
                        "The Dark Knight,Christopher Nolan,1005\n"
                        "Inception,Christopher Nolan,836\n"
                        "Pulp Fiction,Quentin Tarantino,214\n"
                        "Django Unchained,Quentin Tarantino,425\n"
                        "Inglourious Basterds,Quentin Tarantino,321\n"
                        "Gladiator,Ridley Scott,457"
                    ),
                },
            ],
            "expected_csv": (
                "director,film_count,total_revenue\n"
                "Christopher Nolan,2,1841\n"
                "Quentin Tarantino,3,960"
            ),
        },
        {
            "statement": 'Merge the roles table with the box_office table on film_id, filter to Lead roles only, then select actor, title, and revenue_m sorted by revenue_m descending.',
            "solution_code": "roles.merge(box_office, on='film_id')[roles.merge(box_office, on='film_id')['role_type'] == 'Lead'][['actor', 'title', 'revenue_m']].sort_values('revenue_m', ascending=False).reset_index(drop=True)",
            "hint": "merge on film_id, filter role_type == 'Lead' with boolean indexing, select columns, sort descending.",
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'roles',
                    "csv": (
                        "film_id,actor,role_type\n"
                        "1,Marlon Brando,Lead\n"
                        "1,Al Pacino,Lead\n"
                        "1,Diane Keaton,Supporting\n"
                        "2,Robert De Niro,Lead\n"
                        "2,Joe Pesci,Supporting"
                    ),
                },
                {
                    "name": 'box_office',
                    "csv": (
                        "film_id,title,revenue_m\n"
                        "1,The Godfather,245\n"
                        "2,Goodfellas,47"
                    ),
                },
            ],
            "expected_csv": (
                "actor,title,revenue_m\n"
                "Marlon Brando,The Godfather,245\n"
                "Al Pacino,The Godfather,245\n"
                "Robert De Niro,Goodfellas,47"
            ),
        },
        {
            "statement": 'Merge the nominations table with the films table on film_id, fill missing oscar_noms values with 0, then compute the total nominations per genre sorted from highest to lowest.',
            "solution_code": "nominations.merge(films, on='film_id').fillna({'oscar_noms': 0}).groupby('genre')['oscar_noms'].sum().reset_index().sort_values('oscar_noms', ascending=False).reset_index(drop=True)",
            "hint": 'merge on film_id, fillna oscar_noms with 0, groupby genre + sum, sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'nominations',
                    "csv": (
                        "actor,film_id,oscar_noms\n"
                        "Meryl Streep,1,3\n"
                        "Tom Hanks,2,2\n"
                        "Cate Blanchett,3,3\n"
                        "Joaquin Phoenix,4,\n"
                        "Natalie Portman,5,1"
                    ),
                },
                {
                    "name": 'films',
                    "csv": (
                        "film_id,title,genre\n"
                        "1,The Iron Lady,Drama\n"
                        "2,Cast Away,Drama\n"
                        "3,Blue Jasmine,Drama\n"
                        "4,Joker,Drama\n"
                        "5,Black Swan,Thriller"
                    ),
                },
            ],
            "expected_csv": (
                "genre,oscar_noms\n"
                "Drama,8.0\n"
                "Thriller,1.0"
            ),
        },
        {
            "statement": 'Convert studio names in the performances table to uppercase, merge with the studios table on studio_upper, then count the number of films per actor sorted by film count descending.',
            "solution_code": "performances.assign(studio_upper=performances['studio'].str.upper()).merge(studios, on='studio_upper').groupby('actor')['film'].count().reset_index().sort_values('film', ascending=False).reset_index(drop=True)",
            "hint": 'assign studio_upper with str.upper(), merge on studio_upper, groupby actor + count film, sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'performances',
                    "csv": (
                        "actor,studio,film\n"
                        "Tom Hanks,universal,Cast Away\n"
                        "Tom Hanks,warner,The Terminal\n"
                        "Tom Hanks,universal,Forrest Gump\n"
                        "Meryl Streep,universal,The Devil Wears Prada\n"
                        "Cate Blanchett,warner,The Aviator\n"
                        "Cate Blanchett,universal,Blue Jasmine"
                    ),
                },
                {
                    "name": 'studios',
                    "csv": (
                        "studio_upper,location\n"
                        "UNIVERSAL,Hollywood\n"
                        "WARNER,Burbank"
                    ),
                },
            ],
            "expected_csv": (
                "actor,film\n"
                "Tom Hanks,3\n"
                "Cate Blanchett,2\n"
                "Meryl Streep,1"
            ),
        },
        {
            "statement": 'Melt the box_office table so domestic_m and international_m become a single revenue_m column with a market label, filter to markets where revenue_m exceeds 500, then sort by revenue_m descending.',
            "solution_code": "box_office.melt(id_vars='title', var_name='market', value_name='revenue_m')[box_office.melt(id_vars='title', var_name='market', value_name='revenue_m')['revenue_m'] > 500].sort_values('revenue_m', ascending=False).reset_index(drop=True)",
            "hint": "melt with id_vars='title', filter revenue_m > 500 with the double-expression pattern, sort descending.",
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'box_office',
                    "csv": (
                        "title,domestic_m,international_m\n"
                        "The Dark Knight,534,471\n"
                        "Avatar,760,2163\n"
                        "Inception,292,544\n"
                        "Interstellar,188,513\n"
                        "Mad Max Fury Road,154,224"
                    ),
                },
            ],
            "expected_csv": (
                "title,market,revenue_m\n"
                "Avatar,international_m,2163\n"
                "Avatar,domestic_m,760\n"
                "Inception,international_m,544\n"
                "The Dark Knight,domestic_m,534\n"
                "Interstellar,international_m,513"
            ),
        },
        {
            "statement": 'Merge the cast table with the films table on film_id, replace the lowercase genre values with title-case equivalents, then count the number of actors per genre sorted by count descending.',
            "solution_code": "cast.merge(films, on='film_id').replace({'genre': {'action': 'Action', 'sci-fi': 'Sci-Fi', 'drama': 'Drama'}}).groupby('genre')['actor'].count().reset_index().sort_values('actor', ascending=False).reset_index(drop=True)",
            "hint": 'merge on film_id, replace genre strings with a nested dict, groupby genre + count actor, sort descending.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'cast',
                    "csv": (
                        "film_id,actor\n"
                        "1,Christian Bale\n"
                        "1,Heath Ledger\n"
                        "2,Leonardo DiCaprio\n"
                        "3,Russell Crowe\n"
                        "4,Keanu Reeves\n"
                        "5,Mel Gibson"
                    ),
                },
                {
                    "name": 'films',
                    "csv": (
                        "film_id,title,genre\n"
                        "1,The Dark Knight,action\n"
                        "2,Inception,sci-fi\n"
                        "3,Gladiator,action\n"
                        "4,The Matrix,sci-fi\n"
                        "5,Braveheart,drama"
                    ),
                },
            ],
            "expected_csv": (
                "genre,actor\n"
                "Action,3\n"
                "Sci-Fi,2\n"
                "Drama,1"
            ),
        },
        {
            "statement": 'Merge the actors table with the career_stats table on actor_id, assign a score column equal to oscar_wins multiplied by 100 plus box_office_total_m, filter to actors with a score greater than 3500, then select actor and score sorted by score descending.',
            "solution_code": "actors.merge(career_stats, on='actor_id').assign(score=lambda df: df['oscar_wins'] * 100 + df['box_office_total_m'])[actors.merge(career_stats, on='actor_id').assign(score=lambda df: df['oscar_wins'] * 100 + df['box_office_total_m'])['score'] > 3500][['actor', 'score']].sort_values('score', ascending=False).reset_index(drop=True)",
            "hint": 'merge, assign score with a lambda, filter score > 3500 using the double-expression pattern, select columns, sort.',
            "category": 'multi-step',
            "tables": [
                {
                    "name": 'actors',
                    "csv": (
                        "actor_id,actor\n"
                        "1,Leonardo DiCaprio\n"
                        "2,Tom Hanks\n"
                        "3,Meryl Streep\n"
                        "4,Cate Blanchett\n"
                        "5,Joaquin Phoenix"
                    ),
                },
                {
                    "name": 'career_stats',
                    "csv": (
                        "actor_id,oscar_wins,box_office_total_m\n"
                        "1,1,4000\n"
                        "2,2,6500\n"
                        "3,3,3500\n"
                        "4,2,2800\n"
                        "5,1,1500"
                    ),
                },
            ],
            "expected_csv": (
                "actor,score\n"
                "Tom Hanks,6700\n"
                "Leonardo DiCaprio,4100\n"
                "Meryl Streep,3800"
            ),
        },
    ],
}
