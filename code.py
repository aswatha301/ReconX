local http = require "http"
local shortport = require "shortport"
local stdnse = require "stdnse"

description = [[
Enumerates directories and detects 200/403 responses.
]]

author = "Your Name"
categories = {"discovery", "safe"}

portrule = shortport.http

action = function(host, port)
    local results = {}
    local wordlist = stdnse.get_script_args("wordlist") or "dirs.txt"

    for dir in io.lines(wordlist) do
        local r = http.get(host, port, "/" .. dir)
        if r and r.status then
            if r.status == 200 or r.status == 403 then
                table.insert(results, "[" .. r.status .. "] /" .. dir)
            end
        end
    end

    return table.concat(results, "\n")
end
