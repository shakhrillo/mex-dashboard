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
    "Sonntag",
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
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

export function calculateDaysExcludingWeekends(start, end) {
    console.log(start, end);

    const startDate = new Date(start);
    const endDate = new Date(end); // today

    endDate.setHours(0, 0, 0, 0);

    // Calculate total time difference in milliseconds
    const totalMilliseconds = endDate - startDate;

    // Convert to hours and minutes
    const totalMinutes = Math.floor(totalMilliseconds / (1000 * 60));
    const totalHours = Math.floor(totalMinutes / 60);
    const remainingMinutes = totalMinutes % 60;

    // Create an array to keep track of weekend days (0 = Sunday, 6 = Saturday)
    let weekendDays = 0;
    let currentDate = new Date(startDate);

    // Loop through each day in the range
    while (currentDate < endDate) {
        const dayOfWeek = currentDate.getDay();
        if (dayOfWeek === 0 || dayOfWeek === 6) {
            weekendDays++;
        }
        currentDate.setDate(currentDate.getDate() + 1);
    }

    // Calculate effective time excluding weekends
    const effectiveTotalMinutes = totalMinutes - (weekendDays * 24 * 60);
    const effectiveHours = Math.floor(effectiveTotalMinutes / 60);
    const effectiveMinutes = effectiveTotalMinutes % 60;

    console.log(
        "Days:", Math.floor(effectiveHours / 24), "hours", effectiveHours % 24, "effectiveMinutes", effectiveMinutes);
    if (effectiveHours < 0)
        return 0;
    return effectiveHours;
    // return {
    //     days: Math.floor(effectiveHours / 24),
    //     hours: effectiveHours % 24,
    //     minutes: effectiveMinutes
    // };
}

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
        // if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
        //     weekdays.push(new Date(currentDate));
        // }
        weekdays.push(new Date(currentDate)); // O'chadi

        daysToSubtract--; // Move to the previous day
    }

    return weekdays;
};

function addDaysAndMinutes(date, days, minutes) {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    result.setMinutes(result.getMinutes() + minutes);
    return result;
}

function skipWeekend(date) {
    const day = date.getDay();
    if (day === 6) { // Saturday
        date.setDate(date.getDate() + 2); // Skip to Monday
    } else if (day === 0) { // Sunday
        date.setDate(date.getDate() + 1); // Skip to Monday
    }
    return date;
}

function calculateNewDate(initialDate) {
    let newDate = addDaysAndMinutes(initialDate, 2, 12);
    newDate = skipWeekend(newDate);
    return newDate;
}

// Initial date: 23 May 00:00 (year is assumed for Date object)
// const initialDate = new Date('2024-05-23T00:00:00');

// Calculate the new date
// const newDate = calculateNewDate(initialDate);

// console.log("newDate", newDate);


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

export function addTimeSkippingWeekends(startDate, daysToAdd, minutesToAdd) {
    const totalMinutes = daysToAdd * 24 * 60 + minutesToAdd;
    let remainingMinutes = totalMinutes;
    let currentDate = new Date(startDate);

    while (remainingMinutes > 0) {
        currentDate.setMinutes(currentDate.getMinutes() + 1);

        // Skip weekends
        // if (currentDate.getDay() === 6 || currentDate.getDay() === 0) {
        //     continue;
        // }

        remainingMinutes--;
    }

    return currentDate;
}