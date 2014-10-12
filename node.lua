gl.setup(1024, 768)

font = resource.load_font("silkscreen.ttf")
util.file_watch("buzzer.txt", function(content)
    text = content
end)


--video = util.videoplayer("sitcom.mp4", {audio=true})


function node.render()
    
    if text=="Blau" then 
    	font:write(0, 150, text, 350, 0,30,80,180)
    end
    if text=="Orange" then 
    	--video:draw(0, 0, WIDTH, HEIGHT)
    	font:write(0, 150, text, 250, 1,0.2,0,1)
    	
    end
    if text=="Pink" then
    	font:write(0, 150, text, 350, 1,0,1,1)
    end
    if text=="Gruen" then
    	font:write(0, 150, "Grün", 350, 0,1,0,1)
    end
end
