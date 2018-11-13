server=`cat $1 | grep server | awk '{print $1}' |sed 's/^server:\([^\s]*\)/\1/g'`
app=`cat $1 | grep server | awk '{print $2}' |sed 's/^app:\([^\s]*\)/\1/g'`

rate=`cat $1 | grep Success | awk '{print $3}'`
mean=`cat $1 | grep Laten | awk '{print $7}' | tr -d ','`
p50=`cat $1 | grep Laten | awk '{print $8}' | tr -d ','`
p95=`cat $1 | grep Laten | awk '{print $9}' | tr -d ','`
p99=`cat $1 | grep Laten | awk '{print $10}' | tr -d ','`
max=`cat $1 | grep Laten | awk '{print $11}' | tr -d ','`

echo $server,$app,$rate,$mean,$p50,$p95,$p99,$max
