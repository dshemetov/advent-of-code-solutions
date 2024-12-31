function solve(input::Question{2024,9,'a'})
    if input.s == ""
        s = test_string_2024_9
    else
        s = input.s
    end
    s = strip(s, '\n')
    nums = [parse(Int, c) for c in s]

    mem = Dict{Int,Vector{Tuple{Int,Int}}}()
    i = 0
    for (j, n) in enumerate(nums)
        if j % 2 == 1
            mem[(j-1)/2] = (i, i + n - 1)
        else
            # -1 is the index of free memory
            mem[-1] = push!(get(mem, -1, Vector{Tuple{Int,Int}}()), (i, i + n - 1))
        end
        i += n
    end
    mem[-1] = push!(mem[-1], (i + 1, i + 1))

    max_free_index = mem[-1][end][2]
    max_unmoved_id = maximum([k for (k, v) in mem if k != -1])
    max_used_index = mem[max_unmoved_id][end][2]
    while max_free_index < max_used_index
        n = nums[j]
        ixs = mem[j]

        mem[-1][1]
        mem[-1] = push!(mem[-1], (max_free_index + 1, max_free_index + 1))
        max_free_index += 1
    end
    for (j, n) in enumerate(reverse(nums))
        # The assumption is that mem is sorted by start.
        if j % 2 == 1
            v[i:i+n-1] .= (j - 1) / 2
        else
            v[i:i+n-1] .= -1
        end
        i = find_next_open(i)
    end
    return 0
end


function solve(input::Question{2024,9,'b'})
    if input.s == ""
        s = test_string_2024_9
    else
        s = input.s
    end
    return 0
end

test_string_2024_9 = """
2333133121414131402
"""
