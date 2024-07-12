# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
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
    The ProfileSynapse subclass of the Synapse class encapsulates the functionalities related to HIP Task Scenerios.

    It specifies seven fields - `id`, `label`, `type`, `options`, `value`, `image`, `answer` - that define the state of the ProfileSynapse object.
    All of the fields except `answer` are read-only fields defined during object initialization, and `answer` is a mutable
    field that can be updated as the scenario progresses.

    The Config inner class specifies that assignment validation should occur on this class (validate_assignment = True),
    meaning value assignments to the instance fields are checked against their defined types for correctness.

    Attributes:
        id (str): A unique identifier for the task. This field is both mandatory and immutable.
        type (str): A string that specifies the type of the task. This field is both mandatory and immutable and can take values "Generated" and "User" only.
        public_repos (int): A int that captures the public repos of the user.
        created_at (datetime): A datetime that captures the date of account creation.
        total_commits (int): A int that captures the total commits of the user.
        eth_balance (float): A int that captures the eth balance of the user.
        tao_balance (float): A int that captures the tao balance of the user.
        tao_staked (int): A int that captures the tao staked of the user.
        no_of_transactions (int): A int that captures the no of transactions of the user.
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
    created_at: int
    total_commits: int
    eth_balance: float
    eth_nft_balance: int
    tao_balance: float
    tao_staked: float
    no_of_transactions: int
    is_linkedin_email_verified: bool
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
        description="A int that captures the public repos of the user.",
        allow_mutation=False,
    )

    created_at: datetime = pydantic.Field(
        ...,
        title="created_at",
        description="A datetime that captures the date of account creation.",
        allow_mutation=False,
        arbitrary_types_allowed=True
    )

    total_commits: int = pydantic.Field(
        ...,
        title="total_commits",
        description="A int that captures the total commits of the user.",
        allow_mutation=False,
    )

    eth_balance: float = pydantic.Field(
        ...,
        title="eth_balance",
        description="A int that captures the eth balance of the user.",
        allow_mutation=False,
    )

    eth_nft_balance: int = pydantic.Field(
        ...,
        title="eth_nft_balance",
        description="A count of all nfts held by the user",
        allow_mutation=False,
    )
    
    tao_balance: float = pydantic.Field(
        ...,
        title="tao_balance",
        description="A int that captures the tao balance of the user.",
        allow_mutation=False,
    )
    
    tao_staked: float = pydantic.Field(
        ...,
        title="tao_staked",
        description="A int that captures the tao staked of the user.",
        allow_mutation=False,
    )

    no_of_transactions: int = pydantic.Field(
        ...,
        title="no_of_transactions",
        description="A int that captures the no of transactions of the user.",
        allow_mutation=False,
    )

    is_linkedin_email_verified: bool = pydantic.Field(
        "",
        title="is_linkedin_email_verified",
        description="A bool that returns true if the linkedin email is verifed"
    )

    score: float = pydantic.Field(
        "",
        title="score",
        description="A string that captures the score to the profile.",
        allow_mutation=True,
    )

    required_hash_fields: List[str] = pydantic.Field(
        ["id","type","public_repos","created_at","total_commits","eth_balance","eth_nft_balance","tao_balance","tao_staked","no_of_transactions","is_linkedin_email_verified"],
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
        return f"ProfileSynapse(id={self.id}, public_repos={self.public_repos}, created_at={self.created_at}, total_commits={self.total_commits}, eth_balance={self.eth_balance}, eth_nft_balance={self.eth_nft_balance}, tao_balance={self.tao_balance}, tao_staked={self.tao_staked}, no_of_transactions={self.no_of_transactions}, score={self.score})"

    def to_dict(self):
        return {
            "id": self.id,
            "public_repos": self.public_repos,
            "created_at": self.created_at,
            "total_commits": self.total_commits,
            "eth_balance": self.eth_balance,
            "eth_nft_balance": self.eth_nft_balance,
            "tao_balance": self.tao_balance,
            "tao_staked": self.tao_staked,
            "no_of_transactions": self.no_of_transactions,
            "score": self.score,
        }



