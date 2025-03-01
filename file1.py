import streamlit as st

def remove_match_char(list1, list2):
    """Remove matching characters from two lists and return the updated list and a flag."""
    i, j = 0, 0
    while i < len(list1):
        j = 0
        while j < len(list2):
            if list1[i] == list2[j]:
                list1.pop(i)
                list2.pop(j)
                return list1 + ["*"] + list2, True  # Return modified lists
            j += 1
        i += 1
    return list1 + ["*"] + list2, False  # Return lists if no matches

def flames_game(name1, name2):
    """Main function to execute the FLAMES logic."""
    p1 = name1.lower().replace(" ", "")
    p2 = name2.lower().replace(" ", "")
    
    p1_list = list(p1)
    p2_list = list(p2)

    # Remove common characters
    proceed = True
    while proceed:
        updated_list, proceed = remove_match_char(p1_list, p2_list)
        star_index = updated_list.index("*")
        p1_list = updated_list[:star_index]
        p2_list = updated_list[star_index + 1:]

    # Count remaining characters
    count = len(p1_list) + len(p2_list)

    # FLAMES categories
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

    # FLAMES elimination process
    while len(result) > 1:
        split_index = (count % len(result)) - 1
        if split_index >= 0:
            result = result[split_index + 1:] + result[:split_index]
        else:
            result.pop()

    return result[0]

# Streamlit UI
st.title("🔥 FLAMES Relationship Calculator 🔥")

st.write("Enter two names and find out your relationship status!")

# User Input
name1 = st.text_input("Enter Player 1 Name:")
name2 = st.text_input("Enter Player 2 Name:")

# Button to Calculate Relationship
if st.button("Calculate Relationship"):
    if name1 and name2:
        relationship = flames_game(name1, name2)
        st.success(f"💖 Relationship Status: {relationship} 💖")
    else:
        st.error("⚠️ Please enter both names!")
