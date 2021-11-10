// contracts/GLDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

// we need to add a brownie-config.yaml file for imports to work
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract EasyToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20("EachToken", "EzT") {
        _mint(msg.sender, initialSupply);
    }
}
