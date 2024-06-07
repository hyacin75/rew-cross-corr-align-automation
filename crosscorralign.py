import requests
import sys

if len(sys.argv) < 2:
  print("Need an argument")
  exit()

# get the list of relevant measurements (based on them being named posX-YY MON D - where YY is a unique channel identifier)

measurementsurl = "http://localhost:4735/measurements"

measurementsr = requests.get(measurementsurl, headers={"accept": "application/json"})

measurementdata = measurementsr.json()

measurementlist = []

for key in measurementdata:
  if "-" + sys.argv[1] in measurementdata[key]["title"]:
    measurementlist.append(key)


procmeasurl = "http://localhost:4735/measurements/process-measurements"
data = {
  "processName": "Cross corr align",
  "measurementIndices": measurementlist,
  "parameters": {},
  "resultUrl": ""
}

runloop = True
previous = {}
current = {}
firstrun = True
count = 0

while runloop:
  # grabbing the measurements to compare is a shockingly slow process so rather
  # than compare every iteration, after the first, we'll run 10 in one go and
  # then compare
  if firstrun:
    procmeasr = requests.post(procmeasurl, json=data)
  else:
    for i in range(10):
      procmeasr = requests.post(procmeasurl, json=data)

  previous = current.copy()

  for meas in measurementlist:
    singlemeasurl = "http://localhost:4735/measurements/" + str(meas)
    singlemeasr = requests.get(singlemeasurl, headers={"accept": "application/json"})
    current[meas] = singlemeasr.json()

  if not firstrun:
    alldone = True
    for meas in measurementlist:
      if previous[meas] != current[meas]:
        alldone = False
    if alldone:
      runloop = False
    if count >= 50:
      print("~500 executions and still no alignment, quitting")
      exit()

  count += 1
  firstrun = False

data = {
  "processName": "Vector average",
  "measurementIndices": measurementlist,
  "parameters": {},
  "resultUrl": ""
}
vectoravgr = requests.post(procmeasurl, json=data)

print("Cross correlation alignment complete, please visually inspect the results before deleting.")
print("A vector average has been created as well, please rename it before proceeding.")
