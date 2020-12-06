"""Tests for the references module."""
import markdown
import pytest

from mkdocstrings.extension import MkdocstringsExtension
from mkdocstrings.references import fix_refs, relative_url


@pytest.mark.parametrize(
    ("current_url", "to_url", "href_url"),
    [
        ("a/", "a#b", "#b"),
        ("a/", "a/b#c", "b#c"),
        ("a/b/", "a/b#c", "#c"),
        ("a/b/", "a/c#d", "../c#d"),
        ("a/b/", "a#c", "..#c"),
        ("a/b/c/", "d#e", "../../../d#e"),
        ("a/b/", "c/d/#e", "../../c/d/#e"),
        ("a/index.html", "a/index.html#b", "#b"),
        ("a/index.html", "a/b.html#c", "b.html#c"),
        ("a/b.html", "a/b.html#c", "#c"),
        ("a/b.html", "a/c.html#d", "c.html#d"),
        ("a/b.html", "a/index.html#c", "index.html#c"),
        ("a/b/c.html", "d.html#e", "../../d.html#e"),
        ("a/b.html", "c/d.html#e", "../c/d.html#e"),
        ("a/b/index.html", "a/b/c/d.html#e", "c/d.html#e"),
    ],
)
def test_relative_url(current_url, to_url, href_url):
    """
    Compute relative URLs correctly.

    Arguments:
        current_url: The URL of the source page.
        to_url: The URL of the target page.
        href_url: The relative URL to put in the `href` HTML field.
    """
    assert relative_url(current_url, to_url) == href_url


def run_references_test(url_map, source, output, unmapped=None, from_url="page.html"):
    ext = MkdocstringsExtension({})
    md = markdown.Markdown(extensions=[ext])
    content = md.convert(source)
    actual_output, actual_unmapped = fix_refs(content, from_url, url_map)
    assert actual_output == output
    assert actual_unmapped == (unmapped or [])


def test_reference_implicit():
    run_references_test(
        url_map={"Foo": "foo.html#Foo"},
        source="This [Foo][].",
        output='<p>This <a href="foo.html#Foo">Foo</a>.</p>',
    )


def test_reference_explicit_with_markdown_text():
    run_references_test(
        url_map={"Foo": "foo.html#Foo"},
        source="This [`Foo`][Foo].",
        output='<p>This <a href="foo.html#Foo"><code>Foo</code></a>.</p>',
    )


def test_reference_with_punctuation():
    run_references_test(
        url_map={'Foo&"bar': 'foo.html#Foo&"bar'},
        source='This [Foo&"bar][].',
        output='<p>This <a href="foo.html#Foo&amp;&quot;bar">Foo&amp;"bar</a>.</p>',
    )


def test_no_reference_with_space():
    run_references_test(
        url_map={"Foo bar": "foo.html#Foo bar"},
        source="This `[Foo bar][]`.",
        output="<p>This <code>[Foo bar][]</code>.</p>",
    )


def test_no_reference_inside_markdown():
    run_references_test(
        url_map={"Foo": "foo.html#Foo"},
        source="This `[Foo][]`.",
        output="<p>This <code>[Foo][]</code>.</p>",
    )


def test_missing_reference():
    run_references_test(
        url_map={"NotFoo": "foo.html#NotFoo"},
        source="[Foo][]",
        output="<p>[Foo][]</p>",
        unmapped=["Foo"],
    )


def test_missing_reference_with_markdown_text():
    run_references_test(
        url_map={"NotFoo": "foo.html#NotFoo"},
        source="[`Foo`][Foo]",
        output="<p>[<code>Foo</code>][Foo]</p>",
        unmapped=["Foo"],
    )


def test_missing_reference_with_markdown_id():
    run_references_test(
        url_map={"NotFoo": "foo.html#NotFoo"},
        source="[Foo][*oh*]",
        output="<p>[Foo][*oh*]</p>",
        unmapped=["*oh*"],
    )


def test_missing_reference_with_markdown_implicit():
    run_references_test(
        url_map={"Foo": "foo.html#Foo"},
        source="[`Foo`][]",
        output="<p>[<code>Foo</code>][]</p>",
        unmapped=[],
    )
