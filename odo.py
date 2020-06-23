import os, re, fnmatch

reobj = re.compile(r'\d{4}-\d{2}-\d{2}')
root_folder = r'r:\\00_daily_testing'
for root, subs, files in os.walk(root_folder):
    for loc_log in subs:
        if reobj.match(loc_log):
            full_path = os.path.join(root_folder, loc_log)
            for root, dirs, files in os.walk(full_path):
                for file in files:
                    if fnmatch.fnmatch(file, '*.log'):
                        found_files = os.path.join(root, file)
                        important = []
                        search_pattern = ["odometerKm"]
                        if not file: continue    
                        with open(found_files, errors='ignore') as f:
                            f = f.readlines()
                        for line in f:
                            for phrase in search_pattern:
                                if phrase in line:
                                    important.append(line)
                                    filtered = ''.join(important)
                                    print ('File:', found_files)
                                    odo = re.findall(r':\d{6},',filtered)
                                    print ('Odometer:', odo)
                                    break