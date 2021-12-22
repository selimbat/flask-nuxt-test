from flask_restful import Resource
from serpentin.api import api
from serpentin.managers.sales import get_sales, get_sales_by_name_with_infos, compute_progress

class Sales(Resource):
    def get(self):
        """ Return sales """
        sales = get_sales()
        formatted_sales = []
        for s in sales:
            f_s = s.get_formatted_data()
            f_s["progress"] = compute_progress(s)
            formatted_sales.append(f_s)

        return {"sales": formatted_sales}

class Sale(Resource):
    def get(self, salesName, month):
        """ Return one salesman with their deals and statements for a given month """
        sale, deals, statementCompensations = get_sales_by_name_with_infos(salesName, month)
        print(deals)
        formatted_data = {
            "sales": sale.get_formatted_data(),
            "deals": [d.get_formatted_data() for d in deals],
            "compensations": [sc.get_formatted_data() for sc in statementCompensations]
        }
        formatted_data["sales"]["progress"] = compute_progress(sale, deals=deals)

        return formatted_data

api.add_resource(Sales, "/sales")
api.add_resource(Sale, "/sales/<salesName>/<month>")

