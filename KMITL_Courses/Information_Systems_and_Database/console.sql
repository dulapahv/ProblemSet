-- Show the average age at death of the deceased presidents.
-- SELECT AVG("DEATH_AGE")
-- FROM "PRESIDENT"

-- Count all presidents who is in Republican party.
-- SELECT MIN("PARTY"), COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "PARTY" = 'Republican'

-- Show the age at death of the president who died the youngest.
-- SELECT min("DEATH_AGE")
-- FROM "PRESIDENT"

-- Show the age at death of the Democratic president who died the oldest
-- SELECT max("DEATH_AGE")
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

-- Show the aerage age at death of the deceased presidents.
-- SELECT SUM("DEATH_AGE") / COUNT(*)
-- FROM "PRESIDENT"
-- WHERE "DEATH_AGE" IS NOT NULL

-- Find those deceased politicians who served more than 10% of their lives as presidents. List their names and that
-- ercentage.
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
-- Children.
-- SELECT "PRES_NAME", MAX("NR_CHILDREN"), MIN("NR_CHILDREN")
-- FROM "PRES_MARRIAGE"
-- GROUP BY "PRES_NAME"
-- HAVING COUNT(*) >= 2
--   AND MAX("NR_CHILDREN") >= MIN("NR_CHILDREN") + 2

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
--     AND "BIRTH_YR" < 1800
-- ORDER BY "BIRTH_YR", "PRESIDENT"."PRES_NAME"

-- List name, birth year, marriage years, and spouse name of those presidents who were born before 1776 and married
-- before 1800. Order the list on president name in alphabetical order.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "MAR_YEAR", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
--     AND "BIRTH_YR" < 1776
--     AND "MAR_YEAR" < 1800
-- ORDER BY "PRESIDENT"."PRES_NAME"

-- List the name, birth year, age at marriage, spouse's age at marriage, and name, for all presidents who married when
-- they were less than 20 years old, or who married a spouse less than 18 years of age. Order by age of president at
-- marriage.
-- SELECT "PRESIDENT"."PRES_NAME", "BIRTH_YR", "MAR_YEAR", "SP_AGE", "SPOUSE_NAME"
-- FROM "PRESIDENT", "PRES_MARRIAGE"
-- WHERE "PRESIDENT"."PRES_NAME" = "PRES_MARRIAGE"."PRES_NAME"
--     AND ("PR_AGE" < 20
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

-- Page 72