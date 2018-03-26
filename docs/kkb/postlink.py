from xml.etree import ElementTree as ET
from base64 import b64decode
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.exceptions import InvalidSignature

message = '<bank name="Kazkommertsbank JSC"><customer name="Monkey Shmonkey" mail="darkhan@bbtest.kz" phone=""><merchant cert_id="00c183d70b" name="bbTest.kz"><order order_id="888888888888004" amount="100.00" currency="398"><department merchant_id="92061103" amount="100.00"/></order></merchant><merchant_sign type="RSA"/></customer><customer_sign type="RSA"/><results timestamp="2018-03-26 03:04:50"><payment merchant_id="92061103" card="548318-XX-XXXX-0293" amount="100.00" reference="180326030450" approval_code="030450" response_code="00" Secure="No" card_bin="" c_hash="D643983890D0003EA973E88A346CDDBE"/></results></bank>'
signed_message = '<document>%s<bank_sign cert_id="00c183d690" type="SHA/RSA">K0OvLmEKVq2jneFHXBk99WvYvvNppN86aG9PmS4HTSzzp4NHJF5/QaQg/QNFPbUHWpmpjO7tADVDJS14Rx2Fcaa1x/oavY6FqnGHXX91hw9ZBveB/yjKg4ZBLXAj7CU62m5hznTNOWzMNB5AVt+KEmIf2PK+FpTYTkDcIs3s+Bo=</bank_sign></document>' % message
"""
<document>
    <bank name="Kazkommertsbank JSC">
        <customer name="Monkey Shmonkey" mail="darkhan@bbtest.kz" phone="">
            <merchant cert_id="00c183d70b" name="bbTest.kz">
                <order order_id="888888888888004" amount="100.00" currency="398">
                    <department merchant_id="92061103" amount="100.00"/>
                </order>
            </merchant>
            <merchant_sign type="RSA"/>
        </customer>
        <customer_sign type="RSA"/>
        <results timestamp="2018-03-26 03:04:50">
            <payment merchant_id="92061103" card="548318-XX-XXXX-0293" amount="100.00" reference="180326030450" approval_code="030450" response_code="00" Secure="No" card_bin="" c_hash="D643983890D0003EA973E88A346CDDBE"/>
        </results>
    </bank>
    <bank_sign cert_id="00c183d690" type="SHA/RSA">K0OvLmEKVq2jneFHXBk99WvYvvNppN86aG9PmS4HTSzzp4NHJF5/QaQg/QNFPbUHWpmpjO7tADVDJS14Rx2Fcaa1x/oavY6FqnGHXX91hw9ZBveB/yjKg4ZBLXAj7CU62m5hznTNOWzMNB5AVt+KEmIf2PK+FpTYTkDcIs3s+Bo=</bank_sign>
</document>
"""
test_public_key = "-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIFAMGD1pAwDQYJKoZIhvcNAQEEBQAwUzELMAkGA1UEBhMC\nS1oxDDAKBgNVBAoTA0tLQjELMAkGA1UECxMCQ0ExDzANBgNVBAMTBktLQiBDQTEY\nMBYGCSqGSIb3DQEJARYJY2FAa2tiLmt6MB4XDTE1MDgyNzEzMjAwMVoXDTIwMDgy\nNTEzMjAwMVowcTELMAkGA1UEBhMCS1oxDzANBgNVBAcTBkFsbWF0eTETMBEGA1UE\nChMKa2tiY2FfdGVzdDELMAkGA1UECxMCQVQxEzARBgNVBAMTCmtrYmNhX3Rlc3Qx\nGjAYBgkqhkiG9w0BCQEWC2VwYXlAa2tiLmt6MIGeMA0GCSqGSIb3DQEBAQUAA4GM\nADCBiAKBgHubvjO36p31yokU3D6I8UEjSoypp9XwDx2BTRH1IpaagcHhIpM89N6D\nIKR5+epfGa38JHoJOP63gtyWBMGeOAfpUa067rXzOeJu5cQDoJP5LGMzGmFGMxmA\n1O+do0vzO5LnMpPxwgQhdY9PeS09DMzFyX6rVtmBdUWe2q0vIk6ZAgMBAAGjgbcw\ngbQwHQYDVR0OBBYEFC6fvGjFXPR7vleUibg0uzC4eNkXMB8GA1UdIwQYMBaAFO9d\np2Mor8bzfndC253ghJUGfXJTMAwGA1UdEwQFMAMBAQAwDgYDVR0PAQH/BAQDAgTw\nMDUGA1UdHwQuMCwwKqAooCaGJGh0dHA6Ly93d3cua2tiLmt6L2NlcnRyb290L2tr\nYmNhLmNybDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwQwDQYJKoZIhvcN\nAQEEBQADggEBAAn2TBxC2ojyerV/rfFCId4Ef/+tbXGq36G2aJzqjd4ptEIrv8Vv\nTEOa8n8cvZ19cFM5V0rF6yu8We5nwGHNoReA6c9sxk0d7g9tsCEeXEn1DCyccQPV\nptmUvg/l6pHKT6E3yNOyBFCAaXNiRatFzEeiCIFCway9vr4JgkVpCSfWzkTswLX4\nrePQFs/tHR3W4r9GntB5m5GEdLq6tv4ZwMweVOdfHWYT0kdp3/NWFovz81E40/FF\nTpZFCTyetMv89ffH/MzEPuSYsj8A++RvVUBqjiVEyLSz1ir6sNvsQDLc3mACg1HB\nw+lJunGmquzFWUE1vo42Q1m9nLCOSfwAmRI=\n-----END CERTIFICATE-----\n"

verification_key = load_pem_x509_certificate(
    bytes(test_public_key, encoding="UTF-8"),
    backend=default_backend(),
).public_key()

document = ET.fromstring(signed_message)
signature = ""
for bank_sign in document.iterfind("bank_sign"):
    signature = bank_sign.text.strip()
    break

if len(signature):
    try:
        verification_key.verify(
            b64decode(signature)[::-1],
            bytes(message, encoding="UTF-8"),
            PKCS1v15(),
            SHA1(),
        )
        print("OK")
    except InvalidSignature:
        print("FAIL")
