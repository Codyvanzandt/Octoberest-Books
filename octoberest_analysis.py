import gzip
import json
import datetime
from collections import defaultdict, Counter

def find_the_octoberest_books(reviews_file_path, books_file_path, output_file_path, min_necessary_reviews=100, n_top_octoberness=150):
    print("Loading Data...")
    reviews = list(load_reviews(file_path=reviews_file_path, n=None))

    print("Getting Reviews for Sufficiently Popular Books...")
    reviews_for_suf_pop_books = list(get_reviews_for_sufficiently_popular_books(reviews, min_necessay_reviews=min_necessary_reviews))
    
    print("Getting Reviews by Book-Month...")
    reviews_by_book_by_month = get_reviews_by_book_by_month(reviews_for_suf_pop_books)
    
    print("Getting Octoberness...")
    octoberness_by_book = get_octoberness_by_book(reviews_by_book_by_month,books_file_path)
    top_octoberness = octoberness_by_book.most_common(n_top_octoberness)

    print("Replacing Book IDs with Titles...")
    book_id_to_title = build_book_id_to_title_map(books_file_path, n=None)
    titled_top_octoberness = { book_id_to_title[id] : octoberness for id, octoberness in top_octoberness }

    print("Saving as JSON...")
    with open(output_file_path, "w") as output_file:
        json.dump(titled_top_octoberness, output_file, indent=1)
    print("Ding! All done! Enjoy the ~SpoOoOkiness!~")


def load_reviews(file_path="goodreads_reviews_fantasy_paranormal.json.gz",n = 500):
    with gzip.open(file_path) as review_file:
        for i, l in enumerate(review_file):
            review = json.loads(l)
            yield extract_review_fields(review)

            if (n is not None) and (i >= n):
                break
    
def get_reviews_for_sufficiently_popular_books(reviews, min_necessay_reviews=100):
    reviews_per_book = count_reviews_per_book(reviews)
    for review in reviews:
        book_id = review["book_id"]
        if reviews_per_book[book_id] >= min_necessay_reviews:
            yield review

def get_reviews_by_book_by_month(sufficiently_popular_reviews):
    reviews_by_book_by_month = NestedDefaultDict(2,default=list)
    for review in sufficiently_popular_reviews:
        book_id = review["book_id"]
        month = parse_date(review["date_added"]).strftime("%B")
        reviews_by_book_by_month[book_id][month].append(review)
    return reviews_by_book_by_month

def get_octoberness_by_book(reviews_by_book_by_month, book_data_file_path):
    octobernesses = dict()
    for book_id, by_month_reviews in reviews_by_book_by_month.items():
        octoberness = compute_octoberness(by_month_reviews)
        octobernesses[book_id] = octoberness
    return Counter(octobernesses)

def compute_octoberness(book_reviews_by_month):
    october_reviews = 0
    non_october_reviews = 0
    for month, reviews in book_reviews_by_month.items():
        for review in reviews:
            if is_october(review):
                october_reviews += 1
            else:
                non_october_reviews += 1
    return october_reviews / (non_october_reviews/11)


def build_book_id_to_title_map(book_data_path, n=None):
    book_map = dict()
    for book in load_book_data(book_data_path,n=n):
        book_map[book["book_id"]] = book["title"]
    return book_map

def load_book_data(file_path, n=500):
    with gzip.open(file_path) as books_file:
        for i, book in enumerate(books_file):
            book_json = json.loads(book)
            yield book_json
            
            if (n is not None) and (i >= n):
                break

def extract_review_fields(review):
    return {
        "book_id" : review["book_id"],
        "rating" : review["rating"],
        "date_added" : review["date_added"],
        "date_updated" : review["date_updated"],
        "started_at" : review["started_at"],
        "read_at" : review["read_at"],
        "n_votes" : review["n_votes"]
    }

def count_reviews_per_book(reviews):
    book_counts = defaultdict(int)
    for review in reviews:
        book_counts[review["book_id"]] += 1
    return book_counts


def parse_date(date):
    return datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")


def is_october(review):
    return parse_date(review["date_added"]).month == 10


class NestedDefaultDict(defaultdict):
    def __init__(self, depth, default=int, _root=True):
        self.root = _root
        self.depth = depth
        if depth > 1:
            cur_default = lambda: NestedDefaultDict(depth - 1,
                                                    default,
                                                    False)
        else:
            cur_default = default
        defaultdict.__init__(self, cur_default)

    def __repr__(self):
        if self.root:
            return "NestedDefaultDict(%d): {%s}" % (self.depth,
                                                    defaultdict.__repr__(self))
        else:
            return defaultdict.__repr__(self)

