"use strict";


/******************************************************************************
 * BoggleGame: a class holding all the methods necessary to run the boggle game
 */

class BoggleGame {
    // Make instance of BoggleGame to set basic variables for functionality. 

    constructor(){
        this.score = 0;
        this.timeLeft = 60;
        this.entered = [];
    }

    // Submits guess to server for testing. returns feedback dictionary
    async sendGuessToServer(word){
        console.log('entering send guess function');
        const response = await axios({
            method: "POST",
            url: '/guess', 
            data: {guess: word}
        })
        console.log(response);
        this.presentFeedback(response.data, word);
    }

    //presents appropriate feedback based on results of axios request
    presentFeedback(result_dict, word) {
        if (result_dict['result'] === 'ok') {
            if (this.checkDuplicate(word)){
                const $duplicate = $('<div class="bad">');
                $duplicate.text('Duplicate word');
                $feedback.append($duplicate)
            }
            else {
                let score = this.incrementScore(word, result_dict);
                this.updateScore(score);
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

    //checks if word has already been entered
    checkDuplicate(word){
    if (this.entered.includes(word)) {
        return true;
    }
    else {
        this.entered.push(word)
        return false;
    }
    }

    //increase score based on length of guess word
    incrementScore(word, result_dict){
    console.log('entering increment score');
    if (result_dict['result'] === 'ok'){
        this.score += word.length;
        console.log(this.score);
    }
    return this.score;
    }

    //update on-screen score
    updateScore(number){
        console.log('entering updateScore')
        $scoreContainer.text(`Score: ${number}`);
    }

    //submit score to server. 
    async sendScoreToServer(number) {
        console.log('entering send score function');
        const response = await axios ({
            method: "POST", 
            url: '/gameover',
            data: {score: number}
        })
        console.log(response);
    }

    //end the game
    gameOver() {
        clearInterval(timer);
        $playAgain.show();
        $('#timer').hide();
        this.sendScoreToServer(this.score);
    }

    //update available time left
    updateTimer() {
        console.log('running updateTimer');
        console.log(`time left is ${this.timeLeft}`);
        this.timeLeft = this.timeLeft - 1;
        console.log(`timeLeft is ${this.timeLeft}`);
        if (this.timeLeft > 0){
            console.log('You still have time left');
            $('#timer').html(`Timer: ${this.timeLeft}`)
        }
        else {
            this.gameOver();
        }
    }

}
