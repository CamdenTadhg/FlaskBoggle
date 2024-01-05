const $guessInput = $('#guess-input');
const $submitButton = $('.submit-button');
const $feedback = $('.feedback-container');

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
    sendGuessToServer(guess);
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
    presentFeedback(response.data);
}

//Present appropriate feedback based on results of axios request
function presentFeedback(result_dict) {
    if (result_dict['result'] === 'ok') {
        const $good = $('<div class="good">');
        $good.text('Good Job!');
        $feedback.append($good);
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