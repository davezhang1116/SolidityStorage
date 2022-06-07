// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Storage {
    //uint256 public index;
    uint256 public count;
    uint256 public total;

    struct People {
        uint256 index;
        string firstName;
        string middleNameInitial;
        string lastName;
        uint16 yearBorn;
        bool status;
    }

    mapping(uint256 => People) public people;

    constructor() public {
        count = 0;
        total = 0;
    }

    function storeData(
        uint256 _index,
        string memory _firstName,
        string memory _middleNameInitial,
        string memory _lastName,
        uint16 _yearBorn
    ) public {
        people[_index] = People(
            _index,
            _firstName,
            _middleNameInitial,
            _lastName,
            _yearBorn,
            true
        );
        count++;
        total++;
    }

    function removeData(uint256 _index) public returns (string memory) {
        if (retrieveStatus(_index) == true) {
            people[_index].status = false;
            count--;
            return ("Modified!");
        } else {
            people[_index].status = false;
            return ("This person doesn't exist!");
        }
    }

    function retrieveData(uint256 _index)
        public
        returns (
            uint256,
            string memory,
            string memory,
            string memory,
            uint16,
            bool
        )
    {
        return (
            people[_index].index,
            people[_index].firstName,
            people[_index].middleNameInitial,
            people[_index].lastName,
            people[_index].yearBorn,
            people[_index].status
        );
    }

    function retrieveCount() public view returns (uint256) {
        return count;
    }

    function retrieveTotal() public view returns (uint256) {
        return total;
    }

    function retrieveStatus(uint256 _index) public returns (bool) {
        return (people[_index].status);
    }
}
