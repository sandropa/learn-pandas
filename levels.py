LEVELS = {
    1: [
        {
            "statement": "Select the name and alias columns from the characters table.",
            "solution_code": 'characters[["name", "alias"]]',
            "hint": "Use double brackets df[['col1', 'col2']] to select multiple columns.",
            "category": "select",
            "tables": [
                {
                    "name": "characters",
                    "display_csv": (
                        "name,alias,role,city\n"
                        "Walter White,Heisenberg,Cook,Albuquerque\n"
                        "Jesse Pinkman,Cap'n Cook,Cook,Albuquerque\n"
                        "Gustavo Fring,Gus,Distributor,Albuquerque\n"
                        "Saul Goodman,Jimmy McGill,Lawyer,Albuquerque\n"
                        "Mike Ehrmantraut,The Guy,Fixer,Albuquerque"
                    ),
                    "test_csv": (
                        "name,alias,role,city\n"
                        "Walter White,Heisenberg,Cook,Albuquerque\n"
                        "Jesse Pinkman,Cap'n Cook,Cook,Albuquerque\n"
                        "Gustavo Fring,Gus,Distributor,Albuquerque\n"
                        "Saul Goodman,Jimmy McGill,Lawyer,Albuquerque\n"
                        "Mike Ehrmantraut,The Guy,Fixer,Albuquerque\n"
                        "Hank Schrader,ASAC Schrader,DEA Agent,Albuquerque\n"
                        "Tuco Salamanca,Tuco,Dealer,Albuquerque\n"
                        "Skyler White,Sky,Accountant,Albuquerque"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,alias\n"
                "Walter White,Heisenberg\n"
                "Jesse Pinkman,Cap'n Cook\n"
                "Gustavo Fring,Gus\n"
                "Saul Goodman,Jimmy McGill\n"
                "Mike Ehrmantraut,The Guy"
            ),
            "test_expected_csv": (
                "name,alias\n"
                "Walter White,Heisenberg\n"
                "Jesse Pinkman,Cap'n Cook\n"
                "Gustavo Fring,Gus\n"
                "Saul Goodman,Jimmy McGill\n"
                "Mike Ehrmantraut,The Guy\n"
                "Hank Schrader,ASAC Schrader\n"
                "Tuco Salamanca,Tuco\n"
                "Skyler White,Sky"
            ),
        },
        {
            "statement": "Filter the batches table to only show batches with purity above 95.",
            "solution_code": 'batches[batches["purity"] > 95]',
            "hint": "Use boolean indexing: df[df['column'] > value].",
            "category": "filter",
            "tables": [
                {
                    "name": "batches",
                    "display_csv": (
                        "batch_id,product,purity,weight_kg\n"
                        "1,Blue Sky,99.1,25\n"
                        "2,Blue Sky,96.2,30\n"
                        "3,Chili P,72.4,15\n"
                        "4,Blue Sky,98.8,20\n"
                        "5,Blue Sky,91.3,28"
                    ),
                    "test_csv": (
                        "batch_id,product,purity,weight_kg\n"
                        "1,Blue Sky,99.1,25\n"
                        "2,Blue Sky,96.2,30\n"
                        "3,Chili P,72.4,15\n"
                        "4,Blue Sky,98.8,20\n"
                        "5,Blue Sky,91.3,28\n"
                        "6,Blue Sky,97.5,22\n"
                        "7,Chili P,68.9,18\n"
                        "8,Blue Sky,95.1,35"
                    ),
                }
            ],
            "display_expected_csv": (
                "batch_id,product,purity,weight_kg\n"
                "1,Blue Sky,99.1,25\n"
                "2,Blue Sky,96.2,30\n"
                "4,Blue Sky,98.8,20"
            ),
            "test_expected_csv": (
                "batch_id,product,purity,weight_kg\n"
                "1,Blue Sky,99.1,25\n"
                "2,Blue Sky,96.2,30\n"
                "4,Blue Sky,98.8,20\n"
                "6,Blue Sky,97.5,22\n"
                "8,Blue Sky,95.1,35"
            ),
        },
        {
            "statement": "Remove the burner_phone column from the contacts table. Time to clean up.",
            "solution_code": 'contacts.drop(columns=["burner_phone"])',
            "hint": "Use df.drop(columns=['column_name']) to remove a column.",
            "category": "drop-column",
            "tables": [
                {
                    "name": "contacts",
                    "display_csv": (
                        "name,phone,burner_phone,city\n"
                        "Walter White,555-0101,555-9901,Albuquerque\n"
                        "Jesse Pinkman,555-0102,555-9902,Albuquerque\n"
                        "Gustavo Fring,555-0103,555-9903,Albuquerque\n"
                        "Saul Goodman,555-0104,555-9904,Albuquerque"
                    ),
                    "test_csv": (
                        "name,phone,burner_phone,city\n"
                        "Walter White,555-0101,555-9901,Albuquerque\n"
                        "Jesse Pinkman,555-0102,555-9902,Albuquerque\n"
                        "Gustavo Fring,555-0103,555-9903,Albuquerque\n"
                        "Saul Goodman,555-0104,555-9904,Albuquerque\n"
                        "Mike Ehrmantraut,555-0105,555-9905,Albuquerque\n"
                        "Hank Schrader,555-0106,555-9906,Albuquerque\n"
                        "Skyler White,555-0107,555-9907,Albuquerque"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,phone,city\n"
                "Walter White,555-0101,Albuquerque\n"
                "Jesse Pinkman,555-0102,Albuquerque\n"
                "Gustavo Fring,555-0103,Albuquerque\n"
                "Saul Goodman,555-0104,Albuquerque"
            ),
            "test_expected_csv": (
                "name,phone,city\n"
                "Walter White,555-0101,Albuquerque\n"
                "Jesse Pinkman,555-0102,Albuquerque\n"
                "Gustavo Fring,555-0103,Albuquerque\n"
                "Saul Goodman,555-0104,Albuquerque\n"
                "Mike Ehrmantraut,555-0105,Albuquerque\n"
                "Hank Schrader,555-0106,Albuquerque\n"
                "Skyler White,555-0107,Albuquerque"
            ),
        },
        {
            "statement": "Rename the qty column to quantity in the inventory table.",
            "solution_code": 'inventory.rename(columns={"qty": "quantity"})',
            "hint": 'Use df.rename(columns={"old_name": "new_name"}) to rename columns.',
            "category": "rename",
            "tables": [
                {
                    "name": "inventory",
                    "display_csv": (
                        "chemical,qty,unit_price\n"
                        "Methylamine,50,15000\n"
                        "Pseudoephedrine,200,25\n"
                        "Red Phosphorus,30,150\n"
                        "Hydriodic Acid,20,500"
                    ),
                    "test_csv": (
                        "chemical,qty,unit_price\n"
                        "Methylamine,50,15000\n"
                        "Pseudoephedrine,200,25\n"
                        "Red Phosphorus,30,150\n"
                        "Hydriodic Acid,20,500\n"
                        "Sodium Hydroxide,100,45\n"
                        "Aluminum Foil,500,3\n"
                        "Acetone,75,120\n"
                        "Toluene,40,200"
                    ),
                }
            ],
            "display_expected_csv": (
                "chemical,quantity,unit_price\n"
                "Methylamine,50,15000\n"
                "Pseudoephedrine,200,25\n"
                "Red Phosphorus,30,150\n"
                "Hydriodic Acid,20,500"
            ),
            "test_expected_csv": (
                "chemical,quantity,unit_price\n"
                "Methylamine,50,15000\n"
                "Pseudoephedrine,200,25\n"
                "Red Phosphorus,30,150\n"
                "Hydriodic Acid,20,500\n"
                "Sodium Hydroxide,100,45\n"
                "Aluminum Foil,500,3\n"
                "Acetone,75,120\n"
                "Toluene,40,200"
            ),
        },
        {
            "statement": "Add a column called revenue that is price_per_pound multiplied by pounds.",
            "solution_code": 'sales.assign(revenue=sales["price_per_pound"] * sales["pounds"])',
            "hint": "Use df.assign(new_col=expression) or df['new_col'] = expression.",
            "category": "computed-column",
            "tables": [
                {
                    "name": "sales",
                    "display_csv": (
                        "territory,price_per_pound,pounds\n"
                        "Albuquerque,40000,5\n"
                        "Phoenix,35000,3\n"
                        "Denver,38000,4\n"
                        "El Paso,42000,2"
                    ),
                    "test_csv": (
                        "territory,price_per_pound,pounds\n"
                        "Albuquerque,40000,5\n"
                        "Phoenix,35000,3\n"
                        "Denver,38000,4\n"
                        "El Paso,42000,2\n"
                        "Santa Fe,36000,3\n"
                        "Tucson,33000,4\n"
                        "Las Vegas,45000,6\n"
                        "Dallas,41000,3"
                    ),
                }
            ],
            "display_expected_csv": (
                "territory,price_per_pound,pounds,revenue\n"
                "Albuquerque,40000,5,200000\n"
                "Phoenix,35000,3,105000\n"
                "Denver,38000,4,152000\n"
                "El Paso,42000,2,84000"
            ),
            "test_expected_csv": (
                "territory,price_per_pound,pounds,revenue\n"
                "Albuquerque,40000,5,200000\n"
                "Phoenix,35000,3,105000\n"
                "Denver,38000,4,152000\n"
                "El Paso,42000,2,84000\n"
                "Santa Fe,36000,3,108000\n"
                "Tucson,33000,4,132000\n"
                "Las Vegas,45000,6,270000\n"
                "Dallas,41000,3,123000"
            ),
        },
        {
            "statement": "Get all employees who work at Los Pollos Hermanos.",
            "solution_code": 'employees[employees["business"] == "Los Pollos Hermanos"]',
            "hint": 'Use boolean indexing with string comparison: df[df["column"] == "value"].',
            "category": "filter-string",
            "tables": [
                {
                    "name": "employees",
                    "display_csv": (
                        "name,business,role\n"
                        "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                        "Lyle,Los Pollos Hermanos,Shift Lead\n"
                        "Jesse Pinkman,Vamonos Pest,Technician\n"
                        "Walter White,Vamonos Pest,Technician\n"
                        "Mike Ehrmantraut,Madrigal,Consultant"
                    ),
                    "test_csv": (
                        "name,business,role\n"
                        "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                        "Lyle,Los Pollos Hermanos,Shift Lead\n"
                        "Jesse Pinkman,Vamonos Pest,Technician\n"
                        "Walter White,Vamonos Pest,Technician\n"
                        "Mike Ehrmantraut,Madrigal,Consultant\n"
                        "Cynthia,Los Pollos Hermanos,Cashier\n"
                        "Todd Alquist,Vamonos Pest,Technician\n"
                        "Lydia Rodarte-Quayle,Madrigal,Executive\n"
                        "Gale Boetticher,Los Pollos Hermanos,Assistant\n"
                        "Badger,Vamonos Pest,Lookout"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,business,role\n"
                "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                "Lyle,Los Pollos Hermanos,Shift Lead"
            ),
            "test_expected_csv": (
                "name,business,role\n"
                "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                "Lyle,Los Pollos Hermanos,Shift Lead\n"
                "Cynthia,Los Pollos Hermanos,Cashier\n"
                "Gale Boetticher,Los Pollos Hermanos,Assistant"
            ),
        },
        {
            "statement": "Get the buyer and amount for all completed deals.",
            "solution_code": 'deals[deals["status"] == "completed"][["buyer", "amount"]]',
            "hint": "First filter rows with boolean indexing, then select columns with double brackets.",
            "category": "filter-select",
            "tables": [
                {
                    "name": "deals",
                    "display_csv": (
                        "deal_id,buyer,amount,status\n"
                        "1,Tuco,75000,completed\n"
                        "2,Gus,500000,completed\n"
                        "3,Declan,120000,pending\n"
                        "4,Lydia,300000,completed\n"
                        "5,Jack,80000,cancelled"
                    ),
                    "test_csv": (
                        "deal_id,buyer,amount,status\n"
                        "1,Tuco,75000,completed\n"
                        "2,Gus,500000,completed\n"
                        "3,Declan,120000,pending\n"
                        "4,Lydia,300000,completed\n"
                        "5,Jack,80000,cancelled\n"
                        "6,Krazy-8,25000,completed\n"
                        "7,Badger,15000,pending\n"
                        "8,Gus,450000,completed\n"
                        "9,Declan,200000,cancelled\n"
                        "10,Lydia,350000,completed"
                    ),
                }
            ],
            "display_expected_csv": (
                "buyer,amount\n"
                "Tuco,75000\n"
                "Gus,500000\n"
                "Lydia,300000"
            ),
            "test_expected_csv": (
                "buyer,amount\n"
                "Tuco,75000\n"
                "Gus,500000\n"
                "Lydia,300000\n"
                "Krazy-8,25000\n"
                "Gus,450000\n"
                "Lydia,350000"
            ),
        },
        {
            "statement": "Get the unique locations from the laundering table as a DataFrame. Skyler needs an overview.",
            "solution_code": 'laundering[["location"]].drop_duplicates()',
            "hint": "Select the column with double brackets to keep it as a DataFrame, then use .drop_duplicates().",
            "category": "drop-duplicates",
            "tables": [
                {
                    "name": "laundering",
                    "display_csv": (
                        "date,location,amount\n"
                        "2009-03-15,A1A Car Wash,5000\n"
                        "2009-04-01,Nail Salon,8000\n"
                        "2009-04-15,A1A Car Wash,12000\n"
                        "2009-05-01,Laser Tag,3000\n"
                        "2009-05-15,A1A Car Wash,15000\n"
                        "2009-06-01,Nail Salon,9000"
                    ),
                    "test_csv": (
                        "date,location,amount\n"
                        "2009-03-15,A1A Car Wash,5000\n"
                        "2009-04-01,Nail Salon,8000\n"
                        "2009-04-15,A1A Car Wash,12000\n"
                        "2009-05-01,Laser Tag,3000\n"
                        "2009-05-15,A1A Car Wash,15000\n"
                        "2009-06-01,Nail Salon,9000\n"
                        "2009-06-15,Danny's,4500\n"
                        "2009-07-01,A1A Car Wash,18000\n"
                        "2009-07-15,Danny's,6000\n"
                        "2009-08-01,Laser Tag,3500"
                    ),
                }
            ],
            "display_expected_csv": (
                "location\n"
                "A1A Car Wash\n"
                "Nail Salon\n"
                "Laser Tag"
            ),
            "test_expected_csv": (
                "location\n"
                "A1A Car Wash\n"
                "Nail Salon\n"
                "Laser Tag\n"
                "Danny's"
            ),
        },
        {
            "statement": "Hank is investigating. Get suspects with a risk_level above 5 and more than 10 pieces of evidence.",
            "solution_code": 'evidence[(evidence["risk_level"] > 5) & (evidence["evidence_count"] > 10)]',
            "hint": "Combine conditions with & and wrap each condition in parentheses: df[(cond1) & (cond2)].",
            "category": "filter-multiple",
            "tables": [
                {
                    "name": "evidence",
                    "display_csv": (
                        "suspect,risk_level,evidence_count\n"
                        "Walter White,3,12\n"
                        "Jesse Pinkman,7,8\n"
                        "Gustavo Fring,9,15\n"
                        "Saul Goodman,5,6\n"
                        "Mike Ehrmantraut,8,11"
                    ),
                    "test_csv": (
                        "suspect,risk_level,evidence_count\n"
                        "Walter White,3,12\n"
                        "Jesse Pinkman,7,8\n"
                        "Gustavo Fring,9,15\n"
                        "Saul Goodman,5,6\n"
                        "Mike Ehrmantraut,8,11\n"
                        "Tuco Salamanca,10,4\n"
                        "Hector Salamanca,6,13\n"
                        "Lydia Rodarte-Quayle,7,9\n"
                        "Todd Alquist,8,14\n"
                        "Jack Welker,9,7"
                    ),
                }
            ],
            "display_expected_csv": (
                "suspect,risk_level,evidence_count\n"
                "Gustavo Fring,9,15\n"
                "Mike Ehrmantraut,8,11"
            ),
            "test_expected_csv": (
                "suspect,risk_level,evidence_count\n"
                "Gustavo Fring,9,15\n"
                "Mike Ehrmantraut,8,11\n"
                "Hector Salamanca,6,13\n"
                "Todd Alquist,8,14"
            ),
        },
        {
            "statement": "Get all characters affiliated with Heisenberg or the Cartel.",
            "solution_code": 'characters[characters["affiliation"].isin(["Heisenberg", "Cartel"])]',
            "hint": 'Use df[df["column"].isin(["val1", "val2"])] to filter by multiple values.',
            "category": "filter-isin",
            "tables": [
                {
                    "name": "characters",
                    "display_csv": (
                        "name,affiliation,status\n"
                        "Walter White,Heisenberg,Active\n"
                        "Jesse Pinkman,Heisenberg,Active\n"
                        "Gustavo Fring,Cartel,Eliminated\n"
                        "Hank Schrader,DEA,Active\n"
                        "Tuco Salamanca,Cartel,Eliminated\n"
                        "Saul Goodman,Independent,Active"
                    ),
                    "test_csv": (
                        "name,affiliation,status\n"
                        "Walter White,Heisenberg,Active\n"
                        "Jesse Pinkman,Heisenberg,Active\n"
                        "Gustavo Fring,Cartel,Eliminated\n"
                        "Hank Schrader,DEA,Active\n"
                        "Tuco Salamanca,Cartel,Eliminated\n"
                        "Saul Goodman,Independent,Active\n"
                        "Hector Salamanca,Cartel,Eliminated\n"
                        "Skinny Pete,Heisenberg,Active\n"
                        "Steven Gomez,DEA,Active\n"
                        "Badger,Heisenberg,Active"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,affiliation,status\n"
                "Walter White,Heisenberg,Active\n"
                "Jesse Pinkman,Heisenberg,Active\n"
                "Gustavo Fring,Cartel,Eliminated\n"
                "Tuco Salamanca,Cartel,Eliminated"
            ),
            "test_expected_csv": (
                "name,affiliation,status\n"
                "Walter White,Heisenberg,Active\n"
                "Jesse Pinkman,Heisenberg,Active\n"
                "Gustavo Fring,Cartel,Eliminated\n"
                "Tuco Salamanca,Cartel,Eliminated\n"
                "Hector Salamanca,Cartel,Eliminated\n"
                "Skinny Pete,Heisenberg,Active\n"
                "Badger,Heisenberg,Active"
            ),
        },
    ],
    2: [
        {
            "statement": "Sort the cases table by billing_hours in descending order.",
            "solution_code": 'cases.sort_values("billing_hours", ascending=False)',
            "hint": "Use df.sort_values('column', ascending=False) to sort descending.",
            "category": "sort",
            "tables": [
                {
                    "name": "cases",
                    "display_csv": (
                        "case,client,billing_hours\n"
                        "Sandpiper,Elderly Residents,145\n"
                        "Mesa Verde,Kevin Wachtell,82\n"
                        "Kettleman,Craig Kettleman,12\n"
                        "Tuco Defense,Tuco Salamanca,8\n"
                        "Hoboken Squat,Mrs. Strauss,3"
                    ),
                    "test_csv": (
                        "case,client,billing_hours\n"
                        "Sandpiper,Elderly Residents,145\n"
                        "Mesa Verde,Kevin Wachtell,82\n"
                        "Kettleman,Craig Kettleman,12\n"
                        "Tuco Defense,Tuco Salamanca,8\n"
                        "Hoboken Squat,Mrs. Strauss,3\n"
                        "Lalo Bail,Lalo Salamanca,6\n"
                        "Huell Arrest,Huell Babineaux,15\n"
                        "Acker Property,Mr. Acker,28"
                    ),
                }
            ],
            "display_expected_csv": (
                "case,client,billing_hours\n"
                "Sandpiper,Elderly Residents,145\n"
                "Mesa Verde,Kevin Wachtell,82\n"
                "Kettleman,Craig Kettleman,12\n"
                "Tuco Defense,Tuco Salamanca,8\n"
                "Hoboken Squat,Mrs. Strauss,3"
            ),
            "test_expected_csv": (
                "case,client,billing_hours\n"
                "Sandpiper,Elderly Residents,145\n"
                "Mesa Verde,Kevin Wachtell,82\n"
                "Acker Property,Mr. Acker,28\n"
                "Huell Arrest,Huell Babineaux,15\n"
                "Kettleman,Craig Kettleman,12\n"
                "Tuco Defense,Tuco Salamanca,8\n"
                "Lalo Bail,Lalo Salamanca,6\n"
                "Hoboken Squat,Mrs. Strauss,3"
            ),
        },
        {
            "statement": "Calculate the total billing_amount per lawyer from the invoices table.",
            "solution_code": 'invoices.groupby("lawyer")["billing_amount"].sum().reset_index()',
            "hint": "Use df.groupby('column')['value_column'].sum().reset_index().",
            "category": "groupby-sum",
            "tables": [
                {
                    "name": "invoices",
                    "display_csv": (
                        "invoice_id,lawyer,client,billing_amount\n"
                        "1,Jimmy McGill,Mrs. Strauss,450\n"
                        "2,Kim Wexler,Mesa Verde,8200\n"
                        "3,Jimmy McGill,Craig Kettleman,1500\n"
                        "4,Howard Hamlin,Sandpiper,12000\n"
                        "5,Kim Wexler,Acker,3400\n"
                        "6,Jimmy McGill,Tuco Salamanca,700"
                    ),
                    "test_csv": (
                        "invoice_id,lawyer,client,billing_amount\n"
                        "1,Jimmy McGill,Mrs. Strauss,450\n"
                        "2,Kim Wexler,Mesa Verde,8200\n"
                        "3,Jimmy McGill,Craig Kettleman,1500\n"
                        "4,Howard Hamlin,Sandpiper,12000\n"
                        "5,Kim Wexler,Acker,3400\n"
                        "6,Jimmy McGill,Tuco Salamanca,700\n"
                        "7,Howard Hamlin,Mesa Verde,9500\n"
                        "8,Kim Wexler,Sandpiper,6100\n"
                        "9,Jimmy McGill,Huell Babineaux,800\n"
                        "10,Howard Hamlin,Kettleman,4200"
                    ),
                }
            ],
            "display_expected_csv": (
                "lawyer,billing_amount\n"
                "Howard Hamlin,12000\n"
                "Jimmy McGill,2650\n"
                "Kim Wexler,11600"
            ),
            "test_expected_csv": (
                "lawyer,billing_amount\n"
                "Howard Hamlin,25700\n"
                "Jimmy McGill,3450\n"
                "Kim Wexler,17700"
            ),
        },
        {
            "statement": "Merge the lawyers and firms tables on firm_id to see which firm each lawyer belongs to.",
            "solution_code": 'lawyers.merge(firms, on="firm_id")',
            "hint": "Use df1.merge(df2, on='shared_column') to join two tables.",
            "category": "merge",
            "tables": [
                {
                    "name": "lawyers",
                    "display_csv": (
                        "name,firm_id,specialty\n"
                        "Jimmy McGill,1,Criminal\n"
                        "Kim Wexler,2,Banking\n"
                        "Howard Hamlin,2,Litigation\n"
                        "Chuck McGill,2,Constitutional"
                    ),
                    "test_csv": (
                        "name,firm_id,specialty\n"
                        "Jimmy McGill,1,Criminal\n"
                        "Kim Wexler,2,Banking\n"
                        "Howard Hamlin,2,Litigation\n"
                        "Chuck McGill,2,Constitutional\n"
                        "Rich Schweikart,3,Corporate\n"
                        "Clifford Main,4,Litigation\n"
                        "Erin Brill,4,Compliance"
                    ),
                },
                {
                    "name": "firms",
                    "display_csv": (
                        "firm_id,firm_name\n"
                        "1,Davis & Main\n"
                        "2,HHM"
                    ),
                    "test_csv": (
                        "firm_id,firm_name\n"
                        "1,Davis & Main\n"
                        "2,HHM\n"
                        "3,Schweikart & Cokely\n"
                        "4,Davis & Main"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,firm_id,specialty,firm_name\n"
                "Jimmy McGill,1,Criminal,Davis & Main\n"
                "Kim Wexler,2,Banking,HHM\n"
                "Howard Hamlin,2,Litigation,HHM\n"
                "Chuck McGill,2,Constitutional,HHM"
            ),
            "test_expected_csv": (
                "name,firm_id,specialty,firm_name\n"
                "Jimmy McGill,1,Criminal,Davis & Main\n"
                "Kim Wexler,2,Banking,HHM\n"
                "Howard Hamlin,2,Litigation,HHM\n"
                "Chuck McGill,2,Constitutional,HHM\n"
                "Rich Schweikart,3,Corporate,Schweikart & Cokely\n"
                "Clifford Main,4,Litigation,Davis & Main\n"
                "Erin Brill,4,Compliance,Davis & Main"
            ),
        },
        {
            "statement": "Fill missing phone numbers in the directory table with the string Unknown.",
            "solution_code": 'directory.fillna({"phone": "Unknown"})',
            "hint": "Use df.fillna({'column': 'value'}) to fill missing values in a specific column.",
            "category": "fillna",
            "tables": [
                {
                    "name": "directory",
                    "display_csv": (
                        "name,phone,office\n"
                        "Jimmy McGill,505-842-5662,Strip Mall\n"
                        "Kim Wexler,505-242-7700,HHM\n"
                        "Mike Ehrmantraut,,Toll Booth\n"
                        "Nacho Varga,,Upholstery Shop"
                    ),
                    "test_csv": (
                        "name,phone,office\n"
                        "Jimmy McGill,505-842-5662,Strip Mall\n"
                        "Kim Wexler,505-242-7700,HHM\n"
                        "Mike Ehrmantraut,,Toll Booth\n"
                        "Nacho Varga,,Upholstery Shop\n"
                        "Howard Hamlin,505-242-7700,HHM\n"
                        "Chuck McGill,,Home\n"
                        "Lalo Salamanca,,Compound"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,phone,office\n"
                "Jimmy McGill,505-842-5662,Strip Mall\n"
                "Kim Wexler,505-242-7700,HHM\n"
                "Mike Ehrmantraut,Unknown,Toll Booth\n"
                "Nacho Varga,Unknown,Upholstery Shop"
            ),
            "test_expected_csv": (
                "name,phone,office\n"
                "Jimmy McGill,505-842-5662,Strip Mall\n"
                "Kim Wexler,505-242-7700,HHM\n"
                "Mike Ehrmantraut,Unknown,Toll Booth\n"
                "Nacho Varga,Unknown,Upholstery Shop\n"
                "Howard Hamlin,505-242-7700,HHM\n"
                "Chuck McGill,Unknown,Home\n"
                "Lalo Salamanca,Unknown,Compound"
            ),
        },
        {
            "statement": "Count how many cases each outcome has. Return as a DataFrame with columns outcome and count.",
            "solution_code": 'verdicts["outcome"].value_counts().reset_index()',
            "hint": "Use df['column'].value_counts().reset_index() to count occurrences.",
            "category": "value-counts",
            "tables": [
                {
                    "name": "verdicts",
                    "display_csv": (
                        "case_id,defendant,outcome\n"
                        "1,Craig Kettleman,Plea Deal\n"
                        "2,Tuco Salamanca,Acquitted\n"
                        "3,Huell Babineaux,Dismissed\n"
                        "4,Daniel Wormald,Plea Deal\n"
                        "5,Mrs. Strauss,Won"
                    ),
                    "test_csv": (
                        "case_id,defendant,outcome\n"
                        "1,Craig Kettleman,Plea Deal\n"
                        "2,Tuco Salamanca,Acquitted\n"
                        "3,Huell Babineaux,Dismissed\n"
                        "4,Daniel Wormald,Plea Deal\n"
                        "5,Mrs. Strauss,Won\n"
                        "6,Lalo Salamanca,Acquitted\n"
                        "7,Acker,Dismissed\n"
                        "8,Fred Whalen,Plea Deal\n"
                        "9,Everett Acker,Won\n"
                        "10,Jesse Pinkman,Plea Deal"
                    ),
                }
            ],
            "display_expected_csv": (
                "outcome,count\n"
                "Plea Deal,2\n"
                "Acquitted,1\n"
                "Dismissed,1\n"
                "Won,1"
            ),
            "test_expected_csv": (
                "outcome,count\n"
                "Plea Deal,4\n"
                "Acquitted,2\n"
                "Dismissed,2\n"
                "Won,2"
            ),
        },
        {
            "statement": "Get the top 3 clients by total_billed from the accounts table.",
            "solution_code": 'accounts.nlargest(3, "total_billed")',
            "hint": "Use df.nlargest(n, 'column') to get the top n rows by a column.",
            "category": "nlargest",
            "tables": [
                {
                    "name": "accounts",
                    "display_csv": (
                        "client,total_billed,status\n"
                        "Mesa Verde,48000,Active\n"
                        "Sandpiper,125000,Settled\n"
                        "Kettleman,3200,Closed\n"
                        "Acker,15000,Active\n"
                        "Mrs. Strauss,900,Closed"
                    ),
                    "test_csv": (
                        "client,total_billed,status\n"
                        "Mesa Verde,48000,Active\n"
                        "Sandpiper,125000,Settled\n"
                        "Kettleman,3200,Closed\n"
                        "Acker,15000,Active\n"
                        "Mrs. Strauss,900,Closed\n"
                        "Lalo Salamanca,7500,Active\n"
                        "Huell Babineaux,2800,Closed\n"
                        "Daniel Wormald,1200,Closed"
                    ),
                }
            ],
            "display_expected_csv": (
                "client,total_billed,status\n"
                "Sandpiper,125000,Settled\n"
                "Mesa Verde,48000,Active\n"
                "Acker,15000,Active"
            ),
            "test_expected_csv": (
                "client,total_billed,status\n"
                "Sandpiper,125000,Settled\n"
                "Mesa Verde,48000,Active\n"
                "Acker,15000,Active"
            ),
        },
        {
            "statement": "Calculate the mean billing_rate per department from the staff table.",
            "solution_code": 'staff.groupby("department")["billing_rate"].mean().reset_index()',
            "hint": "Use df.groupby('column')['value_column'].mean().reset_index().",
            "category": "groupby-mean",
            "tables": [
                {
                    "name": "staff",
                    "display_csv": (
                        "name,department,billing_rate\n"
                        "Jimmy McGill,Associates,200\n"
                        "Kim Wexler,Associates,250\n"
                        "Howard Hamlin,Partners,450\n"
                        "Chuck McGill,Partners,500\n"
                        "Ernesto,Mailroom,50\n"
                        "Omar,Mailroom,50"
                    ),
                    "test_csv": (
                        "name,department,billing_rate\n"
                        "Jimmy McGill,Associates,200\n"
                        "Kim Wexler,Associates,250\n"
                        "Howard Hamlin,Partners,450\n"
                        "Chuck McGill,Partners,500\n"
                        "Ernesto,Mailroom,50\n"
                        "Omar,Mailroom,50\n"
                        "Rich Schweikart,Partners,475\n"
                        "Erin Brill,Associates,180\n"
                        "Viola Goto,Associates,190\n"
                        "Clifford Main,Partners,460"
                    ),
                }
            ],
            "display_expected_csv": (
                "department,billing_rate\n"
                "Associates,225.0\n"
                "Mailroom,50.0\n"
                "Partners,475.0"
            ),
            "test_expected_csv": (
                "department,billing_rate\n"
                "Associates,205.0\n"
                "Mailroom,50.0\n"
                "Partners,471.25"
            ),
        },
        {
            "statement": "Replace all occurrences of Slippin' Jimmy with Saul Goodman in the name column of the aliases table.",
            "solution_code": "aliases.replace({\"name\": {\"Slippin' Jimmy\": \"Saul Goodman\"}})",
            "hint": "Use df.replace({'column': {'old_value': 'new_value'}}).",
            "category": "replace",
            "tables": [
                {
                    "name": "aliases",
                    "display_csv": (
                        "name,document,year\n"
                        "Slippin' Jimmy,Bar Application,2002\n"
                        "Jimmy McGill,HHM Contract,2003\n"
                        "Slippin' Jimmy,Court Filing,2004\n"
                        "Jimmy McGill,Davis & Main Offer,2005"
                    ),
                    "test_csv": (
                        "name,document,year\n"
                        "Slippin' Jimmy,Bar Application,2002\n"
                        "Jimmy McGill,HHM Contract,2003\n"
                        "Slippin' Jimmy,Court Filing,2004\n"
                        "Jimmy McGill,Davis & Main Offer,2005\n"
                        "Slippin' Jimmy,Insurance Claim,2006\n"
                        "Jimmy McGill,Mesa Verde Brief,2007\n"
                        "Slippin' Jimmy,Elder Law Ad,2008"
                    ),
                }
            ],
            "display_expected_csv": (
                "name,document,year\n"
                "Saul Goodman,Bar Application,2002\n"
                "Jimmy McGill,HHM Contract,2003\n"
                "Saul Goodman,Court Filing,2004\n"
                "Jimmy McGill,Davis & Main Offer,2005"
            ),
            "test_expected_csv": (
                "name,document,year\n"
                "Saul Goodman,Bar Application,2002\n"
                "Jimmy McGill,HHM Contract,2003\n"
                "Saul Goodman,Court Filing,2004\n"
                "Jimmy McGill,Davis & Main Offer,2005\n"
                "Saul Goodman,Insurance Claim,2006\n"
                "Jimmy McGill,Mesa Verde Brief,2007\n"
                "Saul Goodman,Elder Law Ad,2008"
            ),
        },
        {
            "statement": "Merge cases and lawyers on lawyer_id, then select just the case_name and lawyer_name columns.",
            "solution_code": 'cases.merge(lawyers, on="lawyer_id")[["case_name", "lawyer_name"]]',
            "hint": "First merge the two tables, then select the columns you need with double brackets.",
            "category": "merge-select",
            "tables": [
                {
                    "name": "cases",
                    "display_csv": (
                        "case_name,lawyer_id,status\n"
                        "Sandpiper,1,Active\n"
                        "Mesa Verde,2,Active\n"
                        "Kettleman,3,Closed\n"
                        "Tuco Defense,3,Closed"
                    ),
                    "test_csv": (
                        "case_name,lawyer_id,status\n"
                        "Sandpiper,1,Active\n"
                        "Mesa Verde,2,Active\n"
                        "Kettleman,3,Closed\n"
                        "Tuco Defense,3,Closed\n"
                        "Acker,2,Active\n"
                        "Huell,3,Closed\n"
                        "Lalo Bail,3,Active"
                    ),
                },
                {
                    "name": "lawyers",
                    "display_csv": (
                        "lawyer_id,lawyer_name\n"
                        "1,Chuck McGill\n"
                        "2,Kim Wexler\n"
                        "3,Jimmy McGill"
                    ),
                    "test_csv": (
                        "lawyer_id,lawyer_name\n"
                        "1,Chuck McGill\n"
                        "2,Kim Wexler\n"
                        "3,Jimmy McGill"
                    ),
                }
            ],
            "display_expected_csv": (
                "case_name,lawyer_name\n"
                "Sandpiper,Chuck McGill\n"
                "Mesa Verde,Kim Wexler\n"
                "Kettleman,Jimmy McGill\n"
                "Tuco Defense,Jimmy McGill"
            ),
            "test_expected_csv": (
                "case_name,lawyer_name\n"
                "Sandpiper,Chuck McGill\n"
                "Mesa Verde,Kim Wexler\n"
                "Kettleman,Jimmy McGill\n"
                "Tuco Defense,Jimmy McGill\n"
                "Acker,Kim Wexler\n"
                "Huell,Jimmy McGill\n"
                "Lalo Bail,Jimmy McGill"
            ),
        },
        {
            "statement": "Count the number of employees per firm from the payroll table. Return columns firm and name.",
            "solution_code": 'payroll.groupby("firm")["name"].count().reset_index()',
            "hint": "Use df.groupby('column')['other_column'].count().reset_index().",
            "category": "groupby-count",
            "tables": [
                {
                    "name": "payroll",
                    "display_csv": (
                        "name,firm,salary\n"
                        "Jimmy McGill,Davis & Main,45000\n"
                        "Kim Wexler,HHM,62000\n"
                        "Howard Hamlin,HHM,180000\n"
                        "Chuck McGill,HHM,250000\n"
                        "Clifford Main,Davis & Main,195000\n"
                        "Erin Brill,Davis & Main,58000"
                    ),
                    "test_csv": (
                        "name,firm,salary\n"
                        "Jimmy McGill,Davis & Main,45000\n"
                        "Kim Wexler,HHM,62000\n"
                        "Howard Hamlin,HHM,180000\n"
                        "Chuck McGill,HHM,250000\n"
                        "Clifford Main,Davis & Main,195000\n"
                        "Erin Brill,Davis & Main,58000\n"
                        "Rich Schweikart,Schweikart & Cokely,200000\n"
                        "Viola Goto,Schweikart & Cokely,55000\n"
                        "Ernesto,HHM,32000\n"
                        "Omar,HHM,30000"
                    ),
                }
            ],
            "display_expected_csv": (
                "firm,name\n"
                "Davis & Main,3\n"
                "HHM,3"
            ),
            "test_expected_csv": (
                "firm,name\n"
                "Davis & Main,3\n"
                "HHM,5\n"
                "Schweikart & Cokely,2"
            ),
        },
    ],
}
