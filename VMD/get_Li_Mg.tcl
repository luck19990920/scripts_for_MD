# A script to calculate  number of particles passing through the pore in molecular simulation
# Variable bar is boundary z-coordinate of membrane. Please fix its value according to the actual situation 
# Variable num is the number of particles
# In this script, the particle number to be counted starts from 0. Please replace 0 in Line 9 to actual value according to the actual situation  
set n [ molinfo top get numframes ] 
set Li_across 0
set bar 55
set num 8
for { set i 0 } { $i < [ expr $n-1 ] } { incr i } {
    for { set j 0 } { $j <= $num } { incr j } {
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






