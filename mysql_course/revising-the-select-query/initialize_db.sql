USE hackerrank;

CREATE TABLE city (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(17) NOT NULL,
    countrycode varchar(3) NOT NULL,
    district varchar(20) NOT NULL,
    population int NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO city (name, countrycode, district, population) 
VALUES
    ("Rotterdam", "NLD",  "Zuid-Holland",593321),
    ("Scottsdale", "USA", "Arizona", 202705),
    ("Corona", "USA", "California",124966),
    ("Concord", "USA", "California", 121780),
    ("Cedar Rapids", "USA", "Iowa", 120758),
    ("Coral Springs", "USA", "Florida", 117549),
    ("Fairfield", "USA", "California", 92256),
    ("Boulder", "USA", "Colorado", 91238),
    ("Fall River", "USA", "Massachusetts", 90555)
    ;

CREATE TABLE station (
    id int NOT NULL AUTO_INCREMENT,
    city varchar(21),
    state varchar(2),
    lat_n int,
    long_w int,
    PRIMARY KEY (id)
);


INSERT INTO station (city, state, lat_n, long_w) 
VALUES
    ("Tipton", "IN", 34, 98), 
    ("Arlington", "CO", 75, 93), 
    ("Turner", "AR", 50, 101), 
    ("Slidell", "LA", 85, 152), 
    ("Negreet", "LA", 99, 105), 
    ("Glencoe", "KY", 46, 136), 
    ("Chelsea", "IA", 99, 60), 
    ("Pelahatchie", "MS", 39, 28), 
    ("Dorrance", "KS", 102, 122), 
    ("Albany", "CA", 50, 80), 
    ("Monument", "KS", 71, 142), 
    ("Manchester", "MD", 74, 37), 
    ("Prescott", "IA", 40, 66), 
    ("Graettinger", "IA", 95, 150), 
    ("Cahone", "CO", 116, 127), 
    ("Sturgis", "MS", 36, 126), 
    ("Upperco", "MD", 114, 30), 
    ("Highwood", "IL", 27, 151), 
    ("Waipahu", "HI", 106, 34), 
    ("Bowdon", "GA", 89, 78), 
    ("Tyler", "MN", 133, 59), 
    ("Watkins", "CO", 83, 97), 
    ("Republic", "MI", 75, 130), 
    ("Millville", "CA", 33, 146), 
    ("Aguanga", "CA", 80, 66), 
    ("Morenci", "AZ", 105, 110), 
    ("Hoskinston", "KY", 66, 66), 
    ("Talbert", "KY", 40, 59), 
    ("Mccomb", "MS", 74, 43), 
    ("Kirk", "CO", 141, 136), 
    ("Carlock", "IL", 117, 85), 
    ("Seward", "IL", 72, 90), 
    ("Gustine", "CA", 111, 141), 
    ("Delano", "CA", 126, 92), 
    ("Westphalia", "MI", 33, 144), 
    ("Roy", "MT", 41, 52), 
    ("Pattonsburg", "MO", 138, 32), 
    ("Centertown", "MO", 134, 93), 
    ("Norvell", "MI", 125, 94), 
    ("Raymondville", "MO", 71, 148), 
    ("Odin", "IL", 53, 116), 
    ("Jemison", "AL", 62, 26), 
    ("Barrigada", "GU", 61, 148), 
    ("Hesperia", "CA", 106, 71), 
    ("Wickliffe", "KY", 80, 46), 
    ("Culdesac", "ID", 48, 78), 
    ("Roselawn", "IN", 88, 52), 
    ("Portland", "AR", 84, 45), 
    ("Hampden", "MA", 76, 26), 
    ("Sandborn", "IN", 56, 94), 
    ("Seaton", "IL", 128, 78), 
    ("Milledgeville", "IL", 91, 113), 
    ("Gretna", "LA", 75, 143), 
    ("Zionsville", "IN", 58, 36), 
    ("Jolon", "CA", 67, 53), 
    ("Childs", "MD", 93, 104), 
    ("Shreveport", "LA", 136, 39), 
    ("Forest", "MS", 120, 50), 
    ("Sizerock", "KY", 116, 113), 
    ("Algonac", "MI", 119, 80), 
    ("Onaway", "MI", 109, 56), 
    ("Irvington", "IL", 97, 68), 
    ("Winsted", "MN", 69, 73), 
    ("Woodbury", "GA", 103, 93), 
    ("Samantha", "AL", 75, 36), 
    ("Hackleburg", "AL", 120, 121), 
    ("Soldier", "KS", 77, 153), 
    ("Arrowsmith", "IL", 28, 109), 
    ("Columbus", "GA", 67, 47), 
    ("Bentonville", "AR", 37, 78), 
    ("Kirkland", "AZ", 86, 58), 
    ("Wilton", "ME", 57, 157), 
    ("Busby", "MT", 104, 30), 
    ("Robertsdale", "AL", 98, 85), 
    ("Dale", "IN", 70, 34), 
    ("Reeds", "MO", 31, 43), 
    ("Hayfork", "CA", 35, 117), 
    ("Mcbrides", "MI", 74, 36), 
    ("Tennessee", "IL", 55, 156), 
    ("Henderson", "IA", 78, 78), 
    ("Udall", "KS", 113, 60), 
    ("Benedict", "KS", 138, 96), 
    ("Oakfield", "ME", 48, 132), 
    ("Tamms", "IL", 60, 75), 
    ("Haubstadt", "IN", 28, 32), 
    ("Chokio", "MN", 81, 134), 
    ("Clancy", "MT", 46, 164), 
    ("Norwood", "MN", 144, 35), 
    ("Elkton", "MD", 103, 157), 
    ("Bertha", "MN", 40, 105), 
    ("Bridgeport", "MI", 51, 80), 
    ("Cherry", "IL", 68, 47), 
    ("Regina", "KY", 132, 90), 
    ("Griffin", "GA", 39, 152), 
    ("Mascotte", "FL", 121, 146), 
    ("Baldwin", "MD", 82, 40), 
    ("Netawaka", "KS", 109, 120), 
    ("Pony", "MT", 99, 163), 
    ("Franklin", "LA", 82, 32), 
    ("Amo", "IN", 104, 159), 
    ("Vulcan", "MO", 109, 92), 
    ("Alanson", "MI", 91, 72), 
    ("Delta", "LA", 137, 50), 
    ("Carver", "MN", 46, 122), 
    ("Paron", "AR", 59, 104), 
    ("Winchester", "ID", 38, 80), 
    ("Jerome", "AZ", 122, 34), 
    ("Greenview", "CA", 81, 58), 
    ("Cromwell", "MN", 129, 54), 
    ("Quinter", "KS", 60, 25), 
    ("Whitewater", "MO", 83, 71), 
    ("Clarkdale", "AZ", 58, 74), 
    ("Rockton", "IL", 116, 87), 
    ("Pheba", "MS", 91, 127), 
    ("Eleele", "HI", 81, 153), 
    ("Auburn", "IA", 95, 137), 
    ("Oconee", "GA", 93, 119), 
    ("Grandville", "MI", 39, 70), 
    ("Susanville", "CA", 128, 80), 
    ("Rosie", "AR", 73, 162), 
    ("Verona", "MO", 110, 153), 
    ("Richland", "GA", 105, 113), 
    ("Fremont", "MI", 54, 151), 
    ("Philipsburg", "MT", 96, 72), 
    ("Kensett", "IA", 56, 140), 
    ("Koleen", "IN", 138, 111), 
    ("Winslow", "IL", 113, 39), 
    ("Reasnor", "IA", 42, 163), 
    ("Bono", "AR", 133, 150), 
    ("Biggsville", "IL", 86, 139), 
    ("Amazonia", "MO", 46, 148), 
    ("Marysville", "MI", 86, 133), 
    ("Pengilly", "MN", 25, 154), 
    ("Newbury", "MA", 128, 85), 
    ("Kismet", "KS", 100, 157), 
    ("Canton", "ME", 99, 106), 
    ("Grayslake", "IL", 61, 33), 
    ("Bison", "KS", 132, 75), 
    ("Bellevue", "KY", 127, 122), 
    ("Ridgway", "CO", 77, 110), 
    ("Rydal", "GA", 36, 79), 
    ("Lynnville", "KY", 25, 146), 
    ("Deerfield", "MO", 40, 36), 
    ("Montreal", "MO", 129, 127), 
    ("Hope", "MN", 140, 44), 
    ("Gowrie", "IA", 130, 128), 
    ("Andersonville", "GA", 141, 73), 
    ("Crouseville", "ME", 37, 82), 
    ("Cranks", "KY", 56, 27), 
    ("Ledyard", "CT", 135, 144), 
    ("Norway", "ME", 84, 88), 
    ("Eros", "LA", 95, 58), 
    ("Rantoul", "KS", 32, 119), 
    ("Fredericktown", "MO", 106, 113), 
    ("Arkadelphia", "AR", 99, 50), 
    ("Fredericksburg", "IN", 45, 78), 
    ("Manchester", "IA", 130, 123), 
    ("Eriline", "KY", 94, 65), 
    ("Wellington", "KY", 100, 32), 
    ("Edgewater", "MD", 130, 72), 
    ("Ducor", "CA", 141, 102), 
    ("Salem", "KY", 87, 114), 
    ("Sturdivant", "MO", 94, 86), 
    ("Hagatna", "GU", 97, 152), 
    ("Eastlake", "MI", 134, 39), 
    ("Larkspur", "CA", 107, 66), 
    ("Patriot", "IN", 83, 46), 
    ("Corriganville", "MD", 141, 154), 
    ("Carlos", "MN", 115, 66), 
    ("Addison", "MI", 96, 142), 
    ("Tarzana", "CA", 136, 81), 
    ("Grapevine", "AR", 92, 85), 
    ("Kanorado", "KS", 65, 86), 
    ("Climax", "MI", 127, 107), 
    ("Curdsville", "KY", 85, 150), 
    ("Southport", "CT", 59, 63), 
    ("Compton", "IL", 107, 99), 
    ("Notasulga", "AL", 67, 116), 
    ("Rumsey", "KY", 71, 50), 
    ("Rogers", "CT", 140, 33), 
    ("Everton", "MO", 119, 51), 
    ("Skanee", "MI", 70, 130), 
    ("Springerville", "AZ", 125, 151), 
    ("Libertytown", "MD", 145, 112), 
    ("Dumont", "MN", 57, 129), 
    ("Ravenna", "KY", 79, 106), 
    ("Williams", "AZ", 73, 112), 
    ("Decatur", "MI", 63, 161), 
    ("Holbrook", "AZ", 135, 104), 
    ("Sherrill", "AR", 80, 152), 
    ("Brownsdale", "MN", 52, 51), 
    ("Linden", "MI", 53, 33), 
    ("Sedgwick", "AR", 69, 75), 
    ("Rocheport", "MO", 114, 64), 
    ("Clovis", "CA", 92, 138), 
    ("Heyburn", "ID", 82, 121), 
    ("Peabody", "KS", 75, 152), 
    ("Randall", "KS", 48, 136), 
    ("Hayesville", "IA", 120, 42), 
    ("Jordan", "MN", 69, 35), 
    ("Greenville", "IL", 51, 153), 
    ("Macy", "IN", 139, 152), 
    ("Flowood", "MS", 65, 149), 
    ("Napoleon", "IN", 32, 160), 
    ("Leavenworth", "IN", 100, 122), 
    ("Coldwater", "KS", 48, 26), 
    ("Weldon", "CA", 134, 119), 
    ("Yellville", "AR", 36, 42), 
    ("Eustis", "FL", 43, 39), 
    ("Weldona", "CO", 33, 58), 
    ("Midpines", "CA", 106, 59), 
    ("Cascade", "ID", 32, 157), 
    ("Tefft", "IN", 93, 150), 
    ("Showell", "MD", 44, 164), 
    ("Bayville", "ME", 107, 143), 
    ("Brighton", "IL", 108, 33), 
    ("Grimes", "IA", 42, 75), 
    ("Nubieber", "CA", 133, 49), 
    ("Harmony", "MN", 124, 126), 
    ("Beaufort", "MO", 72, 86), 
    ("Arispe", "IA", 31, 138), 
    ("Humeston", "IA", 75, 122), 
    ("Baileyville", "IL", 82, 61), 
    ("Lakeville", "CT", 60, 95), 
    ("Firebrick", "KY", 50, 95), 
    ("Ludington", "MI", 30, 120), 
    ("Channing", "MI", 117, 57), 
    ("Pawnee", "IL", 85, 81), 
    ("Melber", "KY", 37, 56), 
    ("Manchester", "MN", 71, 84), 
    ("Bainbridge", "GA", 62, 57), 
    ("Sanders", "AZ", 131, 97), 
    ("Ottertail", "MN", 100, 44), 
    ("Dupo", "IL", 41, 29), 
    ("Montrose", "CA", 136, 119), 
    ("Schleswig", "IA", 119, 52), 
    ("Richmond", "IL", 113, 163), 
    ("Ermine", "KY", 120, 63), 
    ("Siler", "KY", 137, 117), 
    ("Reeves", "LA", 35, 51), 
    ("Clifton", "AZ", 30, 136), 
    ("Casco", "MI", 139, 109), 
    ("Sturgis", "MI", 117, 135), 
    ("Madisonville", "LA", 112, 53), 
    ("Albion", "IN", 44, 122), 
    ("Lismore", "MN", 59, 104), 
    ("Athens", "IN", 75, 121), 
    ("Eufaula", "AL", 140, 103), 
    ("Wildie", "KY", 70, 112), 
    ("Mosca", "CO", 89, 141), 
    ("Bennington", "IN", 36, 27), 
    ("Lottie", "LA", 110, 83), 
    ("Garland", "ME", 109, 134), 
    ("Clutier", "IA", 61, 127), 
    ("Lupton", "MI", 140, 53), 
    ("Northfield", "MN", 61, 37), 
    ("Daleville", "AL", 122, 136), 
    ("Cuba", "MO", 64, 88), 
    ("Norris", "MT", 47, 37), 
    ("Clopton", "AL", 41, 85), 
    ("Renville", "MN", 142, 99), 
    ("Kirksville", "MO", 140, 144), 
    ("Kingsland", "AR", 78, 85), 
    ("Fairview", "KS", 80, 165), 
    ("Lydia", "LA", 42, 40), 
    ("Bridgton", "ME", 93, 140), 
    ("Brownstown", "IL", 49, 63), 
    ("Monona", "IA", 144, 82), 
    ("Hartland", "MI", 136, 108), 
    ("Andover", "CT", 52, 53), 
    ("Lakota", "IA", 56, 92), 
    ("Mesick", "MI", 82, 109), 
    ("Dryden", "MI", 70, 48), 
    ("Beverly", "KY", 58, 127), 
    ("Pocahontas", "IL", 110, 83), 
    ("Hayneville", "AL", 110, 157), 
    ("Yoder", "IN", 83, 144), 
    ("Gatewood", "MO", 76, 146), 
    ("Madden", "MS", 81, 99), 
    ("Losantville", "IN", 113, 107), 
    ("Cheswold", "DE", 32, 59), 
    ("Caseville", "MI", 103, 98), 
    ("Pomona", "MO", 52, 50), 
    ("Hopkinsville", "KY", 27, 48), 
    ("Jack", "AL", 50, 86), 
    ("Dixie", "GA", 27, 36), 
    ("Hillside", "CO", 99, 69), 
    ("Hawarden", "IA", 91, 47), 
    ("Cannonsburg", "MI", 91, 121), 
    ("Osborne", "KS", 70, 140), 
    ("Farmington", "IL", 92, 72), 
    ("Honolulu", "HI", 110, 140), 
    ("Pfeifer", "KS", 37, 66), 
    ("Oshtemo", "MI", 100, 136), 
    ("Gridley", "KS", 118, 56), 
    ("Fulton", "KY", 111, 52), 
    ("Monroe", "LA", 28, 108), 
    ("Brilliant", "AL", 86, 160), 
    ("Archie", "MO", 40, 28), 
    ("Winslow", "AR", 126, 126), 
    ("Olmitz", "KS", 29, 38), 
    ("Allerton", "IA", 62, 113), 
    ("Norphlet", "AR", 144, 61), 
    ("Keyes", "CA", 77, 86), 
    ("Equality", "AL", 107, 116), 
    ("Neon", "KY", 102, 148), 
    ("Calhoun", "KY", 96, 57), 
    ("Alpine", "AR", 117, 115), 
    ("Mullan", "ID", 143, 155), 
    ("Coalgood", "KY", 57, 149), 
    ("Walnut", "MS", 41, 77), 
    ("Ojai", "CA", 69, 119), 
    ("Julian", "CA", 131, 102), 
    ("Veedersburg", "IN", 79, 95), 
    ("Payson", "AZ", 126, 154), 
    ("Windom", "KS", 114, 126), 
    ("Urbana", "IA", 143, 29), 
    ("Ludlow", "CA", 111, 88), 
    ("Lindsay", "MT", 143, 68), 
    ("Palatka", "FL", 95, 52), 
    ("Bristol", "ME", 88, 95), 
    ("Harmony", "IN", 135, 71), 
    ("Ukiah", "CA", 87, 90), 
    ("Yuma", "AZ", 111, 154), 
    ("Alba", "MI", 92, 104), 
    ("Zachary", "LA", 61, 152), 
    ("Esmond", "IL", 76, 91), 
    ("Waresboro", "GA", 144, 154), 
    ("Hills", "MN", 138, 135), 
    ("Delavan", "MN", 33, 65), 
    ("Magnolia", "MS", 113, 32), 
    ("Byron", "CA", 137, 120), 
    ("Dundee", "IA", 62, 105), 
    ("Baker", "CA", 31, 148), 
    ("Groveoak", "AL", 53, 88), 
    ("Kenner", "LA", 92, 127), 
    ("Many", "LA", 36, 95), 
    ("Seward", "AK", 120, 36), 
    ("Berryton", "KS", 61, 140), 
    ("Chilhowee", "MO", 80, 49), 
    ("Newark", "IL", 73, 130), 
    ("Cowgill", "MO", 137, 28), 
    ("Novinger", "MO", 108, 112), 
    ("Goodman", "MS", 101, 117), 
    ("Cobalt", "CT", 87, 27), 
    ("Eskridge", "KS", 108, 63), 
    ("Bennington", "KS", 94, 83), 
    ("Decatur", "MS", 71, 118), 
    ("Ozona", "FL", 145, 121), 
    ("Jackson", "AL", 111, 67), 
    ("Lapeer", "MI", 129, 114), 
    ("Hazlehurst", "MS", 49, 109), 
    ("Chester", "CA", 70, 124), 
    ("Clarkston", "MI", 94, 81), 
    ("Healdsburg", "CA", 111, 54), 
    ("Hotchkiss", "CO", 70, 72), 
    ("Monroe", "AR", 132, 150), 
    ("Payson", "IL", 82, 92), 
    ("Kell", "IL", 70, 59), 
    ("Strasburg", "CO", 89, 48), 
    ("Coaling", "AL", 144, 52), 
    ("Effingham", "KS", 133, 98), 
    ("Corcoran", "CA", 81, 140), 
    ("Alton", "MO", 80, 112), 
    ("Greenway", "AR", 119, 36), 
    ("Woodsboro", "MD", 77, 142), 
    ("Strawn", "IL", 30, 51), 
    ("Dent", "MN", 71, 137), 
    ("Shingletown", "CA", 61, 102), 
    ("Clio", "IA", 46, 115), 
    ("Yalaha", "FL", 120, 120), 
    ("Leakesville", "MS", 107, 73), 
    ("Shasta", "CA", 99, 156), 
    ("Canton", "MN", 124, 151), 
    ("Agency", "MO", 59, 96), 
    ("Taft", "CA", 108, 147), 
    ("Calpine", "CA", 47, 43), 
    ("Knobel", "AR", 95, 62), 
    ("Tina", "MO", 132, 28), 
    ("Anthony", "KS", 45, 161), 
    ("Emmett", "ID", 57, 32), 
    ("Haverhill", "IA", 62, 109), 
    ("Middleboro", "MA", 108, 149), 
    ("Siloam", "GA", 105, 92), 
    ("Lena", "LA", 78, 130), 
    ("Lee", "IL", 28, 51), 
    ("Freeport", "MI", 114, 51), 
    ("Acme", "LA", 73, 68), 
    ("Gorham", "KS", 111, 65), 
    ("Granger", "IA", 33, 102)
    ;