This is a very simple and dirty python script to automate the worst part of [Supreme Audyssey Calibration](https://www.youtube.com/watch?v=g26gbFdAIxE) by OCA

It requires that your measurements be saved such that "-(channel)" appears in the name, for example, I name my channels -

pos1-TFL

pos2-C

pos3-FL

etc.

With your measurements named something like that, and your MLP measurements on the top of the pile as is always required, you can then enable the API in REW (latest betas) and run the script with a local python interpreter.

Execution is extremely straight forward -

`python .\crosscorralign.py [channel]`

where [channel] is a channel as you have named it in your measurements, i.e. "TRR" or "FL"

If you've got the channels selected and the impulse overlay up, you should see them start attempting to align.

It may continue to run for a little bit after they are fully aligned, as recording and comparing the measurements is a surprisingly slow process, so it runs alignments in batches of 10 after the initial run before doing a compare.  This seems to mean it can go up to two full cycles after achieving alignment before becoming aware everything is aligned.

If it achieves perfect alignment, it will then take a vector average for you, advise you to visually inspect the alignment to ensure there are no errors, and then rename your vector alignment before proceeding further.

If it runs _approximately_ 500 times without achieving alignment, it will quit just for sake of not running forever.  Feel free to restart it at that point, but I have seen measurements that simply will not align, so if you're having to restart it more than a couple times, you may just have to get them as close as possible, take a vector average yourself, and move on - or redo your measurements.

I hope this saves you a bit of carpal tunnel stress, as that clicking "Cross corr align" hundreds upon hundreds of times was certainly starting to take a toll on me both mentally and physically!
