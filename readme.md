## What is
The purpose of this script is simply to keep track of the time you spend on your computer, Not only that you can also find out how much time is spent on work, games, social media, learning, etc.

This script only focuses on storing data, to analyze the stored data you can use your own notebook/script.

## How it works
The script are running in background and keep track of what apps are currently open (only active window). The tracking/polling system is run every `x` seconds then the results are stored to database.

## Stored Data
- [String] Process name (ex: chrome.exe, word.exe) (maximum 50 characters)
- [DateTime]: the current date and time
- [String] Window title (maximum 150 characters)

## Comparison of data size based on `x` value, in one day
Assuming the script runs non-stop and uses maximum string size
The size of the data for each item (bytes) : 50 + 8 + 150 = 208 Byte
Total second in one day : 60 * 60 * 24 = 86400 Sec

```js
// Javascript
const x_values = [10, 30, 60]
const sec_indays = 60 * 60 * 24
const size_each = 208

for (const x of x_values){
	const record_inday = sec_indays / x
	const size_byte = size_each * record_inday
	const size_mb = parseFloat(size_byte / 1024 / 1024).toFixed(2)
	console.log({x, record_inday, size_byte, size_mb})
}
// Result
// {x: 10, record_inday: 8640, size_byte: 1797120, size_mb: '1.71'}
// {x: 30, record_inday: 2880, size_byte: 599040, size_mb: '0.57'}
// {x: 60, record_inday: 1440, size_byte: 299520, size_mb: '0.29'}
```

