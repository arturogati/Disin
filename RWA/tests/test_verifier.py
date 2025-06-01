import pytest
from verification.verifier import BusinessVerifier

@pytest.fixture
def verifier():
    return BusinessVerifier()

def test_verification(verifier):
    result = verifier.verify("test_business")
    assert result["status"].value in ["APPROVED", "REJECTED"]