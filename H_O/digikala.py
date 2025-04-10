import requests

class Digikala:
    def __init__(self):
        self.api_url = "https://abas-server.ir/diji.php"
    
    def search(self, query):
        """
       
        پارامترها:
            query: عبارت جستجو
        """
        try:
            # انجام جستجو
            response = requests.get(self.api_url, params={"q": query})
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    result = data.get("result")
                    
                    # نمایش نتایج
                    if result:
                       
                        print("="*40)
                        print(f"📦نام محصول: {result.get('name')}")
                        print(f"💶قیمت: {result.get('price'):,} تومان")
                        print(f"📎لینک: {result.get('url')}")
                        print("="*40)
                        return result
                    
            print("نتیجه‌ای یافت نشد")
            return None
            
        except Exception as e:
            print(f"خطا در جستجو: {str(e)}")
            return None
