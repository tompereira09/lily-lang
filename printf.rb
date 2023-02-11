class Print
	def printf(args_list)
		joined = args_list.join()
		if args_list[0].include?('"')
			new = joined.split('"')
                	string = new.join(" ")
                end

		return string
	end
end
