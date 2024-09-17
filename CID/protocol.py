# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import bittensor as bt
from typing import List
import datetime as datetime
import pydantic


class ProfileSynapse(bt.Synapse):
    """
    The ProfileSynapse subclass of the Synapse class encapsulates the functionalities related to Identification Scenarios.

    It specifies seven fields - `id`, `label`, `type`, `options`, `value`, `image`, `answer` - that define the state of the ProfileSynapse object.
    All of the fields except `answer` are read-only fields defined during object initialization, and `answer` is a mutable
    field that can be updated as the scenario progresses.

    The Config inner class specifies that assignment validation should occur on this class (validate_assignment = True),
    meaning value assignments to the instance fields are checked against their defined types for correctness.

    Attributes:
        id (str): A unique identifier for the task. This field is both mandatory and immutable.
        type (str): A string that specifies the type of the task. This field is both mandatory and immutable and can take values "Generated" and "User" only.
        public_repos (int): A int that captures the public repos of the user.
        github_created_at (datetime): A datetime that captures the date of account creation.
        total_commits (int): A int that captures the total commits of the user.
        eth_balance (float): A int that captures the eth balance of the user.
        tao_balance (float): A int that captures the tao balance of the user.
        eth_transactions (int): A int that captures the number of Ethereum transactions made by the user.
        tao_transactions (int): A int that captures the number of TAO transactions made by the user.
        x_followers (int): A int that captures the number of followers on X (formerly Twitter).
        insta_followers (int): A int that captures the number of followers on Instagram.
        tiktok_followers (int): A int that captures the number of followers on TikTok.
        fb_followers (int): A int that captures the number of followers on Facebook.
        reddit_post_karma (int): A int that captures the Reddit post karma of the user.
        reddit_comment_karma (int): A int that captures the Reddit comment karma of the user.
        x_created_at (int): A int that captures the X account creation timestamp.
        reddit_created_at (int): A int that captures the Reddit account creation timestamp.
        insta_created_at (int): A int that captures the Instagram account creation timestamp.
        linkedin_created_at (int): A int that captures the LinkedIn account creation timestamp.
        is_linkedin_email_verified (bool): A bool that returns true if the LinkedIn email is verified.
        is_reddit_email_verified (bool): A bool that returns true if the Reddit email is verified.
        is_x_email_verified (bool): A bool that returns true if the X email is verified.
        is_insta_email_verified (bool): A bool that returns true if the Instagram email is verified.
        is_tiktok_email_verified (bool): A bool that returns true if the TikTok email is verified.
        score (float): A string that captures the score to the profile. This field is mutable.


    Methods:
        deserialize() -> "ProfileSynapse": Returns the instance of the current object.


    The `ProfileSynapse` class also overrides the `deserialize` method, returning the
    instance itself when this method is invoked. Additionally, it provides a `Config`
    inner class that enforces the validation of assignments (`validate_assignment = True`).
    """
    id: str
    type: str
    public_repos: int
    github_created_at: int
    total_commits: int
    eth_balance: float
    tao_balance: float
    eth_transactions: int
    tao_transactions: int
    x_followers: int
    insta_followers: int
    tiktok_followers: int
    fb_followers: int
    reddit_post_karma: int
    reddit_comment_karma: int
    x_created_at: int
    reddit_created_at: int
    insta_created_at: int
    linkedin_created_at: int
    is_linkedin_email_verified: bool
    is_reddit_email_verified: bool
    is_x_email_verified: bool
    is_insta_email_verified: bool
    is_tiktok_email_verified: bool
    score: float
    class Config:
        """
        Pydantic model configuration class for ProfileSynapse. This class sets validation of attribute assignment as True.
        validate_assignment set to True means the pydantic model will validate attribute assignments on the class.
        """

        validate_assignment = True
        arbitrary_types_allowed=True

    def deserialize(self) -> "ProfileSynapse":
        """
        Returns the instance of the current ProfileSynapse object.

        This method is intended to be potentially overridden by subclasses for custom deserialization logic.
        In the context of the ProfileSynapse class, it simply returns the instance itself. However, for subclasses
        inheriting from this class, it might give a custom implementation for deserialization if need be.

        Returns:
            ProfileSynapse: The current instance of the ProfileSynapse class.
        """
        return self

    id: str = pydantic.Field(
        ...,
        title="ID",
        description="A unique identifier for the task.",
        allow_mutation=False,
    )

    type: str = pydantic.Field(
        ...,
        title="Type",
        description="A string that specifies the type of the task.",
        allow_mutation=False,
    )

    public_repos: int = pydantic.Field(
        ...,
        title="public_repos",
        description="Number of public repositories of the user.",
        allow_mutation=False,
    )

    github_created_at: datetime = pydantic.Field(
        ...,
        title="github_created_at",
        description="GitHub account creation timestamp.",
        allow_mutation=False,
        arbitrary_types_allowed=True
    )

    total_commits: int = pydantic.Field(
        ...,
        title="total_commits",
        description="Total number of commits made by the user.",
        allow_mutation=False,
    )

    eth_balance: float = pydantic.Field(
        ...,
        title="eth_balance",
        description="Ethereum balance of the user.",
        allow_mutation=False,
    )

    tao_balance: float = pydantic.Field(
        ...,
        title="tao_balance",
        description="TAO balance of the user.",
        allow_mutation=False,
    )

    eth_transactions: int = pydantic.Field(
        ...,
        title="eth_transactions",
        description="Number of Ethereum transactions made by the user.",
        allow_mutation=False,
    )

    tao_transactions: int = pydantic.Field(
        ...,
        title="tao_transactions",
        description="Number of TAO transactions made by the user.",
        allow_mutation=False,
    )

    x_followers: int = pydantic.Field(
        0,
        title="x_followers",
        description="Number of followers on X (formerly Twitter).",
        allow_mutation=False,
    )

    insta_followers: int = pydantic.Field(
        0,
        title="insta_followers",
        description="Number of followers on Instagram.",
        allow_mutation=False,
    )

    tiktok_followers: int = pydantic.Field(
        0,
        title="tiktok_followers",
        description="Number of followers on TikTok.",
        allow_mutation=False,
    )

    fb_followers: int = pydantic.Field(
        0,
        title="fb_followers",
        description="Number of followers on Facebook.",
        allow_mutation=False,
    )

    reddit_post_karma: int = pydantic.Field(
        0,
        title="reddit_post_karma",
        description="Reddit post karma of the user.",
        allow_mutation=False,
    )

    reddit_comment_karma: int = pydantic.Field(
        0,
        title="reddit_comment_karma",
        description="Reddit comment karma of the user.",
        allow_mutation=False,
    )

    x_created_at: int = pydantic.Field(
        0,
        title="x_created_at",
        description="X account creation timestamp.",
        allow_mutation=False,
    )

    reddit_created_at: int = pydantic.Field(
        0,
        title="reddit_created_at",
        description="Reddit account creation timestamp.",
        allow_mutation=False,
    )

    insta_created_at: int = pydantic.Field(
        0,
        title="insta_created_at",
        description="Instagram account creation timestamp.",
        allow_mutation=False,
    )

    linkedin_created_at: int = pydantic.Field(
        0,
        title="linkedin_created_at",
        description="LinkedIn account creation timestamp.",
        allow_mutation=False,
    )

    is_linkedin_email_verified: bool = pydantic.Field(
        False,
        title="is_linkedin_email_verified",
        description="Whether the LinkedIn email is verified.",
        allow_mutation=False,
    )

    is_reddit_email_verified: bool = pydantic.Field(
        False,
        title="is_reddit_email_verified",
        description="Whether the Reddit email is verified.",
        allow_mutation=False,
    )

    is_x_email_verified: bool = pydantic.Field(
        False,
        title="is_x_email_verified",
        description="Whether the X email is verified.",
        allow_mutation=False,
    )

    is_insta_email_verified: bool = pydantic.Field(
        False,
        title="is_insta_email_verified",
        description="Whether the Instagram email is verified.",
        allow_mutation=False,
    )

    is_tiktok_email_verified: bool = pydantic.Field(
        False,
        title="is_tiktok_email_verified",
        description="Whether the TikTok email is verified.",
        allow_mutation=False,
    )

    score: float = pydantic.Field(
        "",
        title="score",
        description="A string that captures the score to the profile.",
        allow_mutation=True,
    )

    required_hash_fields: List[str] = pydantic.Field(
        ["id", "type", "public_repos", "github_created_at", "total_commits", "eth_balance", "tao_balance", "eth_transactions", "tao_transactions", "is_linkedin_email_verified",
         "x_followers", "insta_followers", "tiktok_followers", "fb_followers", "reddit_post_karma", "reddit_comment_karma",
         "x_created_at", "reddit_created_at", "insta_created_at", "linkedin_created_at",
         "is_reddit_email_verified", "is_x_email_verified", "is_insta_email_verified", "is_tiktok_email_verified"],
        title="Required Hash Fields",
        description="A list of fields that are required for the hash.",
        allow_mutation=False,
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the ProfileSynapse object.

        Returns:
            str: A string representation of the ProfileSynapse object.
        """
        return f"ProfileSynapse(id={self.id}, public_repos={self.public_repos}, github_created_at={self.github_created_at}, total_commits={self.total_commits}, eth_balance={self.eth_balance}, tao_balance={self.tao_balance}, eth_transactions={self.eth_transactions}, tao_transactions={self.tao_transactions}, score={self.score})"

    def to_dict(self):
        return {
            "id": self.id,
            "public_repos": self.public_repos,
            "github_created_at": self.github_created_at,
            "total_commits": self.total_commits,
            "eth_balance": self.eth_balance,
            "tao_balance": self.tao_balance,
            "eth_transactions": self.eth_transactions,
            "tao_transactions": self.tao_transactions,
            "x_followers": self.x_followers,
            "insta_followers": self.insta_followers,
            "tiktok_followers": self.tiktok_followers,
            "fb_followers": self.fb_followers,
            "reddit_post_karma": self.reddit_post_karma,
            "reddit_comment_karma": self.reddit_comment_karma,
            "x_created_at": self.x_created_at,
            "reddit_created_at": self.reddit_created_at,
            "insta_created_at": self.insta_created_at,
            "linkedin_created_at": self.linkedin_created_at,
            "is_linkedin_email_verified": self.is_linkedin_email_verified,
            "is_reddit_email_verified": self.is_reddit_email_verified,
            "is_x_email_verified": self.is_x_email_verified,
            "is_insta_email_verified": self.is_insta_email_verified,
            "is_tiktok_email_verified": self.is_tiktok_email_verified,
            "score": self.score,
        }



