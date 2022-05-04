


const questionNumber = document.querySelector(".question-number");
const questionText = document.querySelector(".question-text");
const optionContainer = document.querySelector(".option-container");
const homeBox = document.querySelector(".home-box");
const quizBox = document.querySelector(".quiz-box");
const resultBox = document.querySelector(".result-box");
const retBtn = document.querySelector(".rbtn");
const modBtn = document.querySelector(".mbtn");

let questionCounter = 0;
let currentQuestion;
let availableQuestions = [];
let availableOptions = [];
let questionIndex;
let correctAnswers = 0;
let attempt = 0;
let count = 0;

//push questions into availableQuestions array
function setAvailableQuestions(){
  const totalQuestion = quiz.length;
  for(let i=0; i<totalQuestion; i++){
    availableQuestions.push(quiz[i])
    }
}

//set question numbers and options
function getNewQuestion(){
  //set question number
  questionNumber.innerHTML = "Question " + (questionCounter+1)+ " of " + quiz.length;
  //set question question text
  //get random question
  const questionIndex = availableQuestions[Math.floor(Math.random() * availableQuestions.length)]
  currentQuestion = questionIndex;
  questionText.innerHTML = currentQuestion.q;
  //get the position of 'questionIndex' from the availableQuestions array
  const index1=availableQuestions.indexOf(questionIndex);
  //get the position of the 'questionIndex' from the availableQuestions array so the question doesn't repeat
  availableQuestions.splice(index1,1);

  //set options
  //set length of options
  const optionLen = currentQuestion.options.length
  //push options into availableOptions array
  for(let i=0; i<optionLen; i++){
      availableOptions.push(i)
    }
    optionContainer.innerHTML = '';
  //create options in html
  for(let i=0; i<optionLen; i++){
    const OptonIndex = availableOptions[Math.floor(Math.random() * availableOptions.length)]
    //get position of OptionIndex
    const index2=availableOptions.indexOf(OptonIndex)
    //remove OptionIndex from availableOptions
    availableOptions.splice(index2,1);
    const option = document.createElement("div");
    option.innerHTML=currentQuestion.options[OptonIndex];
    option.id = OptonIndex;
    option.className = "option";
    optionContainer.appendChild(option)
    option.setAttribute("onclick","getResult(this)");
  }
  questionCounter++
}

//get result of current attempt
function getResult(element){
  const id = parseInt(element.id);
  //get answer by comparing id of clicked option
  if(id===currentQuestion.answer){
  //set the green color of the correct option
      element.classList.add("correct");
      correctAnswers++;
      //console.log("correct");
  }
    else{
      element.classList.add("incorrect");
      console.log("incorrect");

      //if the answer is incorrect show the correct answer in green
      const optionLen = optionContainer.children.length;
      for(let i=0; i<optionLen; i++){
        if(parseInt(optionContainer.children[i].id) === currentQuestion.answer){
          optionContainer.children[i].classList.add("correct");
        }
      }

    }
    attempt++;
    unclickableOptions();
}
//make all the options unclickable once user selects an option (user cannot change option)
function unclickableOptions(){
  const optionLen = optionContainer.children.length;
  for(let i=0; i<optionLen; i++){
    optionContainer.children[i].classList.add("cannot-select");
    console.log("cannot-select")
  }
}
function next(){
  if(questionCounter===quiz.length){
    console.log("quiz over");
    quizOver();
  }
  else{
    getNewQuestion();
  }
}

function startQuiz(){
  //show quizBox
  quizBox.classList.remove("hide");
  //hide homeBox
  homeBox.classList.add("hide");
  //count number of times start quiz button is clicked;
   count = count + 1;
   count++;
}

function quizOver(){
  //hide quizBox
  quizBox.classList.add("hide");
  //show resultBox
  resultBox.classList.remove("hide");
  quizResult();
}

//get quiz result
function quizResult(){
  resultBox.querySelector(".total-question").innerHTML = quiz.length;
  resultBox.querySelector(".total-attempt").innerHTML = count;
  resultBox.querySelector(".total-correct").innerHTML = correctAnswers;
  resultBox.querySelector(".total-wrong").innerHTML = attempt - correctAnswers;
  const percentage = (correctAnswers/quiz.length)*100;
  resultBox.querySelector(".total-percentage").innerHTML = percentage.toFixed() + "%";
  resultBox.querySelector(".total-score").innerHTML = correctAnswers + "/" + quiz.length;
  //show module2 button of user passes with 80% or more
  if(percentage>=80){
    modBtn.classList.remove("hide");
  }
  else{
    console.log("failed quiz");
  }
}

function resetQuiz(){
  //show quizBox
  quizBox.classList.add("hide");
  //hide homeBox
  homeBox.classList.remove("hide");
  //hide quizResult
  resultBox.classList.add("hide");
  //reload page
  location.reload()
}

function gotoMod4(){
  window.location.href = "http://127.0.0.1:5000/mod4home";
}

window.onload = function(){
  //first: set all questions in availableQuestions array
  setAvailableQuestions();
  //second: call getNewQuestion function
  getNewQuestion();
}
