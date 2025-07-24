import re
from collections import Counter


def find_repeated_segments(text, min_len=4, freq_threshold=2):
	"""
	Finds all substrings of length >= min_len that appear at least freq_threshold times.
	Returns a dict { substring: frequency }.
	Uses a naive overlapping approach (regex lookahead).
	"""
	seg_freq = {}
	n = len(text)
	
	# For performance, you can limit max_len here: e.g., min(n//2, 20)
	max_len = n // 2
	
	for L in range(min_len, max_len + 1):
		for i in range(n - L + 1):
			seg = text[i:i + L]
			
			# (Optional) If you only want purely alphabetic substrings:
			# if not seg.isalpha():
			#     continue
			
			# Overlapping search with lookahead
			pattern = r"(?=({}))".format(re.escape(seg))
			count = len(re.findall(pattern, text))
			if count >= freq_threshold:
				# Store maximum count found for this substring
				# (instead of re-counting for each occurrence).
				if seg not in seg_freq:
					seg_freq[seg] = count
	return seg_freq


def mark_repeated_segments(text, substring_freqs):
	"""
	Given { substring: frequency }, create intervals (start, end, freq) in 'text'
	for non-overlapping occurrences (sorted by descending 'importance').

	Returns:
	  intervals (list of (start, end, freq))
	  occupied (list of bool) marking which text indices are covered.
	"""
	# -------------------------------------------------------------------------
	# CHANGE #1: Sort by frequency first, then by length. (Option A):
	# substrings_sorted = sorted(
	#     substring_freqs.items(),
	#     key=lambda x: (x[1], len(x[0])),
	#     reverse=True
	# )
	#
	# ALTERNATIVELY (Option B): Sort by "score" = freq * length
	# so that both frequency and substring length matter equally.
	# This often leads to the largest repeated substrings
	# (that also appear multiple times) getting highest priority:
	# -------------------------------------------------------------------------
	substrings_sorted = sorted(
		substring_freqs.items(),
		key=lambda x: (x[1] * len(x[0])),
		reverse=True
	)
	
	intervals = []
	occupied = [False] * len(text)
	
	for seg, freq in substrings_sorted:
		pattern = re.compile(re.escape(seg))
		for match in pattern.finditer(text):
			start, end = match.start(), match.end()
			# Skip if overlapping an already chosen interval
			if any(occupied[start:end]):
				continue
			# Mark this range as occupied
			for i in range(start, end):
				occupied[i] = True
			intervals.append((start, end, freq))
	
	return intervals, occupied


def mark_single_letters(text, occupied):
	"""
	For unoccupied alphabetic chars, create intervals (start, end, freqOfLetter).
	"""
	intervals = []
	letter_counts = Counter(c for c in text if c.isalpha())
	
	n = len(text)
	for i in range(n):
		if not occupied[i] and text[i].isalpha():
			letter = text[i]
			letter_freq = letter_counts[letter]
			intervals.append((i, i + 1, letter_freq))
	return intervals


def compute_color_map(intervals):
	"""
	Map each interval's frequency (or 'score') to a color
	between blue (min) and green (max).

	Returns a dict { (start, end, freq): color_string }.
	"""
	if not intervals:
		return {}
	
	# Default: color by the 'freq' field
	freqs = [iv[2] for iv in intervals]
	
	# OPTIONAL: if you used "score = freq * length" or something,
	# store that in the interval tuple or compute it here:
	#   scores = [iv[2] * (iv[1] - iv[0]) for iv in intervals]
	#   min_val, max_val = min(scores), max(scores)
	# Then in lerp_color(), interpolate based on that score.
	
	min_freq, max_freq = min(freqs), max(freqs)
	
	def lerp_color(freq):
		"""
		Interpolate freq from min_freq->max_freq onto blue->green.
		Blue = (0,0,255), Green = (0,255,0).
		"""
		if min_freq == max_freq:
			# Edge case: all intervals have same freq => all green
			return "rgb(0,255,0)"
		
		ratio = (freq - min_freq) / (max_freq - min_freq)
		start_r, start_g, start_b = 0, 0, 255  # Blue
		end_r, end_g, end_b = 0, 255, 0  # Green
		r = int(start_r + (end_r - start_r) * ratio)
		g = int(start_g + (end_g - start_g) * ratio)
		b = int(start_b + (end_b - start_b) * ratio)
		return f"rgb({r},{g},{b})"
	
	color_map = {}
	for iv in intervals:
		color_map[iv] = lerp_color(iv[2])
	return color_map


def merge_intervals(intervals):
	"""
	Sort intervals by their start position.
	(They are already non-overlapping in this approach.)
	"""
	return sorted(intervals, key=lambda x: x[0])


def colorize_html(text, intervals, color_map):
	"""
	Return an HTML string with each interval in <span style="color: X">.
	"""
	intervals = merge_intervals(intervals)
	result = []
	last_end = 0
	
	for (start, end, freq) in intervals:
		if start > last_end:
			result.append(text[last_end:start])  # uncolored chunk
		seg = text[start:end]
		color = color_map[(start, end, freq)]
		result.append(f"<span style=\"color:{color}; font-weight:bold;\">{seg}</span>")
		last_end = end
	
	# Remainder
	if last_end < len(text):
		result.append(text[last_end:])
	
	return (
			"<html><body>"
			"<pre style='font-family:monospace;font-size:14px;'>"
			+ "".join(result)
			+ "</pre></body></html>"
	)


