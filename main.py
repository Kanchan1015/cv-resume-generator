from utils import collect_user_data ,generate_docx

def main():
    user_data = collect_user_data()
    
    print("\nData collected successfully:")
    generate_docx(user_data)

if __name__ == "__main__":
    main()
