-- Show the average age at death of the deceased presidents.
-- SELECT AVG("DEATH_AGE")
-- FROM "PRESIDENT"

-- Count all presidents who is in Republican party.
-- SELECT MIN("PARTY"), COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "PARTY" = 'Republican'

-- Show the age at death of the president who died the youngest.
-- SELECT MIN("DEATH_AGE")
-- FROM "PRESIDENT"

-- Show the age at death of the Democratic president who died the oldest
-- SELECT MAX("DEATH_AGE")
-- FROM "PRESIDENT"
-- WHERE "PARTY" = 'Democratic'

-- How many inaugurations were there altogether?
-- SELECT COUNT(*)
-- FROM "ADMINISTRATION"

-- How many individual presidents were there?
-- SELECT COUNT(DISTINCT "PRES_NAME")
-- FROM "ADMINISTRATION"

-- How many presidential marriages were there altogether?
-- SELECT COUNT(*)
-- FROM "PRES_MARRIAGE"

-- How many married presidents were there altogether?
-- SELECT COUNT(DISTINCT "PRES_NAME")
-- FROM "PRES_MARRIAGE"

-- Show the average age at death of the deceased presidents.
-- SELECT SUM("DEATH_AGE") / COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "DEATH_AGE" IS NOT NULL

-- Find those deceased politicians who served more than 10% of their lives as presidents. List their names and that
-- percentage.
-- SELECT "PRES_NAME", 100 * "YRS_SERV" / "DEATH_AGE"
-- FROM "PRESIDENT"
-- WHERE (100 * "YRS_SERV" / "DEATH_AGE") > 10
--   AND "DEATH_AGE" IS NOT NULL

-- Give the name and age of president and spouse for those marriages where the president was at least 5 years older than
-- the spouse and the spouse was less than 20
-- SELECT "PRES_NAME", "SPOUSE_NAME", "PR_AGE", "SP_AGE"
-- FROM "PRES_MARRIAGE"
-- WHERE "PR_AGE" > "SP_AGE" + 5
--   AND "SP_AGE" < 20

-- Which presidents were no more than 10% older than their spouse(s) at the time of marriage? List their name, their age
-- at marriage, their spouse's age at marriage and the ratio of the president's age to his spouse's age as a decimal
-- number.
-- SELECT "PRES_NAME", "PR_AGE", "SP_AGE", "PR_AGE" / "SP_AGE"
-- FROM "PRES_MARRIAGE"
-- WHERE 1.0 * "PR_AGE" / "SP_AGE" BETWEEN 1 AND 1.1

-- For each party, calculate the number of presidents who were or who are members of this party. List the name of each
-- party, together with this number.
-- SELECT "PARTY", COUNT(*)
-- FROM "PRESIDENT"
-- GROUP BY "PARTY"
-- ORDER BY "PARTY"

-- For each state find the number of presidents who were born in that state. List the state name together with this
-- number and present in sequence of ascending number and within the same number by ascending state name.
-- SELECT "STATE_BORN", COUNT(*)
-- FROM "PRESIDENT"
-- GROUP BY "STATE_BORN"
-- ORDER BY 2, "STATE_BORN"

-- For each party, calculate the total number of years served by presidents of that party, the number of presidents, and
-- the average number of years served. List party, total number of years served, number of presidents, and average
-- number of years served.
-- SELECT "PARTY", SUM("YRS_SERV"), COUNT(*), AVG("YRS_SERV")
-- FROM "PRESIDENT"
-- GROUP BY "PARTY"

-- Count the presidents who are or were members of the same party and who were born in the same state. List party, state
-- of birth and this number.
-- SELECT "PARTY", "STATE_BORN", COUNT(*)
-- FROM "PRESIDENT"
-- GROUP BY "PARTY", "STATE_BORN"
-- ORDER BY 1, 2

-- For each birth state/party combination, count the presidents who were born in that state and who were or are members
-- of that party. List state, party and this number.
-- SELECT "STATE_BORN", "PARTY", COUNT(*)
-- FROM "PRESIDENT"
-- GROUP BY "STATE_BORN", "PARTY"
-- ORDER BY 1, 2

-- For each party, list the party name and the number of presidents who were born after 1850.
-- SELECT "PARTY", COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "BIRTH_YR" > 1850
-- GROUP BY "PARTY"

-- List the names of presidents and the number of their marriages for those presidents who married more than once.
-- SELECT "PRES_NAME", COUNT(*)
-- FROM "PRES_MARRIAGE"
-- GROUP BY "PRES_NAME"
-- HAVING COUNT(*) > 1

