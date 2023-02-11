require './printf.rb'

#Module Initializing
printer = Print.new()
#Module End

#File Reading Start
file_path = ARGV[0]
file_data = File.readlines(file_path)
#File Reading End

for i in file_data do
	data = i.split(" ")
	
	#printf "Hello World"
	if data[0] == "printf"
		send = data[1...]
		puts printer.printf(send)
	end
end

