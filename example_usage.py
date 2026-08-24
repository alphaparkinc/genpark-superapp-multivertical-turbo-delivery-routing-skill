from client import SuperappMultiverticalTurboDeliveryRoutingClient

def main():
    client = SuperappMultiverticalTurboDeliveryRoutingClient()
    res = client.dispatch_turbo_courier(19.4326, -99.1332, 'Turbo_Pharmacy_Express')
    print('Dispatch: ' + res['dispatch_id'] + ' (' + res['superapp_vertical'] + ')')
    print('Darkstore: ' + res['nearest_darkstore_hub'] + ' | ETA: ' + str(res['estimated_delivery_minutes']) + ' mins')
    print('Cashback Applied: $' + str(res['rappi_pay_cashback_applied_usd']) + ' | Courier Tracking: ' + str(res['courier_telematics_active']))

if __name__ == '__main__':
    main()
