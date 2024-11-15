x=int(input())
flat_dis=100
per_dis=0.1*x
max_dis=max(flat_dis,per_dis)
final_amount=x-max_dis
print(int(final_amount))
