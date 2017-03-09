#!/bin/bash
#Generate TMX file for STS Translation project
#Created by jandre@br.ibm.com
#Date 01, December 2016
#------------------------------------------
# Update file tmx_input_pairs_utf8.txt with input
# from & to words/phrases. That will be read
# to create the final tmx file
#------------------------------------------
usage() { echo "Usage: $0 -i <input file> -o <output file>" 1>&2; exit 1; }

#------------------------------------------
# When running this script, you need to specify 
# an input file name and a output file name
# Example: generate_tmx.bash -i tmx_input_file_pairs_utf8.txt -o tmx_final_file.tmx
#------------------------------------------
while getopts i:o: opts; do
   case ${opts} in
      i) input=${OPTARG} ;;
      o) output=${OPTARG} ;;
      *) usage ;;
   esac
done
#------------------------------------------
# If file already exists clean Output File
#------------------------------------------
if [ -e $output ]; then
    rm $output
fi

#------------------------------------------
# Create Header of tmx file
#------------------------------------------
echo '<?xml version="1.0" encoding="UTF-8"?>' >> $output
echo '<tmx version="1.4">' >> $output
echo '  <header creationtool="" creationtoolversion="'$(date +%c)'"' >> $output
echo '        segtype="sentence" o-tmf="" adminlang="EN"' >> $output
echo '        srclang="en" datatype="rtf" o-encoding="UTF-8" />' >> $output
echo '  <body>' >> $output

#------------------------------------------
# Read records from from input file
# and split between FROM and TO, already
# writing them in the given output file
#------------------------------------------
while read p; do
	FROM=$(echo $p | awk '{split($0,array,":")} END{print array[1]}')
	TO=$(echo $p | awk '{split($0,array,":")} END{print array[2]}')
	echo '    <tu>' >> $output
	echo '      <tuv xml:lang="en">' >> $output
	echo '        <seg>'$FROM'</seg>' >> $output
	echo '      </tuv>' >> $output
	echo '      <tuv xml:lang="es">' >> $output
	echo '        <seg>'$TO'</seg>' >> $output
	echo '      </tuv>' >> $output
	echo '    </tu>' >> $output
done < $input

#------------------------------------------
# Create Trailer of tmx file
#------------------------------------------
echo '  </body>' >> $output
echo '</tmx>' >> $output
