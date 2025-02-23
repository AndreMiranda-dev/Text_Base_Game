    /*
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation, either version 3 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program. If not, see <https://www.gnu.org/licenses/>.
     */



# Text_Base_Game_ReadMe

Green Valley Highschool Break In Text Game Storyboard
Andre Miranda
SNHU
IT-140
Lawrence Meadors
02/03/2025

You are a Highschool student who has forgotten your gym clothes, jacket, bookbag, and all 3 of your textbooks at school but you have 3 big tests tomorrow to study for! To pass each test, you need to collect each of your books. You must find your bookbag before leaving school. If you don’t find your jacket it will be too cold to walk home, and you will have to call your parents to come pick you up losing vital study time as you wait for your parents to get out of work to pick you up, failing 1 test. Finally, if you can’t find your gym clothes you will be worried about smelling bad in gym class and you won’t be able to focus properly on studying, failing 1 test. Beware! The janitor will be out cleaning the school, and the math teacher is staying late grading papers. Get caught being in school after hours and you will be forced to leave. You can choose to leave the school at any time after finding your bookbag, but not finding all other items and you may fail your tests.
Here is the map of Green Valley High School and the items you need to find: 



![image](https://github.com/user-attachments/assets/72193033-7360-4176-b930-51a04b616210)



Pseudocode

START
IMPORT random

DEFINE main()
	DEFINE math book, english book, science book, gym clothes, and book bag
	DEFINE Janitor and Math teacher

	DEFINE layout of the school
	SET math class, English class, science class, gym, and lunch room to an integer
		# this will be used later to figure out where the Janitor is and where he will clean next

	PRINT description, rules, and guidelines for Green Valley Highschool break in game
	PROMPT user to break in to the school when ready by typing in “Enter”
	
	SET all book values to 0
	SET Math Teacher in math class
	SET Janitor to clean Gym
	SET all items in the game with a 0 value
		# this will be used later to see which items were found

	WHILE game is running and not all items collected
		SET move counter to 0
		CALL random number generator and set Janitor to that number
		IF move counter = 6
			SET math teacher to ‘gone home’
			SET janitor to ‘gone home’
			IF not all items collected
CALL get_NSEW()
IF item found set item value to 1
			ELSE:
				PROMPT user to exit
				BREAK while loop

		ELSE:
			IF not caught by teacher or janitor:
				IF not all items collected
CALL get_NSEW()
IF item found set item value to 1
SET move counter += 1
				ELSE:
					PROMPT user to exit
BREAK while loop
			ELSE:
				PRINT “Caught breaking into school after hours!”
				BREAK while loop

CHECK items found and set value to “Pass” if found (value of 1 = found) or “Fail” if not found (value of 0 = not found)

	IF all items found:
		PRINT(‘Great job you passed all your tests and didn’t smell bad during Gym Class’)
	ELIF all books found but not jacket or not gym cloths or not jacket and not gym cloths:
PRINT(‘You didn’t have enough time to study for all your tests and failed your English Test’)
	ELSE:
PRINT(f ‘You {math_book} your math exam, {english_book} your English exam, and {science_book} your science exam.’)
		


DEFINE get_NSEW()
	While True:
		PROMPT user for a north, south, east, or west input
		IF input is valid:
			RETURN input
		ELSE:
			PRINT “Not a valid entry”


CALL main()
END
