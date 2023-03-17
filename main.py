# python3

def parallel_processing(n, m, data):
output = []
    time = [0] * n  # initialize time list with zeros
    for thread in data:
        # find the index of the thread with minimum time
        thread_num = time.index(min(time))
        # append the thread number and its start time to output
        output.append((thread_num, time[thread_num]))
        # process the thread by updating its start time
        time[thread_num] += thread
    return output

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_num, start_time in result:
        print(thread_num, start_time)

if __name__ == "__main__":
    main()
