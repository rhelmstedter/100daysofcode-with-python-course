import api
import webbrowser

def get_user_selection(results):
    choices = [f"[{r.number}] Episode # {r.id}: {r.title}" for r in results[:10]]
    choices_str = "\n".join(choices)
    selection = int(input(f"Your search term was mentioned in the following episodes: \n\n{choices_str}\n\nEnter the corresponding number to visit that page: "))
    return selection

def main():
    search_term = input("What do you want to search for? ").replace(' ', "-")
    results = api.search_site(search_term)

    print(f"There are {len(results)} results for {search_term}.\n")
    selection = get_user_selection(results)
    url = "https://talkpython.fm" + results[selection-1].url
    webbrowser.open(url, new=2)



if __name__ == "__main__":
    main()
