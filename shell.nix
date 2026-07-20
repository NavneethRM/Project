{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    pkgs.python313
    pkgs.gcc
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
  ];

  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.zlib
      pkgs.stdenv.cc.cc.lib
    ]}:$LD_LIBRARY_PATH
  '';
}