-- For those party(ies) which had more than 8 presidents born after 1850 list the name(s) of the party(ies) and the
-- corresponding number(s) of presidents born after 1850.
-- SELECT "PARTY", COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "BIRTH_YR" > 1850
-- GROUP BY "PARTY"
-- HAVING COUNT(*) > 8

-- Find those presidents who married at least twice and those maximum number of children in any of their marriages
-- exceeds their minimum number of children by at least 2. List their names, and the maximum and minimum number of
-- children.
-- SELECT "PRES_NAME", MAX("NR_CHILDREN"), MIN("NR_CHILDREN")
-- FROM "PRES_MARRIAGE"
-- GROUP BY "PRES_NAME"
-- HAVING COUNT(*) >= 2
--    AND MAX("NR_CHILDREN") >= MIN("NR_CHILDREN") + 2

--------------------------------------------------------------------------------

-- A table with 4 columns, where each row consists of the president name of the P_TABLE, and his birth year followed by
-- the president name of the M_TABLE and spouse name.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR","PRES_MARRIAGE"."PRES_NAME", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"

-- List names, birth years, marriage years and spouses of all married presidents. Order by president name.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "MAR_YEAR", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
-- ORDER BY "PRESIDENT"."PRES_NAME"

-- List president name, birth year, the administrations served as president, and the vice president in each
-- administration in order of administration number.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "ADMIN_NR", "VICE_PRES_NAME"
-- FROM "PRESIDENT", "ADMIN_PR_VP"
-- WHERE "PRESIDENT"."PRES_NAME" = "ADMIN_PR_VP"."PRES_NAME"
-- ORDER BY "ADMIN_NR"

-- List the names, birth years, and hobbies of all presidents born before 1800. Order by birth year and president name.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "HOBBY"
-- FROM "PRESIDENT", "PRES_HOBBY"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_HOBBY"."PRES_NAME"
--   AND "BIRTH_YR" < 1800
-- ORDER BY "BIRTH_YR", "PRESIDENT"."PRES_NAME"

-- List name, birth year, marriage years, and spouse name of those presidents who were born before 1776 and married
-- before 1800. Order the list on president name in alphabetical order.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "MAR_YEAR", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
--   AND "BIRTH_YR" < 1776
--   AND "MAR_YEAR" < 1800
-- ORDER BY "PRESIDENT"."PRES_NAME"

-- List the name, birth year, age at marriage, spouse's age at marriage, and name, for all presidents who married when
-- they were less than 20 years old, or who married a spouse less than 18 years of age. Order by age of president at
-- marriage.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "MAR_YEAR", "SP_AGE", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
--   AND ("PR_AGE" < 20
--     OR "SP_AGE" < 18)
-- ORDER BY "PR_AGE"

-- For each president, with more than three children, list their name, their birth year, and the number of children
-- from all marriages. Order by number of children in descending order, and then by name.
-- SELECT "PRESIDENT"."PRES_NAME", MIN("BIRTH_YR"), SUM("NR_CHILDREN")
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
-- GROUP BY "PRESIDENT"."PRES_NAME"
-- HAVING SUM("NR_CHILDREN") > 3
-- ORDER BY 3 DESC, 1

-- List all the facts of those presidential marriages which resulted in a number of children that is greater than the
-- average number of children per presidential marriage.
-- SELECT *
-- FROM "PRES_MARRIAGE"
-- WHERE "NR_CHILDREN" >
--       (SELECT AVG("NR_CHILDREN")
--        FROM "PRES_MARRIAGE")

-- Show the name and age of the president who died the youngest
-- SELECT "PRES_NAME", "DEATH_AGE"
-- FROM "PRESIDENT"
-- WHERE "DEATH_AGE" =
--       (SELECT MIN("DEATH_AGE")
--        FROM "PRESIDENT")

-- List the hobbies and names of all those presidents who served 8 years or longer. Order by hobbies, presidents name.
-- SELECT "HOBBY", "PRES_NAME"
-- FROM "PRES_HOBBY"
-- WHERE "PRES_NAME" IN
--       (SELECT "PRES_NAME"
--        FROM "PRESIDENT"
--        WHERE "YRS_SERV" >= 8)
-- ORDER BY 1, 2

-- SELECT "HOBBY", "PRES_NAME"
-- FROM "PRES_HOBBY"
-- WHERE "PRES_NAME" = ANY
--       (SELECT "PRES_NAME"
--        FROM "PRESIDENT"
--        WHERE "YRS_SERV" >= 8)
-- ORDER BY 1, 2

