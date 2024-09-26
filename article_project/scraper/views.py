import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer


class ScrapeAPIView(APIView):
    def get(self, request):
        query = request.GET.get("query", None)

        if not query:
            return Response({"error": "Query parameter is required"}, status=400)

        # Perform the scraping
        scraped_data = self.scrape_indian_kanoon(query)

        # Save the data to the database
        for data in scraped_data:
            Article.objects.create(title=data["title"], data=data["data"], link=data["link"])

        # Serialize the response
        serializer = ArticleSerializer(scraped_data, many=True)
        return Response(serializer.data)

    def scrape_indian_kanoon(self, query):
        url = f"https://www.indiankanoon.org/search/?formInput={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        results = []
        for i, item in enumerate(soup.find_all("div", class_="result")[:5]):
            title = item.get_text(strip=True)
            link = item.find("a")["href"]
            full_link = f"https://www.indiankanoon.org{link}"

            # Get the full text
            full_text_response = requests.get(full_link)
            full_soup = BeautifulSoup(full_text_response.content, "html.parser")
            content = full_soup.get_text(strip=True)

            # Trim content if it exceeds 10,000 characters
            content = content[:10000] if len(content) > 10000 else content

            results.append({"title": title, "data": content, "link": full_link})

        return results
