from ddgs import DDGS

from pathlib import Path

from datetime import datetime

from brain import ask_ai


BASE_FOLDER = Path(__file__).parent

REPORT_FOLDER = BASE_FOLDER / "reports"

REPORT_FOLDER.mkdir(exist_ok=True)


def research(topic):

    print("\nJARVIS: Starting research...")

    search = DDGS()

    results = list(
        search.text(
            topic,
            max_results=8
        )
    )

    if not results:

        return "No research results found."

    research_data = ""

    sources = []

    for number, result in enumerate(results, 1):

        title = result.get("title", "")

        url = result.get("href", "")

        description = result.get("body", "")

        research_data += f"""

        SOURCE {number}

        TITLE:
        {title}

        URL:
        {url}

        INFORMATION:
        {description}

        """

        sources.append(url)

    prompt = f"""

    Research the following topic:

    {topic}

    Use the following search results:

    {research_data}

    Create a detailed professional research report.

    Include:

    1. Introduction
    2. Main findings
    3. Important facts
    4. Advantages and disadvantages
    5. Conclusion

    Only use information supported by the
    supplied search results.

    Do not invent statistics or facts.

    Explain when information is uncertain.

    Include the source URLs.
    """

    report = ask_ai(prompt)

    filename = datetime.now().strftime(
        "research_%Y%m%d_%H%M%S.txt"
    )

    file_path = REPORT_FOLDER / filename

    report += "\n\nSOURCES:\n"

    for source in sources:

        report += source + "\n"

    file_path.write_text(
        report,
        encoding="utf-8"
    )

    return f"""

    Research completed!

    Your report has been saved.

    Location:

    {file_path}

    """