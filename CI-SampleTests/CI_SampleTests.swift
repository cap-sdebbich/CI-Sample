//
//  CI_SampleTests.swift
//  CI-SampleTests
//
//  Created by Safwen DEBBICHI on 05/02/2019.
//  Copyright © 2019 Safwen DEBBICHI. All rights reserved.
//

import XCTest
@testable import CI_Sample

class CI_SampleTests: XCTestCase {

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testExample() {
        let one = "one"
        let two = "two"
        XCTAssert(one != two, "error one is not two")
    }

}
