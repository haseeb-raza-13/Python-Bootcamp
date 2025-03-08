if {[package vsatisfies [package provide Tcl] 9.0-]} { 
package ifneeded sqlite3 3.44.2 [list load [file join $dir tcl9sqlite3442t.dll] [string totitle sqlite3]] 
} else { 
package ifneeded sqlite3 3.44.2 [list load [file join $dir sqlite3442t.dll] [string totitle sqlite3]] 
} 
