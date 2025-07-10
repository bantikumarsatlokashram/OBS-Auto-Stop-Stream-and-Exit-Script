# OBS Auto Stop Stream and Exit Script

This Lua script for OBS automatically stops your live stream and closes OBS at a specified daily time (default: **6:52 AM IST**).

## 📋 Features

- Monitors the system clock every second.
- Stops the stream exactly at the set time.
- Waits 5 seconds, then exits OBS.
- Runs **entirely inside OBS** (no external tools needed).
- Compatible with **all platforms** supported by OBS (Windows, macOS, Linux).

---

## 🛠 Requirements

- OBS Studio (v28 or newer recommended)
- No external dependencies — uses built-in **Lua scripting**.

---

## 🕓 Default Time Setting

- **Target Time:** `6:52 AM`  
- **Time Zone:** Uses your system's local time.  
  (Make sure your system clock is set to Indian Standard Time (IST) if you're targeting IST.)

---

## 📂 Installation Steps

1. Open OBS Studio.
2. Go to: `Tools > Scripts`.
3. Click the **`+` (Add)** button.
4. Select the file: `stop_stream_at_time.lua`
5. The script will start running automatically.

---

## 🧠 How It Works

- The script checks the system time every second.
- When it matches the target hour and minute, it:
  1. Stops the stream (if active)
  2. Waits 5 seconds
  3. Closes OBS automatically

---

## 🧑‍💻 Customization

You can edit these values directly in the script:

```lua
local target_hour = 6
local target_minute = 52
