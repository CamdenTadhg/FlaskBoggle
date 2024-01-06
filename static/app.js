const $guessInput = $('#guess-input');
const $submitButton = $('.submit-button');
const $feedback = $('.feedback-container');
const $scoreContainer = $('.score-container');
const $playAgain = $('#play-again');
let timer;

const currentGame = new BoggleGame();

//on page load, start timer
document.addEventListener('DOMContentLoaded', function() {
    $playAgain.hide()
    timer = setInterval(() => currentGame.updateTimer(), 1000);
    currentGame.updateTimer();
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
        if (currentGame.timeLeft > 0 && guess != ''){
            currentGame.sendGuessToServer(guess);
        }
        if (guess === ''){
            const $noword = $('<div class="bad">');
            $noword.text('Please enter a word');
            $feedback.append($noword);
        }
    })