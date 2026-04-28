def test_multiple_matches_count_or_iterate(page: Page):
    page.goto(BASE_URL)
    feedback = page.locator('.invalid-feedback')
    expect(feedback).to_have_count(3)

    for message in feedback.all():
        expect(message).to_be_visible()