"""Tests for job_scorer.score_job.

We mock the Gemini API at the boundary (client.models.generate_content)
so tests run offline, fast, and free — no real API quota used.
"""
from job_scorer import score_job


def test_happy_path(mocker):
    """Valid JSON response from Gemini -> dict with int score and string reason."""
    mock_response = mocker.Mock()
    mock_response.text = '{"score": 8, "reason": "good match"}'
    mocker.patch(
        'job_scorer.client.models.generate_content',
        return_value=mock_response,
    )

    result = score_job({
        'title': 'Python Automation Engineer',
        'company': 'Acme',
        'tags': ['python', 'automation'],
    })

    assert result['score'] == 8
    assert result['reason'] == 'good match'


def test_score_cast_to_int(mocker):
    """If Gemini returns score as a string ("9"), it must be cast to int(9)."""
    mock_response = mocker.Mock()
    mock_response.text = '{"score": "9", "reason": "stringy score"}'
    mocker.patch(
        'job_scorer.client.models.generate_content',
        return_value=mock_response,
    )

    result = score_job({'title': 'X', 'company': 'Y', 'tags': []})

    assert result['score'] == 9
    assert isinstance(result['score'], int)


def test_api_exception_returns_failsafe(mocker):
    """If Gemini raises any exception, return {score: None, reason: 'scoring failed: ...'}."""
    mocker.patch(
        'job_scorer.client.models.generate_content',
        side_effect=Exception('network down'),
    )

    result = score_job({'title': 'X', 'company': 'Y', 'tags': ['python']})

    assert result['score'] is None
    assert result['reason'].startswith('scoring failed:')
    assert 'network down' in result['reason']


def test_invalid_json_returns_failsafe(mocker):
    """If Gemini returns malformed text, fail-safe path triggers with JSONDecodeError."""
    mock_response = mocker.Mock()
    mock_response.text = 'not json at all'
    mocker.patch(
        'job_scorer.client.models.generate_content',
        return_value=mock_response,
    )

    result = score_job({'title': 'X', 'company': 'Y', 'tags': ['python']})

    assert result['score'] is None
    assert 'JSONDecodeError' in result['reason']


def test_empty_tags_does_not_crash(mocker):
    """Job with empty tags list should still score (empty join -> empty string)."""
    mock_response = mocker.Mock()
    mock_response.text = '{"score": 5, "reason": "no tags provided"}'
    mocker.patch(
        'job_scorer.client.models.generate_content',
        return_value=mock_response,
    )

    result = score_job({'title': 'X', 'company': 'Y', 'tags': []})

    assert result['score'] == 5


def test_missing_fields_use_defaults(mocker):
    """Job dict missing title/company/tags should use job.get() defaults, not crash."""
    mock_response = mocker.Mock()
    mock_response.text = '{"score": 3, "reason": "incomplete data"}'
    mocker.patch(
        'job_scorer.client.models.generate_content',
        return_value=mock_response,
    )

    result = score_job({})  # totally empty dict

    assert result['score'] == 3
    assert result['reason'] == 'incomplete data'
