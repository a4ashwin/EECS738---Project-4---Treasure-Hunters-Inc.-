EECS738--- Project 4 - Treasure Hunters Inc.
 Prerequisites
 Python 3.7.3, Pandas Library, Numpy Library

 Introduction:
 In this project, We do the treasure hunting and monster fighting for you
1. Set up a new git repository in your GitHub account
2. Think up a map-like environment with treasure, obstacles and opponents
3. Choose a programming language (Python, C/C++, Java)
4. Formulate ideas on how reinforcement learning can be used to find treasure efficiently while avoiding obstacles and opponents
5. Build one or more reinforcement policies to model situational assessments, actions and rewards programmatically
6. Document your process and results
7. Commit your source code, documentation and other supporting files to the git repository in GitHub4
 
Idea:
 Reinforcement learning is used to make optimal decisions for problem solving in step by step manner. It works on the basis of small tasks that can be performed based on the states of the environment and the rewards based on the steps that are taken to reach the goal. In our project, Dora is at start position and wants to find the treasure by moving through the grid. In her journey, she can choose any path, but there are rewards attached with each state like if there is a lion in that state, -10.Dora will be trained multiple times so that she can find the optimal path to reach the tressure with maximum reward.  



Process:
	I have implemented Reinforce learning in the python file and step by step details of the implementation have been commented in the python file

 Result:
 We have successfully implemented the Reinforce Learning Algorithm and got optimal result for the problem discussed above based on the rewards.

 Built With:
 Python 3.7.3
 Pandas
 NumPy

 Authors:
 Ashwin Rathore

 License:
 This project is created for Course EECS 738 Assignment for University of Kansas. 
