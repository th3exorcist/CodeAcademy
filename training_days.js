// The scope of `random` is too loose 

const name = 'Nala';
const days = 1;
const getRandEvent = () => {
 let random = Math.floor(Math.random() * 3);
  if (random === 0) {
    return 'Marathon';
  } else if (random === 1) {
    return 'Triathlon';
  } else if (random === 2) {
    return 'Pentathlon';
  }
};

// The scope of `days` is too tight 

function getTrainingDays(days, event) {

  if (event === 'Marathon') {
    let days = 50;
  } else if (event === 'Triathlon') {
    let days = 100;
  } else if (event === 'Pentathlon') {
    let days = 200;
  }

  return days;
}

// The scope of `name` is too tight 
function logEvent(name, event) {
  name = 'Nala';
  console.log(`${name}'s event is: ${event}`);
}

function logTime(name, days) {
  name = 'Nala';
  console.log(`${name}'s time to train is: ${days} days`);
}

const event = getRandEvent();
day = getTrainingDays(event);
// Define a `name` variable. Use it as an argument after updating logEvent and logTime 


logEvent(event);
logTime(day);

// Another competitor

const event2 = getRandEvent();
const days2 = getTrainingDays(event2);
const name2 = 'Warren';

logEvent(name2, event2);
logTime(name2, days2);
