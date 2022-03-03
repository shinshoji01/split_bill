import pandas as pd
import numpy as np
import argparse

def main():
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=str, help="path of bill")
    args = parser.parse_args()
    print("")
    print(f"filename: {args.path}")
    print("")

    print("all data:")
    print("------------------------------------------------------")
    data = pd.read_excel(args.path, sheet_name=1, engine="openpyxl")
    data = data[np.array(1-data.iloc[:,0].isna(),dtype=np.bool)]
    member_list = pd.read_excel(args.path, index_col=0, header=None, engine="openpyxl")
    member_list = member_list.loc[:, np.array(1-member_list.iloc[0, :].isna(), dtype=np.bool)]
    member_list[member_list.isnull()]=0
    print(data)
    
    split_type = list(set(data["分割タイプ"].values))
    print(data)
    split_type.sort()
    
    all_members = member_list.values[0]
    print("------------------------------------------------------")
    print("")
    print("all members: ", all_members)
    print("")
    
    members = {}
    for i in range(len(split_type)):
        members[split_type[i]] = member_list.values[2+i][member_list.values[2+i]!=0]
    leader = member_list.values[1][0]
    
    print("------------------------------------------------------")
    print("")
    for type in split_type:
        print(f"type {type}: {', '.join(members[type])}")
    print("")

    each_bill = {}
    for type in split_type:
        each_bill[type] = np.sum(data[data["分割タイプ"]==type]["金額"].values)/len(members[type])

    print("------------------------------------------------------")
    print("")

    print("Results:")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    for member in all_members:
        if member != leader:
            payment = 0
            for type in split_type:
                if member in members[type]:
                    payment += each_bill[type]
            payment -= np.sum(data[data["払った人"]==member]["金額"].values)
            arrow = "->" if payment>0 else "<-"
            print(f"{member} {arrow} {leader}: {np.abs(payment)}")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    
    
    
    
if __name__ == '__main__':
    main()
