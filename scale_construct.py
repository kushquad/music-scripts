import sys

# Note definitions
notes_sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Scale definitions
major_scale = [2, 2, 1, 2, 2, 2, 1]
natural_minor_scale = [2, 1, 2, 2, 1, 2, 2]
harmonic_minor_scale = [2, 1, 2, 2, 1, 3, 1]
melodic_minor_scale = [2, 1, 2, 2, 2, 2, 1]
blues_scale = [3, 2, 1, 1, 3, 2]
major_pentatonic_scale = [2, 2, 3, 2, 3]
minor_pentatonic_scale = [3, 2, 2, 3, 2]

# From my experimentation
orientalish_scale = [2, 3, 2, 2, 1, 2]

scale_mapping = {'major': major_scale,
                 'minor': natural_minor_scale,
                 'hminor': harmonic_minor_scale,
                 'mminor': melodic_minor_scale,
                 'blues': blues_scale,
                 'pentatonic': major_pentatonic_scale,
                 'minorpentatonic': minor_pentatonic_scale,
                 'oriental': orientalish_scale
                }
                
def apply_scale(scale, notes, key):
    l = len(notes)
    scale_notes = [key]
    index = notes.index(key)
    for i in xrange(len(scale)):
        new_index = (index + scale[i])%l
        scale_notes.append(notes[new_index])
        index = new_index
    return scale_notes
    
key = sys.argv[1]
if not key in notes_sharps:
    print 'Note name not recognized'
    sys.exit(0)
scale = sys.argv[2]
if not (scale in scale_mapping.keys()):
    print 'Scale name not recognized'
    sys.exit(0)
    
returned_noteset = apply_scale(scale_mapping[scale], notes_sharps, key)
print returned_noteset
