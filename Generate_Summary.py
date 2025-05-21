def generate_summary_report(all_articles, output_csv="summary_report.csv", historical_year=2021):
    from collections import defaultdict
    from datetime import datetime
    import csv
    from dateutil.parser import parse as parse_date

    summary = defaultdict(lambda: {
        "sources": set(),
        "total_count": 0,
        "historical_count": 0,
        "earliest": None
    })

    cutoff_date = datetime(historical_year, 1, 1)

    for article in all_articles:
        country = article.get("country", "Unknown")
        source = article.get("source", "Unknown")
        published = article.get("published", "")

        summary[country]["sources"].add(source)
        summary[country]["total_count"] += 1

        try:
            pub_date = parse_date(published)
            if summary[country]["earliest"] is None or pub_date < summary[country]["earliest"]:
                summary[country]["earliest"] = pub_date
            if pub_date < cutoff_date:
                summary[country]["historical_count"] += 1
        except Exception:
            pass

    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "News Agency", "Total Articles Downloaded", "Total Historical Data"])
        for country, data in summary.items():
            sources = ", ".join(sorted(data["sources"]))
            total = data["total_count"]
            historical = data["historical_count"]
            writer.writerow([country, sources, total, historical])

    print(f"\nSummary CSV saved to '{output_csv}'")
