#!/usr/bin/env lua

-- This program takes two optional arguments.
-- The first one is always the input filename (or '-' for stdin).
-- The second one is always the output filename (or '-' for stdout).
-- All other arguments are ignored.

local args = table.pack(...)
local input = nil
local output = nil

-- Select input.
if args[1] and args[1]~="-" then
  input = assert(io.open(args[1], "r"))
else
  input = io.input()
end

-- Select output.
if args[2] and args[2]~="-" then
  output = assert(io.open(args[2], "w"))
else
  output = io.output()
end

-- Load data.
local data = {}
for l in input:lines() do
  a, b = l:match("(%d+) (%d+)")
  if a and b then
    a, b = tonumber(a), tonumber(b)
    if a and b then
      table.insert(data, {a, b})
    else
      break
    end
  else
    break
  end
end

-- Ensure correct order of input data.
table.sort(data, function(t1, t2) return t1[1]<t2[1] end)

-- Find the biggest gap in which any person is in the room.
local max_gap = -1

-- First person enters.
local first_enter_time = data[1][1]
local last_exit_time = data[1][2]
table.remove(data, 1)
print("First person was in the room from "..first_enter_time.." to "..last_exit_time..".")

-- Simulate people going in and out.
for _, t in ipairs(data) do
  local enter_time = t[1]
  local exit_time = t[2]
  if enter_time > last_exit_time then
    -- Record new gap
    local new_gap = last_exit_time - first_enter_time + 1
    max_gap = math.max(max_gap, new_gap)
    print("The light turned off at "..last_exit_time.." and it was active for "..new_gap.." hours")
    -- Next person enters the room.
    first_enter_time = enter_time
    last_exit_time = exit_time
    print("A new person entered the room at "..enter_time.." and stayed until "..exit_time..".")
  else
    -- Continue recording movement.
    last_exit_time = exit_time
    print("Next person got in at "..enter_time.." and stayed in until "..exit_time..".")
  end
end

-- Calculate the last gap.
local last_gap = last_exit_time - first_enter_time + 1
max_gap = math.max(max_gap, last_gap)
print("Light finally died after being on for "..last_gap.." hours.")

-- Output the result.
output:write(tostring(max_gap).."\n")
