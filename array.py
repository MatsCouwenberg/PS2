data = """0901062
0937870
0889003
0833967
0938842
0931792
0840609
0937871
0938844
0894147
0931795
0945799
0930552
0947807
0882111
0937889
0898000
0901651
0949032
0844989
0938856
0898448
0950061
0931107"""

# Split the data into lines and add 'r' before each number
result_array = [f"r{line}" for line in data.strip().split('\n')]

# Print the resulting array
print(result_array)
