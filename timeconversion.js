/**
 Given a time in 12-hour am/pm format,
 convert it to military 24 hour time

 midnight is 00:00:00 in military
 noon is 12:00:00 
  
INPUT= S, a string representing time in 12 hour format
hh:mm:ssAm or hh:mm:ssPm
00<=mm,ss<=59

OUTPUT = string in 24 hour format

12:00:00AM == 00:00:00 
01:00:00AM == 01:00:00 same 
02:00:00AM == 02:00:00
03:00:00AM == 03:00:00
04:00:00AM == 04:00:00
05:00:00AM == 05:00:00
06:00:00AM == 06:00:00
07:00:00AM == 07:00:00
08:00:00AM == 08:00:00


12:00:00PM == 12:00:00 (same)
01:00:00PM == 13:00:00
          == 14:00:00
         3     15:00:00
         4     16:00:00
          5    17:00:00
          6    18:00:00
          7    19:00:00
         8     20:00:00
          9    21:00:00
          10    22:00:00
           11   23:00:00

 */

function timeC(s) {
    //
    let newsum = 0
    let res = ""

    //If char at index 8 == A 
    //is AM.  
    //convert s.charAt(0) & s.charAt(1) to INT 
    //add 12 to  S[0] & S[1]
    //convert everything back to new string
    //return new string
    let combo = parseInt(s.charAt(0) + s.charAt(1))

    if (s.charAt(8) == 'P' && combo < 12) {
        newsum = 12 + combo
        let cstring = newsum.toString()
        let remstr = s.slice(2, 8)
        res = cstring + remstr
    } else if (s.charAt(8) == 'A' && combo == 12) {
        res = "00" + s.slice(2, 8)

    } else {
        res = s.slice(0, 8)
    }
    return res

}

timeC("07:00:59PM")