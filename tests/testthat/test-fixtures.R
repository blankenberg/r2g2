test_that("R fixture scripts are present", {
  fixture_dir <- testthat::test_path("..", "test_r_scripts")
  fixtures <- list.files(fixture_dir, pattern = "\\.[rR]$", full.names = TRUE)

  expect_true(dir.exists(fixture_dir))
  expect_gt(length(fixtures), 0)
  expect_true(any(basename(fixtures) == "test.r"))
})
