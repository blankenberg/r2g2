from xml.etree import ElementTree

from r2g2.anvio import FakeArg
from r2g2.utils import simplify_text, str_typeint


def test_simplify_text_replaces_unsafe_characters():
    assert simplify_text("R2-G2 package/name") == "R2_G2_package_name"


def test_str_typeint_maps_known_and_unknown_r_types():
    assert str_typeint(13) == "INTSXP"
    assert str_typeint(999) == "UNKNOWN_TYPE(999)"


def test_fakearg_records_argument_metadata_and_generates_xml():
    parser = FakeArg(description="test parser")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads")

    params = parser.oynaxraoret_get_params({})

    assert len(params) == 2
    threads_param = next(param for param in params if param.name == "threads")
    xml = ElementTree.fromstring(threads_param.to_xml_param())

    assert xml.attrib["name"] == "threads"
    assert xml.attrib["type"] == "integer"
    assert xml.attrib["value"] == "4"
    assert threads_param.to_cmd_line().strip() == (
        "#if $str( $threads ):\n"
        "    --threads '${threads}'\n"
        "#end if"
    )
