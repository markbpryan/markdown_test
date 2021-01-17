# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.14.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.14.0) - 2021-01-06

<small>[Compare with 0.13.6](https://github.com/pawamoy/mkdocstrings/compare/0.13.6...0.14.0)</small>

Special thanks to Oleh [@oprypin](https://github.com/oprypin) Prypin who did an amazing job (this is a euphemism)
at improving MkDocstrings, fixing hard-to-fix bugs with clever solutions, implementing great new features
and refactoring the code for better performance and readability! Thanks Oleh!

### Bug Fixes
- Fix double code tags ([e84d401](https://github.com/pawamoy/mkdocstrings/commit/e84d401c6dcb9aecb8cc1a58d3a0f339e1c3e78f) by Timothée Mazzucotelli).
- Don't mutate the original Markdown config for permalinks ([8f6b163](https://github.com/pawamoy/mkdocstrings/commit/8f6b163b50551da22f65e9b736e042562f77f2d7) by Oleh Prypin).
- Preserve text immediately before an autodoc ([07466fa](https://github.com/pawamoy/mkdocstrings/commit/07466fafb54963a4e35e69007b6291a0382aaeb4) by Oleh Prypin). [PR #207](https://github.com/pawamoy/mkdocstrings/pull/207)
- Remove `href` attributes from headings in templates ([d5602ff](https://github.com/pawamoy/mkdocstrings/commit/d5602ff3bb1a75ac1c8c457e972271b6c66eb8dd) by Oleh Prypin). [PR #204](https://github.com/pawamoy/mkdocstrings/pull/204)
- Don't let `toc` extension append its permalink twice ([a154f5c](https://github.com/pawamoy/mkdocstrings/commit/a154f5c4c6ef9abd221e1f89e44847ae2cf25436) by Oleh Prypin). [PR #203](https://github.com/pawamoy/mkdocstrings/pull/203)
- Fix undefined entity for `&para;` ([2c29211](https://github.com/pawamoy/mkdocstrings/commit/2c29211002d515db40e5bdabf6cbf32ec8633a05) by Timothée Mazzucotelli).
- Make ids of Markdown sub-documents prefixed with the parent item id ([d493d33](https://github.com/pawamoy/mkdocstrings/commit/d493d33b3827d93e84a7b2e39f0a10dfcb782402) by Oleh Prypin). [Issue #186](https://github.com/pawamoy/mkdocstrings/issues/186) and [#193](https://github.com/pawamoy/mkdocstrings/issues/193), [PR #199](https://github.com/pawamoy/mkdocstrings/pull/199)
- More lenient regex for data-mkdocstrings-identifier ([dcfec8e](https://github.com/pawamoy/mkdocstrings/commit/dcfec8edfdff050debc5856dfc213d3119a84792) by Oleh Prypin).
- Shift Markdown headings according to the current `heading_level` ([13f41ae](https://github.com/pawamoy/mkdocstrings/commit/13f41aec5a95c82c1229baa4ac3caf4abb2add51) by Oleh Prypin). [Issue #192](https://github.com/pawamoy/mkdocstrings/issues/192), [PR #195](https://github.com/pawamoy/mkdocstrings/pull/195)
- Fix footnotes appearing in all following objects ([af24bc2](https://github.com/pawamoy/mkdocstrings/commit/af24bc246a6938ebcae7cf6ff677b194cf1af95c) by Oleh Prypin). [Issue #186](https://github.com/pawamoy/mkdocstrings/issues/186), [PR #195](https://github.com/pawamoy/mkdocstrings/pull/195)
- Fix cross-references from the root index page ([9c9f2a0](https://github.com/pawamoy/mkdocstrings/commit/9c9f2a04af94e0d88f57fd76249f7985166a9b88) by Oleh Prypin). [Issue #184](https://github.com/pawamoy/mkdocstrings/issues/184), [PR #185](https://github.com/pawamoy/mkdocstrings/pull/185)
- Fix incorrect argument name passed to Markdown ([10ce502](https://github.com/pawamoy/mkdocstrings/commit/10ce502d5fd58f1e5a4e14308ffad1bc3d7116ee) by Timothée Mazzucotelli).
- Fix error when a digit immediately follows a code tag ([9b92341](https://github.com/pawamoy/mkdocstrings/commit/9b9234160edc54b53c81a618b12095e7dd829059) by Oleh Prypin). [Issue #169](https://github.com/pawamoy/mkdocstrings/issues/169), [PR #175](https://github.com/pawamoy/mkdocstrings/pull/175)
- Detecting paths relative to template directory in logging ([a50046b](https://github.com/pawamoy/mkdocstrings/commit/a50046b5d58d62df4ba13f4c197e80edd1995eb9) by Oleh Prypin). [Issue #166](https://github.com/pawamoy/mkdocstrings/issues/166)

### Code Refactoring
- BlockProcessor already receives strings, use them as such ([bcf7da9](https://github.com/pawamoy/mkdocstrings/commit/bcf7da911a310a63351c5082e84bb763d90d5b3b) by Oleh Prypin).
- Remove some unused code ([8504084](https://github.com/pawamoy/mkdocstrings/commit/850408421cc027be8374673cc74c71fff26f3833) by Oleh Prypin). [PR #206](https://github.com/pawamoy/mkdocstrings/pull/206)
- Improve XML parsing error handling ([ad86410](https://github.com/pawamoy/mkdocstrings/commit/ad864100b644ab1ee8daaa0d3923bc87dee1c5ca) by Timothée Mazzucotelli).
- Explicitly use MarkupSafe ([6b9ebe7](https://github.com/pawamoy/mkdocstrings/commit/6b9ebe7d510e82971acef89e9e946af3c0cc96d3) by Oleh Prypin).
- Split out the handler cache, expose it through the plugin ([6453026](https://github.com/pawamoy/mkdocstrings/commit/6453026fac287387090a67cce70c078377d107dd) by Oleh Prypin). [Issue #179](https://github.com/pawamoy/mkdocstrings/issues/179), [PR #191](https://github.com/pawamoy/mkdocstrings/pull/191)
- Use ChainMap instead of copying dicts ([c634d2c](https://github.com/pawamoy/mkdocstrings/commit/c634d2ce6377de26caa553048bb28ef1e672f7aa) by Oleh Prypin). [PR #171](https://github.com/pawamoy/mkdocstrings/pull/171)
- Rename logging to loggers to avoid confusion ([7a119cc](https://github.com/pawamoy/mkdocstrings/commit/7a119ccf27cf77cf2cbd114e7fad0a9e4e97bbd8) by Timothée Mazzucotelli).
- Simplify logging ([409f93e](https://github.com/pawamoy/mkdocstrings/commit/409f93ed26d7d8292a8bc7a6c32cb270b3769409) by Timothée Mazzucotelli).

### Features
- Allow specifying `heading_level` as a Markdown heading ([10efc28](https://github.com/pawamoy/mkdocstrings/commit/10efc281e04b2a430cec53e49208ccc09e591667) by Oleh Prypin). [PR #170](https://github.com/pawamoy/mkdocstrings/pull/170)
- Allow any characters in identifiers ([7ede68a](https://github.com/pawamoy/mkdocstrings/commit/7ede68a0917b494eda2198931a8ad1c97fc8fce4) by Oleh Prypin). [PR #174](https://github.com/pawamoy/mkdocstrings/pull/174)
- Allow namespace packages for handlers ([39b0465](https://github.com/pawamoy/mkdocstrings/commit/39b046548f57dc59993241b24d2cf12fb5e488eb) by Timothée Mazzucotelli).
- Add template debugging/logging ([33b32c1](https://github.com/pawamoy/mkdocstrings/commit/33b32c1410bf6e8432768865c8aa86b8e091ab59) by Timothée Mazzucotelli).
- Add initial support for the ReadTheDocs theme ([1028115](https://github.com/pawamoy/mkdocstrings/commit/1028115682ed0806d6570c749af0e382c67d6120) by Timothée Mazzucotelli). [Issue #107](https://github.com/pawamoy/mkdocstrings/issues/107), [PR #159](https://github.com/pawamoy/mkdocstrings/pull/159)
- Add option to show type annotations in signatures ([f94ce9b](https://github.com/pawamoy/mkdocstrings/commit/f94ce9bdb2afc2c41c21a53636980ca077b757ce) by Timothée Mazzucotelli). [Issue #106](https://github.com/pawamoy/mkdocstrings/issues/106)

### Packaging
- Accept verions of `pytkdocs` up to 0.10.x (see [changelog](https://pawamoy.github.io/pytkdocs/changelog/#0100-2020-12-06)).

### Performance Improvements
- Call `update_env` only once per `Markdown` instance ([b198c74](https://github.com/pawamoy/mkdocstrings/commit/b198c74338dc3b54b999eadeef9946d69277ad77) by Oleh Prypin). [PR #201](https://github.com/pawamoy/mkdocstrings/pull/201)
- Disable Jinja's `auto_reload` to reduce disk reads ([3b28c58](https://github.com/pawamoy/mkdocstrings/commit/3b28c58c77642071419d4a98e007d5a854b7984f) by Oleh Prypin). [PR #200](https://github.com/pawamoy/mkdocstrings/pull/200)
- Rework autorefs replacement to not re-parse the final HTML ([22a9e4b](https://github.com/pawamoy/mkdocstrings/commit/22a9e4bf1b73f9b9b1a7c4876f0c677f919bc4d7) by Oleh Prypin). [Issue #187](https://github.com/pawamoy/mkdocstrings/issues/187), [PR #188](https://github.com/pawamoy/mkdocstrings/pull/188)


## [0.13.6](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.6) - 2020-09-28

<small>[Compare with 0.13.5](https://github.com/pawamoy/mkdocstrings/compare/0.13.5...0.13.6)</small>

### Bug Fixes
- Fix rendering when clicking on hidden toc entries ([2af4d31](https://github.com/pawamoy/mkdocstrings/commit/2af4d310adefec614235a2c1d04d5ff56bf9c220) by Timothée Mazzucotelli). Issue [#60](https://github.com/pawamoy/mkdocstrings/issues/60).


## [0.13.5](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.5) - 2020-09-28

<small>[Compare with 0.13.4](https://github.com/pawamoy/mkdocstrings/compare/0.13.4...0.13.5)</small>

## Packaging
- Accept `pytkdocs` version up to 0.9.x ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#090-2020-09-28)).


## [0.13.4](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.4) - 2020-09-25

<small>[Compare with 0.13.3](https://github.com/pawamoy/mkdocstrings/compare/0.13.3...0.13.4)</small>

### Bug Fixes
- Bring back arbitrary `**config` to Python handler ([fca7d4c](https://github.com/pawamoy/mkdocstrings/commit/fca7d4c75ffd7a84eaeccd27facd5575604dbfab) by Florimond Manca). Issue [#154](https://github.com/pawamoy/mkdocstrings/issues/154), PR [#155](https://github.com/pawamoy/mkdocstrings/pull/155)


## [0.13.3](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.3) - 2020-09-25

<small>[Compare with 0.13.2](https://github.com/pawamoy/mkdocstrings/compare/0.13.2...0.13.3)</small>

### Packaging
- Accept `pytkdocs` version up to 0.8.x ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#080-2020-09-25)).


## [0.13.2](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.2) - 2020-09-08

<small>[Compare with 0.13.1](https://github.com/pawamoy/mkdocstrings/compare/0.13.1...0.13.2)</small>

### Bug Fixes
- Fix relative URLs when `use_directory_urls` is false ([421d189](https://github.com/pawamoy/mkdocstrings/commit/421d189fff9ea2608e40d85e0a93e30334782b90) by Timothée Mazzucotelli). References: [#149](https://github.com/pawamoy/mkdocstrings/issues/149)


## [0.13.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.1) - 2020-09-03

<small>[Compare with 0.13.0](https://github.com/pawamoy/mkdocstrings/compare/0.13.0...0.13.1)</small>

### Bug Fixes
- Use relative links for cross-references ([9c77f1f](https://github.com/pawamoy/mkdocstrings/commit/9c77f1f461fa87842ae39945f9521ee85b1e413b) by Timothée Mazzucotelli). References: [#144](https://github.com/pawamoy/mkdocstrings/issues/144), [#147](https://github.com/pawamoy/mkdocstrings/issues/147)


## [0.13.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.13.0) - 2020-08-21

<small>[Compare with 0.12.2](https://github.com/pawamoy/mkdocstrings/compare/0.12.2...0.13.0)</small>

### Bug Fixes
- Accept dashes in module names ([fcf79d0](https://github.com/pawamoy/mkdocstrings/commit/fcf79d0024ec46c3862c94202864e054c04a6d0b) by Timothée Mazzucotelli). References: [#140](https://github.com/pawamoy/mkdocstrings/issues/140)

### Features
- Add option to show full path of direct members only ([d1b9401](https://github.com/pawamoy/mkdocstrings/commit/d1b9401afecb20d3123eec7334605cb15bf9d877) by Aaron Dunmore). References: [#134](https://github.com/pawamoy/mkdocstrings/issues/134), [#136](https://github.com/pawamoy/mkdocstrings/issues/136)

### Packaging
- Accept `pymdown-extensions` versions up to 0.8.x ([see release notes](https://facelessuser.github.io/pymdown-extensions/about/releases/8.0/#8.0)) ([178d48d](https://github.com/pawamoy/mkdocstrings/commit/178d48da7a62daf285dfc5f6ff230e8bce82ed53) by Hugo van Kemenade). PR [#146](https://github.com/pawamoy/mkdocstrings/issue/146)


## [0.12.2](https://github.com/pawamoy/mkdocstrings/releases/tag/0.12.2) - 2020-07-24

<small>[Compare with 0.12.1](https://github.com/pawamoy/mkdocstrings/compare/0.12.1...0.12.2)</small>

### Packaging
- Accept `pytkdocs` version up to 0.7.x ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#070-2020-07-24)).


## [0.12.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.12.1) - 2020-07-07

<small>[Compare with 0.12.0](https://github.com/pawamoy/mkdocstrings/compare/0.12.0...0.12.1)</small>

### Bug Fixes
- Fix HTML-escaped sequence parsing as XML ([db297f1](https://github.com/pawamoy/mkdocstrings/commit/db297f19013fc402eeff1f2827057a959e481c66) by Timothée Mazzucotelli).
- Allow running mkdocs from non-default interpreter ([283dd7b](https://github.com/pawamoy/mkdocstrings/commit/283dd7b83eeba675a16d96d2e829851c1273a625) by Jared Khan).


## [0.12.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.12.0) - 2020-06-14

<small>[Compare with 0.11.4](https://github.com/pawamoy/mkdocstrings/compare/0.11.4...0.12.0)</small>

### Features
- Support attributes section in Google-style docstrings ([8300253](https://github.com/pawamoy/mkdocstrings/commit/83002532b2294ea33dcec4f2672a5a6d0f64def1) by Timothée Mazzucotelli). References: [#88](https://github.com/pawamoy/mkdocstrings/issues/88)
- Support examples section in Google-style docstrings ([650c754](https://github.com/pawamoy/mkdocstrings/commit/650c754afdd5d4fb96b1e2529f378d025a2e7daf) by Iago González). References: [#112](https://github.com/pawamoy/mkdocstrings/issues/112)

### Packaging
- Accept `pytkdocs` version up to 0.6.x ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#060-2020-06-14)).

## [0.11.4](https://github.com/pawamoy/mkdocstrings/releases/tag/0.11.4) - 2020-06-08

<small>[Compare with 0.11.3](https://github.com/pawamoy/mkdocstrings/compare/0.11.3...0.11.4)</small>

### Packaging
- Accept `pytkdocs` version up to 0.5.x ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#050-2020-06-08)).
  If it breaks your docs, please [open issues on `pytkdocs`' bug-tracker](https://github.com/pawamoy/pytkdocs/issues),
  or pin `pytkdocs` version to while waiting for bug fixes <0.5.0 :clown:.


## [0.11.3](https://github.com/pawamoy/mkdocstrings/releases/tag/0.11.3) - 2020-06-07

<small>[Compare with 0.11.2](https://github.com/pawamoy/mkdocstrings/compare/0.11.2...0.11.3)</small>

### Bug Fixes
- Support custom theme directory configuration ([1243cf6](https://github.com/pawamoy/mkdocstrings/commit/1243cf673aaf371e5cbf42a3e0d1aa80482398a3) by Abhishek Thakur). References: [#120](https://github.com/pawamoy/mkdocstrings/issues/120), [#121](https://github.com/pawamoy/mkdocstrings/issues/121)


## [0.11.2](https://github.com/pawamoy/mkdocstrings/releases/tag/0.11.2) - 2020-05-20

<small>[Compare with 0.11.1](https://github.com/pawamoy/mkdocstrings/compare/0.11.1...0.11.2)</small>

### Packaging
- Increase `pytkdocs` version range to accept 0.4.0
  ([changelog](https://pawamoy.github.io/pytkdocs/changelog/#040-2020-05-17)).


## [0.11.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.11.1) - 2020-05-14

<small>[Compare with 0.11.0](https://github.com/pawamoy/mkdocstrings/compare/0.11.0...0.11.1)</small>

### Bug Fixes
- Fix integration with mkdocs logging *une bonne fois pour toute* ([3293cbf](https://github.com/pawamoy/mkdocstrings/commit/3293cbf161f05d36de6c1d50b5de9742bf99066e) by Timothée Mazzucotelli).
- Discard setup commands stdout ([ea44cea](https://github.com/pawamoy/mkdocstrings/commit/ea44cea33159ed3a6b0b34b4cd52a17a40bd6460) by Timothée Mazzucotelli). References: [#91](https://github.com/pawamoy/mkdocstrings/issues/91)
- Use the proper python executable to start subprocesses ([9fe3b39](https://github.com/pawamoy/mkdocstrings/commit/9fe3b3915bd8f15011f8f3632a227d1eb56603fd) by Reece Dunham). References: [#91](https://github.com/pawamoy/mkdocstrings/issues/91), [#103](https://github.com/pawamoy/mkdocstrings/issues/103)


## [0.11.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.11.0) - 2020-04-23

<small>[Compare with 0.10.3](https://github.com/pawamoy/mkdocstrings/compare/0.10.3...0.11.0)</small>

### Bug Fixes
- Properly raise on errors (respect strict mode) ([2097208](https://github.com/pawamoy/mkdocstrings/commit/20972082a94b64bec02c77d6a80384d8042f60ea) by Timothée Mazzucotelli). Related issues/PRs: [#86](https://github.com/pawamoy/mkdocstrings/issues/86)
- Hook properly to MkDocs logging ([b23daed](https://github.com/pawamoy/mkdocstrings/commit/b23daed3743bbd2d3f024df34582a317c51a1af0) by Timothée Mazzucotelli). Related issues/PRs: [#86](https://github.com/pawamoy/mkdocstrings/issues/86)

### Features
- Add `setup_commands` option to python handler ([599f8e5](https://github.com/pawamoy/mkdocstrings/commit/599f8e528f55093b0011b732da959b747c1e02c0) by Ross Mechanic). Related issues/PRs: [#89](https://github.com/pawamoy/mkdocstrings/issues/89), [#90](https://github.com/pawamoy/mkdocstrings/issues/90)
- Add option to allow overriding templates ([7360021](https://github.com/pawamoy/mkdocstrings/commit/7360021ab4753706d0f6209ed960050f5d424ad8) by Mikaël Capelle). Related issues/PRs: [#59](https://github.com/pawamoy/mkdocstrings/issues/59), [#82](https://github.com/pawamoy/mkdocstrings/issues/82)


## [0.10.3](https://github.com/pawamoy/mkdocstrings/releases/tag/0.10.3) - 2020-04-10

<small>[Compare with 0.10.2](https://github.com/pawamoy/mkdocstrings/compare/0.10.2...0.10.3)</small>

### Bug Fixes
- Handle `site_url` not being defined ([9fb4a9b](https://github.com/pawamoy/mkdocstrings/commit/9fb4a9bbebe2457b389921ba1ee3e1f924c5691b) by Timothée Mazzucotelli). Related issues/PRs: [#77](https://github.com/pawamoy/mkdocstrings/issues/77)

### Packaging
This version increases the accepted range of versions for the `pytkdocs` dependency to `>=0.2.0, <0.4.0`.
The `pytkdocs` project just released [version 0.3.0](https://pawamoy.github.io/pytkdocs/changelog/#030-2020-04-10)
which:

- adds support for complex markup in docstrings sections items descriptions
- adds support for different indentations in docstrings sections (tabulations or less/more than 4 spaces)
- fixes docstring parsing for arguments whose names start with `*`, like `*args` and `**kwargs`


## [0.10.2](https://github.com/pawamoy/mkdocstrings/releases/tag/0.10.2) - 2020-04-07

<small>[Compare with 0.10.1](https://github.com/pawamoy/mkdocstrings/compare/0.10.1...0.10.2)</small>

### Packaging
This version increases the accepted range of versions for the `pymdown-extensions` dependency,
as well as for the `mkdocs-material` development dependency. Indeed, both these projects recently
released major versions 7 and 5 respectively. Users who wish to use these new versions will be able to.
See issue [#74](https://github.com/pawamoy/mkdocstrings/issues/74).

## [0.10.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.10.1) - 2020-04-03

<small>[Compare with 0.10.0](https://github.com/pawamoy/mkdocstrings/compare/0.10.0...0.10.1)</small>

### Bug Fixes
- Fix jinja2 error for jinja2 < 2.11 ([387f970](https://github.com/pawamoy/mkdocstrings/commit/387f97088ad2b7b25389ae6cf303bae071e90e6c) by Timothée Mazzucotelli). Related issues/PRs: [#67](https://github.com/pawamoy/mkdocstrings/issues/67), [#72](https://github.com/pawamoy/mkdocstrings/issues/72)
- Fix missing dependency pymdown-extensions ([648b99d](https://github.com/pawamoy/mkdocstrings/commit/648b99dab9d1af87db474ce7683de50c9bf8996d) by Timothée Mazzucotelli). Related issues/PRs: [#66](https://github.com/pawamoy/mkdocstrings/issues/66)
- Fix heading level of hidden toc entries ([475cc62](https://github.com/pawamoy/mkdocstrings/commit/475cc62b1cf4342b82ca8685166306441e4b83c4) by Timothée Mazzucotelli). Related issues/PRs: [#65](https://github.com/pawamoy/mkdocstrings/issues/65)
- Fix rendering signatures containing keyword_only ([c6c5add](https://github.com/pawamoy/mkdocstrings/commit/c6c5addd8be65beaf7055c9d0f512e0de8b3eba4) by Timothée Mazzucotelli). Related issues/PRs: [#68](https://github.com/pawamoy/mkdocstrings/issues/68)


## [0.10.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.10.0) - 2020-03-27

<small>[Compare with 0.9.1](https://github.com/pawamoy/mkdocstrings/compare/0.9.1...0.10.0)</small>

### Features
- Prepare for new `pytkdocs` version ([336421a](https://github.com/pawamoy/mkdocstrings/commit/336421af95d752671276c2e88c5c173bff4093cc)).
  Add options `filters` and `members` to the Python collector to reflect the new `pytkdocs` options.
  See [the default configuration of the Python collector](https://pawamoy.github.io/mkdocstrings/reference/handlers/python/#mkdocstrings.handlers.python.PythonCollector.DEFAULT_CONFIG).


## [0.9.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.9.1) - 2020-03-21

<small>[Compare with 0.9.0](https://github.com/pawamoy/mkdocstrings/compare/0.9.0...0.9.1)</small>

### Bug fixes
- Fix cross-references when deploying to GitHub pages ([36f804b](https://github.com/pawamoy/mkdocstrings/commit/36f804beab01531c0331ed89d21f3e5e15bd8585)).


## [0.9.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.9.0) - 2020-03-21

<small>[Compare with 0.8.0](https://github.com/pawamoy/mkdocstrings/compare/0.8.0...0.9.0)</small>

This version is a big refactor. We will just list the new features without pointing to particular commits.
The documentation rendering looks slightly different, and should be better than before.
No identified breaking changes for end-users.

### Features
- **Language agnostic:** we moved the code responsible for loading Python documentation into a new project,
  [`pytkdocs`](https://github.com/pawamoy/pytkdocs), and implemented a "handlers" logic, effectively allowing to
  support any given language. Waiting for your handlers contributions :wink:!
- **Multiple themes support:** handlers can offer templates for multiple `mkdocs` themes.
- **Better cross-references:** cross-references now not only work between documented objects (between all languages,
  given the objects' identifiers are unique), but also for every heading of your Markdown pages.
- **Configuration options:** the rendering of Python documentation can now be configured,
  (globally and locally thanks to the handlers system),
  [check the docs!](https://pawamoy.github.io/mkdocstrings/reference/handlers/python/#mkdocstrings.handlers.python.PythonRenderer.DEFAULT_CONFIG)
  Also see the [recommended CSS](https://pawamoy.github.io/mkdocstrings/handlers/python/#recommended-style).
- **Proper logging messages:** `mkdocstrings` now logs debug, warning and error messages, useful when troubleshooting.

### Bug fixes
- Various fixes and better error handling.


## [0.8.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.8.0) - 2020-03-04

<small>[Compare with 0.7.2](https://github.com/pawamoy/mkdocstrings/compare/0.7.2...0.8.0)</small>

### Breaking Changes
- Be compatible with Mkdocs >= 1.1 ([5a974a4](https://github.com/pawamoy/mkdocstrings/commit/5a974a4eb810904d6836e216d8539affc8acaa6f)).
  This is a breaking change as we're not compatible with versions of Mkdocs below 1.1 anymore.
  If you cannot upgrade Mkdocs to 1.1, pin mkdocstrings' version to 0.7.2.

## [0.7.2](https://github.com/pawamoy/mkdocstrings/releases/tag/0.7.2) - 2020-03-04

<small>[Compare with 0.7.1](https://github.com/pawamoy/mkdocstrings/compare/0.7.1...0.7.2)</small>

### Bug Fixes
- Catch `OSError` when trying to get source lines ([8e8d604](https://github.com/pawamoy/mkdocstrings/commit/8e8d604ba95363c140841c84535d2350d7ebbfe3)).
- Do not render signature empty sentinel ([16dfd73](https://github.com/pawamoy/mkdocstrings/commit/16dfd73cf30d01314dba756d3f10308b99c87dcc)).
- Fix for nested classes and their attributes ([7fef903](https://github.com/pawamoy/mkdocstrings/commit/7fef9037c5299d6106347b0db29f85a644f85c16)).
- Fix `relative_file_path` method ([52715ad](https://github.com/pawamoy/mkdocstrings/commit/52715adc59fe2e26a9e91df88bac8b8b32d4635e)).
- Wrap file path in backticks to escape it ([2525f39](https://github.com/pawamoy/mkdocstrings/commit/2525f39ad8c181679fa33db8e6dfaa28eb39c289)).

## [0.7.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.7.1) - 2020-02-18

<small>[Compare with 0.7.0](https://github.com/pawamoy/mkdocstrings/compare/0.7.0...0.7.1)</small>

### Bug Fixes
- Replace literal slash with os.sep for Windows compatibility ([70f9af5](https://github.com/pawamoy/mkdocstrings/commit/70f9af5e33cda694cda33870c84a770c853d84b5)).


## [0.7.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.7.0) - 2020-01-13

<small>[Compare with 0.6.1](https://github.com/pawamoy/mkdocstrings/compare/0.6.1...0.7.0)</small>

### Bug Fixes
- Don't mark args or kwargs as required ([4049d6f](https://github.com/pawamoy/mkdocstrings/commit/4049d6f27c332b05db06bcfe6cc564f3c1c0f013)).
- Filter submodules ([7b11095](https://github.com/pawamoy/mkdocstrings/commit/7b110959529c5fc0275fb98c6d97e7c71e205900)).

### Code Refactoring
- Don't guess lang in generated docs ([db4f60a](https://github.com/pawamoy/mkdocstrings/commit/db4f60a13dd0d191d7515683d7d42ae374b39fae)).
- Render at HTML step with custom markdown converter ([9b5a3e1](https://github.com/pawamoy/mkdocstrings/commit/9b5a3e126cd584893a8d0858ca9b67b8251e88f1)).

### Features
- Change forward ref to ref, fix optional unions ([2f0bfaa](https://github.com/pawamoy/mkdocstrings/commit/2f0bfaabf367bfa513c20fb1230409306e43add2)).
- Discover package submodules ([231062a](https://github.com/pawamoy/mkdocstrings/commit/231062a3a107abc02134f102a06693969cf603ad)).
- Implement watched source code (hacks) ([4a67953](https://github.com/pawamoy/mkdocstrings/commit/4a67953c0af9da363d52ba058b3c51cf4cbfaabe)).


## [0.6.1](https://github.com/pawamoy/mkdocstrings/releases/tag/0.6.1) - 2020-01-02

<small>[Compare with 0.6.0](https://github.com/pawamoy/mkdocstrings/compare/0.6.0...0.6.1)</small>

### Bug Fixes
- Break docstring discarding loop if found ([5a17fec](https://github.com/pawamoy/mkdocstrings/commit/5a17fec5beed2003d19ccdcb359b46b79bfcf469)).
- Fix discarding docstring ([143f7cb](https://github.com/pawamoy/mkdocstrings/commit/143f7cb00f02a7d3179cc5606ed7903566250227)).
- Fix getting annotation from nodes ([ecde72b](https://github.com/pawamoy/mkdocstrings/commit/ecde72bb22ccedb36aa847dd50504c63ad04498c)).
- Fix various things ([affbf06](https://github.com/pawamoy/mkdocstrings/commit/affbf064d457d4b626e8f67d38e94d7919bc2df2)).

### Code Refactoring
- Break as soon as we find the same attr in a parent class while trying to discard the docstring ([65d7908](https://github.com/pawamoy/mkdocstrings/commit/65d7908f489ec465b2803ea8f55c70d0f9d7586b)).
- Split Docstring.parse method to improve readability ([2226e2d](https://github.com/pawamoy/mkdocstrings/commit/2226e2d55a6b9bbdd5a56183f1a9ba3c5f01b5ac)).


## [0.6.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.6.0) - 2019-12-28

<small>[Compare with 0.5.0](https://github.com/pawamoy/mkdocstrings/compare/0.5.0...0.6.0)</small>

### Bug Fixes
- Fix GenericMeta import error on Python 3.7+ ([febf2b9](https://github.com/pawamoy/mkdocstrings/commit/febf2b9749d97cce80f5d20339372842fdffc908)).

### Code Refactoring
- More classes. Still ugly code though :'( ([f41c119](https://github.com/pawamoy/mkdocstrings/commit/f41c11988d8d849a0310cca511c2d93a74cab86f)).
- Split into more modules ([f1872a4](https://github.com/pawamoy/mkdocstrings/commit/f1872a4c8d41a0b9603b7f344de3186110a4e1bd)).
- Use Object subclasses ([40dd106](https://github.com/pawamoy/mkdocstrings/commit/40dd1062188e6ad6ef6fbc12ddead2132fe6af1e)).


## [0.5.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.5.0) - 2019-12-22

<small>[Compare with 0.4.0](https://github.com/pawamoy/mkdocstrings/compare/0.4.0...0.5.0)</small>

### Features
- Use divs in HTML contents to ease styling ([2a36a0e](https://github.com/pawamoy/mkdocstrings/commit/2a36a0eba7f52c43a3eba593ddd971acaa0a9c92)).


## [0.4.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.4.0) - 2019-12-22

<small>[Compare with 0.3.0](https://github.com/pawamoy/mkdocstrings/compare/0.3.0...0.4.0)</small>

### Features
- Parse docstrings Google-style blocks, get types from signature ([5af0c7b](https://github.com/pawamoy/mkdocstrings/commit/5af0c7b766ea7158d603b44c6df278dbcd189864)).


## [0.3.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.3.0) - 2019-12-21

<small>[Compare with 0.2.0](https://github.com/pawamoy/mkdocstrings/compare/0.2.0...0.3.0)</small>

### Features
- Allow object referencing in docstrings ([2dd50c0](https://github.com/pawamoy/mkdocstrings/commit/2dd50c06f96acaf0e2f969f217f0cbcfb1de2fd4)).


## [0.2.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.2.0) - 2019-12-15

<small>[Compare with 0.1.0](https://github.com/pawamoy/mkdocstrings/compare/0.1.0...0.2.0)</small>

### Misc
- Refactor, features, etc. ([111fa85](https://github.com/pawamoy/mkdocstrings/commit/111fa85a6305a198ac4e19a75bb491b98683929c)).


## [0.1.0](https://github.com/pawamoy/mkdocstrings/releases/tag/0.1.0) - 2019-12-12

<small>[Compare with first commit](https://github.com/pawamoy/mkdocstrings/compare/f1dd8fb2b4a4ae81f9144fe062ca9743ae82bd69...0.1.0)</small>

### Misc
- Clean up (delete unused files) ([c227043](https://github.com/pawamoy/mkdocstrings/commit/c227043814381b95031e426725e97106931f4ef9)).
- Clean up unused makefile rules ([edc01e9](https://github.com/pawamoy/mkdocstrings/commit/edc01e99aa7b762e800d9ae25cd5b842812dc326)).
- Initial commit ([f1dd8fb](https://github.com/pawamoy/mkdocstrings/commit/f1dd8fb2b4a4ae81f9144fe062ca9743ae82bd69)).
- Update readme ([ae56bdd](https://github.com/pawamoy/mkdocstrings/commit/ae56bdd9ac5692665409e99eb0fd509d8dfc605e)).
- Add plugin ([6ed5cb1](https://github.com/pawamoy/mkdocstrings/commit/6ed5cb1879b498ddc8d0fe1c04db7e3527f2ff81)).
- First PoC, needs better theming ([18a00b9](https://github.com/pawamoy/mkdocstrings/commit/18a00b9405a94405256a1ad2ae45886da40296e4)).
- Get attributes docstrings ([7838fff](https://github.com/pawamoy/mkdocstrings/commit/7838fffa5b1d5a481fd2ea5a94d305a96b06c321)).
- Refactor ([f68f1a8](https://github.com/pawamoy/mkdocstrings/commit/f68f1a89d477a55a6e86a9eb4c92bd5d6416b5cc)).