-- SELECT "HOBBY", "PRESIDENT"."PRES_NAME"
-- FROM "PRESIDENT", "PRES_HOBBY"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_HOBBY"."PRES_NAME"
--   AND "YRS_SERV" >= 8
-- ORDER BY 1, 2

-- Which presidents never won an election?
-- SELECT "PRES_NAME"
-- FROM "PRESIDENT"
-- WHERE "PRES_NAME" NOT IN
--       (SELECT DISTINCT "CANDIDATE"
--        FROM "ELECTION"
--        WHERE "WINNER_LOSER_INDIC" = 'W')

-- Which state provided the largest number of presidents, and what is that number?
-- SELECT "STATE_BORN", COUNT(*)
-- FROM "PRESIDENT"
-- GROUP BY "STATE_BORN"
-- HAVING COUNT(*) >= ALL
--        (SELECT COUNT(*)
--         FROM "PRESIDENT"
--         GROUP BY "STATE_BORN")

-- Find those states which entered the union before President Washington was inaugurated.
-- SELECT "STATE_NAME"
-- FROM "STATE"
-- WHERE "YEAR_ENTERED" < ALL
--       (SELECT "YEAR_INAUGURATED"
--        FROM "ADMINISTRATION"
--        WHERE "PRES_NAME" = 'Washington G')

-- List all the facts available in the table PRESIDENT about those presidents who were inaugurated after Hawaii entered
-- the union.
-- SELECT *
-- FROM "PRESIDENT"
-- WHERE "PRES_NAME" = ANY
--       (SELECT "PRES_NAME"
--        FROM "ADMINISTRATION"
--        WHERE "YEAR_INAUGURATED" >
--              (SELECT "YEAR_ENTERED"
--               FROM "STATE"
--               WHERE "STATE_NAME" = 'Hawaii'))

-- List the names and ages at death of those presidents who were married more than once. Order by name.
-- SELECT "PRES_NAME", "DEATH_AGE"
-- FROM "PRESIDENT"
-- WHERE "PRES_NAME" IN
--       (SELECT "PRES_NAME"
--        FROM "PRES_MARRIAGE"
--        GROUP BY "PRES_NAME"
--        HAVING COUNT(*) > 1)
-- ORDER BY "PRES_NAME"

-- Find those states which entered the union the same year as President Eisenhower was born. Order by state name.
-- SELECT "STATE_NAME"
-- FROM "STATE", "PRESIDENT"
-- WHERE "YEAR_ENTERED" = "BIRTH_YR"
--   AND "PRES_NAME" = 'Eisenhower D D'
-- ORDER BY "STATE_NAME"

-- SELECT "STATE_NAME"
-- FROM "STATE"
-- WHERE "YEAR_ENTERED" =
--       (SELECT "BIRTH_YR"
--        FROM "PRESIDENT"
--        WHERE "PRES_NAME" = 'Eisenhower D D')
-- ORDER BY "STATE_NAME"

-- For each president who was born in a year in which at least one other president was born list his name and birth
-- year.
-- SELECT "PRES_NAME", "BIRTH_YR"
-- FROM "PRESIDENT"
-- WHERE "BIRTH_YR" IN
--       (SELECT "BIRTH_YR"
--        FROM "PRESIDENT"
--        GROUP BY "BIRTH_YR"
--        HAVING COUNT(*) > 1)

-- List presidents born on same year. List each president only once.
-- SELECT T1."PRES_NAME", T1."BIRTH_YR", T2."PRES_NAME", T2."BIRTH_YR"
-- FROM "PRESIDENT" T1, "PRESIDENT" T2
-- WHERE T1."BIRTH_YR" = T2."BIRTH_YR"
--   AND T1."PRES_NAME" < T2."PRES_NAME"

-- Using the table ELECTION for all elections after 1900, create a new table with the following columns:
-- ELECTION YEAR, WINNER, WINNER VOTES, LOSERS, LOSERS VOTES
-- SELECT W."ELECTION_YEAR", W."CANDIDATE", W."VOTES", L."CANDIDATE", L."VOTES"
-- FROM "ELECTION" W, "ELECTION" L
-- WHERE W."ELECTION_YEAR" = L."ELECTION_YEAR"
--   AND W."ELECTION_YEAR" > 1900
--   AND W."WINNER_LOSER_INDIC" = 'W'
--   AND L."WINNER_LOSER_INDIC" = 'L'
-- ORDER BY W."ELECTION_YEAR", L."VOTES" DESC

-- List election year and winner of those elections in which the winner received more than 80% of the votes of that
-- election.
-- SELECT "ELECTION_YEAR", "CANDIDATE"
-- FROM "ELECTION" E
-- WHERE "WINNER_LOSER_INDIC" = 'W'
--   AND "VOTES" >
--       (SELECT 0.8 * SUM("VOTES")
--        FROM "ELECTION"
--        WHERE "ELECTION"."ELECTION_YEAR" = E."ELECTION_YEAR")

