{
  "targets": [
    {
      "target_name": "tree_sitter_haskell_binding",
      "type": "shared_library",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "link_settings": {
        "libraries": ["-L/Volumes/Ramdisk/node-custom/lib", "-lnode.84",]
      },
      "sources": [
        "src/parser.c",
        "src/binding.cc",
        "src/scanner.cc",
      ],
      "cflags_c": [
        "-std=c99",
      ]
    }
  ]
}
