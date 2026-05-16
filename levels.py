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
}
