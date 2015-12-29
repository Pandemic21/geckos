import praw
import time

def get_post_data():
	#file format:
	#<URL to image>,<author>
	try:
		f = open('geckos.txt', 'r')
	except Exception as e:
		gen_log('Fatal error reading "geckos.txt", verify the file exists\nError {0}: {1}'.format(e.errno, e.strerror))
		exit(1)
	data = f.readline().rstrip().split(',')
	try: 
		gen_log('geckos.txt data[0] = ' + data[0] + ', data[1] = ' + data[1])
	except Exception as e:
		gen_log('Fatal error parsing "geckos.txt", verify there is data in the file')
		exit(1)
	return data

def create_post(title, url):
	gen_log('Title=' + title)
	gen_log('URL=' + url)
	r.submit('geckos',title,url=url)

def remove_from_file(line_to_archive):
	gen_log('line to archive=' + line_to_archive)
	f = open(archivefile, 'a')
	f.write(line_to_archive)
	f.close()
	with open(sourcefile, 'r') as fin:
		data = fin.read().splitlines(True)
	with open(sourcefile, 'w') as fout:
		fout.writelines(data[1:])
	
#logs to the log file
#log file is "nerfgerf.log" in the current directory
def gen_log(data):
	f = open(logfile, 'a')
	datetime =  str(time.strftime("%Y/%m/%d")) + " " + str(time.strftime("%H:%M:%S"))
	f.write(datetime + ": " + data + "\n")
	f.close()
	print datetime + ": " + data

###########################################################################################
###########################################################################################
###########################################################################################

r = praw.Reddit('/r/geckos daily post by /u/Pandemic21')
logfile = 'geckos.log'
sourcefile = 'geckos.txt'
archivefile = 'geckos_archive.txt'

username = ''
password = ''
r.login(username,password)

data = get_post_data()
create_post('Your daily random gecko post for ' + str(time.strftime("%m/%d")) + ' by ' + data[1],data[0])
remove_from_file(data[0] + ',' + data[1] + ',' + str(time.strftime("%m/%d")))
