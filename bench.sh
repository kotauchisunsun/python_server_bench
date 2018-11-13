for server in `echo wsgiref tornado twisted gunicorn`
do
    for app in `echo flask falcon`
    do
        {
            echo "server:$server app:$app"
            python3 bench_server.py $server $app &
            pid=$!
            sleep 10

            #ab -n 100000 -c 100 http://localhost:3000/ 
            #ab -n 100 -c 1 http://localhost:3000/ 
            echo "GET http://localhost:3000" | ./vegeta attack -duration=180s -rate 550 | ./vegeta report

            children=`ps --ppid=$pid | cut -d' ' -f1`
            kill -9 $pid $children
            echo
            sleep 60
            wait
        } | tee "$server"_"$app".log
    done 
done

