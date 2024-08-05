## What is
The purpose of this script is simply to keep track of the time you spend on your computer. Not only track your screen time but you can also find out how much time is spent on work, games, social media, learning, etc, or find out which app you use the most.

This script only focuses on storing data, to analyze the stored data you can use your own notebook/script.

## How it works
The script are running in background and keep track of what apps are currently open (only active window). The tracking/polling system is run every `x` seconds then the results are stored to database.

## Stored Data
- [String] Process name (ex: chrome.exe, word.exe) (maximum 50 characters)
- [DateTime]: the current date and time
- [String] Window title (maximum 150 characters)

On sqlite database the maximum size for each item (bytes) would be 50 + 8 + 150 = 208 Byte

## Comparison of data size based on `x` value, in one day
Assuming the script runs non-stop and uses maximum string size

```js
// Javascript
const x_values = [10, 30, 60]
const sec_inday = 60 * 60 * 24
const size_each = 208

for (const x of x_values){
	const record_inday 	= sec_inday / x
	const size_mb 		= size_each * record_inday / 1024 / 1024
	const size_inday 	= (size_mb).toFixed(2) + " MB"
	const size_inmonth 	= (size_mb * 30).toFixed(2) + " MB"
	const size_inyear 	= (size_mb * 30 * 12).toFixed(2) + " MB"

	console.log({ x, record_inday, size_inday, size_inmonth, size_inyear })
}

// Result
// {x: 10, record_inday: 8640, size_inday: '1.71 MB', size_inmonth: '51.42 MB', size_inyear: '616.99 MB'}
// {x: 30, record_inday: 2880, size_inday: '0.57 MB', size_inmonth: '17.14 MB', size_inyear: '205.66 MB'}
// {x: 60, record_inday: 1440, size_inday: '0.29 MB', size_inmonth: '8.57 MB', size_inyear: '102.83 MB'}

```

