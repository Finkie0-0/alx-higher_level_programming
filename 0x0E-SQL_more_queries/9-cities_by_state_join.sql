-- script lists all cities in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.states_id = states.id;