def ansi_24bit_color(r, g, b, bold=True):
	"""
	Return an ANSI escape code for 24-bit (True Color) foreground.
	'bold=True' toggles bold text.
	"""
	code = f"\033[38;2;{r};{g};{b}m"
	if bold:
		code += "\033[1m"
	return code


def colorize_console(text, intervals, color_map):
	"""
	Build a console string with ANSI colors for each interval.
	"""
	intervals = merge_intervals(intervals)
	output = []
	last_end = 0
	
	for (start, end, freq) in intervals:
		# Add uncolored portion
		if start > last_end:
			output.append(text[last_end:start])
		# Parse "rgb(R,G,B)"
		color_str = color_map[(start, end, freq)]
		rgb_values = color_str.strip("rgb()").split(",")
		r, g, b = map(int, rgb_values)
		seg = text[start:end]
		
		# Start color
		output.append(ansi_24bit_color(r, g, b, bold=True))
		output.append(seg)
		# Reset color
		output.append("\033[0m")
		
		last_end = end
	
	# Any tail text uncolored
	if last_end < len(text):
		output.append(text[last_end:])
	
	return "".join(output)


def main():
	# Sample text from Ricky McCormick’s note (page1 + page2).
	page1 = """(MNDMKNEARSE-N-S-M-KNARE) (ACSM?)
TFRNE NPtNSE NPBSER CBRNSE NPRSE INC
PRSE NMRSE OPRE HLDNLDNCBE(TFXLE TCXL N CBE)
AL-PRPPIT XLYPPIY NCBE MGKSE W CD RCBR NSE PRSE
WLDRCBRNSE NT SGNENTXSE-CRSLE-CLTRSE WLDNCBE
ALWLD NCBE TSME LRSE RLSE VRGLSNE AS N WLD NCBE
(NOPFSE NLSRE NCBE)NTE GDDMNSENCURERCBRNE
     (TENE TFRNE NCBRTSENCBE INC)
         (FLRSE PRSE ONDE 71 NCBE)
         (CDNSE PRSE ONSDE 74 NCBE)
         (PRTSE PRSE ONREDE 75 NCBE)
(TF NRCMSP SOLE MRDE LUSE TO TE WLD N WLD NCBE)
                     (194 WLD'S NCBE) (TRFXL)"""
	
	page2 = """ALPNTE GLSE - SE ERtE
VLSE MTSE-CTSE-WSE-FRTSE
PNRTRSE ONDRSE WLD NCBE
 NWLDXLRCMSP NEWLD S TS MEXL
    DVLMT 6TUNSE NCBEXL
  (MUNSARSTENMUNARSE)
KLSE-LRSTE-TR SE-TRSE-MKSE?-MRSE
    (SAEGNSE SE NMRSE)
NMNRCBRNSE PTE ZPTE WSRCBRMSE
36MLSE 74SPRKSE 29KENOSOLE 173RTRSE
 35 GLE CLGSE VUNVTRE DKRSE PSESHLE
  651MTCSE HTLSE NCVTCTRS NMRE
   99.84.S ZUNE PLSE NCRSE AOLTSE NSRSE NBSE
    NSREONSE PVTSE WLD NCBE (3XORL)
    BNMSE NRSE INZ NTRLE RCBRNSE NTSRCRSNE
    LSPNSE NGSPSE MKSERBSE NCBEAVXLR
      HM CRE NMRE NCBE 1/2 MUND PLSE
        D-W-M-4 MIL XDRLX"""
	
	combined_text = page1 + "\n\n--- PAGE 2 ---\n\n" + page2
	
	# 1) Find repeated segments (with min_len=4 by default)
	substring_freqs = find_repeated_segments(combined_text, min_len=4, freq_threshold=2)
	
	# 2) Mark repeated substrings (non-overlapping)
	repeated_intervals, occupied = mark_repeated_segments(combined_text, substring_freqs)
	
	# 3) Mark leftover single letters
	single_intervals = mark_single_letters(combined_text, occupied)
	
	# Combine intervals
	all_intervals = repeated_intervals + single_intervals
	
	# 4) Build a color map (blue -> green) based on freq
	color_map = compute_color_map(all_intervals)
	
	# 5) Generate HTML output
	html_output = colorize_html(combined_text, all_intervals, color_map)
	with open("mccormick_colored_gradient.html", "w", encoding="utf-8") as f:
		f.write(html_output)
	print("HTML output written to 'mccormick_colored_gradient.html'.")
	
	# 6) Print colored text to the console
	console_colored_str = colorize_console(combined_text, all_intervals, color_map)
	print("\n========== CONSOLE COLORED OUTPUT BELOW ==========\n")
	print(console_colored_str)
	print("\n==================================================\n")


if __name__ == "__main__":
	main()
