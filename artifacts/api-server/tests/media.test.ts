import assert from "node:assert/strict";
import test from "node:test";
import { parseByteRange } from "../src/routes/media";

test("serves full media when there is no Range header", () => {
  assert.equal(parseByteRange(undefined, 1000), null);
});

test("supports closed, open-ended and suffix byte ranges for seeking", () => {
  assert.deepEqual(parseByteRange("bytes=0-99", 1000), { start: 0, end: 99 });
  assert.deepEqual(parseByteRange("bytes=500-", 1000), { start: 500, end: 999 });
  assert.deepEqual(parseByteRange("bytes=-200", 1000), { start: 800, end: 999 });
  assert.deepEqual(parseByteRange("bytes=900-2000", 1000), { start: 900, end: 999 });
  assert.deepEqual(parseByteRange("bytes=-2000", 1000), { start: 0, end: 999 });
});

test("rejects invalid and out-of-bounds ranges", () => {
  for (const value of ["bytes=1000-", "bytes=500-400", "bytes=-0", "bytes=-",
    "bad", "bytes=0-1,3-4", "bytes=99999999999999999-"]) {
    assert.equal(parseByteRange(value, 1000), false, value);
  }
  assert.equal(parseByteRange("bytes=0-", 0), false);
});
