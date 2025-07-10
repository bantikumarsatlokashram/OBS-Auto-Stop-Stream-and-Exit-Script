obs = obslua

-- Target time (24-hour format)
local target_hour = 6
local target_minute = 52
local already_triggered = false

function script_description()
    return "Stops the stream and exits OBS at 6:52 AM IST daily"
end

function on_tick()
    local time = os.date("*t")  -- Get current local time
    if time.hour == target_hour and time.min == target_minute and not already_triggered then
        already_triggered = true

        if obs.obs_frontend_streaming_active() then
            obs.obs_frontend_stop_streaming()
        end

        -- Delay OBS exit by 5 seconds to ensure stream stops
        obs.timer_add(function()
            obs.obs_frontend_exit()
        end, 5000)
    elseif time.hour ~= target_hour or time.min ~= target_minute then
        -- Reset trigger after the minute has passed
        already_triggered = false
    end
end

function script_load(settings)
    obs.timer_add(on_tick, 1000) -- check every second
end
