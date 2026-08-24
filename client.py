class SuperappMultiverticalTurboDeliveryRoutingClient:
    def dispatch_turbo_courier(self, user_lat=4.6097, user_lon=-74.0817, basket_type='Turbo_Fresh_Groceries'):
        return {
            'dispatch_id': 'rpp_dsp_9918',
            'superapp_vertical': basket_type,
            'nearest_darkstore_hub': 'BOGOTA_CHAPINERO_HUB_01',
            'estimated_delivery_minutes': 9.5,
            'courier_telematics_active': True,
            'rappi_pay_cashback_applied_usd': 1.80,
            'multivertical_cross_sell_active': True
        }
