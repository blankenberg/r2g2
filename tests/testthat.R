if (!requireNamespace("testthat", quietly = TRUE)) {
  stop("The R package 'testthat' is required to run R tests.", call. = FALSE)
}

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- normalizePath(sub("^--file=", "", file_arg[[1]]))
test_dir <- file.path(dirname(script_path), "testthat")

testthat::test_dir(test_dir, reporter = "summary")
