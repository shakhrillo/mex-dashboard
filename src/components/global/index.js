export const machines = [
    "Emac50-1",
    "E 35-1",
    "E45-1",
    "E45-2",
    "F 450iA-1",
    "E50-2",
    "E50-3",
    "F 150iA-1",
    "EM 50-1",
    "EM 50-2",
    "EM 50-3",
    "KM 50-1",
    "KM 80-1",
    "KM 150-1",
    "EM 55-1",
    "KM 420-1",
    "E 120-1",
    "E 80-1",
    "F 250iA-1",
];

// get weekdays name
export const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

// get the month name
export const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];

export const calculateDaysExcludingWeekends = (startDate, endDate) => {
    const start = new Date(startDate);
    const end = new Date(endDate);
    start.setHours(0, 0, 0, 0);
    end.setHours(0, 0, 0, 0);
    console.log("Start Date: ", start);
    console.log("End Date: ", end);
    let totalDays = 0;
    let weekendDays = 0;

    for (let date = new Date(start); date < end; date.setDate(date.getDate() + 1)) {
        if (date.getDay() === 0 || date.getDay() === 6) {
            weekendDays++;
        } else {
            totalDays++;
        }
    }
    console.log("Total Days: ", totalDays);
    console.log("Weekend Days: ", weekendDays);
    return totalDays;
};

export const getLastFiveWeekdays = () => {
    const weekdays = [];
    let currentDate = new Date();
    let daysToSubtract = 0;

    // Loop until we have collected five weekdays
    while (weekdays.length < 5) {
        // Subtract days one by one
        currentDate = new Date();
        currentDate.setDate(currentDate.getDate() - daysToSubtract);

        // Check if the current day is not Saturday or Sunday
        if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
            weekdays.push(new Date(currentDate));
        }

        daysToSubtract--; // Move to the previous day
    }

    return weekdays;
};

export function addMinutes(date, minutes) {
    const millisecondsPerMinute = 60000;
    let updatedTime = new Date(date).getTime() + minutes * millisecondsPerMinute;
    let newDate = new Date(updatedTime);

    // Function to check if a date is on a weekend
    function isWeekend(d) {
        const day = d.getDay();
        return day === 6 || day === 0; // 6 is Saturday, 0 is Sunday
    }

    // If the new date is on a weekend, move to the next Monday
    while (isWeekend(newDate)) {
        newDate.setDate(newDate.getDate() + 1);
        newDate.setHours(0, 0, 0, 0); // Reset time to the start of the day
    }

    return newDate;
}