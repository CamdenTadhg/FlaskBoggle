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
    timer = setInterval(currentGame.updateTimer, 1000);
    timer2 = setInterval(console.log('hi'), 100);
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
        clearInterval(timer2);
        console.log('submit button pressed');
        $feedback.empty();
        event.preventDefault();
        let guess = $guessInput.val();
        console.log('guess is ', guess)
        if (currentGame.timeLeft > 0){
            currentGame.sendGuessToServer(guess);
        }
    })