from flask import Flask, jsonify, request

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].lower() < right_half[j].lower():
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def binary_search(arr, title):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = arr[mid]

        if mid_title.lower() == title.lower():
            return mid_title  
        elif mid_title.lower() < title.lower():
            low = mid + 1
        else:
            high = mid - 1

    return None

merge_sort(video_titles)


@app.route('/search_title', methods=['GET'])
def search_title():
    title = request.args.get('title')
    print(title)
    
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400

    found_title = binary_search(video_titles, title)

    if found_title:
        return jsonify("Success"), 200
    else:
        print("Video not found")
        return jsonify("Video not found"), 404

if __name__ == '__main__':
    
    app.run(debug=True)