-- Select the president's name, birth year and the year of inauguration of his first administration, and order the
-- result in sequence of year of inauguration
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "YEAR_INAUGURATED"
-- FROM "PRESIDENT", "ADMINISTRATION"
-- WHERE "PRESIDENT"."PRES_NAME" = "ADMINISTRATION"."PRES_NAME"
--   AND "YEAR_INAUGURATED" =
--       (SELECT MIN("YEAR_INAUGURATED")
--        FROM "ADMINISTRATION"
--        WHERE "PRESIDENT"."PRES_NAME" = "ADMINISTRATION"."PRES_NAME")
-- ORDER BY "YEAR_INAUGURATED"

-- For those presidents whose number of marriages equals the number of administrations they served as president, list
-- their name and this number
-- SELECT "PRES_NAME", COUNT(*)
-- FROM "PRES_MARRIAGE"
-- GROUP BY "PRES_NAME"
-- HAVING COUNT(*) =
--        (SELECT COUNT(*)
--         FROM "ADMINISTRATION"
--         WHERE "ADMINISTRATION"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME")

-- Find the names of those presidents born in a state which entered the union not more than 30 years earlier than their
-- first inauguration year.
-- SELECT "PRES_NAME"
-- FROM "PRESIDENT" X
-- WHERE "STATE_BORN" IN
--       (SELECT "STATE_NAME"
--        FROM "STATE"
--        WHERE "YEAR_ENTERED" + 30 >= ANY
--              (SELECT MIN("YEAR_INAUGURATED")
--               FROM "ADMINISTRATION"
--               WHERE "PRES_NAME" = X."PRES_NAME"))

-- List hobbies that at least 3 Democratic presidents have in common.
-- SELECT "HOBBY"
-- FROM "PRES_HOBBY", "PRESIDENT"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_HOBBY"."PRES_NAME"
--   AND "PARTY" = 'Democratic'
-- GROUP BY "HOBBY"
-- HAVING COUNT(*) >= 3

--  List details of presidents who belonged to the party which has the highest number of presidents in Ohio.
-- SELECT p.*
-- FROM "PRESIDENT" p
--          JOIN (SELECT "PARTY"
--                FROM "PRESIDENT"
--                WHERE "STATE_BORN" = 'Ohio'
--                GROUP BY "PARTY"
--                ORDER BY COUNT(*) DESC
--                LIMIT 1) q ON p."PARTY" = q."PARTY"
-- WHERE p."STATE_BORN" = 'Ohio'

-- List the rows of the top two candidates by votes for each year
-- SELECT *
-- FROM "ELECTION" e
-- WHERE e."WINNER_LOSER_INDIC" = 'W'
--   AND e."CANDIDATE" IN
--       (SELECT "CANDIDATE"
--        FROM "ELECTION"
--        WHERE "ELECTION_YEAR" = e."ELECTION_YEAR"
--        ORDER BY "VOTES" DESC
--        LIMIT 2)
-- ORDER BY "ELECTION_YEAR", "VOTES" DESC

-- List the name of the youngest second wife
-- SELECT "SPOUSE_NAME"
-- FROM "PRES_MARRIAGE"
-- WHERE "PRES_NAME" IN (SELECT "PRES_NAME"
--                       FROM "PRES_MARRIAGE"
--                       GROUP BY "PRES_NAME"
--                       HAVING COUNT(*) > 1)
-- ORDER BY "SP_AGE"
-- LIMIT 1;

-- List hobbies that no Republican presidents have in common.
-- SELECT "HOBBY"
-- FROM "PRES_HOBBY", "PRESIDENT"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_HOBBY"."PRES_NAME"
--   AND "PARTY" = 'Republican'
-- GROUP BY "HOBBY"
-- HAVING COUNT(*) = 1

-- List details of Republican presidents who have maximum total number of hobbies in the party.
SELECT "PRESIDENT".*
FROM "PRESIDENT"
         JOIN (SELECT "PRESIDENT"."PRES_NAME"
               FROM "PRES_HOBBY", "PRESIDENT"
               WHERE "PRESIDENT"."PRES_NAME" = "PRES_HOBBY"."PRES_NAME"
                 AND "PARTY" = 'Republican'
               GROUP BY "PRESIDENT"."PRES_NAME"
               ORDER BY COUNT(*) DESC
               LIMIT 1) q ON "PRESIDENT"."PRES_NAME" = q."PRES_NAME"
