// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FairGaming {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function isFairGame(uint randomNumber, uint threshold) public pure returns (bool) {
        return randomNumber >= threshold;
    }
}