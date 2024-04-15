#!/usr/bin/env python3
"""Test cases for the GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Mock the return value of get_json
        mock_get_json.return_value = {"name": org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        org_data = client.org

        # Assert that get_json was called once with the correct URL
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

        # Assert that the returned data is as expected
        self.assertEqual(org_data, {"name": org_name})

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the expected
        URL."""
        # Mock the org method to return a known payload
        mock_org_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:

            mock_org.return_value = mock_org_payload
            # Create an instance of GithubOrgClient
            client = GithubOrgClient('testorg')

            # Access the _public_repos_url property
            public_repos_url = client._public_repos_url

            # Assert that the returned URL is as expected
            self.assertEqual(public_repos_url,
                             "https://api.github.com/orgs/testorg/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the expected list of
        repos."""
        # Mock the return value of get_json
        mock_repos_url = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "GPL-3.0"}},
            {"name": "repo3", "license": {"key": "MIT"}}
        ]

        # Mock the _public_repos_url property
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('testorg')

            # Call the public_repos method
            repos = client.public_repos()

            # Assert that the returned list of repos is as expected
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            # Assert that get_json and _public_repos_url were called once
            mock_get_json.assert_called_once_with(mock_repos_url)
            mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
