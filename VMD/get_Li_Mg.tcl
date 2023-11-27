set n [ molinfo top get numframes ] 
set Li_across 0
set bar 55
for { set i 0 } { $i < [ expr $n-1 ] } { incr i } {
    for { set j 0 } { $j <= 1706 } { incr j } {
        set Li_t1 [ atomselect top "index $j" frame $i ]
        set Li_t2 [ atomselect top "index $j" frame [expr $i+1 ] ]
        if { [ $Li_t1 get z ] <= $bar && [ $Li_t2 get z ] >= $bar } {
            incr Li_across
        }
        $Li_t1 delete
        $Li_t2 delete 
    } 
    puts "Frame $i"
}
puts "$Li_across"






