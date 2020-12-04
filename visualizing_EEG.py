import mne

mne.set_log_level("WARNING")
raw = mne.io.read_raw_edf("S001R04.edf", preload=True)
raw.rename_channels(lambda s: s.strip("."))
raw.set_montage("standard_1020", match_case=False)
raw.set_eeg_reference("average")

raw.plot()