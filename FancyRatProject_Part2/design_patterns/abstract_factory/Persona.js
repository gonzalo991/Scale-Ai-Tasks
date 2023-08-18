/**
Concept to cover (this is what your task must be about):
APPLIED JAVASCRIPT.

Practical use and implementation of Javascript to solve real-world coding problems. You can ask the 
chatbot to help you solve whatever problem that requires code creation.

Operation for 1st prompt (you only need to follow this for your 1st prompt):

Rewrite: Ask the assistant to edit or modify an existing piece of code following various instructions.

Subsequent Prompt Guidance (how you must continue your conversation past the first response):

(Conversation) Follow-up on previous responses: For all subsequent prompts, you must ask follow-ups, 
refinements, or clarifications specifically on previous responses or prompts. This should feel and sound like 
a CONVERSATION - follow-up prompts shouldn’t be able to stand on their own in a new conversation and receive the 
same response.

----------

In this task, you will have conversations with the Bot to improve its coding abilities. 

At each turn of the conversation, you will give the model an instruction and receive a response 
from the model trying to follow that instruction. You will then rewrite the model’s response in 
accordance with the guidelines. 

To ensure diversity of conversations, you will be assigned a Concept, and an Operation to begin the 
conversation. You will also be assigned a Subsequent Prompt Guidance on how to continue the conversation. 


IMPORTANT UPDATE:

We are currently working on improving the chatbot's code generation ability. Our goal is to ask questions 
that prompt the chatbot to respond with generated code, along with an explanation of the generated code. So:

Follow the operation given in the instructions for the first prompt.
All subsequent prompts should be asking the bot to generate or modify code in some way.
You will encounter the same instructions more than once; however, it is important to ask unique 
and diverse questions for each task. Remember, repeating them is not allowed.
 * 
 */

class Persona {
    // Define the constructor
    constructor(name, surname, age, occupation) {
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.occupation = occupation;
    }

    // Define getters and setters for the class
    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
    }

    getSurname() {
        return this.surname;
    }

    setSurname(surname) {
        this.surname = surname;
    }

    getAge() {
        return this.age;
    }

    setAge(age) {
        this.age = age;
    }

    getOccupation() {
        return this.occupation;
    }

    setOccupation(occupation) {
        this.occupation = occupation;
    }
}