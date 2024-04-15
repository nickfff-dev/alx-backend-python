#!/usr/bin/env python3
"""Test cases for the GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient, get_json
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license correctly identifies the
        presence of a license key."""
        # Call the has_license method
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the result is as expected
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (TEST_PAYLOAD[0][0],
         TEST_PAYLOAD[0][1],
         TEST_PAYLOAD[0][2],
         TEST_PAYLOAD[0][3]),
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient."""
    @classmethod
    def setUpClass(cls):
        """Set up class with the necessary patches."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(*args, **kwargs):
            url = args[0]
            if 'repos' in url:
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: cls.org_payload)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that the public_repos method returns the expected list of
        repos."""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient('google')

        # Call the public_repos method
        repos = client.public_repos()

        # Assert that the returned list of repos is as expected
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that the public_repos method returns the expected list of
        repos with a specific license."""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient('google')

        # Call the public_repos method
        repos = client.public_repos('apache-2.0')

        # Assert that the returned list of repos is as expected
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
