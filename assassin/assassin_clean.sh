l=""
for f in *.txt; do
    lines=$(wc -l "$f" | awk '{print $1}');
    # echo $lines $f
    mv "$f" "0$lines $f" 
done
