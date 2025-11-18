def get_last_operation(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT op_type, num1, num2, result, success FROM operations ORDER BY id DESC LIMIT 1;")
    row = cur.fetchone()
    cur.close()
    return row

def test_sumar_integration(client, db_conn):
    response = client.post("/sumar", data={"num1": "10", "num2": "5"})
    assert response.status_code == 200
    assert b"15.0" in response.data
    op = get_last_operation(db_conn)
    assert op[0] == "suma"
    assert op[1] == 10.0
    assert op[2] == 5.0
    assert op[3] == "15.0"
    assert op[4] is True

def test_dividir_por_cero_integration(client, db_conn):
    response = client.post("/dividir", data={"num1": "10", "num2": "0"})
    assert "División por cero" in response.data
    op = get_last_operation(db_conn)
    assert op[0] == "division"
    assert op[4] is False
