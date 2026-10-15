import os
import sys
import frappe
from frappe.utils import nowdate, flt
import erpnext.setup.setup_wizard.operations.install_fixtures as fixtures

def setup_manufacturing_data():
    frappe.init('frontend')
    frappe.connect()
    frappe.flags.ignore_permissions = True
    frappe.set_user("Administrator")

    print(">>> [1/7] Memasang Fixtures & Parameter Regional Indonesia...")
    try:
        fixtures.install("Indonesia")
        frappe.db.commit()
    except Exception as e:
        frappe.db.rollback()
        print(f"Fixtures sudah terpasang atau dilewati: {e}")

    print(">>> [2/7] Menyiapkan Perusahaan (Company)...")
    company_name = "PT Plastikindo Jaya Makmur"
    company_abbr = "PJM"
    
    # Setup Fiscal Year
    year_name = "2026-2027"
    if not frappe.db.exists("Fiscal Year", year_name):
        fy = frappe.get_doc({
            "doctype": "Fiscal Year",
            "year": year_name,
            "year_start_date": "2026-01-01",
            "year_end_date": "2026-12-31"
        })
        fy.insert(ignore_permissions=True)
        frappe.db.commit()

    if not frappe.db.exists("Company", company_name):
        print(f"Membuat Company: {company_name}")
        company = frappe.get_doc({
            "doctype": "Company",
            "company_name": company_name,
            "abbr": company_abbr,
            "default_currency": "IDR",
            "country": "Indonesia",
            "create_chart_of_accounts_based_on": "Standard Template",
            "chart_of_accounts": "Standard",
            "domain": "Manufacturing"
        })
        company.insert(ignore_permissions=True)
    else:
        company = frappe.get_doc("Company", company_name)
    
    frappe.db.commit()

    # Set Default Global
    frappe.db.set_default("company", company_name)
    frappe.db.set_default("currency", "IDR")
    frappe.db.set_default("country", "Indonesia")

    # Complete Setup Wizard Flag
    frappe.db.set_single_value("System Settings", "setup_complete", 1)
    frappe.db.commit()

    print(">>> [3/7] Menyiapkan Gudang (Warehouse)...")
    parent_wh = f"All Warehouses - {company_abbr}"
    if not frappe.db.exists("Warehouse", parent_wh):
        p_wh = frappe.get_doc({
            "doctype": "Warehouse",
            "warehouse_name": "All Warehouses",
            "company": company_name,
            "is_group": 1
        })
        p_wh.insert(ignore_permissions=True)

    warehouses = [
        {"warehouse_name": "Stores", "warehouse_type": "Stores"},
        {"warehouse_name": "Work In Progress", "warehouse_type": "Work In Progress"},
        {"warehouse_name": "Finished Goods", "warehouse_type": "Finished Goods"}
    ]
    for wh in warehouses:
        wh_full_name = f"{wh['warehouse_name']} - {company_abbr}"
        if not frappe.db.exists("Warehouse", wh_full_name):
            print(f"Membuat Warehouse: {wh_full_name}")
            doc = frappe.get_doc({
                "doctype": "Warehouse",
                "warehouse_name": wh['warehouse_name'],
                "company": company_name,
                "warehouse_type": wh['warehouse_type'] if frappe.db.exists("Warehouse Type", wh['warehouse_type']) else None,
                "parent_warehouse": parent_wh
            })
            doc.insert(ignore_permissions=True)

    frappe.db.commit()

    print(">>> [4/7] Menyiapkan Item Group...")
    item_groups = [
        {"name": "Raw Material", "parent": "All Item Groups"},
        {"name": "Sub Assemblies", "parent": "All Item Groups"},
        {"name": "Packaging Material", "parent": "All Item Groups"},
        {"name": "Consumables", "parent": "All Item Groups"},
        {"name": "Plastic Products", "parent": "All Item Groups"}
    ]
    for ig in item_groups:
        if not frappe.db.exists("Item Group", ig["name"]):
            print(f"Membuat Item Group: {ig['name']}")
            doc = frappe.get_doc({
                "doctype": "Item Group",
                "item_group_name": ig["name"],
                "parent_item_group": ig["parent"],
                "is_group": 0
            })
            doc.insert(ignore_permissions=True)

    frappe.db.commit()

    print(">>> [5/7] Menyiapkan Workstation, Operation & Routing...")
    # Workstations
    workstations = [
        {"name": "WS-INJ-01", "workstation_name": "WS-INJ-01", "hour_rate_electricity": 45000, "hour_rate_labour": 25000, "production_capacity": 1},
        {"name": "WS-INJ-02", "workstation_name": "WS-INJ-02", "hour_rate_electricity": 35000, "hour_rate_labour": 25000, "production_capacity": 1},
        {"name": "WS-ASSY-01", "workstation_name": "WS-ASSY-01", "hour_rate_electricity": 5000, "hour_rate_labour": 40000, "production_capacity": 4},
        {"name": "WS-PACK-01", "workstation_name": "WS-PACK-01", "hour_rate_electricity": 3000, "hour_rate_labour": 30000, "production_capacity": 2}
    ]
    for ws in workstations:
        if not frappe.db.exists("Workstation", ws["name"]):
            print(f"Membuat Workstation: {ws['name']}")
            doc = frappe.get_doc({
                "doctype": "Workstation",
                "workstation_name": ws["name"],
                "hour_rate_electricity": ws["hour_rate_electricity"],
                "hour_rate_labour": ws["hour_rate_labour"],
                "production_capacity": ws["production_capacity"]
            })
            doc.insert(ignore_permissions=True)

    # Operations
    operations = [
        {"name": "OP-MIXING", "workstation": "WS-INJ-01", "desc": "Pencampuran Biji Plastik dan Pewarna/Aditif"},
        {"name": "OP-INJ-BODY", "workstation": "WS-INJ-01", "desc": "Molding Wadah Utama Kotak Makan Bento 3 Sekat"},
        {"name": "OP-INJ-LID", "workstation": "WS-INJ-02", "desc": "Molding Tutup Transparan Kotak Makan"},
        {"name": "OP-TRIM-QC", "workstation": "WS-ASSY-01", "desc": "Pembersihan Sisa Runner & Inspeksi Cacat Visual"},
        {"name": "OP-ASSY-SEAL", "workstation": "WS-ASSY-01", "desc": "Pemasangan Karet Seal Silikon ke Alur Tutup"},
        {"name": "OP-PACKING", "workstation": "WS-PACK-01", "desc": "Pemasangan Paper Sleeve Label, Plastik OPP, dan Masuk Dus"}
    ]
    for op in operations:
        if not frappe.db.exists("Operation", op["name"]):
            print(f"Membuat Operation: {op['name']}")
            doc = frappe.get_doc({
                "doctype": "Operation",
                "name": op["name"],
                "workstation": op["workstation"],
                "description": op["desc"]
            })
            doc.insert(ignore_permissions=True)

    # Routing
    routing_name = "ROUT-BENTO-01"
    if not frappe.db.exists("Routing", routing_name):
        print(f"Membuat Routing: {routing_name}")
        doc = frappe.get_doc({
            "doctype": "Routing",
            "routing_name": routing_name,
            "operations": [
                {"sequence_id": 1, "operation": "OP-INJ-BODY", "workstation": "WS-INJ-01", "time_in_mins": 0.416, "operating_cost": 486.11},
                {"sequence_id": 2, "operation": "OP-INJ-LID", "workstation": "WS-INJ-02", "time_in_mins": 0.333, "operating_cost": 333.33},
                {"sequence_id": 3, "operation": "OP-TRIM-QC", "workstation": "WS-ASSY-01", "time_in_mins": 0.250, "operating_cost": 187.50},
                {"sequence_id": 4, "operation": "OP-ASSY-SEAL", "workstation": "WS-ASSY-01", "time_in_mins": 0.200, "operating_cost": 150.00},
                {"sequence_id": 5, "operation": "OP-PACKING", "workstation": "WS-PACK-01", "time_in_mins": 0.250, "operating_cost": 137.50}
            ]
        })
        doc.insert(ignore_permissions=True)

    frappe.db.commit()

    print(">>> [6/7] Menyiapkan Master Items & BOM...")
    # Items
    items = [
        {"item_code": "RM-PP-NAT", "item_name": "Biji Plastik PP Food Grade Natural", "item_group": "Raw Material", "stock_uom": "Kg", "valuation_rate": 22000, "standard_rate": 22000, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-MB-BLU", "item_name": "Masterbatch Pewarna Biru Food Grade", "item_group": "Raw Material", "stock_uom": "Kg", "valuation_rate": 65000, "standard_rate": 65000, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-MB-CLR", "item_name": "Clarifier Additive Transparan", "item_group": "Raw Material", "stock_uom": "Kg", "valuation_rate": 85000, "standard_rate": 85000, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-SIL-SEAL", "item_name": "Karet Seal Silikon 1000ml", "item_group": "Raw Material", "stock_uom": "Nos", "valuation_rate": 1500, "standard_rate": 1500, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-PLST-OPP", "item_name": "Plastik Pembungkus OPP 25x20cm", "item_group": "Consumables", "stock_uom": "Nos", "valuation_rate": 200, "standard_rate": 200, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-LBL-BTO", "item_name": "Paper Sleeve Label Bento", "item_group": "Consumables", "stock_uom": "Nos", "valuation_rate": 500, "standard_rate": 500, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "RM-BOX-CTN", "item_name": "Karton Box Master (Isi 24 Set)", "item_group": "Packaging Material", "stock_uom": "Nos", "valuation_rate": 6000, "standard_rate": 6000, "is_purchase_item": 1, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "SFG-KM-BODY", "item_name": "Body Kotak Makan Bento Biru", "item_group": "Sub Assemblies", "stock_uom": "Nos", "valuation_rate": 3500, "standard_rate": 3500, "is_purchase_item": 0, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "SFG-KM-LID", "item_name": "Tutup Kotak Makan Transparan", "item_group": "Sub Assemblies", "stock_uom": "Nos", "valuation_rate": 2200, "standard_rate": 2200, "is_purchase_item": 0, "is_sales_item": 0, "include_item_in_manufacturing": 1},
        {"item_code": "FG-KM-01", "item_name": "Kotak Makan Bento 3 Sekat 1000ml", "item_group": "Plastic Products", "stock_uom": "Nos", "valuation_rate": 7611, "standard_rate": 13500, "is_purchase_item": 0, "is_sales_item": 1, "include_item_in_manufacturing": 1}
    ]

    for itm in items:
        if not frappe.db.exists("Item", itm["item_code"]):
            print(f"Membuat Item: {itm['item_code']}")
            doc = frappe.get_doc({
                "doctype": "Item",
                "item_code": itm["item_code"],
                "item_name": itm["item_name"],
                "item_group": itm["item_group"],
                "stock_uom": itm["stock_uom"],
                "is_stock_item": 1,
                "valuation_rate": itm["valuation_rate"],
                "standard_rate": itm["standard_rate"],
                "is_purchase_item": itm["is_purchase_item"],
                "is_sales_item": itm["is_sales_item"],
                "include_item_in_manufacturing": itm["include_item_in_manufacturing"]
            })
            doc.insert(ignore_permissions=True)

    frappe.db.commit()

    # BOM
    bom_item = "FG-KM-01"
    existing_boms = frappe.db.get_list("BOM", filters={"item": bom_item, "is_active": 1, "docstatus": 1})
    if not existing_boms:
        print(f"Membuat BOM untuk: {bom_item}")
        bom_doc = frappe.get_doc({
            "doctype": "BOM",
            "item": bom_item,
            "quantity": 1,
            "currency": "IDR",
            "is_active": 1,
            "is_default": 1,
            "with_operations": 1,
            "routing": "ROUT-BENTO-01",
            "operations": [
                {"sequence_id": 1, "operation": "OP-INJ-BODY", "workstation": "WS-INJ-01", "time_in_mins": 0.416, "hour_rate": 70000, "operating_cost": 486.11},
                {"sequence_id": 2, "operation": "OP-INJ-LID", "workstation": "WS-INJ-02", "time_in_mins": 0.333, "hour_rate": 60000, "operating_cost": 333.33},
                {"sequence_id": 3, "operation": "OP-TRIM-QC", "workstation": "WS-ASSY-01", "time_in_mins": 0.250, "hour_rate": 45000, "operating_cost": 187.50},
                {"sequence_id": 4, "operation": "OP-ASSY-SEAL", "workstation": "WS-ASSY-01", "time_in_mins": 0.200, "hour_rate": 45000, "operating_cost": 150.00},
                {"sequence_id": 5, "operation": "OP-PACKING", "workstation": "WS-PACK-01", "time_in_mins": 0.250, "hour_rate": 33000, "operating_cost": 137.50}
            ],
            "items": [
                {"item_code": "RM-PP-NAT", "qty": 0.153, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "rate": 22000, "amount": 3366},
                {"item_code": "RM-MB-BLU", "qty": 0.005, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "rate": 65000, "amount": 325},
                {"item_code": "RM-MB-CLR", "qty": 0.002, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "rate": 85000, "amount": 170},
                {"item_code": "RM-SIL-SEAL", "qty": 1.000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "rate": 1500, "amount": 1500},
                {"item_code": "RM-PLST-OPP", "qty": 1.000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "rate": 200, "amount": 200},
                {"item_code": "RM-LBL-BTO", "qty": 1.000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "rate": 500, "amount": 500}
            ]
        })
        bom_doc.insert(ignore_permissions=True)
        bom_doc.submit()
        print(f"BOM berhasil dibuat dan disubmit: {bom_doc.name}")

    frappe.db.commit()

    print(">>> [7/7] Menyiapkan Saldo Awal Stok & Work Order Contoh...")
    target_wh = f"Stores - {company_abbr}"
    stock_entries = frappe.db.get_list("Stock Entry", filters={"company": company_name, "stock_entry_type": "Material Receipt", "docstatus": 1})
    if not stock_entries:
        print(f"Membuat Saldo Awal Bahan Baku di: {target_wh}")
        se_doc = frappe.get_doc({
            "doctype": "Stock Entry",
            "stock_entry_type": "Material Receipt",
            "company": company_name,
            "to_warehouse": target_wh,
            "posting_date": nowdate(),
            "items": [
                {"item_code": "RM-PP-NAT", "qty": 500, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 22000},
                {"item_code": "RM-MB-BLU", "qty": 25, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 65000},
                {"item_code": "RM-MB-CLR", "qty": 10, "uom": "Kg", "stock_uom": "Kg", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 85000},
                {"item_code": "RM-SIL-SEAL", "qty": 2000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 1500},
                {"item_code": "RM-PLST-OPP", "qty": 3000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 200},
                {"item_code": "RM-LBL-BTO", "qty": 3000, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 500},
                {"item_code": "RM-BOX-CTN", "qty": 150, "uom": "Nos", "stock_uom": "Nos", "conversion_factor": 1, "t_warehouse": target_wh, "basic_rate": 6000}
            ]
        })
        se_doc.insert(ignore_permissions=True)
        se_doc.submit()
        print(f"Stock Entry saldo awal berhasil disubmit: {se_doc.name}")

    frappe.db.commit()

    # Work Order
    active_bom = frappe.db.get_value("BOM", {"item": "FG-KM-01", "is_active": 1, "is_default": 1})
    if active_bom and not frappe.db.exists("Work Order", {"production_item": "FG-KM-01", "company": company_name}):
        print(f"Membuat Contoh Work Order Produksi 1000 Set Kotak Makan...")
        wo_doc = frappe.get_doc({
            "doctype": "Work Order",
            "company": company_name,
            "production_item": "FG-KM-01",
            "bom_no": active_bom,
            "qty": 1000,
            "wip_warehouse": f"Work In Progress - {company_abbr}",
            "fg_warehouse": f"Finished Goods - {company_abbr}",
            "planned_start_date": nowdate()
        })
        wo_doc.insert(ignore_permissions=True)
        wo_doc.submit()
        print(f"Work Order berhasil dibuat dan disubmit: {wo_doc.name}")

    frappe.db.commit()
    print("==================================================================")
    print(">>> Seluruh data Manufaktur telah BERHASIL dimasukkan ke database ERPNext! ✅")
    print("==================================================================")

if __name__ == "__main__":
    setup_manufacturing_data()
