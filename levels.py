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
                    "csv": (
                        "name,alias,role,city\n"
                        "Walter White,Heisenberg,Cook,Albuquerque\n"
                        "Jesse Pinkman,Cap'n Cook,Cook,Albuquerque\n"
                        "Gustavo Fring,Gus,Distributor,Albuquerque\n"
                        "Saul Goodman,Jimmy McGill,Lawyer,Albuquerque\n"
                        "Mike Ehrmantraut,The Guy,Fixer,Albuquerque"
                    ),
                }
            ],
            "expected_csv": (
                "name,alias\n"
                "Walter White,Heisenberg\n"
                "Jesse Pinkman,Cap'n Cook\n"
                "Gustavo Fring,Gus\n"
                "Saul Goodman,Jimmy McGill\n"
                "Mike Ehrmantraut,The Guy"
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
                    "csv": (
                        "batch_id,product,purity,weight_kg\n"
                        "1,Blue Sky,99.1,25\n"
                        "2,Blue Sky,96.2,30\n"
                        "3,Chili P,72.4,15\n"
                        "4,Blue Sky,98.8,20\n"
                        "5,Blue Sky,91.3,28"
                    ),
                }
            ],
            "expected_csv": (
                "batch_id,product,purity,weight_kg\n"
                "1,Blue Sky,99.1,25\n"
                "2,Blue Sky,96.2,30\n"
                "4,Blue Sky,98.8,20"
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
                    "csv": (
                        "name,phone,burner_phone,city\n"
                        "Walter White,555-0101,555-9901,Albuquerque\n"
                        "Jesse Pinkman,555-0102,555-9902,Albuquerque\n"
                        "Gustavo Fring,555-0103,555-9903,Albuquerque\n"
                        "Saul Goodman,555-0104,555-9904,Albuquerque"
                    ),
                }
            ],
            "expected_csv": (
                "name,phone,city\n"
                "Walter White,555-0101,Albuquerque\n"
                "Jesse Pinkman,555-0102,Albuquerque\n"
                "Gustavo Fring,555-0103,Albuquerque\n"
                "Saul Goodman,555-0104,Albuquerque"
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
                    "csv": (
                        "chemical,qty,unit_price\n"
                        "Methylamine,50,15000\n"
                        "Pseudoephedrine,200,25\n"
                        "Red Phosphorus,30,150\n"
                        "Hydriodic Acid,20,500"
                    ),
                }
            ],
            "expected_csv": (
                "chemical,quantity,unit_price\n"
                "Methylamine,50,15000\n"
                "Pseudoephedrine,200,25\n"
                "Red Phosphorus,30,150\n"
                "Hydriodic Acid,20,500"
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
                    "csv": (
                        "territory,price_per_pound,pounds\n"
                        "Albuquerque,40000,5\n"
                        "Phoenix,35000,3\n"
                        "Denver,38000,4\n"
                        "El Paso,42000,2"
                    ),
                }
            ],
            "expected_csv": (
                "territory,price_per_pound,pounds,revenue\n"
                "Albuquerque,40000,5,200000\n"
                "Phoenix,35000,3,105000\n"
                "Denver,38000,4,152000\n"
                "El Paso,42000,2,84000"
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
                    "csv": (
                        "name,business,role\n"
                        "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                        "Lyle,Los Pollos Hermanos,Shift Lead\n"
                        "Jesse Pinkman,Vamonos Pest,Technician\n"
                        "Walter White,Vamonos Pest,Technician\n"
                        "Mike Ehrmantraut,Madrigal,Consultant"
                    ),
                }
            ],
            "expected_csv": (
                "name,business,role\n"
                "Gustavo Fring,Los Pollos Hermanos,Manager\n"
                "Lyle,Los Pollos Hermanos,Shift Lead"
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
                    "csv": (
                        "deal_id,buyer,amount,status\n"
                        "1,Tuco,75000,completed\n"
                        "2,Gus,500000,completed\n"
                        "3,Declan,120000,pending\n"
                        "4,Lydia,300000,completed\n"
                        "5,Jack,80000,cancelled"
                    ),
                }
            ],
            "expected_csv": (
                "buyer,amount\n"
                "Tuco,75000\n"
                "Gus,500000\n"
                "Lydia,300000"
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
                    "csv": (
                        "date,location,amount\n"
                        "2009-03-15,A1A Car Wash,5000\n"
                        "2009-04-01,Nail Salon,8000\n"
                        "2009-04-15,A1A Car Wash,12000\n"
                        "2009-05-01,Laser Tag,3000\n"
                        "2009-05-15,A1A Car Wash,15000\n"
                        "2009-06-01,Nail Salon,9000"
                    ),
                }
            ],
            "expected_csv": (
                "location\n"
                "A1A Car Wash\n"
                "Nail Salon\n"
                "Laser Tag"
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
                    "csv": (
                        "suspect,risk_level,evidence_count\n"
                        "Walter White,3,12\n"
                        "Jesse Pinkman,7,8\n"
                        "Gustavo Fring,9,15\n"
                        "Saul Goodman,5,6\n"
                        "Mike Ehrmantraut,8,11"
                    ),
                }
            ],
            "expected_csv": (
                "suspect,risk_level,evidence_count\n"
                "Gustavo Fring,9,15\n"
                "Mike Ehrmantraut,8,11"
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
                    "csv": (
                        "name,affiliation,status\n"
                        "Walter White,Heisenberg,Active\n"
                        "Jesse Pinkman,Heisenberg,Active\n"
                        "Gustavo Fring,Cartel,Eliminated\n"
                        "Hank Schrader,DEA,Active\n"
                        "Tuco Salamanca,Cartel,Eliminated\n"
                        "Saul Goodman,Independent,Active"
                    ),
                }
            ],
            "expected_csv": (
                "name,affiliation,status\n"
                "Walter White,Heisenberg,Active\n"
                "Jesse Pinkman,Heisenberg,Active\n"
                "Gustavo Fring,Cartel,Eliminated\n"
                "Tuco Salamanca,Cartel,Eliminated"
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
                    "csv": (
                        "case,client,billing_hours\n"
                        "Sandpiper,Elderly Residents,145\n"
                        "Mesa Verde,Kevin Wachtell,82\n"
                        "Kettleman,Craig Kettleman,12\n"
                        "Tuco Defense,Tuco Salamanca,8\n"
                        "Hoboken Squat,Mrs. Strauss,3"
                    ),
                }
            ],
            "expected_csv": (
                "case,client,billing_hours\n"
                "Sandpiper,Elderly Residents,145\n"
                "Mesa Verde,Kevin Wachtell,82\n"
                "Kettleman,Craig Kettleman,12\n"
                "Tuco Defense,Tuco Salamanca,8\n"
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
                    "csv": (
                        "invoice_id,lawyer,client,billing_amount\n"
                        "1,Jimmy McGill,Mrs. Strauss,450\n"
                        "2,Kim Wexler,Mesa Verde,8200\n"
                        "3,Jimmy McGill,Craig Kettleman,1500\n"
                        "4,Howard Hamlin,Sandpiper,12000\n"
                        "5,Kim Wexler,Acker,3400\n"
                        "6,Jimmy McGill,Tuco Salamanca,700"
                    ),
                }
            ],
            "expected_csv": (
                "lawyer,billing_amount\n"
                "Howard Hamlin,12000\n"
                "Jimmy McGill,2650\n"
                "Kim Wexler,11600"
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
                    "csv": (
                        "name,firm_id,specialty\n"
                        "Jimmy McGill,1,Criminal\n"
                        "Kim Wexler,2,Banking\n"
                        "Howard Hamlin,2,Litigation\n"
                        "Chuck McGill,2,Constitutional"
                    ),
                },
                {
                    "name": "firms",
                    "csv": (
                        "firm_id,firm_name\n"
                        "1,Davis & Main\n"
                        "2,HHM"
                    ),
                }
            ],
            "expected_csv": (
                "name,firm_id,specialty,firm_name\n"
                "Jimmy McGill,1,Criminal,Davis & Main\n"
                "Kim Wexler,2,Banking,HHM\n"
                "Howard Hamlin,2,Litigation,HHM\n"
                "Chuck McGill,2,Constitutional,HHM"
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
                    "csv": (
                        "name,phone,office\n"
                        "Jimmy McGill,505-842-5662,Strip Mall\n"
                        "Kim Wexler,505-242-7700,HHM\n"
                        "Mike Ehrmantraut,,Toll Booth\n"
                        "Nacho Varga,,Upholstery Shop"
                    ),
                }
            ],
            "expected_csv": (
                "name,phone,office\n"
                "Jimmy McGill,505-842-5662,Strip Mall\n"
                "Kim Wexler,505-242-7700,HHM\n"
                "Mike Ehrmantraut,Unknown,Toll Booth\n"
                "Nacho Varga,Unknown,Upholstery Shop"
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
                    "csv": (
                        "case_id,defendant,outcome\n"
                        "1,Craig Kettleman,Plea Deal\n"
                        "2,Tuco Salamanca,Acquitted\n"
                        "3,Huell Babineaux,Dismissed\n"
                        "4,Daniel Wormald,Plea Deal\n"
                        "5,Mrs. Strauss,Won"
                    ),
                }
            ],
            "expected_csv": (
                "outcome,count\n"
                "Plea Deal,2\n"
                "Acquitted,1\n"
                "Dismissed,1\n"
                "Won,1"
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
                    "csv": (
                        "client,total_billed,status\n"
                        "Mesa Verde,48000,Active\n"
                        "Sandpiper,125000,Settled\n"
                        "Kettleman,3200,Closed\n"
                        "Acker,15000,Active\n"
                        "Mrs. Strauss,900,Closed"
                    ),
                }
            ],
            "expected_csv": (
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
                    "csv": (
                        "name,department,billing_rate\n"
                        "Jimmy McGill,Associates,200\n"
                        "Kim Wexler,Associates,250\n"
                        "Howard Hamlin,Partners,450\n"
                        "Chuck McGill,Partners,500\n"
                        "Ernesto,Mailroom,50\n"
                        "Omar,Mailroom,50"
                    ),
                }
            ],
            "expected_csv": (
                "department,billing_rate\n"
                "Associates,225.0\n"
                "Mailroom,50.0\n"
                "Partners,475.0"
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
                    "csv": (
                        "name,document,year\n"
                        "Slippin' Jimmy,Bar Application,2002\n"
                        "Jimmy McGill,HHM Contract,2003\n"
                        "Slippin' Jimmy,Court Filing,2004\n"
                        "Jimmy McGill,Davis & Main Offer,2005"
                    ),
                }
            ],
            "expected_csv": (
                "name,document,year\n"
                "Saul Goodman,Bar Application,2002\n"
                "Jimmy McGill,HHM Contract,2003\n"
                "Saul Goodman,Court Filing,2004\n"
                "Jimmy McGill,Davis & Main Offer,2005"
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
                    "csv": (
                        "case_name,lawyer_id,status\n"
                        "Sandpiper,1,Active\n"
                        "Mesa Verde,2,Active\n"
                        "Kettleman,3,Closed\n"
                        "Tuco Defense,3,Closed"
                    ),
                },
                {
                    "name": "lawyers",
                    "csv": (
                        "lawyer_id,lawyer_name\n"
                        "1,Chuck McGill\n"
                        "2,Kim Wexler\n"
                        "3,Jimmy McGill"
                    ),
                }
            ],
            "expected_csv": (
                "case_name,lawyer_name\n"
                "Sandpiper,Chuck McGill\n"
                "Mesa Verde,Kim Wexler\n"
                "Kettleman,Jimmy McGill\n"
                "Tuco Defense,Jimmy McGill"
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
                    "csv": (
                        "name,firm,salary\n"
                        "Jimmy McGill,Davis & Main,45000\n"
                        "Kim Wexler,HHM,62000\n"
                        "Howard Hamlin,HHM,180000\n"
                        "Chuck McGill,HHM,250000\n"
                        "Clifford Main,Davis & Main,195000\n"
                        "Erin Brill,Davis & Main,58000"
                    ),
                }
            ],
            "expected_csv": (
                "firm,name\n"
                "Davis & Main,3\n"
                "HHM,3"
            ),
        },
    ],
    3: [
        {
            "statement": "Pivot the vitals table so each metric becomes a column, with patient as the index.",
            "solution_code": 'vitals.pivot(index="patient", columns="metric", values="value").reset_index()',
            "hint": "Use df.pivot(index=..., columns=..., values=...).reset_index().",
            "category": "pivot",
            "tables": [
                {
                    "name": "vitals",
                    "csv": (
                        "patient,metric,value\n"
                        "Rebecca Adler,heart_rate,110\n"
                        "Rebecca Adler,temperature,101.3\n"
                        "Rebecca Adler,bp_systolic,85\n"
                        "John Henry Giles,heart_rate,95\n"
                        "John Henry Giles,temperature,99.1\n"
                        "John Henry Giles,bp_systolic,140"
                    ),
                }
            ],
            "expected_csv": (
                "patient,bp_systolic,heart_rate,temperature\n"
                "John Henry Giles,140.0,95.0,99.1\n"
                "Rebecca Adler,85.0,110.0,101.3"
            ),
        },
        {
            "statement": "Melt the lab_results table so that the test columns (white_cells, creatinine, sodium) become rows. Keep patient as the identifier. Name the variable column test and the value column result.",
            "solution_code": 'lab_results.melt(id_vars="patient", var_name="test", value_name="result")',
            "hint": "Use df.melt(id_vars='id_col', var_name='name', value_name='value').",
            "category": "melt",
            "tables": [
                {
                    "name": "lab_results",
                    "csv": (
                        "patient,white_cells,creatinine,sodium\n"
                        "Rebecca Adler,12.4,1.1,138\n"
                        "John Henry Giles,8.2,2.8,141\n"
                        "Chi Park,6.1,0.9,140"
                    ),
                }
            ],
            "expected_csv": (
                "patient,test,result\n"
                "Rebecca Adler,white_cells,12.4\n"
                "John Henry Giles,white_cells,8.2\n"
                "Chi Park,white_cells,6.1\n"
                "Rebecca Adler,creatinine,1.1\n"
                "John Henry Giles,creatinine,2.8\n"
                "Chi Park,creatinine,0.9\n"
                "Rebecca Adler,sodium,138.0\n"
                "John Henry Giles,sodium,141.0\n"
                "Chi Park,sodium,140.0"
            ),
        },
        {
            "statement": "Extract the department from the staff_id column. The format is DEPT-NUMBER (e.g. DIAG-042). Add a department column with just the department prefix.",
            "solution_code": 'staff.assign(department=staff["staff_id"].str.split("-").str[0])',
            "hint": "Use .str.split('-').str[0] to get the part before the hyphen.",
            "category": "str-split",
            "tables": [
                {
                    "name": "staff",
                    "csv": (
                        "name,staff_id,salary\n"
                        "Gregory House,DIAG-001,250000\n"
                        "Lisa Cuddy,ADMIN-001,280000\n"
                        "James Wilson,ONCO-001,210000\n"
                        "Eric Foreman,DIAG-002,145000\n"
                        "Robert Chase,SURG-001,155000"
                    ),
                }
            ],
            "expected_csv": (
                "name,staff_id,salary,department\n"
                "Gregory House,DIAG-001,250000,DIAG\n"
                "Lisa Cuddy,ADMIN-001,280000,ADMIN\n"
                "James Wilson,ONCO-001,210000,ONCO\n"
                "Eric Foreman,DIAG-002,145000,DIAG\n"
                "Robert Chase,SURG-001,155000,SURG"
            ),
        },
        {
            "statement": "Filter the symptoms table to rows where the description contains the word 'pain' (case-insensitive).",
            "solution_code": 'symptoms[symptoms["description"].str.contains("pain", case=False)]',
            "hint": "Use df[df['column'].str.contains('word', case=False)] for case-insensitive search.",
            "category": "str-contains",
            "tables": [
                {
                    "name": "symptoms",
                    "csv": (
                        "patient,description,severity\n"
                        "Rebecca Adler,Severe chest pain,8\n"
                        "Rebecca Adler,Difficulty speaking,7\n"
                        "John Henry Giles,Abdominal pain and nausea,6\n"
                        "John Henry Giles,Blurred vision,5\n"
                        "Eve,Painful rash on legs,4\n"
                        "Eve,Fever and chills,7"
                    ),
                }
            ],
            "expected_csv": (
                "patient,description,severity\n"
                "Rebecca Adler,Severe chest pain,8\n"
                "John Henry Giles,Abdominal pain and nausea,6\n"
                "Eve,Painful rash on legs,4"
            ),
        },
        {
            "statement": "Rank the doctors by cases_solved in descending order. Add a rank column using the min method.",
            "solution_code": 'doctors.assign(rank=doctors["cases_solved"].rank(method="min", ascending=False).astype(int))',
            "hint": "Use df['col'].rank(method='min', ascending=False) and .astype(int).",
            "category": "rank",
            "tables": [
                {
                    "name": "doctors",
                    "csv": (
                        "name,department,cases_solved\n"
                        "Gregory House,Diagnostics,847\n"
                        "James Wilson,Oncology,312\n"
                        "Eric Foreman,Diagnostics,201\n"
                        "Robert Chase,Surgery,189\n"
                        "Allison Cameron,Immunology,176"
                    ),
                }
            ],
            "expected_csv": (
                "name,department,cases_solved,rank\n"
                "Gregory House,Diagnostics,847,1\n"
                "James Wilson,Oncology,312,2\n"
                "Eric Foreman,Diagnostics,201,3\n"
                "Robert Chase,Surgery,189,4\n"
                "Allison Cameron,Immunology,176,5"
            ),
        },
        {
            "statement": "Calculate the cumulative sum of dosage_mg for each patient, ordered by day. Add it as a column called total_dosage.",
            "solution_code": 'prescriptions.assign(total_dosage=prescriptions.groupby("patient")["dosage_mg"].cumsum())',
            "hint": "Use df.groupby('col')['val'].cumsum() for a cumulative sum within groups.",
            "category": "cumsum",
            "tables": [
                {
                    "name": "prescriptions",
                    "csv": (
                        "patient,day,drug,dosage_mg\n"
                        "Rebecca Adler,1,Prednisone,60\n"
                        "Rebecca Adler,2,Prednisone,60\n"
                        "Rebecca Adler,3,Prednisone,40\n"
                        "John Henry Giles,1,Interferon,200\n"
                        "John Henry Giles,2,Interferon,200\n"
                        "John Henry Giles,3,Interferon,150"
                    ),
                }
            ],
            "expected_csv": (
                "patient,day,drug,dosage_mg,total_dosage\n"
                "Rebecca Adler,1,Prednisone,60,60\n"
                "Rebecca Adler,2,Prednisone,60,120\n"
                "Rebecca Adler,3,Prednisone,40,160\n"
                "John Henry Giles,1,Interferon,200,200\n"
                "John Henry Giles,2,Interferon,200,400\n"
                "John Henry Giles,3,Interferon,150,550"
            ),
        },
        {
            "statement": "Calculate each doctor's cases_solved as a percentage of their department's total. Add it as a pct column, rounded to 1 decimal place.",
            "solution_code": 'doctors.assign(pct=(doctors["cases_solved"] / doctors.groupby("department")["cases_solved"].transform("sum") * 100).round(1))',
            "hint": "Use groupby().transform('sum') to get the group total, then divide and multiply by 100.",
            "category": "transform",
            "tables": [
                {
                    "name": "doctors",
                    "csv": (
                        "name,department,cases_solved\n"
                        "Gregory House,Diagnostics,120\n"
                        "Eric Foreman,Diagnostics,80\n"
                        "Robert Chase,Surgery,95\n"
                        "Chris Taub,Surgery,55\n"
                        "James Wilson,Oncology,110"
                    ),
                }
            ],
            "expected_csv": (
                "name,department,cases_solved,pct\n"
                "Gregory House,Diagnostics,120,60.0\n"
                "Eric Foreman,Diagnostics,80,40.0\n"
                "Robert Chase,Surgery,95,63.3\n"
                "Chris Taub,Surgery,55,36.7\n"
                "James Wilson,Oncology,110,100.0"
            ),
        },
        {
            "statement": "Create a cross-tabulation showing how many patients each doctor treated per department. Use doctor as rows and department as columns.",
            "solution_code": 'pd.crosstab(consults["doctor"], consults["department"])',
            "hint": "Use pd.crosstab(df['row_col'], df['col_col']) to create a frequency table.",
            "category": "crosstab",
            "tables": [
                {
                    "name": "consults",
                    "csv": (
                        "doctor,patient,department\n"
                        "House,Rebecca Adler,Diagnostics\n"
                        "House,John Henry Giles,Diagnostics\n"
                        "House,Eve,Neurology\n"
                        "Wilson,Mark Warner,Oncology\n"
                        "Wilson,Eve,Diagnostics\n"
                        "Foreman,Rebecca Adler,Neurology\n"
                        "Foreman,Chi Park,Neurology"
                    ),
                }
            ],
            "expected_csv": (
                "doctor,Diagnostics,Neurology,Oncology\n"
                "Foreman,0,2,0\n"
                "House,2,1,0\n"
                "Wilson,1,0,1"
            ),
        },
        {
            "statement": "For each patient, find the date of their earliest admission. Return columns patient and admitted.",
            "solution_code": 'admissions.groupby("patient")["admitted"].min().reset_index()',
            "hint": "Use df.groupby('col')['date_col'].min().reset_index() to get the earliest date per group.",
            "category": "groupby-min",
            "tables": [
                {
                    "name": "admissions",
                    "csv": (
                        "patient,admitted,department,doctor\n"
                        "Rebecca Adler,2004-11-16,Diagnostics,House\n"
                        "Rebecca Adler,2005-03-22,Neurology,Foreman\n"
                        "John Henry Giles,2005-01-10,Diagnostics,House\n"
                        "Eve,2005-05-03,Diagnostics,House\n"
                        "Eve,2004-09-14,Neurology,Foreman"
                    ),
                }
            ],
            "expected_csv": (
                "patient,admitted\n"
                "Eve,2004-09-14\n"
                "John Henry Giles,2005-01-10\n"
                "Rebecca Adler,2004-11-16"
            ),
        },
        {
            "statement": "Filter the diagnoses table to keep only rows where the same patient has been diagnosed more than once. It's never lupus... or is it?",
            "solution_code": 'diagnoses[diagnoses.groupby("patient")["patient"].transform("count") > 1]',
            "hint": "Use groupby().transform('count') to get the count per group, then filter rows where count > 1.",
            "category": "filter-transform",
            "tables": [
                {
                    "name": "diagnoses",
                    "csv": (
                        "patient,diagnosis,doctor\n"
                        "Rebecca Adler,Neurocysticercosis,House\n"
                        "John Henry Giles,Colchicine Poisoning,House\n"
                        "Rebecca Adler,Tapeworm,House\n"
                        "Eve,African Sleeping Sickness,House\n"
                        "Chi Park,Lupus,Foreman\n"
                        "Mark Warner,Thymoma,Wilson"
                    ),
                }
            ],
            "expected_csv": (
                "patient,diagnosis,doctor\n"
                "Rebecca Adler,Neurocysticercosis,House\n"
                "Rebecca Adler,Tapeworm,House"
            ),
        },
    ],
}
