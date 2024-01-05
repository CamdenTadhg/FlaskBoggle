const $guessInput = $('#guess-input');
const $submitButton = $('.submit-button');
const $feedback = $('.feedback-container');
const $scoreContainer = $('.score-container');
const $playAgain = $('#play-again');

let score = 0;
let timer;
let timeLeft = 60;
let entered = [];

//on page load, start timer
document.addEventListener('DOMContentLoaded', function() {
    $playAgain.hide()
    timer = setInterval(updateTimer, 1000);
    updateTimer();
})

//on clicking in input box, clear previous input and remove previous feedback
$guessInput.on('click', function(event){
    console.log('input box clicked');
    $guessInput.val('');
    $feedback.empty();
})

//on pressing submit, pull value from form and submit to server
    $submitButton.on('click', function(event){
        console.log('submit button pressed');
        $feedback.empty();
        event.preventDefault();
        let guess = $guessInput.val();
        console.log('guess is ', guess)
        if (timeLeft > 0){
            sendGuessToServer(guess);
        }
    })

//submit guess to server for testing. Return feedback dictionary
async function sendGuessToServer(word) {
    console.log('entering send guess function');
    const response = await axios({
        method: "POST",
        url: '/guess', 
        data: {guess: word}
    })
    console.log(response);
    presentFeedback(response.data, word);
}

//Present appropriate feedback based on results of axios request
function presentFeedback(result_dict, word) {
    if (result_dict['result'] === 'ok') {
        if (checkDuplicate(word)){
            const $duplicate = $('<div class="bad">');
            $duplicate.text('Duplicate word');
            $feedback.append($duplicate)
        }
        else {
            let score = incrementScore(word, result_dict);
            updateScore(score);
            const $good = $('<div class="good">');
            $good.text('Good Job!');
            $feedback.append($good);
        }
    }
    if (result_dict['result'] === 'not-on-board') {
        const $board = $('<div class="bad">');
        $board.text('Not on this board!');
        $feedback.append($board);
    }
    if (result_dict['result'] === 'not-word') {
        const $word = $('<div class="bad">');
        $word.text("That's not a word!");
        $feedback.append($word);
        }
    }

//check if word has already been entered
function checkDuplicate(word){
    if (entered.includes(word)) {
        return true;
    }
    else {
        entered.push(word)
        return false;
    }
}

//increase score based on length of guess word
function incrementScore(word, result_dict){
    console.log('entering increment score');
    if (result_dict['result'] === 'ok'){
        score += word.length;
        console.log(score);
    }
    return score;
}

//update on-screen score
function updateScore(number){
    console.log('entering updateScore')
    $scoreContainer.text(`Score: ${number}`);
}

//counts down a 60 second timer for game play
function updateTimer(){
    timeLeft = timeLeft - 1;
    if (timeLeft >= 0){
        $('#timer').text(`Timer: ${timeLeft}`);
    }
    else {
        gameOver();
    }
}

//stops timer countdown after time is up
function gameOver(){
    console.log('game over')
    clearInterval(timer);
    sendScoreToServer(score);
    $('#timer').hide();
    $playAgain.show();
}

//submit score to server. 
async function sendScoreToServer(number) {
    console.log('entering send score function');
    const response = await axios ({
        method: "POST", 
        url: '/gameover',
        data: {score: number}
    })
    console.log(response);
}