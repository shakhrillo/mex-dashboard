export const machines = [
    "E 35-1",
    "E 45-1",
    "E 45-2",
    "F450iA-1",
    "E 50-2",
    "E 50-3",
    "F150iA-1",
    "Emac50-1",
    "Emac50-2",
    "Emac50-3",
    "KM 50-1",
    "KM 80-1",
    "KM 150-1",
    "E 55-1",
    "KM 420-1",
    "E 120-1",
    "E 80-1",
    "F250iA-1"
];

// get weekdays name
export const weekdays = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag"
];

// get the month name
export const monthNames = [
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember"
];

export const calculateDaysExcludingWeekends = (startDate, endDate) => {
    const start = new Date(startDate);
    const end = new Date(endDate);

    start.setHours(0, 0, 0, 0);
    end.setHours(0, 0, 0, 0);
    let totalDays = 0;
    let weekendDays = 0;

    for (let date = new Date(start); date < end; date.setDate(date.getDate() + 1)) {
        if (date.getDay() === 0 || date.getDay() === 6) {
            weekendDays++;
        } else {
            totalDays++;
        }
    }
    return totalDays;
};

export const getLastFiveWeekdays = () => {
    const weekdays = [];
    let currentDate = new Date();
    let daysToSubtract = 0;

    // Loop until we have collected five weekdays
    while (weekdays.length < 7) {
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

export function addMinutes(date, minutes, days = 0) {
    const millisecondsPerMinute = 60000;
    let updatedTime = new Date(date).getTime() + minutes * millisecondsPerMinute + days * 24 * 60 * millisecondsPerMinute;
    let newDate = new Date(updatedTime);

    // Function to check if a date is on a weekend
    function isWeekend(d) {
        const day = d.getDay();
        return day === 6 || day === 0; // 6 is Saturday, 0 is Sunday
    }

    // If the new date is on a weekend, move to the next Monday
    while (isWeekend(newDate)) {
        newDate.setDate(newDate.getDate() + 1);
        // newDate.setHours(
        //     // by calculating the minutes
        //     Math.floor(minutes / 60),
        //     minutes % 60,
        //     0,
        //     0
        // );
    }

    return newDate;
}