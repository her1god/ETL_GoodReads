from etl.extract import extract_book_details, extract_book_reviews, extract_books
from etl.transform import transform_book_details, transform_book_reviews, transform_books
from etl.load import load_data

def main():
    # Ekstraksi data
    book_details_df = extract_book_details()
    book_reviews_df = extract_book_reviews()
    books_df = extract_books()

    # Transformasi data
    transformed_book_details_df = transform_book_details(book_details_df.copy())
    transformed_book_reviews_df = transform_book_reviews(book_reviews_df.copy())
    transformed_books_df = transform_books(books_df)

    # Menggabungkan DataFrame berdasarkan kolom 'book_id'
    merged_df = transformed_books_df.merge(transformed_book_details_df, on='book_id', how='inner')
    merged_df = merged_df.merge(transformed_book_reviews_df, on='book_id', how='inner')

    # Mengonversi tipe data kembali ke integer setelah penggabungan
    columns_to_int = ['book_id', 'num_pages', 'likes_on_review', 'reviewer_total_reviews', 'reviewer_followers', 'review_rating', 'reviewer_id']
    for col in columns_to_int:
        if col in merged_df.columns:
            merged_df[col] = merged_df[col].fillna(0).astype(int)

    # Menghapus kolom 'Unnamed: 0' jika ada
    if 'Unnamed: 0' in merged_df.columns:
        merged_df = merged_df.drop(columns=['Unnamed: 0'])

    # Buat DataFrame clean_merged_books, clean_books_data, dan clean_books_reviews
    clean_merged_books = merged_df
    clean_books_data = merged_df[['book_id', 'title', 'total_books', 'total_votes', 'cover_image_uri', 'book_title', 'book_details', 'format', 'publication_info', 'num_pages', 'genres', 'num_ratings', 'num_reviews', 'average_rating', 'rating_distribution']].drop_duplicates().reset_index(drop=True)
    clean_books_reviews = merged_df[['book_id', 'reviewer_id', 'reviewer_name', 'likes_on_review', 'review_content', 'reviewer_followers', 'reviewer_total_reviews', 'review_date', 'review_rating']]

    # Pemuatan data
    load_data(clean_merged_books, 'data_clean/clean_merged_books.csv', "clean_merged_books")
    load_data(clean_books_data, 'data_clean/clean_books_data.csv', "clean_books_data")
    load_data(clean_books_reviews, 'data_clean/clean_books_reviews.csv', "clean_books_reviews")

if __name__ == "__main__":
    main()