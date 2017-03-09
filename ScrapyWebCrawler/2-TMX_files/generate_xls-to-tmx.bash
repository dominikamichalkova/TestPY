#!/bin/bash
#Generate TMX file for STS Translation project
#Created by jandre@br.ibm.com
#Date 01, December 2016
#------------------------------------------
# Update file tmx_input_pairs_utf8.txt with input
# from & to words/phrases. That will be read
# to create the final tmx file
#------------------------------------------
print_help() {
    echo "This script is used for transforming excel files to csv files."
    echo "Usage: $0 [-h] -i <input file> -o <output file>"
    exit 0;
}

usage() { 
    echo "Usage: $0 -i <input file> -o <output file>" 1>&2; exit 1; 
}

#------------------------------------------
# When running this script, you need to specify 
# an input file name and a output file name
# Example: generate_tmx.bash -i tmx_input_file_pairs_utf8.txt -o tmx_final_file.tmx
#------------------------------------------
while getopts i:o:h: opts; do
   case ${opts} in
      i) input=${OPTARG} ;;
      o) output=${OPTARG} ;;
      h) print_help ;;
      *) usage ;;
   esac
done

#------------------------------------------
# Transforms Excel file to csv and replaces
# invalid XML characters
#------------------------------------------
xlsx2csv -d '|' $input | grep -vx ',' | sed -e 's/\&/\&amp;/g' | sed -e 's/</\&lt;/g' | sed -e 's/>/\&gt;/g' | sed -e "s/'/\&apos;/g" | sed -e 's/"/\&quot;/g' > input_csv.tmp

#------------------------------------------
# Setting encoding to utf-8 - maybe not necessary
#------------------------------------------
encoding=$(file -i input_csv.tmp | cut -f 2 -d '=')

if [ $encoding != 'utf-8' ]; then
    iconv -f $encoding -t UTF8 input_csv.tmp > input_csv.tmp    
fi

#------------------------------------------
# If file already exists clean Output File
#------------------------------------------
if [ -e $output ]; then
    rm $output
fi

#------------------------------------------
# Replacing | with :
#------------------------------------------
sed -i 's/|/:/g' input_csv.tmp

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
done < input_csv.tmp

rm -f input_csv.tmp

#------------------------------------------
# Create Trailer of tmx file
#------------------------------------------
echo '  </body>' >> $output
echo '</tmx>' >> $output
